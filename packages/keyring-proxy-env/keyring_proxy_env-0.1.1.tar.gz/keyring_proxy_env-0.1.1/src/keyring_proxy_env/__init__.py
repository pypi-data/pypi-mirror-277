import logging
import os

import keyring.backend
import keyring.credentials
import keyring.errors

from keyring_proxy.transport import Credential

logger = logging.getLogger(__name__)


def make_key(*args: str) -> str:
    return "_".join(arg.upper().replace("-", "_") for arg in args)

def get_key(key: str) -> str | None:
    logger.debug(f"Getting {key!r}")
    return os.getenv(key)


class EnvProxyBackend(keyring.backend.KeyringBackend):

    logfile: str = "keyring-proxy.log"
    log: bool = False
    prefix: str = "KEYRING"

    def __init__(self):
        super().__init__()
        if self.log:
            logging.basicConfig(level=logging.DEBUG)

    

    def _get_cred(self, service: str, username: str | None):
        if username is None:
            username_key = make_key(self.prefix, service, "USERNAME")
            username = get_key(username_key)        
        if username is None:
            password_key = make_key(self.prefix, service, "PASSWORD")
        else:
            password_key = make_key(self.prefix, service, username, "PASSWORD")
        
        password = get_key(password_key)
        
        if username is None and password is None:
            return None
        
        return Credential(username, password)

    def get_credential(self, service: str, username: str | None) -> keyring.credentials.Credential | None:
        logger.debug(f"get_credential({service!r}, {username!r})")
        result = self._get_cred(service, username)
        if result is None:
            return None
        return result.to_keyring_cred()

    def get_password(self, service: str, username: str) -> str | None:
        logger.debug(f"get_password({service!r}, {username!r})")
        cred = self._get_cred(service, username)
        if cred is None:
            return None
        return cred.password

    def set_password(self, service: str, username: str, password: str):
        raise keyring.errors.PasswordSetError("set_password not implemented")

    def delete_password(self, service: str, username: str):
        raise keyring.errors.PasswordDeleteError("delete_password not implemented")
