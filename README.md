#一个使用python编写的爬虫

>* 最终目的是为了完成一个完整稳定鲁棒性强的C++爬虫

##介绍

- 本开源项目目前包含了三个版本的简介爬虫
- 分别是：
1. C++（爬取指定网址信息）
2. Python2(可爬取百度贴吧单页图片，某些网站图片检索信息请自己查看图片审查元素进行匹配)
3. Python3(可爬取百度贴吧单页图片，某些网站图片检索信息请自己查看图片审查元素进行匹配)

## 问题解决

除C++/crawler1.cpp外其他爬虫程序均以验证可行

### 针对C++/crawler.cpp有如下建议

- c++程序建议在vs2010及其版本以上运行
- 若直接运行出错，做以下修改即可
 1. 点击project菜单
 2. 在弹出的菜单选项里选择最下面的“your_project_name Properties”
 3. 再选择“General”
 4. 最后把“Project Default”下的“Character Set”修改为“Use Multi-Byte Character Set”（默认为“Use Unicode Character Set”）即可

- sscnaf函数在vs2010下会产生警告，建议改成安全版sscnaf_s
- sscnaf函数在vs2013下会产生错误，必须改成安全版sscnaf_s
