import requests
import openpyxl
import pandas as pd
import xlsxwriter
from requests_html import HTMLSession
import random,time

session = HTMLSession() # 自带了user-agent
import time
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Cookies":"buvid4=178AD660-EB46-D5D1-69DB-6F0F663E951B42110-022022201-FdTQVU3R1aR1u86ZnN2wLQ==; buvid3=81542DAD-7677-FEA9-A4FB-75B783D7901B56292infoc; b_nut=1650567755; _uuid=87E4AF8C-1FDD-16BC-E4DF-BEFBE28EE28656759infoc; LIVE_BUVID=AUTO1216505677623581; CURRENT_BLACKGAP=0; blackside_state=0; rpdid=|(u))lJm~~~)0J'uYl|lY~))R; i-wanna-go-back=-1; nostalgia_conf=-1; buvid_fp_plain=undefined; DedeUserID=37210060; DedeUserID__ckMd5=73e11faf519c77e9; b_ut=5; CURRENT_QUALITY=0; fingerprint=414ac0980fe51afdb1a0959a068e6223; SESSDATA=1d54d188,1666212591,2eb82*41; bili_jct=ad706f4fbfe2eeda8512447f84ad90b0; sid=c7h7j14p; buvid_fp=414ac0980fe51afdb1a0959a068e6223; bsource=search_baidu; UM_distinctid=1809f4fb62718f-0d0f49b0113e37-17333273-144000-1809f4fb628500; CURRENT_FNVAL=4048; PVID=1; innersign=0; b_lsid=2710553C3_180BB44B9EA; bp_video_offset_37210060=659578054660587500"
}
def get_data():
    """
    get_data函数是用于爬取B站每周必看的视频数据信息
    """
    for i in range(1, 161):
        res = session.get(
            # 该数据 并不在网页上，而是通过异步加载的方式获取的数据
            # 然后我们通过访问接口活得json数据
            url="https://api.bilibili.com/x/web-interface/popular/series/one?number={}".format(i),headers=headers
        )
        all_data = []
        # 查看是否爬取成功
        print(i, res.status_code, "数据获取成功！")
        # 获取接口返回的数据
        js = res.json()
        # 读取json文件的每个视频信息并存放到一个列表里面，用于后期的持久化
        week = i
        videos = js["data"]["list"]
        for rank, video in enumerate(videos):
            all_data.append(
                [
                    week,
                    rank + 1,
                    video["aid"],
                    video["tname"],
                    video["title"],
                    video["pubdate"],
                    video["owner"]["mid"],
                    video["owner"]["name"],
                    video["owner"]["face"],
                    video["pic"],
                    video["stat"]["view"],
                    video["stat"]["danmaku"],
                    video["stat"]["reply"],
                    video["stat"]["favorite"],
                    video["stat"]["coin"],
                    video["stat"]["share"],
                    video["stat"]["like"],
                    video["short_link"],
                    video["bvid"],
                    video["rcmd_reason"],
                ]
            )
#         print(all_data)

        src_data = pd.read_excel("hot_week20220418.xlsx")

        data = pd.DataFrame(all_data,
                            columns=["week", "rank", "aid", "tname", "title", "pubdate", "owner_mid", "owner_name",
                                     "owner_face", "pic", "view", "danmaku", "reply", "favorite", "coin",
                                     "share", "like", "link", "bvid", "rcmd_reason"])

        pd.DataFrame(src_data).append(data).to_excel("hot_week20220417.xlsx", index=False,encoding="utf-8")
        time.sleep(random.randint(1, 4))
 # 初始化excel表格用于数据存放
pd.DataFrame([], columns=["week", "rank","aid", "tname", "title", "pubdate", "owner_mid", "owner_name",#                               "owner_face", "pic", "view", "danmaku", "reply", "favorite", "coin",
                                       "share", "like", "link", "bvid", "rcmd_reason"]).to_excel("hot_week202200417.xlsx", index=False)
         #调用爬虫方法
get_data()