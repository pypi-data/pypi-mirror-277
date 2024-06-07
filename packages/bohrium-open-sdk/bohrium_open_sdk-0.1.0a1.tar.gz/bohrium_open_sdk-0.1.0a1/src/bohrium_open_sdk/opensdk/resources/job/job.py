import logging
import os
import uuid
from pathlib import Path
from typing import Optional
from unittest import result

from ..._exceptions import NotFoundError
from ..._resource import SyncAPIResource
from ..._response import APIResponse
from ..._tiefblue_client import Tiefblue
from ...types.job.job import JobAddRequest

logger = logging.getLogger(__name__)


class Job(SyncAPIResource):

    def detail(self, job_id):
        uri = f"/{self._client.api_prefix}/v1/job/{job_id}"
        response = self._client.get(uri)
        return APIResponse(response).json

    def submit(
        self,
        *,
        project_id: int,
        job_name: str,
        machine_type: str,
        cmd: str,
        image_address: str,
        job_group_id: int = 0,
        work_dir: str = "",
        dataset_path: list = [],
        log_files: list = [],
        out_files: list = [],
    ):
        data = self.create_job(project_id, job_name, job_group_id)

        if work_dir != "":
            if not os.path.exists(work_dir):
                raise FileNotFoundError
            if os.path.isdir(work_dir):
                self.upload_dir(work_dir, data.storePath, data.token)
            else:
                file_name = os.path.basename(work_dir)
                object_key = os.path.join(data["storePath"], file_name)
                self.upload(work_dir, object_key, data["token"])

        ep = os.path.expanduser(result)
        p = Path(ep).absolute().resolve()
        p = p.joinpath(str(uuid.uuid4()) + "_temp.zip")

        job_add_request = JobAddRequest(
            download_path=str(p.absolute().resolve()),
            dataset_path=dataset_path,
            job_name=job_name,
            project_id=project_id,
            job_id=data["jobId"],
            oss_path=data["storePath"],
            image_name=image_address,
            scass_type=machine_type,
            cmd=cmd,
            log_files=log_files,
            out_files=out_files,
        )
        return self.insert(job_add_request.to_dict())

    def insert(self, data):
        uri = f"/{self._client.api_prefix}/v2/job/add"
        response = self._client.post(uri, json=data)
        return APIResponse(response).json

    def delete(self, job_id):
        uri = f"/{self._client.api_prefix}/v1/job/del/{job_id}"
        response = self._client.post(uri)
        return APIResponse(response).json

    def terminate(self, job_id):
        uri = f"/{self._client.api_prefix}/v1/job/terminate/{job_id}"
        response = self._client.post(uri)
        return APIResponse(response).json

    def kill(self, job_id):
        uri = f"/{self._client.api_prefix}/v1/job/kill/{job_id}"
        response = self._client.post(uri)
        return APIResponse(response).json

    def log(self, job_id, log_file="STDOUTERR", page=-1, page_size=8192):
        uri = f"/{self._client.api_prefix}/v1/job/{job_id}/log"
        response = self._client.get(
            uri,
            params={"logFile": log_file, "page": page, "pageSize": page_size},
        )
        return APIResponse(response).json

    def create_job(
        self,
        project_id: int,
        name: Optional[str] = None,
        group_id: Optional[int] = 0,
    ):
        uri = f"/{self._client.api_prefix}/v1/job/create"
        data = {
            "projectId": project_id,
            "name": name,
            "bohrGroupId": group_id,
        }
        response = self._client.post(uri, json=data)
        return APIResponse(response).data

    def create_job_group(self, project_id, job_group_name):
        uri = f"/{self._client.api_prefix}/v1/job_group/add"
        response = self._client.post(
            uri,
            json={"name": job_group_name, "projectId": project_id},
        )

        return APIResponse(response).json

    def upload(
        self,
        file_path: str,
        object_key: str,
        token: str,
    ):
        tiefblue = Tiefblue()
        custom_headers = {"Authorization": token}

        tiefblue.upload_from_file_multi_part(
            object_key=object_key,
            custom_headers=custom_headers,
            file_path=file_path,
            progress_bar=True,
        )

    def upload_dir(self, work_dir, store_path, token):
        # TODO: upload rule
        if not work_dir.endswith("/"):
            work_dir = work_dir + "/"
        for root, _, files in os.walk(work_dir):
            for file in files:
                full_path = os.path.join(root, file)
                object_key = full_path.replace(work_dir, store_path)
                self.upload(full_path, object_key, token)

    def download(self, job_id, save_path):
        detail = self.detail(job_id)

        result_url = detail.get("data").get("resultUrl")

        if not result_url:
            raise NotFoundError("Result url not found")

        # check save path
        # if not exist create it
        if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))

        logger.debug(
            f"Downloading job {job_id} to {save_path}, result url: {result_url}"
        )

        tiefblue = Tiefblue()
        tiefblue.download_from_url(result_url, save_path)
