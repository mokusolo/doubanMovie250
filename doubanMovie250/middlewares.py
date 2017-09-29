# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random


class Doubanmovie250SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    proxy_list = [
        "http://114.223.38.14:8118",
        "http://60.24.153.214:8118",
        "http://114.223.168.98:8118",
    ]

    def process_request(self, request, spider):
        ip = random.choice(self.proxy_list)
        print("ippppppppp", ip)
        request.meta['proxy'] = ip
