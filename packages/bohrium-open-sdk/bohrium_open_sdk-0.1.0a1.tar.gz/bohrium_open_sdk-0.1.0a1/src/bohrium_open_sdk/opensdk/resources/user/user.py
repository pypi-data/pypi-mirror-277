import logging

from ..._resource import SyncAPIResource
from ..._response import APIResponse

log = logging.getLogger(__name__)


class User(SyncAPIResource):

    def getInfo(self):
        response = self._client.get("openapi/v1/ak/get")
        return APIResponse(response).json
