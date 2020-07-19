#!/usr/bin/python3
import requests
import json
from bs4 import BeautifulSoup as b4
### Its simple thing shows that zee5 didn't care about their data theft😬😬 ###
class dl:
	def __init__(self, url, tk):
		self.url = url
		self.tk = tk
	def generate(self):
		r = requests.get(self.url)
		rr = r.content
			try:
				a = b4(rr, 'html5lib')
				b = json.loads(a.find_all("script")[9].prettify()[39:-11])["EpisodeDetail"]["episodeData"]['hls'][0].replace('drm', 'hls')
				xm = requests.get(self.tk)
				gj = json.loads(xm.content.decode('utf-8'))['video_token']
				if "index.m3u8" in b:
					pr = ("https://zee5vod.akamaized.net" + b + gj)
					if "index.m3u8" in pr:
						 ### For my convenience i used 576p . If u want to view  in different quality change pixel##
						cr = pr.replace('index.m3u8', 'index576p/576p.m3u8')
						print (cr)
				elif "master.m3u8" in b:
					print (b + gj)
			except KeyboardInterrupt:
				print ("quit")
az = input('\n Enter  TvShow link : ') 
zx = dl(az, "https://useraction.zee5.com/token/")
zx.generate()
