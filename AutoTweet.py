import requests
import random 
import json
import time
from bs4 import BeautifulSoup


banner = """

        ░█████╗░██╗░░░██╗████████╗░█████╗░  ████████╗░██╗░░░░░░░██╗███████╗███████╗████████╗
        ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ╚══██╔══╝░██║░░██╗░░██║██╔════╝██╔════╝╚══██╔══╝
        ███████║██║░░░██║░░░██║░░░██║░░██║  ░░░██║░░░░╚██╗████╗██╔╝█████╗░░█████╗░░░░░██║░░░
        ██╔══██║██║░░░██║░░░██║░░░██║░░██║  ░░░██║░░░░░████╔═████║░██╔══╝░░██╔══╝░░░░░██║░░░
        ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ░░░██║░░░░░╚██╔╝░╚██╔╝░███████╗███████╗░░░██║░░░
        ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░░░╚═╝░░░

            Coded by : Remax Alghamdi - instagram : @ 0637871936 - Discord : Remax#6666 .
"""

print(banner)
time.sleep(3)


Words = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
token = (random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words))
ct0 = ''
auth_token = ''
tweets = open('list.txt', 'r', encoding='utf-8').read().splitlines()
username = input(str("Enter username : "))
password = input(str("Enter password : "))
times = int(input("Tweet every (Seconds) : "))
updatecook = int(input("cookies update  after ( ? ) tweets : "))


def login():
	session = requests.Session()
	url = "https://twitter.com/sessions"
	session.headers = {
	"Host": "twitter.com",
	"Content-Type": "application/x-www-form-urlencoded",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
	}
	cookies = {
	"_mb_tk":token
	}
	data = {
	"authenticity_token":token,
	"session[username_or_email]":username,
	"session[password]":password
	}
	response = session.post(url, data=data , cookies=cookies)
	r = session.cookies.get_dict()
	return r


def gettoken():
	tokens = login()
	cookie = tokens
	g = json.dumps(cookie)
	y = json.loads(g)
	c = str(y["ct0"])
	v = str(y["auth_token"])	
	ct0 = c
	auth_token = v
	print("Update Cookies .")
	print("ct0 = "+ct0)
	print("auth token = "+auth_token)
	tweet(cookie,ct0,auth_token)


def tweet(cookie,ct0,auth_token):
	x = 0
	while True:
		for tweett in tweets:
			x +=1
			if x <= updatecook:
				url = "https://twitter.com/i/api/1.1/statuses/update.json"
				headers = {
				"Host": "twitter.com",
				"Connection": "keep-alive",
				"authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
				"x-twitter-client-language": "ar",
				"x-csrf-token": ct0,
				"x-twitter-auth-type": "OAuth2Session",
				"x-twitter-active-user": "yes",
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
				"content-type": "application/x-www-form-urlencoded",
				"Accept": "*/*",
				"Origin": "https://twitter.com",
				"Sec-Fetch-Site": "same-origin",
				"Sec-Fetch-Mode": "cors",
				"Sec-Fetch-Dest": "empty",
				"Referer": "https://twitter.com/compose/tweet",
				"Accept-Encoding": "gzip, deflate, br",
				"Accept-Language": "ar,en;q=0.9,en-US;q=0.8"
				}
				cookies = cookie
				data = {
				"include_profile_interstitial_type":"1",
				"include_blocking":"1",
				"include_blocked_by":"1",
				"include_followed_by":"1",
				"include_want_retweets":"1",
				"include_mute_edge":"1",
				"include_can_dm":"1",
				"include_can_media_tag":"1",
				"skip_status":"1",
				"cards_platform":"Web-12",
				"include_cards":"1",
				"include_ext_alt_text":"true",
				"include_quote_count":"true",
				"include_reply_count":"1",
				"tweet_mode":"extended",
				"simple_quoted_tweet":"true",
				"trim_user":"false",
				"include_ext_media_color":"true",
				"include_ext_media_availability":"true",
				"auto_populate_reply_metadata":"false",
				"batch_mode":"off",
				"status":tweett
				}
				req = requests.post(url, cookies=cookies, data=data, headers=headers)
				print(req.text)
				print("Tweet done : "+tweett)
				time.sleep(times)
			else:
				gettoken()

gettoken()