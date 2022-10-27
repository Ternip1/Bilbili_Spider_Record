# _*_ coding : utf-8 _*_
# @Time : 2022/4/23 2:49
# @Author : luocheng
# @File : 更新时间
# @Project : test
# _*_ coding : utf-8 _*_
# @Time : 2022/4/23 2:37
# @Author : luocheng
# @File : 追番人数
# @Project : test
#追番人数
import random
import requests
import os
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "cookies":"_uuid=34A1529E-99E2-E45B-344B-47D78B5B881738006infoc; b_nut=1645462840; buvid3=D5AF3015-3AE0-F7FA-BCBB-4F1964F9741842110infoc; buvid4=178AD660-EB46-D5D1-69DB-6F0F663E951B42110-022022201-FdTQVU3R1aR1u86ZnN2wLQ==; LIVE_BUVID=AUTO5716456234292189; buvid_fp_plain=undefined; SESSDATA=671f5f47,1661530926,17ace*21; bili_jct=1e69f407a26e5f0a331552835e682a03; DedeUserID=37210060; DedeUserID__ckMd5=73e11faf519c77e9; sid=9b35b5pp; i-wanna-go-back=-1; b_ut=5; buvid_fp=877a0ce25ec0453d3eb99f8a4c1a80b2; blackside_state=1; rpdid=|(u))lJm~lkm0J'uYRlm~mkYk; CURRENT_BLACKGAP=0; nostalgia_conf=-1; CURRENT_QUALITY=116; fingerprint3=7eadfed897109e9c358a02a192666324; fingerprint=554c9663db9fa6e02cd30802a993973c; PVID=2; bsource=search_baidu; bp_video_offset_37210060=651615138022948900; b_lsid=10D6CC119_1804D4787A1; innersign=1; CURRENT_FNVAL=4048"
}
i = 1
file = "更新时间rank.csv"
url = "https://api.bilibili.com/pgc/season/index/result?season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=0&st=1&sort=0&page="+str(i)+"&season_type=1&pagesize=20&type=1"
for i in range(1,163):
    res = requests.get(url,headers=headers)
    df = pd.DataFrame(res.json()['data']['list'])
    df.to_csv(file,index=False, mode='a',header=not os.path.exists(file), encoding="u8")
    i +=1
    time.sleep(random.randint(1,8))