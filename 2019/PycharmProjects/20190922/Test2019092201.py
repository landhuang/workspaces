
import requests



'''爬取喜马拉雅服务器系统时间戳，用于生成xm-sign'''
def getxmtime():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Accept': 'text/html,application/xhtml+ xml,application/xml;q = 0.9,image/webp,image/apng,*/*;q=0.8, application/signe-exchange;v = b3',
        'Host': 'www.ximalaya.com'
    }
    url="https://www.ximalaya.com/revision/time"
    response = requests.get(url, headers=headers)
    print(response)
    html = response.text
    return html

