from selenium import webdriver
from bs4 import BeautifulSoup

id = 6600261658122131725
url = 'https://h5.hulushequ.cn/item/%d'


class Scraping:
    result = []

    def __init__(self, driver, id, url):
        self.driver = driver
        self.id = id
        self.url_template = url
        self.file = open('result.txt', 'w')

    def getUrl(self):
        self.url = self.url_template % self.id
        return self

    def getRet(self):
        self.driver.get(self.url)
        html = self.driver.page_source
        soup = BeautifulSoup(html, features='lxml')
        video = soup.find('video')
        self.id += 2048
        if video:
            self.result.append(str(video))
            print('已找到%d个' % len(self.result))
        else:
            print('没找着 😪')
        return self

    def saveFile(self):
        for video in self.result:
            self.file.write(video)
        self.file.close()


if __name__ == '__main__':
    driver = webdriver.Chrome('/Users/honest/chromedriver')
    driver.maximize_window()

    scan = Scraping(driver, id, url)
    while(len(scan.result) < 10):
        scan.getUrl().getRet()
    scan.saveFile()
