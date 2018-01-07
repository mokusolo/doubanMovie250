scrapy爬取豆瓣电影前250
====
记录使用过程
----------------
1. $ virtualenv scrapySth
2. $ cd scrapySth
3. $ source bin/activate
4. $ pip3 install scrapy
5. $ scrapy startproject doubanMovie250
6. $ cd doubanMovie250
7. (make changes according to your need)
8. $ scrapy crawl doubanMovie250 -o doubanMovie250.csv
