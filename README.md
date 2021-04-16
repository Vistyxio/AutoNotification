# AutoNotification

## 概括：一个用来抓取网站新闻并推送到手机上的Python程序

## 初衷

学校会在官网发布各种重要的通知，但经常上官网看通知实属麻烦。且作为普通学生，唯一一条能够被动接收到通知的渠道就是“班级群”，而班级群上面还有“班委群”，班委群上面还要涉及到导员等院系和学校的工作人员。这条渠道里的通知由层层“官僚”把控，心情好了就转发，心情不好就忘了，这一层层中但凡有一人忘记转发，作为底层人民的我就收不到通知，短则几天，多则数周。正好前段时间入手了一个树莓派，便想到了写这么一个程序，直接从官网抓取新的通知发送到手机上。

## 环境

###### 树莓派环境：
树莓派4B 8G版本  
树莓派64位操作系统  
Linux内核版本5.10.17-v8+ aarch64  
Python 3.7.3  
pip 21.0.1  
需要使用的库（均为最新）sys、time、json、urllib、requests、re、BeautifulSoup

###### 手机环境：

IFTTT软件

## 概述

抓取学校官网上的新闻，与本地上一次抓取到的最新新闻对比，如有更新就把新闻的标题和链接等信息通过发送POST请求到IFTTT的链接（To trigger an Event. Make a POST or GET web request to:）。IFTTT会解析数据并给手机发送一个通知（就像QQ来消息那样的一个通知）。并把最新的一条新闻存到本地以便下一次抓取比对。

## 准备

进入IFTTT官网（ https://ifttt.com/home ），注册账号（邮箱密码即可）。  
![注册登录](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(8).jpg)  
进入My Applets，点加号新建。  
![进入my Applets](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(9).jpg)  
![创建](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(12).jpg)  
If this选择Webhooks，点击下面的蓝方框（Receive a web request），输入事件名称。  
![点击Add](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(13).jpg)  
![搜索Webhooks](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(14).jpg)  
![选择Receive a web request](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(15).jpg)  
![输入事件名称](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(16).jpg)  
Then that选择Notifications，根据需求选择两个蓝方框其一，左边是普通通知，右边是“rich”通知，可以包含更多的内容（Rich notifications may include a title, image, and link that opens in a browser or installed app.），我选择的是右边的Rich notifications，然后给通知中的各个部分定义变量名，按需确定。  
![点击Add](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(17).jpg)  
![搜索Notification](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(18).jpg)  
![二选一](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(19).jpg)  
![我选择了Rich notifications 定义变量名](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(20).jpg)  
![Create action](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(21).jpg)  
然后Continue、Finish。  
![Continue](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(1).jpg)  
![Finish](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(2).jpg)  
回到My Applets，点击刚创建的蓝框，进入其界面，点击名称上面的Webhooks标志，点击右上角的Documentation按钮，即可看到使用方法。  
![点击Webhooks标志](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(3).jpg)  
![点击Documentation按钮](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(4).jpg)  
看不懂没关系，先把 “https://maker.ifttt.com/trigger/{event}/等等等” 这样的一个链接复制出来保存，其中{event}就是刚才自定义的事件名称，可以直接替换，下面的JSON body也复制出来，用于发送“Rich notifications”中的标题、链接等信息。  
![记住key和链接还有json格式](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(5).jpg)  
同时手机下载IFTTT应用并登录，确保其能够后台发送通知，必要时关闭其电池优化。  
![手机上的IFTTT](https://github.com/Vistyxio/AutoNotification/blob/main/images/0%20(7).jpg)  

## 详细

* import库，如下。

######  给手机发通知部分：

* 需要准备如下的json格式数据（具体的IFTTT变量名和对应的变量名自行设定）。

* 然后按如下格式发送requests的POST请求即可（注意链接中的{event}要改成IFTT中设置的事件名称）。

###### 抓取新闻列表部分：

* 

## 使用



## 安全

由于使用了第三方软件IFTTT，因此尽量不要发送包含个人信息、内部通知、涉及机密等敏感内容的通知。
