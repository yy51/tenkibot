pip install twitter
from twitter import Twitter, OAuth

import requests
from bs4 import BeautifulSoup
import time

#Tenkiの取得
def Tenkijp(address):
    Url = "https://tenki.jp"

    Req = requests.get(Url + "/search/?keyword=" + address)
    Soup = BeautifulSoup(Req.text, 'lxml')


    Sed = Soup.find_all(class_="search-entry-data")

    HrfUrl = None
    for val in Sed:
        if val.find(class_="address").text.find("以下に掲載がない場合"):
            HrfUrl = val.a.get("href")
            break


    myDict = {}
    #住所からhrefを取得
    if not(HrfUrl is None):
        time.sleep(1) #一回requestを投げているので1秒待つ
        Req = requests.get(Url + HrfUrl)
        Soup = BeautifulSoup(Req.text, 'lxml')
        TodaySoup = Soup.find(class_="today-weather")

        ans = TodaySoup.find(class_="rain-probability").text

    return ans


def RainProbability(address):

    probability = Tenkijp(address) #ans = 降水確率+\n+ww%+\n+xx%+\n+yy%+\n+zz%
    data = probability.split() #data = ['降水確率', 'ww%', 'xx%', 'yy%', 'zz%']
    #print(data)

    data[0] = '0' #フラグの初期化, data = ['0', 'ww%', 'xx%', 'yy%', 'zz%']

    for i in range(1,5):
      data[i] = data[i].rstrip("%") #data = ['降水確率', 'ww', 'xx', 'yy', 'zz']

      if(data[i]!='---'):
        if(int(data[i])>=30): #降水確率が一つでも30%を超えていればフラグを1にする
          data[0] = '1'

    print(data)
    if(data[0]=='1'):
      #text = 'これはテストです'
      text= '今日の'+address+'は傘が必要です\n\n降水確率\n00～06時 '+data[1]+'%\n06～12時 '+data[2]+'%\n12～18時 '+data[3]+'%\n18～24時 '+data[4]+'%'
      print(text)
      return text
    else:
      return 0

RainProbability("広島県東広島市")


def main():
  access_token = "hogehoge"
  access_token_secret = "hogehoge"
  api_key = "hogehoge"
  api_secret = "hogehoge"

  t = Twitter(auth = OAuth(access_token, access_token_secret, api_key, api_secret))

  text = RainProbability("広島県東広島市")

  if(text!=0):
    statusUpdate = t.statuses.update(status=text)

    # 生の投稿データの出力
    print(statusUpdate)

    # 要素を絞った投稿データの出力
    print(statusUpdate['user']['screen_name'])
    print(statusUpdate['user']['name'])
    print(statusUpdate['text'])

main()
