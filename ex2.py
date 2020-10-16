import os
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        data = {'path': file_path}
        HEADERS = {"Authorization": f"OAuth {self.token}"}
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', headers=HEADERS, params=data)
        url = response.json()['href']
        requests.put(url, data={'path': file_path})
        return 'Done'


if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload('2.py')
    print(result)
