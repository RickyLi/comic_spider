# comic_spider

###最近在追一个漫画，网页上看垃圾广告太多就想自己被图片爬下来下到本地看，所以花了两天时间用python写了一个简单的爬虫
###写的比较挫，写的过程中也是在网上各种找资料，资料真的是多啊，这里也只是记录一下

程序主要分三部分：
1、获取章节的链接地址  对应getUrl.py文件
2、从章节第一页中获取章节有多少张图片  对应getInfo.py文件
3、循环每章节每页，下载图片到本地  对应downImage.py文件
