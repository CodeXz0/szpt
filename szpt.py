import requests
import json
import random
import base64
import re
from Crypto.Cipher import AES
from bs4 import BeautifulSoup

class szpt:
    def __init__(self):
        print("开始登录")
        
    def rds(self,length):
        chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'
        return ''.join(random.choice(chars) for i in range(length))
        
    def padding(self,data, iv):
        length = len(iv)
        bytes_length = len(data.encode('utf-8'))
        padding_size = length if (bytes_length == length) else bytes_length
        padd = length - padding_size % length
        padding_text = chr(padd) * padd
        return data + padding_text

    def szpt_encrypt(self,data,key):
        key = key.encode('utf-8')
        iv = self.rds(16).encode('utf-8')
        data = self.rds(64)+data
        cipher = AES.new(key, AES.MODE_CBC, iv)
        content_padding = self.padding(data, iv)
        encrypt_bytes = cipher.encrypt(content_padding.encode('utf-8'))
        result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
        return result

    def main(self):
        user = input("请输入学号：")
        passwd = input("请输入密码：")

        s = requests.session()
        url="https://authserver.szpt.edu.cn/authserver/login?service=https://i.szpt.edu.cn/deal_with_st"

        html = s.get(url)
        cookie_dict = requests.utils.dict_from_cookiejar(s.cookies)
  
        key = re.search('<*?id="pwdEncryptSalt".*?value="(.*?)".*?>', html.text).group(1)
        execution = re.search('<*?id="execution".*?value="(.*?)".*?>', html.text).group(1)
        
        headers = {
            "Host": "authserver.szpt.edu.cn",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "279",
            "Origin": "https://authserver.szpt.edu.cn",
            "Referer": "https://authserver.szpt.edu.cn/authserver/login?service=https://i.szpt.edu.cn/deal_with_st",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Te": "trailers",
            "Connection": "close",
        }
        url = "https://authserver.szpt.edu.cn/authserver/login"
        data = {
            "username": user,
            "password": self.szpt_encrypt(passwd,key),
            "_eventId": "submit",
            "cllt": "userNameLogin",
            "dllt": "generalLogin",
            "lt": "",
            "execution": execution
        }
        response = s.post(url, headers=headers,data=data)
        soup = BeautifulSoup(response.text, 'lxml')
        msg = soup.find('span', id='msg')
        if msg == None:
            print("登录成功")
            html = s.get(response.url)

        else:
            print("登录失败："+msg.text)
            exit()
        #获取考勤打卡记录
        url = "https://i.szpt.edu.cn/zsy_jiekou_kq?row=25&blcode=kqdk&manuid=&manrid="
        response = s.get(url)
        data = json.loads(response.text)
        print(data['mkmc'])
        for i in range(0, len(data["data"]["kaoqin"])):
            print('课程名称：{}，考勤记录：{}，打卡时间：{}'.format(data["data"]["kaoqin"][i]["KCMC"],data["data"]["kaoqin"][i]["KQJQ"],data["data"]["kaoqin"][i]["DKSJ"]))
if __name__ == '__main__':
    szpt = szpt()
    szpt.main()

#by Crypt
