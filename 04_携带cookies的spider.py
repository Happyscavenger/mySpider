import requests

session = requests.session()
post_url = 'http://www.renren.com/PLogin.do'
post_data = {'email':'131******23','password':'password'}
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36'}
session.post(post_url,data=post_data,headers=headers)
r = session.get('http://www.renren.com/966483194/profile',headers=headers)
with open('renren.html','w',encoding='utf-8')as f :
    f.write(r.content.decode())