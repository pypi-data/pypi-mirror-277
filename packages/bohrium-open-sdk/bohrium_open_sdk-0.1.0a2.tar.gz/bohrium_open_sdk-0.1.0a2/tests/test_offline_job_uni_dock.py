import os
import time
from pathlib import Path

import pytest
from bohrium_open_sdk import OpenSDK, UploadInputItem
from dotenv import find_dotenv, load_dotenv
from glom import glom

load_dotenv(find_dotenv(), override=True)


def get_access_key():
    return os.getenv("ACCESS_KEY")


def get_bohrium_project_id():
    return int(os.getenv("BOHRIUM_PROJECT_ID"))


def submit_job(client: OpenSDK):
    ext_config = {"jobConfig": {"jobRead": 1}}
    inputs = {
        "center_x": 0,
        "center_y": 0,
        "center_z": 0,
        "input_ligands": [
            UploadInputItem(
                src=Path(__file__).parent / "data" / "uni_dock" / "uniDock_ligand.sdf"
            )
        ],
        "input_protein": UploadInputItem(
            src=Path(__file__).parent / "data" / "uni_dock" / "uniDock_protein.pdb"
        ),
        "local_only": False,
        "mode": "fast",
        "num_modes": 1,
        "random_seed": False,
        "score_only": False,
        "scoring": "vinardo",
        "size_x": 25,
        "size_y": 25,
        "size_z": 25,
        "unimol_bias": False,
    }

    sub_model_name = "UniDockModel"
    resp = client.app.job.submit(
        app_key="uni-dock",
        sub_model_name=sub_model_name,
        project_id=get_bohrium_project_id(),
        inputs=inputs,
        ext_config=ext_config,
    )
    return resp


def test_submit_job():
    client = OpenSDK(access_key=get_access_key())
    resp = submit_job(client) or {}
    assert resp.get("code") == 0
    assert glom(resp, "data.jobId") is not None


def test_list_jobs():
    client = OpenSDK(access_key=get_access_key())
    res = client.app.job.list() or {}

    assert res.get("code") == 0
    assert glom(res, "data") is not None
    assert isinstance(glom(res, "data.items"), list)


def get_one_job_from_list(client: OpenSDK):
    jobs_rsp = client.app.job.list() or {}
    assert isinstance(glom(jobs_rsp, "data.items"), list)

    jobs = glom(jobs_rsp, "data.items")
    if len(jobs) == 0:
        assert False, "No job is running or finished"

    # APP_JOB_STATUS_WAIT_SUBMIT = -10 //预创建
    # APP_JOB_STATUS_SUBMIT      = 0  //已提交
    # APP_JOB_STATUS_RUNNING     = 1  // 运行中
    # APP_JOB_STATUS_SUCCESS     = 10 //运行成功
    # APP_JOB_STATUS_FAIL        = 30 //运行失败
    # APP_JOB_STATUS_KILL        = 31 //人工停止
    accessible_jobs = list(filter(lambda x: x.get("status") == 10, jobs))
    if not accessible_jobs:
        accessible_jobs = list(filter(lambda x: x.get("status") == 1, jobs))
    if not accessible_jobs:
        assert False, "No job is running or finished"

    current_job = accessible_jobs[0]
    return current_job


def test_get_job():
    client = OpenSDK(access_key=get_access_key())
    current_job = get_one_job_from_list(client)

    assert type(current_job.get("id")) == int
    assert current_job.get("jobName") is not None

    current_job_id = current_job.get("id")

    job_rsp = client.app.job.detail(current_job_id) or {}
    assert job_rsp.get("code") == 0
    assert glom(job_rsp, "data") is not None

    current_job_data = glom(job_rsp, "data")
    assert current_job_data.get("id") == current_job_id
    assert current_job_data.get("jobName") == current_job.get("jobName")


def test_download_job_result():
    client = OpenSDK(access_key=get_access_key())
    current_job = get_one_job_from_list(client)

    job_id = current_job.get("id")

    import tempfile

    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Temporary directory created: {temp_dir}")
        temp_dir = Path(temp_dir)
        is_ok = client.app.job.download(
            job_id, remote_target="config.json", save_path=temp_dir / "outputs"
        )

        assert is_ok
        assert (temp_dir / "outputs").exists()
        assert (temp_dir / "outputs" / "config.json").exists()

        is_ok = client.app.job.download(
            job_id, remote_target="task", save_path=temp_dir / "task"
        )

        assert is_ok
        assert (temp_dir / "task").exists()
        assert (temp_dir / "task").is_dir()


def test_get_job_log():
    client = OpenSDK(access_key=get_access_key())
    current_job = get_one_job_from_list(client)

    job_id = current_job.get("id")

    log_rsp = client.app.job.log(job_id) or {}

    assert log_rsp.get("code") == 0
    assert glom(log_rsp, "data") is not None
    assert glom(log_rsp, "data.log") is not None


def test_kill_job():
    client = OpenSDK(access_key=get_access_key())

    resp = submit_job(client) or {}

    assert resp.get("data") is not None
    assert glom(resp, "data.jobId") is not None

    time.sleep(5)

    job_id = glom(resp, "data.jobId")

    kill_rsp = client.app.job.kill(job_id) or {}

    assert kill_rsp.get("code") == 0

    resp = client.app.job.detail(job_id) or {}

    assert resp.get("code") == 0
    assert glom(resp, "data") is not None
    assert glom(resp, "data.status") == 31


def test_delete_job():
    client = OpenSDK(access_key=get_access_key())

    resp = submit_job(client) or {}
    assert resp.get("data") is not None
    assert glom(resp, "data.jobId") is not None

    time.sleep(5)

    job_id = glom(resp, "data.jobId")

    delete_res = client.app.job.delete(job_id)

    assert delete_res.get("code") != 0

    kill_rsp = client.app.job.kill(job_id)
    assert kill_rsp.get("code") == 0
    delete_res = client.app.job.delete(job_id)
    assert delete_res.get("code") == 0
