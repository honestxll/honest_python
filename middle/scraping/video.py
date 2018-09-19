# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
import lxml.html


class Render(QWebEngineView):               # 子类Render继承父类QWebEngineView
    def __init__(self, url):
        self.html = ''
        self.app = QApplication(sys.argv)
        # 子类构造函数继承父类，这种写法python2和3通用，还可以是super().__init__()
        QWebEngineView.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self):
        self.page().toHtml(self.callable)

    def callable(self, data):
        self.html = data
        self.app.quit()


if __name__ == '__main__':
    url = 'http://h5.hulushequ.cn/item/6602744689781119245'

    r = Render(url)
    result = r.html

    tree = lxml.html.fromstring(result)
    # a = tree.cssselect('#result')[0].text_content()
    print(tree.text_content())
