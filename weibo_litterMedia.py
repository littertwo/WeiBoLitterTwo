
from weibo import Client
import webbrowser

APP_KEY = '74868326'
APP_SECRET = 'c6f2b4844139d8c1ef98b2af50594dfe'
CALLBACK_URL = 'https://www.baidu.com'

token = ''
c = Client(api_key=APP_KEY, api_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
myObject = Client(api_key=APP_KEY, api_secret=APP_SECRET, redirect_uri=CALLBACK_URL, token=token)

BIG_VIPIDS =''

def getCode():
    global c
    c.authorize_url
    webbrowser.open(c.authorize_url,1,True)
    return "b10a8b1d9b9d5f86f6e41d86f6a7985f"#每次不同


def getToken(code):
    global c
    c.set_code(authorization_code=code)

    global token
    token = c.token

    global myObject
    myObject = Client(APP_KEY, APP_SECRET, CALLBACK_URL, token)

def testApi(object):
    print (object)


#获取大V动态
def getBigVipDynamic(bigVipId):
    global myObject
    print(myObject.get('statuses/timeline_batch',uid=bigVipId))

if __name__ == "__main__":
    #获取code
    code = getCode()
    if len(code) > 0:
        # 获取token,生成可以直接调用api的对象myObject
        objest = getToken(code)
        getBigVipDynamic(BIG_VIPIDS)
    else:
        print("还没有获取到code")
    # http://weibo.com/aj/v6/like/add?ajwvr=6&__rnd=1499158073334点赞
    # testApi(objest)