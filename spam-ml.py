#coded by Nubzbie
#Source-code
import requests, sys, json
from requests import post

Gameid = raw_input("Game id : ")
jml = int(input("Jumlah : "))

publicagent = {
  'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.12 Safari/537.36 OPR/14.0.1116.4',
  'referer':'https://m.mobilelegends.com/en/codexchange',
}

keke = {
  "gameid":Gameid,"captcha":"","language":"en",
}

mlkuy = requests.post("https://mapi.mobilelegends.com/api/sendmail", data=keke, headers=publicagent)
for i in range(jml):
  for x in mlkuy:
    y = json.loads(x)
    print ('Message : '+ y['message'])