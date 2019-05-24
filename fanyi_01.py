import requests
import json
import sys

# query_string=sys.argv[1]
query_string = input('请输入')
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36'}
data = {"query": query_string,
        "from": "en",
        "to": "zh", }


post_url = 'http://fanyi.baidu.com/basetrans'
r = requests.post(post_url,data=data,headers=headers)
dict_ret = json.loads(r.content.decode())
ret = dict_ret['trans'][0]['dst']
print('result is:', ret)