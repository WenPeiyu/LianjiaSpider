# LianjiaSpider
Lianjia, *connecting house* in Chinese, is the biggest housing agency in China, 
whose business covers most cities and most types of real estate business.
Many project is aimed at build a web crawler to fetch the housing transaction data on [LianJia](www.lianjia.com),
however, the website has various anti-crawler techs. 
Inspired by the [article1](https://blog.csdn.net/oXieNiMa/article/details/81705916) and [article2](https://www.jianshu.com/p/ffff30c5a0f7), 
I build a web crawler by a js api in [LianjiaDitu](https://sh.lianjia.com/ditu/). 
The key point of using this api is how to generate the authorization code from parameters. 
I learn much from the above referenced article about browser js debugging, 
which helps me to know deeply about the authorization generated process.

## Version
+ 0.1 traditional crawler
+ 0.2 api crawler

## TODO
+ multi-threading
+ general database interface
+ data analysis 
+ visualization
+ command line interface or GUI

