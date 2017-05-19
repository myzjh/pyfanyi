# coding:utf-8
'''
Created on 2017年3月28日

@author: zhangjh
'''
import requests
import pyttsx

class Tran:
    # 翻译
    def translate(self, keyword):
        lang = self.LangDetect(keyword)
        url = 'http://fanyi.baidu.com/v2transapi'
        params = {'from':lang, 'to':'zh', 'query':keyword, 'transtype':'realtime', 'simple_means_flag':3}
        response = requests.post(url, data=params)
        json = response.json()
        if not json:
            print 'no json' + json
            response = requests.post(url, data=params)
        simpleMean = json['trans_result']['data'][0]['dst']
        means = json['dict_result']['simple_means']['word_means']
#         for m in json['dict_result']['simple_means']['word_means']:
#             simpleMean = simpleMean.join(','+m)
        ms = u'，'.join(means)
        return simpleMean + ',' + ms
    # 检测输入的语言
    def LangDetect(self, keyword):
        url = 'http://fanyi.baidu.com/langdetect'
        params = {'query':keyword}
        response = requests.post(url, data=params)
        print not response
        print response
        if not response:
            response = requests.post(url, data=params)
        json = response.json()
        return json['lan']
    
    # 朗读
    def speak(self, keyword):
        speaker = pyttsx.init()
        # 控制语速 default 200
        speaker.setProperty('rate', 120)
        # 控制音量 default 1.0
        speaker.setProperty('volume', 1.8)
        speaker.say(keyword)
        speaker.runAndWait()
    
# app = Tran()
# result = app.translate('cosplay')
# print result
# app.speak(result)
# app.speak(u'''s''')
# jsono = json.loads(result)
# print jsono['trans_result']['data'][0]['dst']
# for mean in jsono['dict_result']['simple_means']['word_means'] : 
#     print mean

# print app.LangDetect("dark")
