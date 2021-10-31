import requests
import os
import json


def search_music_by_name():
    name = input('input music name')

    platform_msg = '''
        1. 网易云
        2. QQ
        3.酷狗
        4.酷我
    '''
    print(platform_msg)

    platform = input('input music platform')
    print('----')

    url = 'https://music.liuzhijin.cn/'
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        # 判断请求是异步还是同步
        'x-requested-with':'XMLHttpRequest',
    }

    param = {
        'name': name,
        'filter': 'name',
        'type': platform,
        'page': 1 
    }

    res = requests.post(url=url, data=param, headers=headers)
    res_json = res.json()



if __name__ == '__main__':
    search_music_by_name()