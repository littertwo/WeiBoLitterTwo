
from weibo import Client
import webbrowser
from urllib import request
from urllib import parse
import ssl

APP_KEY = '74868326'
APP_SECRET = 'c6f2b4844139d8c1ef98b2af50594dfe'
CALLBACK_URL = 'https://www.baidu.com'

token = ''
c = Client(api_key=APP_KEY, api_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
myObject = Client(api_key=APP_KEY, api_secret=APP_SECRET, redirect_uri=CALLBACK_URL, token=token)

BIG_VIPIDS ='2858445711,3927703605'

def getCode():
    global c
    c.authorize_url
    webbrowser.open(c.authorize_url,1,True)
    return "1b5a23fda4c9e25efab9a8f799ec92b3"#每次不同

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
    print(myObject.get('statuses/home_timeline'))


#根据动态的id和评论内容进行评论
def commentWithDynamicIdandContent(dynamicID,content):
    global myObject
    # print(myObject.post('comments/create',id=dynamicID,comment=content))
    return myObject.post('comments/create',id=dynamicID,comment=content)


#根据评论id进行点赞
def zanWithCommentId(commentId):
    # url = 'https://api.weibo.com/2/attitudes/create.json'
    # global token
    # parmar = parse.urlencode({
    #     'attitude':'simle',
    #     'access_token':token['access_token'],#'2.007BkyKG0efIEF8b6a8f4dabH4ccsB'
    #     'id':commentId
    # })
    # parmar = parmar.encode('utf-8')
    # context = ssl._create_unverified_context()
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # req = request.Request(url=url,headers=headers,data=parmar)
    # response = request.urlopen(req,timeout=60,context=context)
    # URL：https: // api.weibo.com / 2 / attitudes / destroy.json#取消赞
    response = myObject.post('attitudes/create',id=commentId,attitude='simle')
    print(response)

if __name__ == "__main__":
    #获取code
    code = getCode()
    if len(code) > 0:
        # 获取token,生成可以直接调用api的对象myObject
        objest = getToken(code)
        # xuyang 3190974695
        # getBigVipDynamic(3190974695)
        # commentWithDynamicIdandContent(4126174533432348,"test2")
        zanWithCommentId(4126195131831592)
    else:
        print("还没有获取到code")