scrapy爬取豆瓣电影前250
====
记录使用过程
----------------
1. $ virtualenv scrapySth（为了各环境的独立性，创建虚拟环境）
2. $ cd scrapySth
3. $ source bin/activate（激活虚拟环境）
4. $ pip3 install scrapy（在虚拟环境中安装scrapy，安装完成后终端 $ scrapy 能看到版本信息等说明安装成功）
5. $ scrapy startproject doubanMovie250
6. $ cd doubanMovie250
7. （根据需求更改）
8. $ scrapy crawl doubanMovie250 -o doubanMovie250.csv
