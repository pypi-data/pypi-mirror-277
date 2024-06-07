from ..._resource import SyncAPIResource
from ..._response import APIResponse
from .app_job import AppJob


class App(SyncAPIResource):
    job: AppJob

    def __init__(self, _client) -> None:
        self.job = AppJob(_client)
        super().__init__(_client)

    def get_app_info(self, app_key: str):
        response = self._client.get(
            "/openapi/v1/square/app/schema", params={"appKey": app_key}
        )
        return APIResponse(response).json
