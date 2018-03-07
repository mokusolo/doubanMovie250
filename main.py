# 为了在pycharm中调试，解决方案参考https://stackoverflow.com/questions/21788939/how-to-use-pycharm-to-debug-scrapy-projects

from scrapy import cmdline

cmdline.execute("scrapy crawl doubanMovie250 -o 11111.csv".split())
