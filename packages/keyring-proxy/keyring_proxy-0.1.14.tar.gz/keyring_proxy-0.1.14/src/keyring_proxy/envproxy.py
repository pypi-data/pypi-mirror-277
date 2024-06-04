import dataclasses
import logging
import os
from typing import overload, override

from keyring_proxy.transport import (
    Credential,
    CredentialRequest,
    CredentialResponse,
    DeleteRequest,
    DeleteResponse,
    GetRequest,
    GetResponse,
    ReqPacket,
    Requests,
    Responses,
    RespPacket,
    SetRequest,
    SetResponse,
    TransportClient,
    TransportServer,
)

DEFAULT_PREFIX = "KEYRING"

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class RuntimeTransport(TransportClient):
    prefix: str

    def _get_cred(self, service: str, username: str | None):
        if username is None:
            username = os.getenv(f"{self.prefix}_{service.replace('-','_')}_USERNAME")
            password = os.getenv(f"{self.prefix}_{service.replace('-','_')}_PASSWORD")
        else:
            password = os.getenv(f"{self.prefix}_{service.replace('-','_')}_{username.replace('-','_')}_PASSWORD")
        if username is None and password is None:
            return CredentialResponse(None)
        return CredentialResponse(Credential(username, password))

    @override
    def _communicate(self, req: ReqPacket) -> RespPacket:
        raise Exception("Not implemented")

    @overload
    def communicate(self, req: GetRequest) -> GetResponse: ...

    @overload
    def communicate(self, req: SetRequest) -> SetResponse: ...

    @overload
    def communicate(self, req: DeleteRequest) -> DeleteResponse: ...

    @overload
    def communicate(self, req: CredentialRequest) -> CredentialResponse: ...

    @override
    def communicate(self, req: Requests) -> Responses:
        match req:
            case GetRequest(service, username):
                cred = self._get_cred(service, username)
                if cred.result is None:
                    return GetResponse(None)
                return GetResponse(cred.result.password)
            case SetRequest(_, _, _):
                raise Exception("Not implemented")
            case DeleteRequest(_, _):
                raise Exception("Not implemented")
            case CredentialRequest(service, username):
                return self._get_cred(service, username)

    @classmethod
    def from_prefix(cls, prefix: str):
        return cls(prefix)


@dataclasses.dataclass
class StdioProxyFrontend(TransportServer):
    pass
