"# bigdata" 

1 修改pip源地址；

C:\Users\用户名\AppData\Local\pip
```
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
```
或者
```
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
```
返回日志： Writing to C:\Users\Administrator\AppData\Roaming\pip\pip.ini
***
2 使用.env和.flaskenv进行配置，需要pip按照python-dotenv


### markdown 语法
- [ ] 任务一 未做任务 `- + 空格 + [ ]`
- [x] 任务二 已做任务 `- + 空格 + [x]`

 *斜体*或_斜体_
 
**粗体**

***加粗斜体***

~~删除线~~

++下划线++

==背景高亮==

欢迎阅读 [择势勤](https://www.jianshu.com/u/16d77399d3a7 "择势勤")

* 无序列表项 一
+ 无序列表项 二
- 无序列表项 三

：   轻量级文本标记语言（左侧有一个可见的冒号和四个不可见的空格）

[TOC]