import requests
from pprint import pprint
import os

name_file = os.path.join(os.getcwd(), 'file.txt')




class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_file_list(self):
        url_files = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url=url_files, headers=headers)
        return response.json()


    def _get_upload_link(self, disk_file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        header = self.get_headers()
        params = {
            'path': disk_file_path,
            'overwrite': True}
        response = requests.get(url=url, headers=header, params=params)
        for k, v in response.json().items():
            if k == 'href':
                return self.upload_file_to_disk(v, name_file)
            else:
                print(k,v)

    def upload_file_to_disk(self, href, file_name):
        url = href
        response = requests.put(url=url, data=open(file_name, 'rb'))
        if response.status_code == 201:
            print('ok')
        else:
            print(response.status_code)



if __name__ == '__main__':
    TOKEN = 'AQAAAABVTIbUAADLW-DUpXP72UBDvBK3bGTO_fg'
    Ya = YaUploader(TOKEN)
    Ya._get_upload_link(os.path.basename(name_file))