import requests
import time
import hashlib
import random
import json

# 爬取喜马拉雅的音乐的类
# https://blog.csdn.net/steadyhzc/article/details/99708520
# 这个接口可以直接获取 http://m.ximalaya.com/m-revision/page/album/queryAlbumPage/399914
class ximalaya(object):

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"
        }

    def getServerTime(self):
        """
        获取喜马拉雅服务器的时间戳
        :return:
        """
        # 这个地址就是返回服务器时间戳的接口
        serverTimeUrl = "https://www.ximalaya.com/revision/time"
        response = requests.get(serverTimeUrl,headers = self.headers)
        return response.text

    def getSign(self,serverTime):
        """
        生成 xm-sign
        规则是 md5(ximalaya-服务器时间戳)(100以内随机数)服务器时间戳(100以内随机数)现在时间戳
        :param serverTime:
        :return:
        """
        nowTime = str(round(time.time()*1000))

        sign = str(hashlib.md5("ximalaya-{}".format(serverTime).encode()).hexdigest()) + "({})".format(str(round(random.random()*100))) + serverTime + "({})".format(str(round(random.random()*100))) + nowTime
        # 将xm-sign添加到请求头中
        self.headers["xm-sign"] = sign
        # return sign

    def getInfos(self,albumId,pageNum,sort,pageSize):
        # 先调用该方法获取xm-sign
        self.getSign(self.getServerTime())
        # 将访问数据接口的参数写好
        params = {
            'albumId': albumId, # 页面id
            'pageNum': pageNum,
            'sort': sort,
            'pageSize':pageSize,# 一页有多少数据
        }
        # 喜马拉雅数据接口
        url = "https://www.ximalaya.com/revision/play/album"
        response = requests.get(url,params=params,headers=self.headers)
        infos = json.loads(response.text)
        return infos

if __name__ == '__main__':
    ximalaya = ximalaya()
    # print(ximalaya.getInfos('399914','1','1','30'))
    print(ximalaya.getInfos('399914','1','1','30').get('data').get('tracksAudioPlay')[9])
    print(ximalaya.getInfos('399914','1','1','30').get('data').get('tracksAudioPlay')[9].get('trackName'))
    print(ximalaya.getInfos('399914','1','1','30').get('data').get('tracksAudioPlay')[9].get('src'))
