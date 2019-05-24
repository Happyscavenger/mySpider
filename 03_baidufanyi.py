import requests
import json
class BaiduFanyi():

    def __init__(self,query_string):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36'}
        self.lang_url = 'http://fanyi.baidu.com/langdetect'
        self.trans_url = 'http://fanyi.baidu.com/basetrans'
        self.query_string = query_string

    def parse_url(self,url,data):
        # 发送请求，获取响应
        response = requests.post(url,data=data,headers=self.headers)
        return json.loads(response.content.decode())

    def get_ret(self,dict_response):
        # 获取翻译结果
        ret = dict_response['trans'][0]['dst']
        print('result is:',ret)

    def run(self):
        # 实现主要逻辑
        # 准备post的url地址，post_data
        lang_detect_data = {'query':self.query_string}
        # 发送post请求获取响应,获取输入的类型
        lang = self.parse_url(self.lang_url,lang_detect_data)['lan']
        # 提取语言类型
        # 准备post数据
        if lang == 'zh':
            trans_data ={'query':self.query_string,'from':'zh','to':'en'}
        else:
            trans_data={'query': self.query_string, 'from': 'en', 'to': "zh"}
        # 发送请求，获取响应
        dict_response = self.parse_url(self.trans_url,trans_data)
        # 提取翻译结果
        self.get_ret(dict_response)

if __name__ == '__main__':
    while True:
        query_string = input('请输入你要翻译的字段')
        fanyi = BaiduFanyi(query_string)
        fanyi.run()
        if query_string == '0':
            break