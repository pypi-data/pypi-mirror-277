import requests

class STRKEYAPI:
    def __init__(self, url, apikey):
        self.url = url
        self.apikey = apikey

    def checkkey(self, key):
        params = {
            'key': key
        }

        request = requests.get(url=f'{self.url}/checkkey', params=params)
        return request.text

    def addkey(self, key, worktime):
        params = {
            'key': key,
            'apikey': self.apikey,
            'worktime': worktime
        }

        request = requests.get(url=f'{self.url}/addkey', params=params)
        return request.text

    def deletekey(self, key):
        params = {
            'key': key,
            'apikey': self.apikey
        }

        request = requests.get(url=f'{self.url}/deletekey', params=params)
        return request.text
