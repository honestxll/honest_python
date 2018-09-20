# coding = utf-8
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import json
import urllib
import time

url = 'https://h5.hulushequ.cn/bds/webapi/item/related/?item_id=6600261658122131725&parent_rid=81144811537421673192&share_app_name=pipixia&page_type=video&new_layout=1'


class Scarping:
    result = []

    def __init__(self, url):
        self.url = url

    def getJson(self):
        try:
            ret = urlopen(self.url).read().decode('utf-8')
        except Exception as error:
            print('出错了：', error)
        else:
            jsonDict = json.loads(ret)
            if jsonDict['status_code'] == 0:
                for item in jsonDict['data']['data']:
                    like_count = item['stats']['like_count']
                    if like_count >= 50000:
                        video_url = item['video']['video_download']['url_list'][0]['url']
                        video_title = item['video']['text']
                        placeholder = item['video']['video_download']['cover_image']['url_list'][1]['url']
                        local_video = 'videos/' + str(int(time.time())) + '.mp4'
                        local_img = 'images/' + str(int(time.time())) + '.jpg'
                        data_dict = {'title': video_title,
                                     'url': video_url, 'placeholder': placeholder}
                        if data_dict in self.result:
                            pass
                        else:
                            # 存入下载
                            data_dict['local_video'] = local_video
                            data_dict['local_img'] = local_img
                            self.result.append(data_dict)
                            self.download(video_url, local_video, 1)
                            self.download(placeholder, local_img, 2)
                            # 生成新的文件名

                        print('找到了%d个🤔' % len(self.result))

    def download(self, url, local, file_type = 1):
        directory = 'videos/'
        if file_type == 2:
            directory = 'images/'
        try:
            urlretrieve(url, directory + local)
        except Exception as error:
            print('下载文件的时候出错了：', error)
        else:
            print('下载' + directory[:-1] + '完成 🤭')

    def saveFile(self):
        file = open('result.json', 'w')
        file.write(json.dumps(self.result))
        file.close()


if __name__ == '__main__':
    scan = Scarping(url)
    while len(scan.result) < 10:
        scan.getJson()
    scan.saveFile()
    print('采集完成')
