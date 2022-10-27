import requests
from pprint import pprint
import pandas as pd
#from bilibili_api import video, sync
import datetime as dt
url_dict = {
	'综合': 'https://www.bilibili.com/v/popular/all',
	'全站': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all',
	'动画': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=1&type=all',
	'音乐': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=3&type=all',
	'舞蹈': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=129&type=all',
	'游戏': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=4&type=all',
	'知识': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=36&type=all',
	'科技': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=188&type=all',
	'运动': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=234&type=all',
	'汽车': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=223&type=all',
	'生活': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=160&type=all',
	'美食': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=211&type=all',
	'动物圈': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=217&type=all',
	'鬼畜': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=119&type=all',
	'时尚': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=155&type=all',
	'娱乐': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=5&type=all',
	'影视': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=181&type=all',
	'原创': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=origin',
	'新人': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=rookie',
}
headers = {
	'Accept': 'application/json, text/plain, */*',
	'Origin': 'https://www.bilibili.com',
	# 'Accept-Encoding': 'br, gzip, deflate',
	'Host': 'api.bilibili.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15',
	'Accept-Language': 'zh-cn',
	'Connection': 'keep-alive',
	'Referer': 'https://www.bilibili.com/v/popular/rank/all'
}

for i in url_dict.items():
	url = i[1]  # url地址
	tab_name = i[0]  # tab页名称
	title_list = []
	play_cnt_list = []  # 播放数
	danmu_cnt_list = []  # 播放数
	coin_cnt_list = []  # 投币数
	like_cnt_list = []  # 点赞数
	dislike_cnt_list = []  # 点踩数
	share_cnt_list = []  # 分享数
	favorite_cnt_list = []  # 收藏数
	author_list = []
	score_list = []
	video_url = []
	reply_list = []#评论数
	try:
		r = requests.get(url, headers=headers)
		print(r.status_code)
		# pprint(r.content.decode())
		# pprint(r.json())
		json_data = r.json()
		list_data = json_data['data']['list']
		for data in list_data:
			title_list.append(data['title'])
			play_cnt_list.append(data['stat']['view'])
			danmu_cnt_list.append(data['stat']['danmaku'])
			coin_cnt_list.append(data['stat']['coin'])
			like_cnt_list.append(data['stat']['like'])
			dislike_cnt_list.append(data['stat']['dislike'])
			share_cnt_list.append(data['stat']['share'])
			favorite_cnt_list.append(data['stat']['favorite'])
			author_list.append(data['owner']['name'])
			score_list.append(data['score'])
			reply_list.append(data['stat']['reply'])
			video_url.append('https://www.bilibili.com/video/' + data['bvid'])
			print('*' * 30)
	except Exception as e:
		print("爬取失败:{}".format(str(e)))

	df = pd.DataFrame(
		{'视频标题': title_list,
		 '视频地址': video_url,
		 '作者': author_list,
		 '综合得分': score_list,
		 '播放数': play_cnt_list,
		 '弹幕数': danmu_cnt_list,
		 '投币数': coin_cnt_list,
		 '点赞数': like_cnt_list,
		 '点踩数': dislike_cnt_list,
		 '分享数': share_cnt_list,
		 '收藏数': favorite_cnt_list,
		 '评论数': reply_list,
		 })
	date = str(dt.date.today())
	df.to_csv('B站TOP100-{}{}.csv'.format(tab_name,date))
	print('写入成功: ' + 'B站TOP100-{}{}.csv'.format(tab_name,date))
