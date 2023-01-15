#此脚本用于获取讲座信息
from PIL import Image
import requests
import base64
import time
import json
import io

class Szpt_Baoming():

    def __init__(self):
        print("by: Eday")

    def Show_Qrcode(self, qrcode):
        import threading
        img = base64.b64decode(qrcode)
        img = Image.open(io.BytesIO(img))
        threading.Thread(target=img.show).run()
        print("请微信扫描二维码登录")

    def Main_Login(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }
        url="https://api-xcx-qunsou.weiyoubot.cn/xcx/enroll_web/v1/pc_code"

        s = requests.Session()
        html = s.get(url, headers=headers)
        html = html.json()#
        code = html['data']['code']
        result = html['data']['qrcode'].split(",")[1]
        self.Show_Qrcode(result)

        url="https://api-xcx-qunsou.weiyoubot.cn/xcx/enroll_web/v1/pc_login?code={}".format(code)
        for i in range(1,20):
            html = s.get(url, headers=headers).text
            html = json.loads(html)
            if html['msg'] == 'ok':
                print("扫码成功")
                print('已获取token:',html["data"]['access_token'])
                break
            time.sleep(1.3)
        else:
            print("已超时，请重新运行")
        token = html["data"]['access_token']
        return token

    def Get_Info(self,token):
        url="https://api-xcx-qunsou.weiyoubot.cn/xcx/enroll/v1/user/history?access_token={}".format(token)
        html = requests.get(url).text
        html = json.loads(html)
        for i in range(0,6):
            print("讲座{}:".format(i+1),html['data'][i]['title'])
        else:
            info = input("请输入要报名的讲座序号:")
            print("你选择的是:",html['data'][int(info)-1]['title'],'eid为:',html['data'][int(info)-1]['eid'])
if __name__ == '__main__':
    main = Szpt_Baoming()
    token = main.Main_Login()
    main.Get_Info(token)
