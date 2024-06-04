import requests

from cryptlab.common.exceptions import PKIEntryAlreadySet
from cryptlab.orchestrator.serverscripts.bridge import Bridge


class PKIConnection:
    def get(self, key: str) -> str:
        raise NotImplementedError()

    def set(self, key: str, value: str):
        raise NotImplementedError()


class LocalPKIConnection(PKIConnection):
    def __init__(self, url: str, server_id: str):
        self.url = url
        self.server_id = server_id

    def get(self, key: str):
        r = requests.get(self.url + f"/pki/{key}", cookies={"token": self.server_id})
        if r.status_code == 200:
            return r.json()["result"]
        else:
            raise KeyError(f"{key} not found in PKI")

    def set(self, key: str, value: str):
        r = requests.post(
            self.url + f"/pki/{key}",
            json={"value": value},
            cookies={"token": self.server_id},
        )
        if r.status_code == 409:
            raise PKIEntryAlreadySet()


class OrchestratedPKIConnection(PKIConnection):
    def __init__(self, bridge: Bridge, server_id: str):
        self.bridge = bridge
        self.server_id = server_id

    def get(self, key: str):
        res = self.bridge.get_pki_entry(self.server_id, key)
        if res:
            return res
        else:
            raise KeyError(f"{key} not found in PKI")

    def set(self, key: str, value: str):
        self.bridge.set_pki_entry(self.server_id, key, value)
