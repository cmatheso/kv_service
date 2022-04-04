import json
import os
import requests
import urllib.parse

class kv_service_client:
    """A client to the kv_service."""

    ENV_NAME_KV_SERVICE_URL = 'KV_SERVICE_URL'

    def __init__(self):
        embeddedUrl = None
        if self.ENV_NAME_KV_SERVICE_URL in os.environ:
            embeddedUrl = os.environ[self.ENV_NAME_KV_SERVICE_URL]

        if embeddedUrl is None:
            raise Exception(f'{self.ENV_NAME_KV_SERVICE_URL} not found!')
        
        self.url = embeddedUrl

    def __build_url(self, *args:str) -> str:
        return self.url + '/kv/' + "/".join(map(lambda x: urllib.parse.quote_plus(x), args))

    def read_key(self, key:str) -> str:
        try:
            resp = requests.get(self.__build_url(key))
            if resp.status_code == 200:
                model = json.loads(resp.text)
                return model['value']
        except:
            pass
        
        return None

    def update_key(self, key:str, val:str) -> bool:
        try:
            r = requests.post(self.__build_url(key), data = json.dumps({ 'value': val }))
            return r.status_code == 200
        except:
            return False

    def delete_key(self, key:str) -> bool:
        try:
            r = requests.delete(self.__build_url(key))
            return r.status_code == 200
        except:
            return False
