from urllib.request import urlopen
import json

rid = 6602744689781119245
target = 1
urlDemo = 'https://h5.hulushequ.cn/bds/webapi/item/related/?item_id=1&parent_rid=%d&share_app_name=pipixia&page_type=video&new_layout=1'


def getJson(url, rid):
    while rid < 10000:
        try:
            ret = urlopen(urlDemo % rid).read().decode('utf-8')
        except Exception as error:
            print('出错了', error)
        else:
            ret = urlopen(urlDemo % rid).read().decode('utf-8')
            getVideo(ret)
            rid += 1


def saveFile(obj, filename, mode='w'):
    file = open(filename, mode)
    file.write(str(obj))
    file.close()


def getVideo(obj):
    global target
    jsonDict = json.loads(obj)
    # saveFile(str(jsonDict), filename='dict.json')
    if jsonDict['message'] == 'success':
        if jsonDict['data']['data'][0]['stats']['like_count'] > 50000:
            print('找到%d个' % target)
            saveFile(jsonDict['data']['data'][0]['video']
                     ['video_download']['url_list'][0]['url'] + '\n', 'result.txt', 'a')
            target += 1


if __name__ == '__main__':
    getJson(url=urlDemo, rid=1)
