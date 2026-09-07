% 《这本书能让你连接互联网》
% hoochanlon
% 

# 《这本书能让你连接互联网》

原书在线版：https://hoochanlon.github.io/fq-book/#/

源仓库：https://github.com/hoochanlon/fq-book

许可：Creative Commons BY-NC 4.0（允许非商用分享与演绎）

本 EPUB 由 Docsify Markdown 源文件按官方目录自动转换，供微信读书等本地阅读器导入使用。远程插图依赖原图床/IPFS，离线环境可能无法显示图片，正文不受影响。

---

# 关于本书

## 前言

本书着重于上网的方式与获取网站信息的技巧，并对相关流行且主要且典型的软件做简要的上手配置，以及原理的相关说明。

VPN、Proxy不时也会出现新应用，操作方式多数基本也大同小异；当然，随着长城的升级或是自身服务器等问题导致甚至较长期间无法使用，甚至服务商跑路造成完全失效，实在没必要每个软件操作都面面俱到；但只要把步骤方法要点及原理讲明白，其实这些都是触类旁通的。掌握了书中这些技巧与方法，以后面对新事物也是可以快速上手的，如有疑难可以在本书项目中发起相关issues。

相关技术资料过于繁杂而且各种封锁手段的程度也较为严重，自搭使用免费云又需要限制条件很高visa信用卡；不过可以办一张中国银行的银联卡，买美元转账到visa借记卡；但这对于平常的普通网民来说，实在太过于麻烦了。

此书针对的受众是追求自由免费地互联网且有意向了解计算机专业的相关人群等，不过也因本人知识水平有限，同时也避免重复的“造轮子”，对细节原理等方面需要参考维基或转载及演绎其他作者的一些相关文章，因此允许演绎该作及共享但禁止商用。

由于需要使用jakarta各项相关产品与内容等等；仅此，科学上网只是为研究需要，以下是免责声明：

* 本书面向海外华人用户且仅供科研与学习，切勿用于其他用途
* 中国居民请自觉关闭本书并24小时内删掉与此相关的所有内容，否则出现一切后果本书作者概不负责

此书献给热爱互联网的人们，以上...

***[About Me（关于作者）](https://hoochanlon.github.io/hoochanlon/hcl/index.html)***


# 阅读须知

## 4GFW

> **【重要】** GFW本质上是巨大的高性能分布式入侵检测维稳系统并不是单纯的防火墙

<!-- ![](https://ipfs.io/ipfs/Qme29LCkkA2XrjLZtzaGsmgMmSL1y3wn2nyXE749E7zD4i?3.png) -->

![](https://i.postimg.cc/QNqxQy7t/2018-05-23-210035.png)

摘自维基百科：[互联网审查](https://zh.wikipedia.org/zh-hans/%E4%BA%92%E8%81%94%E7%BD%91%E5%AE%A1%E6%9F%A5)

![](https://i.postimg.cc/vHvnMVWq/Snipaste-2019-06-06-14-06-20.png)


## 注意事项

> **【说明】** 示例以Win10为准，mac步骤可能会略有不同，但方法思路可以说是一致的
搭建VPS节点、镜像、网页代理以及刷路由等，其限制条件较高，故并未涉及此
在高校使用VPN，需安装使用经特殊处理的校园网客户端，若使用代理则不必考虑它
网游互联需关注本机客户端与远程服务器之间的UDP转发支持及当前NAT类型
刷梅林路由这类网关翻墙，可防游戏厂商因作弊将其封杀，还可共享直连翻墙网络
提供自搭条件的VPN使用协议、数据流量等各方面特征明显，易被GFW监测并封杀
付费VPN比代理的使用操作更简单且稳定性高很多，无需过多关心NAT类型与协议转发
为了有效合理的使用VPN或代理服务，请在系统`国家/地区`选项中改成香港地区
科学上网的细节原理等各方面的解释，可参考书中科学普及与细节补充等相关章节

<!-- > * **代理账号分享站点不因网速而特别的卡顿很可能它占用CPU资源开始挖矿了** -->
<!-- 购买ss账号事先请询问卖家该账号的服务器是否支持UDP转发以免被坑导致不愉快 -->
<!-- 搭建镜像站点也只能访问一些特定网站，因此不在该书涉猎范围内 -->
<!-- 使用梅林路由刷机装代理插件本机转发UDP，可防游戏厂商误认为外挂将其封杀 -->
<!-- 示例以Win10为准，mac步骤可能略有不同，但方式总的来说上是一致的 -->
<!-- 搭建VPS节点受限较高，而镜像也仅限于访问特定站点，故不在涉猎范围 -->
<!-- > * **建议别到以邀请码传销性质的ss站点购买账号** -->


## 隐私防护

> **【说明】** 需要提供正反面持照信息与证件号时，请搜索一些相似图片或使用相关生成
需要提供个人手机号码时，请用个人购买的专属虚拟电话，公用的很多已失效
需要提供个人验证邮箱时，请用临时邮箱注册该不受信任的站点测试体验其功能
软件产品方面尽量使用国外的，因为国内制度和谐严重且毫无新意并带有流氓问题
对个人隐私极其看重的话，在使用不可替代的国产软件时，还是放在虚拟机中运行
使用Tor+VPN等结合使用浏览网页，已基本满足对上网隐私信息的匿名安全保障
讨论有关NSFW话题时，使用安全的VPN或代理来参与非国内的自由开放社交问答平台
在IPFS中请谨慎上传隐私文件，该系统会永久储存且任何人都不能对文件进行相关修改
编写程序或制作连接互联网教程的网络ID最好与国内社交等注册ID隔离
存储zeronet的`users.json`验证账号文件不要轻易外泄，以免造成被迫下线等不必要的损失
最后，Google 搜索一下 `安全科学上网` 一般经验都是来自搜索、实践与总结

<!-- 棱镜门与防火长城本质是一样都是监控维稳，总之这是一个隐私换效率的时代
绝对的隐私是不存在的，虽协助政府监控但企业并不会将个人隐私公开化处理（国外） -->
<!-- > * **telegram、g+、quora等都是很不错的互动社交平台，最重要的是学好英语走遍天下都不怕** -->


# 快速开始

## 快速入手

## 速成索引

> **【提示】** 首先，**了解必要的proxy、VPN软件配置与使用方式**，接着 **使用web代理访问提供服务器的网站获取节点** 或是 **离线安装Chrome代理插件并访问该站获取节点**，再结合 **方法论** 配置代理或VPN软件进行科学上网。
>
> * **有基础的**：可直接通过阅读方法论篇章，做到快速吸收，触类旁通，其他篇章均为程式工具上的补充，可选择性阅读。
> * **没有基础的**：建议跳过方法论篇，阅读相关的VPN、代理工具使用章节等，了解并加以实践工具的使用，再来看方法论。
>
> 以上两点是对此的补充说明。

****掌握必要的代理配置及 VPN 的使用**
** 

  * [SS/SSR](#)
  * [v2ray](#)
  * [SSH-Tunnel](#)
  * [网页代理的使用](#)
  * [典型VPN概览](#)
  * [opera](#)（注意示例中以压缩包的形式安装Chrome插件）

****方法论**
** 

  * [获取梯子上网的方式](#)

> **【说明】** 快速开始仅为速成互联，关于科学上网的细节原理等各方面的解释，可参考书中科学普及与细节补充等相关章节

## 速成示例

速成示例作业站点由 [WebOutlook](https://github.com/hoodiearon/WebOutlook) 提供支持

![](https://i.postimg.cc/Fz2bDWSs/Snipaste-2019-07-01-04-27-55.png)

### chrome 离线安装代理扩展插件

借助 [173app](https://173app.com) 下载 [skyzip](https://173app.com/apps/hbgknjagaclofapkgkeapamhmglnbphi) 

![](https://i.postimg.cc/jq4Q0cr9/Snipaste-2019-07-01-03-43-31.png)

将下载好的插件 `.crx` 格式改为压缩格式 `.zip` 并解压

![](https://i.postimg.cc/brnvP3Z5/Snipaste-2019-07-01-03-51-18.png)

在`开发者模式` 选中 `加载已解压的扩展程序` 即可

![](https://i.postimg.cc/hjzCSdcw/hasi9.png)

打开扩展开关并点亮 skyzip 成绿色

![](https://i.postimg.cc/ht2rS7yz/Snipaste-2019-07-01-04-12-46.png)

测试

![](https://i.postimg.cc/PqGqvSFB/Snipaste-2019-07-01-04-15-42.png)

### free-ss.site 节点导入影梭

先在 [github](https://github.com/) 上搜索 `shadowsocks-windows` 并下载此代理软件；win7需要下载此类框架运行环境，win10自带。

![](https://i.postimg.cc/dtxRWXJR/Snipaste-2019-07-01-02-52-33.png)

利用 skyzip 打开 https://free-ss.site

![](https://i.postimg.cc/zfxpz271/Snipaste-2019-07-01-04-54-26.png)

也可借助 [jsproxy](https://github.com/EtherDream/jsproxy/) 项目提供的 [web代理网址](https://jsproxy.ga/)，在此基础上又嵌套一个web代理 [croxyproxy](https://www.croxyproxy.com/) ，用以加载爱国上网服务器网站节点信息。

** 嵌套操作 **

?> 嵌套的原因是：虽然有些web代理没被墙，但并不会完全加载各个网站的相关脚本等其他代码，所以就用到其他web代理（也有很多被墙的）作为嵌套使用。

![](https://i.postimg.cc/7YsJHTcq/new11.png)

`鼠标 Shadowsocks 右键 -> 服务器 -> 扫描二维码` 添加节点服务器

![](https://i.postimg.cc/15vSbGdr/Snipaste-2019-07-01-00-03-43.png)

配置地址:`127.0.0.1` 端口:`1080` 并确定

![](https://i.postimg.cc/MHvGF9YN/Snipaste-2019-07-01-03-21-10.png)

将 `系统代理` 开启并测试

![](https://i.postimg.cc/K8qTfcMv/Snipaste-2019-07-01-04-44-42.png)

### tunsafe 导入配置作业

进入[tunsafe官网](https://tunsafe.com/)，可以看到此外它还提供独立的虚拟网卡和软件（集合安装器需要全局翻墙环境），然后下载并安装这两个文件。

![](https://i.postimg.cc/1XRCdppx/20190607083401.png)

安装很简单，默认就行；注意勾选下始终信任项目就好了。

![](https://i.postimg.cc/Z5LLG954/20190607083553.png)

在 `user guide` 选择 `using tunsafe windows`接着再选择`free vpn servers`

![](https://i.postimg.cc/7LKsW3r8/20190606205200.png)

点击 `create new account`，选择服务器，然后生成下载该配置文件，**建议下载多个配置文件测试连接效果**。

![](https://i.postimg.cc/63NrzTyJ/20190606205536.png)

打开软件在`File`项中选择`browse in explorer` 就会打开软件配置目录源

![](https://i.postimg.cc/hv8Qj0rf/Snipaste-2019-06-06-21-11-36.png)

将下载好的conf导入到该目录

![](https://i.postimg.cc/SRYVwsqj/20190607092202.png)

如果连接不上，那换一个服务器连接测试，即可

!> 也有可能存在恶意禁用的问题，详情请看：[简谈国产杀软 - 恶意禁用连接互联网服务问题](append/guochan-sharuan?id=恶意禁用连接互联网服务问题)

![](https://i.postimg.cc/T3RbDfrP/Snipaste-2019-06-07-08-54-24.png)


# 方法论

## 获取梯子上网的方式

!>在访问该类站点时，请注意ta的邮箱、镜像、分享地址、订阅源等相关信息，如果打开网址不是因为网速而特别的卡顿，注意它已经挖矿了，关闭并长期不再访问它。
由于部署项目可改写相关代码的原因，资助之类的二维码，并不是原作者或该站所有者本人，也就是说用此筹众敛财罢了；有些coder或是维护人员不了解也不注重网页优化。因此，有些部署在云平台上的网址是无法被搜索引擎抓取到的。
不过，输入一些关键词，在云平台二级域名却很容易找到，示例在以下herokuapp主题中； 可以说此类网址有点类似暗网的隐蔽性质，仅个人认为用deep network描述它比较合适点。
涉及到的相关站点与软件，只是方法中一个具体的示例，关于此类站点或软件还有很多，随着社会逐移的加速发展，部分站点可能会失效。
ps：关于更详细的站点收录，请点击参考此github项目[hamuleite](https://github.com/hoochanlon/hamuleite)

* doub

![](https://i.postimg.cc/QdbQ863Q/doub-io-sxsx-131.png)

![](https://i.postimg.cc/KjBTdffg/doub-io-sxsx-132.png)

* herokuapp

![](https://i.postimg.cc/Nft2K1bp/2018-05-01-191319.png)

## 获取梯子上网的方式

获取此类工具的方式有很多，关键是留心，以下列出这常见的一些方式：

* 利用搜索引擎

    [qwant](https://www.qwant.com/)搜索相关翻墙软件的关键词，页面中的各类资料等等都很完善很是不错；顺带使用[similarsitesearch](https://www.similarsitesearch.com/cn/)查询相似站点

* 对含有爱国软件信息的站点进行查找

    使用[github](https://www.github.com/)搜索相关的关键词`vpn`、`v2ray、ss/ssr分享`等字眼，即可有相关软件下载以及节点使用

* 使用VPN或代理

    在已有能够连接互联网的VPN或代理的情况下，又继续 Google 查找并下载其他的爱国上网软件工具

* 发送Email邮件

    有些提供爱国软件的公司/组织会开设一个邮箱，用于自动回复科学上网工具以及页面镜像地址。比如：发送标题为`help`给`get@psiphon3.com`

* 打开镜像站点

    打开相关镜像站点页面进行浏览或下载资源等各类操作，示例镜像（已失效 2019）：[SS分享论坛镜像](https://www.ssrshare.xyz/)

* web代理或代理浏览器

    网上找一个加密的Web代理浏览被屏蔽的页面，通常玩搜索引擎越溜越容易找到，示例：[anyproxy](https://www.anyproxy.cn/)，顺带使用tor、puffin、upx等代理浏览器完成翻墙并获取其他相关爱国上网软件

* 浏览器扩展下载站

    使用[chrome-extension-downloader](https://chrome-extension-downloader.com/)下载相关代理插件，再通过其翻墙后又获取其他科学上网工具，VPN以及Web代理获取此类工具的方式同理

* 修改hosts、DNS

    IP/服务器地址查询，取得相关SS站点与VPN官网IP地址并添加进hosts，结合一些知名的DNS或是使用DNS加密软件防止污染，以打开部分SSR分享站点或是VPN官网等相关网址获取相关工具。

* P2P下载

    P2P协议是加密传输的且由于其分布式的特点，GFW难以搞敏感词过滤以及赶尽杀绝。连上某个[eMule](https://www.emule-project.net/home/perl/general.cgi?l=42)服务器后即可搜索`tor`等相关工具了

* 移动设备

 ?> 较多数爱国软件会限制中国用户，建议更安卓手机地区首选项语言，例如修改成含有中文的国家：新加坡；共享 PC 互联网网络，再利用原生安卓系统下载Google商店安装并下载相关代理或VPN软件。ps：手机没有刷权限的话，选择免费翻墙工具进行科学上网，那就请使用谷歌空间、Turbo、ssr吧。

* 个人博客及视频平台

 一些私人博客出于某种目的（技术分享，客流营销），为了吸引更多的访客，也会开放几个代理节点分享，即使需要注册的，最多个临时邮箱注册后拿来用就行了；油管up主也会制作许多翻墙教程，这里推荐油管up主，作为示例：[浪漫生活](https://www.youtube.com/channel/UCCHgXss80ZgWlwGCDDnZ5tg)、[ImShuker](https://www.youtube.com/channel/UCOe8kqJurA5WOzgC0pbjc2Q)

* 社会工程学

    如果你有朋友在外企、有熟人在国外再者有技术宅男，可以找他们要一份翻墙工具。最好是压缩并配上密码，因为GFW已经有对无加密压缩文件的深度检测能力

* 求助网络

    用**社交软件或是问答、综合社区**等进行相关求助，如果你只能在国内局域网环境，这个方法也是效果最差的了...不过，你可以这样做，下载[teleplus](https://play.google.com/store/apps/details?id=in.teleplus&hl=zh)这套着内置代理壳等软件进行订阅相关爱国上网分享频道：
    * [SSR V2ray Share](https://t.me/freeshadowsock)
    * [V2ray,Vmess免费节点发放](https://t.me/V2list)
    * [免费vpn评测](https://t.me/vpnchina)
    * [Telegaram Socks5 Proxies（tg代理）](https://t.me/TgProxies)
    * [账号圈](https://t.me/XRAcc) （如果有兴趣玩玩STORM Cracker扫描节点代理等可用账号，也尝不可）
    
* **Github，熟练的使用Github，这非常的重要！网页时光机做个备份，PDF用来留底吧(⊙ω⊙)**

    这个市场很广，毕竟是刚需，总有些为了宣传推广软件的人会在GitHub发布相关的软件广告，比如说：[小三VPN](https://github.com/sharmajv/vpn) 、老王VPN等等同类之流，可以试着体验，借着免费体验期换一个长期更好VPN提供商。

    什么是更好的VPN？家庭级的独立IP，非共用、万人骑的IP，快速稳定，长期维护和更新，有较好的售后服务，并拥有大量的稳定客户的VPN。

* **战略家模式**

   **先抛砖引玉吧：**

    * [如何着手分析一个行业？](https://www.zhihu.com/question/20219092)
    * [行业分析，就这个框架就够了](https://zhuanlan.zhihu.com/p/42983413)
    * [如何快速地了解一个陌生行业/领域？](https://www.zhihu.com/question/19698319)
    * [随机生成用户密码邮箱&知乎免登录的方法](http://chromecj.com/productivity/2019-05/2681.html)
   
    **这个“玉”就是你自己！收集各类相关资料并结合word、excel、ppt、mind、uml等相关软件进行数据分析，与同好朋友或是网络、软件相关人探讨并以实践加以论证**

多数人算得上精致的利己主义者吧，反正拿来用就是还管这么多，实在失效了，大不了换个站点就是了。能够提出改善等建议的用户几乎没有...最多收到过几封感谢信，没收到F词的邮件就不错了...我在站点嵌入 Google UA(user analytics) 得到的数据：基本上待在ss分享站点的时长就是已连接到互联网的时长，一两分钟而已，过后就转向其他地方了...

绝大多数国人的 PR、issue 均是一坨大便！PR都是很low的readme上的语言描述修改，部分配置文件的简单修改提交，也并不保证完善性，属于临时性bug补丁；issue除了刷存在感、嘲讽、挖苦，简直跟个巨婴低能儿一样。从来不指望这些人对项目有什么改善！除了跟风从众，跟饭圈、小粉红一样发动网暴这动员优点，其他的可谓是一无是处。

科学上网的工具有很多，方式也不少，受到各方面不同程度的封杀也很多；随着各个方面的管制加深，随时面临断网的单一上网方式，已经不能满足需要了；因此掌握科学上网的方式与技巧，并有效地结合各种VPN或代理软件的使用就显得尤为必要了。

举个例子，通过扩展下载站下载代理插件、web代理或是DNSCrypt访问ss站点，使用ss翻墙后又下载其他VPN或代理，像这样组成一个个互相连接的节点，相对来说就不是那么容易断网了。

<!-- 以下是个人进行科学上网的方式总览图：

<!-- ![](https://ipfs.io/ipfs/QmRhbqdGy8wmZhnE68D8uesrEgDFAsp2pcJE2frMuKfrvs?1.png) -->

<!-- ![](https://i.postimg.cc/Bbx7pj5R/2018-05-05-154505.png) -->


## 获取国外手机号码

英国的 giffgaff 实体电话卡，目前已无法在中国注册了，图方便的话淘宝、咸鱼，以及小众分享之类平台购买。不嫌麻烦的话，翻墙注册，以台湾作为中转站，快递先寄到台湾，再寄到中国。中国卡在海外即便你开通漫游流量，在海外无法访问谷歌等某些app。因为这个原因此类卡就成为很多人的刚需。

## kitesim

> **【说明】** 有些号码下发需要几十分钟不等的时间，并不是立刻就能接码的，建议直接联系APP内的客服。无论是接码卡还是流量卡均不能打电话。kitesim港卡收不到短信，注意避雷。一旦发现卡不能用了，最好找寻其他esim平台。

### 流量功能需手机支持esim

不同于其他虚拟号，它调用的全是运营商的正式卡段。即使在国内上网，IP也会显示在当地。线路相当纯净，等同于底特律化身为人。支持 esim 的手机，下单后扫码写入即可完成激活。

kitesim 套餐：
* 能接码就不能使用流量
* 能使用流量就不能接码

### 接码功能普通手机均能支持

美区ID登录 AppStore 下载 kitesim 号码选择美国，按照流程付款。

* 点击订单，在激活里找到号码，并激活
  * 关闭手机WiFi，回到设置，点击蜂窝网络
  * 选择SIM卡，并打开数据漫游，这时才能接码成功。

实体号码验证平台：https://www.phonevalidator.com/index.aspx

## X-esim + esimplus

!> 5ber已经跑路了，已经找不到能够以app的形式支持esim第二个app了，遗憾。

该方法可使普通手机升级E-SIM，且支持短信接码，并能使用流量上网。

网址：

* https://xesim.cc
* https://esimplus.me

前提条件：

* 苹果手机
* MasterCard
* 35美元开卡费
* 具体一定的上网冲浪能力和折腾精神

使用方式：

* 准备 [X-esim](https://xesim.cc/) 实体卡  + 海外  [esimplus](https://esimplus.me/) e-sim 二维码
* 蜂窝网络  -> 数据漫游 -> sim 卡应用程序 -> x-esim -> 下载 esim 
  * 输入 LPA 激活码 （打开 esimplus 的二维码，手机扫描到一长串数字就是LPA激活码）
  * 如果没有确认码，直接点击发送就行
  * 写号完成后，再次打开 sim 卡应用程序，点击 xesim
    * 点击 sim 管理列表，启用下载好的 esim

需注意：一次只能启用一个esim，根据政策的不同，一张卡只能下载15个手机号。

参考出处及详细视频教学：

* [星环无限 - 超高性价比美国流量eSIM | 原生高质量美国IP | 保号套餐 | 流量套餐 | 多国流量&多国漫游 | 跨境电商 | 出国旅游 | 留学](https://www.youtube.com/watch?v=Xmz0As2eBC0)
* [星环无限 - 海外账号卡在手机验证？无需实体卡，轻松搞定海外APP验证码，告别注册失败!](https://www.youtube.com/watch?v=I65a7BKtCf0)

看到这里，知道为什么管控esim那么严了吧...咱妈都是为你好啊！过去Wi-Fi也是！！！还想深入的话，那就去买美股吧：[zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide)

> **【提示】** 以上这些都不行的话，找个靠谱的收费接码平台凑合用吧，或是出国托人代购手机卡什么的。


## 开通虚拟信用卡摸索历程

> **【说明】** **免责声明**
>
> **本书所有区块链相关数据与资料仅供用户学习及研究之用，不构成任何投资、法律等其他领域的建议和依据。 强烈建议您独自对内容进行研究、审查、分析和验证，谨慎使用相关数据及内容，并自行承担所带来的一切风险。**

## 随言前置

因时间关系的原因，暂没空了解虚拟币是怎么像印钞机一样生产的，估计和挖矿八九不离十了。就留个标记吧。这些开卡商之所以用虚拟币的原因基本上也能推得出来一二了。

1. 保值：地缘政治国际关系使得美元兑换汇率波动较大
1. 规避审查，以及相关交易争议

数字移民，这词真好。还有离岸爱国，真是异曲同工之妙。

## 信息提炼

过时教程：万里汇相关申请虚拟信用卡的教程、[【教程】免信用卡为cloudflare添加付款方式](https://www.nodeseek.com/post-84328-1)

重要教程：

* [星环无限 - 美国虚拟信用卡申请教学，超多支付场景，线上可开，人手必备！简单KYC|低费率|升级海外软件|绑定苹果ID(youtube)](https://www.youtube.com/watch?v=MfAe_cQjyh8)

参考教程：[数字移民指南](https://shuziyimin.net/)、[Tangent-Wei/crypto_info](https://github.com/Tangent-Wei/crypto_info)

准备工具：

* 过时教程提炼出来的网页工具
    * 信用卡号生成网站：[https://namso-gen.com](https://namso-gen.com/?tab=basic&network=random)
    * 信用卡校验测活网站：[https://www.mrchecker.net](https://www.mrchecker.net/card-checker/ccn2/)
    * 卡BIN查询网站：[https://bincheck.io/zh](https://bincheck.io/zh)
    * [美国地址生成器](https://www.meiguodizhi.com/)：
        * 免税州：俄勒冈州、特拉华州、新罕布什尔州、蒙大拿州、阿拉斯加州
* 信用卡最低开卡费 + 最低充值费：
    * 人民币兑换美元约7:1，虚拟币兑换美元目前基本等价（2025.11.13）
    * 准备约450-500块钱
* 虚拟信用卡开卡应用，binpay：https://app.binpay.cc/pages/passport/invitation?r=1121893
* 虚拟币交易所：[欧易](https://www.okx.com/zh-hans)

## 开卡成功过程关键展示

**这里的“注册完毕”包含在 Binpay 与欧易中完成手机、邮箱、身份证、人脸等全部认证。**

补充欧易使用视频教程：[YOUTUBE - 欧易教程，欧易怎么玩（中国大陆用户）？注册→充值→提现→交易——欧易注册教学欧易交易欧易注册欧易卖币欧易怎么使用欧易买币欧易充值欧易下载欧易提现欧易提现人民币欧易购买okex](https://www.youtube.com/watch?v=U94fVBRfcQA)

跟着 [星环无限 - 美国虚拟信用卡申请教学，超多支付场景，线上可开，人手必备！简单KYC|低费率|升级海外软件|绑定苹果ID](https://www.bilibili.com/video/BV15u2FBgEeT) 做一遍注册完binpay，然后注册欧易账号，并购买虚拟币。

购买虚拟币：以alipay为例：通过alipay id找到商家，将钱转账到对方账户后，截图交易成功记录及账单，上传支付记录，等待商家支付虚拟币。首次充值可以试着充值最低额度，摸索一两小时基本上也会了一点。

从欧易购买好虚拟币后，与binpay进行交易，步骤如图：

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-12_21-49-26.png)

过几分钟后，就会收到邮件及系统的转出成功提示

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-12_21-54-02.png)

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-12_22-24-31.png)

接着打开binpay，将充值到账的虚拟币，转换成美元

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-12_22-26-55.png)

这时钱包有了美元额度，就可以申请开卡了。

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-12_22-27-54.png)

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-12_22-29-06.png)

设置密码激活卡

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-12_22-30-58.png)

## 使用 cloud flare r2 服务信用卡资料填写

免税州见信息提炼部分，使用美国地址生成器 https://www.meiguodizhi.com ，填入邮寄信息等。

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-12_22-38-44.png)

r2 存储桶使用成功！

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-12_22-45-24.png)

## btw

在国内能用上海外的服务胜似蜀道难，难怪这么多人用支付宝收付款，原来是微信太容易触发风控了，迟早电话卡也会被限制，迟早也会成赛博北朝鲜。当刹那 Power 和艾滋一样，通过母婴、血液和性传播，必然免不了折腾，都是为你好的宏大叙事，好东西，韭菜就是用不了，普通人不可能三角，也太典了。


## 美区ID购买小火箭

## 前言

美区号被盗了已有三年了，这一次将号牢牢掌握在自己手中。我的谷歌账号、chatgpt都是买的，但苹果ID最好还是要自己亲自注册，防止邮箱用自己的，手机号、手机设备是别人的，导致账号被盗。apple id和注册谷歌账号还是有点差别，当时我以为和雅虎台湾一样，用国内手机号注册不了美区ID，以及我也忘了是哪个网站来着，注册账号必须要vsia提供信用卡。这些步骤可谓劝退一大部分人。直到今天，自己创建了美区id才知道我想多了...

从这篇[iPhone/iPad V2ray/SS 翻墙APP教程](https://fanqiang.gitbook.io/fanqiang/ios/potatsolite)文档来看，看来翻墙工具比起18年那会，也多了一些。当我再点进去一看[注册苹果美区 Apple ID 帐号并购买APP指南](https://fanqiang.gitbook.io/fanqiang/ios/appleid)，不由得一句“卧槽”，自己落后好几年了...这个翻墙教程的作者是李洪志的弟子，看来几年过去了，轮子宣传隐蔽了很多，除了翻墙新闻，几乎看不到什么轮子痕迹，不想18年那会，非常直白，基本上每个页面都有相关宣传标语。现在你不去管它，几乎不用管它，也算少有的从电脑到手机、以及路由器等等各种翻墙教程合集。

现在又有了 https://ihmily.github.io/proxy-guide 看起来更像是一本书，虽有体系，但大部分人还是倾向于开箱即用的那种。

## 注册美区apple id

为了玩杀戮尖塔才注册港区ID，登录App Store发现也没有才转到美区的。教程参考：

* [美区苹果ID注册教程（2025年9月保姆级实测教程）](https://zhuanlan.zhihu.com/p/1948722982823368489)
* [www.shenfendaquan.com](https://www.shenfendaquan.com/Index/index/custom_result)

为了在手机玩上游戏王遇上了“无法验证app需要互联网连接以验证是否信任开发者”的错误，原来需要用签证才能正常使用，签证有两种方式，证书签名、id签名，推荐使用爱思助手来进行签名：

* https://www.i4.cn/news_detail_40956.html
* https://www.i4-cn.com/archives/2767

无意间发现的购买证书的网站：https://pan.iosku.top  没用过，不保证可靠性。证书一般都要钱买的，也可以去官网购买，开发者认证年费真是相当的贵了，唤醒了我当初开发[Free NTFS for Mac](https://github.com/hoochanlon/Free-NTFS-for-Mac)的记忆。

以上过程让我又经历了一次“刷机”，太累了。

长截图下载：https://github.com/hoochanlon/picx-images-hosting/blob/master/imgs/fkca/PixPin_2025-11-13_12-52-53.png

## 购买礼品卡给美区ID充值买小火箭

现在iPhone也有免费的梯子了 点击 [singbox](https://www.youtube.com/watch?v=fzr2CI3NC64) 查看YouTube教程。

* [最新Apple美区ID注册方法 | 100%注册成功| 支持国内手机号验证登录 | 国内网络环境即可 | 超低门槛 | 人人都学得会](https://www.bilibili.com/video/BV1wxySBREJm)
* [苹果美区礼品卡购买方法大全，购买/兑换/使用全流程手把手指导，美区买游戏/开会员/内购升级必备！](https://www.bilibili.com/video/BV16KyZB6E7k/)

### 开始前的碎碎念

为什么使用礼品卡：

1. 在有visa、MasterCard的情况下，最好应该是提前设置好支付方式，没有设置就需要用礼品卡了。
1. 美国区账号不能绑定在中国办的国际信用卡。
1. 方便与他人交易，常见于淘宝卖家。
1. 避免直接使用设置里的apple id登录，使用设置里的apple id登录相当于换了整个设备，用了“别人”的手机。

才想起来，礼品卡不能用于游戏内购的续订项目。银联的借记卡用不了，可能是需要银联的信用卡，之前的信用卡注销了，不然还可以验证一下，可惜了。

### 正式开始

购买礼品卡的方式，第三方：淘宝、咸鱼、pockyt shop。我这选是官方。

进入：https://www.apple.com 美版，下拉到最底，选择“[Gift Cards](https://www.apple.com/shop/gift-cards)” 点击[buy](https://www.apple.com/shop/buy-giftcard/giftcard)。

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-13_20-10-33.png)

最低额度是充值10$

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-13_20-14-20.png) 

以我的为例，填好自己的姓名、邮箱，选择“no message”，点击"Add to Bag"，二次确认"check out"

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-13_20-16-03.png)

用美国地址生成器 https://www.meiguodizhi.com 邮箱选择自己用的,电话选择地址生成器生成的，电话不会被验证，临时邮箱时间较短，最好也用自己的，方便自己接受邮件。

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-13_20-26-55.png)

邮件接收

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-13_21-12-40.png)

图片看起来没截到，连接VPN，登录AppStore，填兑换码，购买小火箭

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/fkca/PixPin_2025-11-14_00-32-26.png)

### 剩余时间随便边看边写点什么

#### chatgpt plus订阅方法信息收集

前置条件：
* 具备翻墙软件
* 具备chatgpt账号
在没能力靠自己实现订阅充值之前，省时间的方式也只能是靠淘宝咸鱼卖家。

因为我的chatgpt账号以及订阅过了，所以暂没法跟着视频一步步做。在通过相关UP了解到“国内注册的国际信用卡无法绑定美区ID”，以及在UP演示过程中手机信息提示银行卡并未开通境外支付相关信息，也不得不感慨国内限制实在是...太妈的烂了！

* [【2025最新】GPT Plus微信就能直接充，最简便，最省钱，最安全的充值方式分享。不折腾外币卡，不折腾美区ID，独享账号](https://www.bilibili.com/video/BV1kFsnzgEN7)
* [（不适用苹果手机）不需要visa或mastercard，不用第三方代充，不用虚拟卡，使用国内银联卡绑定谷歌商店订阅ChatGPTPlus](https://www.bilibili.com/video/BV1NJYaziEXv)
* [bewild.ai](https://bewild.ai/)

btw:

从 [美区 PayPal 注册教程](https://www.bilibili.com/video/BV1ye4HzXE1A) 评论区信息得到：招行的万事达普卡，全球人民币支付，绑定美区app store不行，但美区google可以。看了 [【最新情况】英国保号神卡 giffgaff 突然暂停向中国邮寄实体卡 ｜ 原因分析 ｜ 解决办法](https://www.bilibili.com/video/BV1Rs2MBcE3n) 给我的感触就是“无利不起早，当福利知道的人多了也就没福利了”。


## 国外云服务器自搭梯子示例

国内直接访问境外网站必然受限制，原因在于国内对境外流量进行了严格控制。但国内到台湾之间是互通的。 也就是可以买一台最便宜的台湾服务器作为中转当做跳板。不得不说，这个免费梯子真厉害：[Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers)

## 在服务器上安装Shadowsocks服务端

### 选型安装shadowsocks-libev

推荐使用官方维护的 shadowsocks-libev，因为简单、稳定、性能好。

更新软件源和安装shadowsocks-libev

```bash
sudo apt update
sudo apt install shadowsocks-libev
```

### 配置 Shadowsocks 服务

配置文件默认放在 `/etc/shadowsocks-libev/config.json` 修改配置 `vi /etc/shadowsocks-libev/config.json`

修改如下：

```json
{
    "server": "0.0.0.0",
    "mode": "tcp_and_udp",
    "server_port": 8488,
    "local_port": 1080,
    "password": "your-password",
    "timeout": 86400,
    "method": "chacha20-ietf-poly1305"
}
```

参数简单解释：

* ​`server`​: `0.0.0.0`​ 表示监听所有网卡。
* ​`server_port`​: 自定义你需要开启的端口。
* `local_port`: 本地默认代理端口。
* ​`method`​: 可选 `chacha20-ietf-poly1305`​、`aes-256-gcm`​ 等。

端口配置参考：

* 知名端口 (Well-known ports)：从 0 到 1023，这些端口号通常被操作系统和系统级应用程序使用，如 HTTP (80)、HTTPS (443)、FTP (21) 等。
* 注册端口 (Registered ports)：从 1024 到 49151，这些端口号是为特定应用程序或服务保留的，并且可以由应用程序开发者注册使用。
* 动态/私有端口 (Dynamic/Private ports)：从 49152 到 65535，这些端口通常用于客户端和服务端之间的动态连接，如 NAT (网络地址转换) 和临时端口。

### 服务端启动

1. 启动服务 `sudo systemctl restart shadowsocks-libev.service`
2. 检查状态 `sudo systemctl status shadowsocks-libev.service`
3. 防火墙放行端口 `ufw allow 8848`
4. 配置开机自动启动：`sudo systemctl enable shadowsocks-libev.service`

`ss -tulpn | grep ss-server` 在服务器上检查端口是否在监听，正常会显示 `ss-server`​ 在监听配置好的端口。

## 在你自己的电脑上安装 clash 并配置

clash 下载地址：https://www.clashverge.dev/index.html 

### 关键配置展示解读

```yaml
# 本地从哪里走代理
port: 7890
socks-port: 7891
redir-port: 7892
allow-lan: false
mode: Rule
log-level: info
external-controller: 127.0.0.1:9090

...

# 代理
proxies:
  - name: "海外服务器IP地址"
    type: ss
    server: 海外服务器IP地址
    port: 8848
    cipher: chacha20-ietf-poly1305
    password: "你的密码"
    udp: false

# 节点
proxy-groups:
  - name: CroLAX
    type: select
    proxies:
      - "海外服务器IP地址"
      - "DIRECT"
```

客户端配置链接参考：

* Windows：[Clash for Windows](https://www.clashforwindows.net)  
* Mac：[Clash Verge](https://clashverge.net)
* Android：[Clash for Android](https://clashforandroid.org/clash-for-android-download)
* iOS：[Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118)

### 在【订阅】-> 【新建】 修改 Clash 配置。

clash 完整配置模板如下，复制粘贴，修改如上“关键配置解读”的proxies和proxy-groups部分即可。

更详细的配置见：https://github.com/HenryChiao/mihomo_yamls

```yml
port: 7890
socks-port: 7891
redir-port: 7892
allow-lan: false
mode: Rule
log-level: info
external-controller: 127.0.0.1:9090
secret: ""
cfw-bypass:
  - localhost
  - 127.*
  - 10.*
  - 172.16.*
  - 172.17.*
  - 172.18.*
  - 172.19.*
  - 172.20.*
  - 172.21.*
  - 172.22.*
  - 172.23.*
  - 172.24.*
  - 172.25.*
  - 172.26.*
  - 172.27.*
  - 172.28.*
  - 172.29.*
  - 172.30.*
  - 172.31.*
  - 192.168.*
  - <local>
cfw-latency-timeout: 3000
proxies:
  - name: "海外服务器IP地址"
    type: ss
    server: 海外服务器IP地址
    port: 8848
    cipher: chacha20-ietf-poly1305
    password: "你的密码"
    udp: false
proxy-groups:
  - name: CroLAX
    type: select
    proxies:
      - "海外服务器IP地址"
      - "DIRECT"
rules:
  - DOMAIN,hls.itunes.apple.com,CroLAX
  - DOMAIN,itunes.apple.com,CroLAX
  - DOMAIN,itunes.com,CroLAX
  - DOMAIN-SUFFIX,icloud.com,DIRECT
  - DOMAIN-SUFFIX,icloud-content.com,DIRECT
  - DOMAIN-SUFFIX,me.com,DIRECT
  - DOMAIN-SUFFIX,mzstatic.com,DIRECT
  - DOMAIN-SUFFIX,aaplimg.com,DIRECT
  - DOMAIN-SUFFIX,cdn-apple.com,DIRECT
  - DOMAIN-SUFFIX,apple.com,DIRECT
  ## 国内网站
  - DOMAIN-SUFFIX,akadns.net,DIRECT
  - DOMAIN-SUFFIX,akamaized.net,DIRECT
  - DOMAIN-SUFFIX,cn,DIRECT
  - DOMAIN-KEYWORD,-cn,DIRECT
  - DOMAIN-SUFFIX,126.com,DIRECT
  - DOMAIN-SUFFIX,126.net,DIRECT
  - DOMAIN-SUFFIX,127.net,DIRECT
  - DOMAIN-SUFFIX,163.com,DIRECT
  - DOMAIN-SUFFIX,360buyimg.com,DIRECT
  - DOMAIN-SUFFIX,36kr.com,DIRECT
  - DOMAIN-SUFFIX,acfun.tv,DIRECT
  - DOMAIN-SUFFIX,air-matters.com,DIRECT
  - DOMAIN-SUFFIX,aixifan.com,DIRECT
  - DOMAIN-KEYWORD,alicdn,DIRECT
  - DOMAIN-KEYWORD,alipay,DIRECT
  - DOMAIN-KEYWORD,taobao,DIRECT
  - DOMAIN-SUFFIX,amap.com,DIRECT
  - DOMAIN-SUFFIX,autonavi.com,DIRECT
  - DOMAIN-KEYWORD,baidu,DIRECT
  - DOMAIN-SUFFIX,bdimg.com,DIRECT
  - DOMAIN-SUFFIX,bdstatic.com,DIRECT
  - DOMAIN-SUFFIX,bilibili.com,DIRECT
  - DOMAIN-SUFFIX,caiyunapp.com,DIRECT
  - DOMAIN-SUFFIX,clouddn.com,DIRECT
  - DOMAIN-SUFFIX,cnbeta.com,DIRECT
  - DOMAIN-SUFFIX,cnbetacdn.com,DIRECT
  - DOMAIN-SUFFIX,cootekservice.com,DIRECT
  - DOMAIN-SUFFIX,csdn.net,DIRECT
  - DOMAIN-SUFFIX,ctrip.com,DIRECT
  - DOMAIN-SUFFIX,dgtle.com,DIRECT
  - DOMAIN-SUFFIX,dianping.com,DIRECT
  - DOMAIN-SUFFIX,douban.com,DIRECT
  - DOMAIN-SUFFIX,doubanio.com,DIRECT
  - DOMAIN-SUFFIX,duokan.com,DIRECT
  - DOMAIN-SUFFIX,easou.com,DIRECT
  - DOMAIN-SUFFIX,ele.me,DIRECT
  - DOMAIN-SUFFIX,feng.com,DIRECT
  - DOMAIN-SUFFIX,fir.im,DIRECT
  - DOMAIN-SUFFIX,frdic.com,DIRECT
  - DOMAIN-SUFFIX,g-cores.com,DIRECT
  - DOMAIN-SUFFIX,godic.net,DIRECT
  - DOMAIN-SUFFIX,gtimg.com,DIRECT
  - DOMAIN-SUFFIX,hongxiu.com,DIRECT
  - DOMAIN-SUFFIX,hxcdn.net,DIRECT
  - DOMAIN-SUFFIX,iciba.com,DIRECT
  - DOMAIN-SUFFIX,ifeng.com,DIRECT
  - DOMAIN-SUFFIX,ifengimg.com,DIRECT
  - DOMAIN-SUFFIX,ipip.net,DIRECT
  - DOMAIN-SUFFIX,iqiyi.com,DIRECT
  - DOMAIN-SUFFIX,jd.com,DIRECT
  - DOMAIN-SUFFIX,jianshu.com,DIRECT
  - DOMAIN-SUFFIX,knewone.com,DIRECT
  - DOMAIN-SUFFIX,le.com,DIRECT
  - DOMAIN-SUFFIX,lecloud.com,DIRECT
  - DOMAIN-SUFFIX,lemicp.com,DIRECT
  - DOMAIN-SUFFIX,licdn.com,DIRECT
  - DOMAIN-SUFFIX,luoo.net,DIRECT
  - DOMAIN-SUFFIX,meituan.com,DIRECT
  - DOMAIN-SUFFIX,meituan.net,DIRECT
  - DOMAIN-SUFFIX,mi.com,DIRECT
  - DOMAIN-SUFFIX,miaopai.com,DIRECT
  - DOMAIN-SUFFIX,microsoft.com,DIRECT
  - DOMAIN-SUFFIX,microsoftonline.com,DIRECT
  - DOMAIN-SUFFIX,miui.com,DIRECT
  - DOMAIN-SUFFIX,miwifi.com,DIRECT
  - DOMAIN-SUFFIX,mob.com,DIRECT
  - DOMAIN-SUFFIX,netease.com,DIRECT
  - DOMAIN-SUFFIX,office.com,DIRECT
  - DOMAIN-KEYWORD,officecdn,DIRECT
  - DOMAIN-SUFFIX,office365.com,DIRECT
  - DOMAIN-SUFFIX,oschina.net,DIRECT
  - DOMAIN-SUFFIX,ppsimg.com,DIRECT
  - DOMAIN-SUFFIX,pstatp.com,DIRECT
  - DOMAIN-SUFFIX,qcloud.com,DIRECT
  - DOMAIN-SUFFIX,qdaily.com,DIRECT
  - DOMAIN-SUFFIX,qdmm.com,DIRECT
  - DOMAIN-SUFFIX,qhimg.com,DIRECT
  - DOMAIN-SUFFIX,qhres.com,DIRECT
  - DOMAIN-SUFFIX,qidian.com,DIRECT
  - DOMAIN-SUFFIX,qihucdn.com,DIRECT
  - DOMAIN-SUFFIX,qiniu.com,DIRECT
  - DOMAIN-SUFFIX,qiniucdn.com,DIRECT
  - DOMAIN-SUFFIX,qiyipic.com,DIRECT
  - DOMAIN-SUFFIX,qq.com,DIRECT
  - DOMAIN-SUFFIX,qqurl.com,DIRECT
  - DOMAIN-SUFFIX,rarbg.to,DIRECT
  - DOMAIN-SUFFIX,ruguoapp.com,DIRECT
  - DOMAIN-SUFFIX,segmentfault.com,DIRECT
  - DOMAIN-SUFFIX,sinaapp.com,DIRECT
  - DOMAIN-SUFFIX,smzdm.com,DIRECT
  - DOMAIN-SUFFIX,sogou.com,DIRECT
  - DOMAIN-SUFFIX,sogoucdn.com,DIRECT
  - DOMAIN-SUFFIX,sohu.com,DIRECT
  - DOMAIN-SUFFIX,soku.com,DIRECT
  - DOMAIN-SUFFIX,speedtest.net,DIRECT
  - DOMAIN-SUFFIX,sspai.com,DIRECT
  - DOMAIN-SUFFIX,suning.com,DIRECT
  - DOMAIN-SUFFIX,taobao.com,DIRECT
  - DOMAIN-SUFFIX,tencent.com,DIRECT
  - DOMAIN-SUFFIX,tenpay.com,DIRECT
  - DOMAIN-SUFFIX,tianyancha.com,DIRECT
  - DOMAIN-SUFFIX,tmall.com,DIRECT
  - DOMAIN-SUFFIX,tudou.com,DIRECT
  - DOMAIN-SUFFIX,umetrip.com,DIRECT
  - DOMAIN-SUFFIX,upaiyun.com,DIRECT
  - DOMAIN-SUFFIX,upyun.com,DIRECT
  - DOMAIN-SUFFIX,veryzhun.com,DIRECT
  - DOMAIN-SUFFIX,weather.com,DIRECT
  - DOMAIN-SUFFIX,weibo.com,DIRECT
  - DOMAIN-SUFFIX,xiami.com,DIRECT
  - DOMAIN-SUFFIX,xiami.net,DIRECT
  - DOMAIN-SUFFIX,xiaomicp.com,DIRECT
  - DOMAIN-SUFFIX,ximalaya.com,DIRECT
  - DOMAIN-SUFFIX,xmcdn.com,DIRECT
  - DOMAIN-SUFFIX,xunlei.com,DIRECT
  - DOMAIN-SUFFIX,yhd.com,DIRECT
  - DOMAIN-SUFFIX,yihaodianimg.com,DIRECT
  - DOMAIN-SUFFIX,yinxiang.com,DIRECT
  - DOMAIN-SUFFIX,ykimg.com,DIRECT
  - DOMAIN-SUFFIX,youdao.com,DIRECT
  - DOMAIN-SUFFIX,youku.com,DIRECT
  - DOMAIN-SUFFIX,zealer.com,DIRECT
  - DOMAIN-SUFFIX,zhihu.com,DIRECT
  - DOMAIN-SUFFIX,zhimg.com,DIRECT
  - DOMAIN-SUFFIX,zimuzu.tv,DIRECT
  - DOMAIN-KEYWORD,netflix,CroLAX
  - DOMAIN-KEYWORD,nflx,CroLAX
  ## 抗 DNS 污染
  - DOMAIN-KEYWORD,amazon,CroLAX
  - DOMAIN-KEYWORD,google,CroLAX
  - DOMAIN-KEYWORD,gmail,CroLAX
  - DOMAIN-KEYWORD,youtube,CroLAX
  - DOMAIN-KEYWORD,facebook,CroLAX
  - DOMAIN-SUFFIX,fb.me,CroLAX
  - DOMAIN-SUFFIX,fbcdn.net,CroLAX
  - DOMAIN-KEYWORD,twitter,CroLAX
  - DOMAIN-KEYWORD,instagram,CroLAX
  - DOMAIN-KEYWORD,dropbox,CroLAX
  - DOMAIN-SUFFIX,twimg.com,CroLAX
  - DOMAIN-KEYWORD,blogspot,CroLAX
  - DOMAIN-SUFFIX,youtu.be,CroLAX
  - DOMAIN-KEYWORD,whatsapp,CroLAX
  - DOMAIN-KEYWORD,googleapis,CroLAX
# Clubhouse
  - DOMAIN-SUFFIX,clubhouse.com,CroLAX
  - DOMAIN-SUFFIX,clubhouseapi.com,CroLAX
  - DOMAIN-SUFFIX,joinclubhouse.com,CroLAX
  - DOMAIN-SUFFIX,clubhouseprod.s3.amazonaws.com,CroLAX
  - DOMAIN-SUFFIX,clubhouse.pubnub.com,CroLAX

  - DOMAIN-SUFFIX, ap-oversea-tls.agora.io, DIRECT
  - DOMAIN-SUFFIX, ap-oversea.agora.io, DIRECT
  - DOMAIN-SUFFIX, ap-oversea2.agora.io, DIRECT
  - DOMAIN-SUFFIX, report-oversea.agora.io, DIRECT
  - IP-CIDR, 3.0.163.78/32, DIRECT
  - IP-CIDR, 13.230.60.35/32, DIRECT
  - IP-CIDR, 23.248.191.103/32, DIRECT
  - IP-CIDR, 23.248.191.105/32, DIRECT
  - IP-CIDR, 23.98.43.152/32, DIRECT
  - IP-CIDR, 35.178.208.187/32, DIRECT
  - IP-CIDR, 45.40.48.11/32, DIRECT
  - IP-CIDR, 45.255.124.98/32, DIRECT
  - IP-CIDR, 45.255.124.100/32, DIRECT
  - IP-CIDR, 45.255.124.101/32, DIRECT
  - IP-CIDR, 45.255.124.104/32, DIRECT
  - IP-CIDR, 45.255.124.105/32, DIRECT
  - IP-CIDR, 45.255.124.107/32, DIRECT
  - IP-CIDR, 45.255.124.108/32, DIRECT
  - IP-CIDR, 45.255.124.109/32, DIRECT
  - IP-CIDR, 45.255.124.135/32, DIRECT
  - IP-CIDR, 50.17.126.121/32, DIRECT
  - IP-CIDR, 52.52.84.170/32, DIRECT
  - IP-CIDR, 52.58.56.244/32, DIRECT
  - IP-CIDR, 52.194.158.59/32, DIRECT
  - IP-CIDR, 52.221.46.208/32, DIRECT
  - IP-CIDR, 54.178.26.110/32, DIRECT
  - IP-CIDR, 69.28.51.148/32, DIRECT
  - IP-CIDR, 103.59.49.10/32, DIRECT
  - IP-CIDR, 103.65.41.166/32, DIRECT
  - IP-CIDR, 103.65.41.169/32, DIRECT
  - IP-CIDR, 103.98.18.181/32, DIRECT
  - IP-CIDR, 103.98.18.183/32, DIRECT
  - IP-CIDR, 103.98.18.184/32, DIRECT
  - IP-CIDR, 103.98.18.189/32, DIRECT
  - IP-CIDR, 120.227.115.126/32, DIRECT
  - IP-CIDR, 122.10.255.165/32, DIRECT
  - IP-CIDR, 128.1.87.196/32, DIRECT
  - IP-CIDR, 129.227.71.203/32, DIRECT
  - IP-CIDR, 129.227.115.130/32, DIRECT
  - IP-CIDR, 148.153.126.146/32, DIRECT
  - IP-CIDR, 148.153.172.73/32, DIRECT
  - IP-CIDR, 148.153.172.74/32, DIRECT
  - IP-CIDR, 148.153.172.75/32, DIRECT
  - IP-CIDR, 148.153.172.76/32, DIRECT
  - IP-CIDR, 148.153.172.77/32, DIRECT
  - IP-CIDR, 164.52.0.244/32, DIRECT
  - IP-CIDR, 164.52.6.19/32, DIRECT
  - IP-CIDR, 164.52.6.21/32, DIRECT
  - IP-CIDR, 164.52.6.23/32, DIRECT
  - IP-CIDR, 164.52.6.24/32, DIRECT
  - IP-CIDR, 164.52.6.25/32, DIRECT
  - IP-CIDR, 164.52.32.57/32, DIRECT
  - IP-CIDR, 164.52.32.59/32, DIRECT
  - IP-CIDR, 164.52.32.60/32, DIRECT
  - IP-CIDR, 164.52.36.228/32, DIRECT
  - IP-CIDR, 164.52.36.232/32, DIRECT
  - IP-CIDR, 164.52.36.238/32, DIRECT
  - IP-CIDR, 164.52.36.243/32, DIRECT
  - IP-CIDR, 164.52.36.245/32, DIRECT
  - IP-CIDR, 164.52.36.254/32, DIRECT
  - IP-CIDR, 164.52.102.35/32, DIRECT
  - IP-CIDR, 164.52.102.66/32, DIRECT
  - IP-CIDR, 164.52.102.67/32, DIRECT
  - IP-CIDR, 164.52.102.68/32, DIRECT
  - IP-CIDR, 164.52.102.69/32, DIRECT
  - IP-CIDR, 164.52.102.70/32, DIRECT
  - IP-CIDR, 164.52.102.75/32, DIRECT
  - IP-CIDR, 164.52.102.76/32, DIRECT
  - IP-CIDR, 164.52.102.77/32, DIRECT
  - IP-CIDR, 164.52.102.91/32, DIRECT
  - IP-CIDR, 164.52.124.102/32, DIRECT
  - IP-CIDR, 199.190.44.36/32, DIRECT
  - IP-CIDR, 199.190.44.37/32, DIRECT
  - IP-CIDR, 202.181.136.106/32, DIRECT
  - IP-CIDR, 202.226.25.162/32, DIRECT
  - IP-CIDR, 202.226.25.166/32, DIRECT
  - IP-CIDR, 202.226.25.171/32, DIRECT
  - IP-CIDR, 202.226.25.195/32, DIRECT
  - IP-CIDR, 202.226.25.198/32, DIRECT
  - IP-CIDR, 129.227.57.143/32, DIRECT
  - IP-CIDR, 129.227.234.70/32, DIRECT
  - IP-CIDR, 129.227.234.82/32, DIRECT
  - IP-CIDR, 129.227.234.119/32, DIRECT
  - IP-CIDR, 129.227.71.144/32, DIRECT
  - IP-CIDR, 129.227.57.132/32, DIRECT
  - IP-CIDR, 129.227.57.134/32, DIRECT
  - IP-CIDR, 129.227.57.145/32, DIRECT
  - IP-CIDR, 129.227.71.141/32, DIRECT
  - IP-CIDR, 129.227.234.83/32, DIRECT
  - IP-CIDR, 129.227.71.142/32, DIRECT
  - IP-CIDR, 129.227.71.132/32, DIRECT
  - IP-CIDR, 129.227.71.133/32, DIRECT
  - IP-CIDR, 129.227.71.134/32, DIRECT
  - IP-CIDR, 129.227.234.67/32, DIRECT
  - IP-CIDR, 129.227.234.110/32, DIRECT
  - IP-CIDR, 129.227.234.112/32, DIRECT
  - IP-CIDR, 129.227.234.124/32, DIRECT
  - IP-CIDR, 129.227.71.140/32, DIRECT
  - IP-CIDR, 129.227.71.130/32, DIRECT
  - IP-CIDR, 129.227.71.131/32, DIRECT
  - IP-CIDR, 129.227.71.143/32, DIRECT
  - IP-CIDR, 129.227.156.17/32, DIRECT
  - IP-CIDR, 129.227.57.137/32, DIRECT
  - IP-CIDR, 129.227.156.20/32, DIRECT
  ## 国外网站
  - DOMAIN-SUFFIX,openai.com,CroLAX
  - DOMAIN-SUFFIX,9to5mac.com,CroLAX
  - DOMAIN-SUFFIX,abpchina.org,CroLAX
  - DOMAIN-SUFFIX,adblockplus.org,CroLAX
  - DOMAIN-SUFFIX,adobe.com,CroLAX
  - DOMAIN-SUFFIX,alfredapp.com,CroLAX
  - DOMAIN-SUFFIX,amplitude.com,CroLAX
  - DOMAIN-SUFFIX,ampproject.org,CroLAX
  - DOMAIN-SUFFIX,android.com,CroLAX
  - DOMAIN-SUFFIX,angularjs.org,CroLAX
  - DOMAIN-SUFFIX,aolcdn.com,CroLAX
  - DOMAIN-SUFFIX,apkpure.com,CroLAX
  - DOMAIN-SUFFIX,appledaily.com,CroLAX
  - DOMAIN-SUFFIX,appshopper.com,CroLAX
  - DOMAIN-SUFFIX,appspot.com,CroLAX
  - DOMAIN-SUFFIX,arcgis.com,CroLAX
  - DOMAIN-SUFFIX,archive.org,CroLAX
  - DOMAIN-SUFFIX,armorgames.com,CroLAX
  - DOMAIN-SUFFIX,aspnetcdn.com,CroLAX
  - DOMAIN-SUFFIX,att.com,CroLAX
  - DOMAIN-SUFFIX,awsstatic.com,CroLAX
  - DOMAIN-SUFFIX,azureedge.net,CroLAX
  - DOMAIN-SUFFIX,azurewebsites.net,CroLAX
  - DOMAIN-SUFFIX,bing.com,CroLAX
  - DOMAIN-SUFFIX,bintray.com,CroLAX
  - DOMAIN-SUFFIX,bit.com,CroLAX
  - DOMAIN-SUFFIX,bit.ly,CroLAX
  - DOMAIN-SUFFIX,bitbucket.org,CroLAX
  - DOMAIN-SUFFIX,bjango.com,CroLAX
  - DOMAIN-SUFFIX,bkrtx.com,CroLAX
  - DOMAIN-SUFFIX,blog.com,CroLAX
  - DOMAIN-SUFFIX,blogcdn.com,CroLAX
  - DOMAIN-SUFFIX,blogger.com,CroLAX
  - DOMAIN-SUFFIX,blogsmithmedia.com,CroLAX
  - DOMAIN-SUFFIX,blogspot.com,CroLAX
  - DOMAIN-SUFFIX,blogspot.hk,CroLAX
  - DOMAIN-SUFFIX,bloomberg.com,CroLAX
  - DOMAIN-SUFFIX,box.com,CroLAX
  - DOMAIN-SUFFIX,box.net,CroLAX
  - DOMAIN-SUFFIX,cachefly.net,CroLAX
  - DOMAIN-SUFFIX,chromium.org,CroLAX
  - DOMAIN-SUFFIX,cl.ly,CroLAX
  - DOMAIN-SUFFIX,cloudflare.com,CroLAX
  - DOMAIN-SUFFIX,cloudfront.net,CroLAX
  - DOMAIN-SUFFIX,cloudmagic.com,CroLAX
  - DOMAIN-SUFFIX,cmail19.com,CroLAX
  - DOMAIN-SUFFIX,cnet.com,CroLAX
  - DOMAIN-SUFFIX,cocoapods.org,CroLAX
  - DOMAIN-SUFFIX,comodoca.com,CroLAX
  - DOMAIN-SUFFIX,crashlytics.com,CroLAX
  - DOMAIN-SUFFIX,culturedcode.com,CroLAX
  - DOMAIN-SUFFIX,d.pr,CroLAX
  - DOMAIN-SUFFIX,danilo.to,CroLAX
  - DOMAIN-SUFFIX,dayone.me,CroLAX
  - DOMAIN-SUFFIX,db.tt,CroLAX
  - DOMAIN-SUFFIX,deskconnect.com,CroLAX
  - DOMAIN-SUFFIX,disq.us,CroLAX
  - DOMAIN-SUFFIX,disqus.com,CroLAX
  - DOMAIN-SUFFIX,disquscdn.com,CroLAX
  - DOMAIN-SUFFIX,dnsimple.com,CroLAX
  - DOMAIN-SUFFIX,docker.com,CroLAX
  - DOMAIN-SUFFIX,dribbble.com,CroLAX
  - DOMAIN-SUFFIX,droplr.com,CroLAX
  - DOMAIN-SUFFIX,duckduckgo.com,CroLAX
  - DOMAIN-SUFFIX,dueapp.com,CroLAX
  - DOMAIN-SUFFIX,dytt8.net,CroLAX
  - DOMAIN-SUFFIX,edgecastcdn.net,CroLAX
  - DOMAIN-SUFFIX,edgekey.net,CroLAX
  - DOMAIN-SUFFIX,edgesuite.net,CroLAX
  - DOMAIN-SUFFIX,engadget.com,CroLAX
  - DOMAIN-SUFFIX,entrust.net,CroLAX
  - DOMAIN-SUFFIX,eurekavpt.com,CroLAX
  - DOMAIN-SUFFIX,evernote.com,CroLAX
  - DOMAIN-SUFFIX,fabric.io,CroLAX
  - DOMAIN-SUFFIX,fast.com,CroLAX
  - DOMAIN-SUFFIX,fastly.net,CroLAX
  - DOMAIN-SUFFIX,fc2.com,CroLAX
  - DOMAIN-SUFFIX,feedburner.com,CroLAX
  - DOMAIN-SUFFIX,feedly.com,CroLAX
  - DOMAIN-SUFFIX,feedsportal.com,CroLAX
  - DOMAIN-SUFFIX,fiftythree.com,CroLAX
  - DOMAIN-SUFFIX,firebaseio.com,CroLAX
  - DOMAIN-SUFFIX,flexibits.com,CroLAX
  - DOMAIN-SUFFIX,flickr.com,CroLAX
  - DOMAIN-SUFFIX,flipboard.com,CroLAX
  - DOMAIN-SUFFIX,g.co,CroLAX
  - DOMAIN-SUFFIX,gabia.net,CroLAX
  - DOMAIN-SUFFIX,geni.us,CroLAX
  - DOMAIN-SUFFIX,gfx.ms,CroLAX
  - DOMAIN-SUFFIX,ggpht.com,CroLAX
  - DOMAIN-SUFFIX,ghostnoteapp.com,CroLAX
  - DOMAIN-SUFFIX,git.io,CroLAX
  - DOMAIN-KEYWORD,github,CroLAX
  - DOMAIN-KEYWORD,linkedin,CroLAX
  - DOMAIN-SUFFIX,globalsign.com,CroLAX
  - DOMAIN-SUFFIX,gmodules.com,CroLAX
  - DOMAIN-SUFFIX,godaddy.com,CroLAX
  - DOMAIN-SUFFIX,golang.org,CroLAX
  - DOMAIN-SUFFIX,gongm.in,CroLAX
  - DOMAIN-SUFFIX,goo.gl,CroLAX
  - DOMAIN-SUFFIX,goodreaders.com,CroLAX
  - DOMAIN-SUFFIX,goodreads.com,CroLAX
  - DOMAIN-SUFFIX,gravatar.com,CroLAX
  - DOMAIN-SUFFIX,gstatic.com,CroLAX
  - DOMAIN-SUFFIX,gvt0.com,CroLAX
  - DOMAIN-SUFFIX,hockeyapp.net,CroLAX
  - DOMAIN-SUFFIX,hotmail.com,CroLAX
  - DOMAIN-SUFFIX,icons8.com,CroLAX
  - DOMAIN-SUFFIX,ift.tt,CroLAX
  - DOMAIN-SUFFIX,ifttt.com,CroLAX
  - DOMAIN-SUFFIX,iherb.com,CroLAX
  - DOMAIN-SUFFIX,imageshack.us,CroLAX
  - DOMAIN-SUFFIX,img.ly,CroLAX
  - DOMAIN-SUFFIX,imgur.com,CroLAX
  - DOMAIN-SUFFIX,imore.com,CroLAX
  - DOMAIN-SUFFIX,instapaper.com,CroLAX
  - DOMAIN-SUFFIX,ipn.li,CroLAX
  - DOMAIN-SUFFIX,is.gd,CroLAX
  - DOMAIN-SUFFIX,issuu.com,CroLAX
  - DOMAIN-SUFFIX,itgonglun.com,CroLAX
  - DOMAIN-SUFFIX,itun.es,CroLAX
  - DOMAIN-SUFFIX,ixquick.com,CroLAX
  - DOMAIN-SUFFIX,j.mp,CroLAX
  - DOMAIN-SUFFIX,js.revsci.net,CroLAX
  - DOMAIN-SUFFIX,jshint.com,CroLAX
  - DOMAIN-SUFFIX,jtvnw.net,CroLAX
  - DOMAIN-SUFFIX,justgetflux.com,CroLAX
  - DOMAIN-SUFFIX,kat.cr,CroLAX
  - DOMAIN-SUFFIX,klip.me,CroLAX
  - DOMAIN-SUFFIX,libsyn.com,CroLAX
  - DOMAIN-SUFFIX,linode.com,CroLAX
  - DOMAIN-SUFFIX,lithium.com,CroLAX
  - DOMAIN-SUFFIX,littlehj.com,CroLAX
  - DOMAIN-SUFFIX,live.com,CroLAX
  - DOMAIN-SUFFIX,live.net,CroLAX
  - DOMAIN-SUFFIX,livefilestore.com,CroLAX
  - DOMAIN-SUFFIX,llnwd.net,CroLAX
  - DOMAIN-SUFFIX,macid.co,CroLAX
  - DOMAIN-SUFFIX,macromedia.com,CroLAX
  - DOMAIN-SUFFIX,macrumors.com,CroLAX
  - DOMAIN-SUFFIX,mashable.com,CroLAX
  - DOMAIN-SUFFIX,mathjax.org,CroLAX
  - DOMAIN-SUFFIX,medium.com,CroLAX
  - DOMAIN-SUFFIX,mega.co.nz,CroLAX
  - DOMAIN-SUFFIX,mega.nz,CroLAX
  - DOMAIN-SUFFIX,megaupload.com,CroLAX
  - DOMAIN-SUFFIX,microsofttranslator.com,CroLAX
  - DOMAIN-SUFFIX,mindnode.com,CroLAX
  - DOMAIN-SUFFIX,mobile01.com,CroLAX
  - DOMAIN-SUFFIX,modmyi.com,CroLAX
  - DOMAIN-SUFFIX,msedge.net,CroLAX
  - DOMAIN-SUFFIX,myfontastic.com,CroLAX
  - DOMAIN-SUFFIX,name.com,CroLAX
  - DOMAIN-SUFFIX,nextmedia.com,CroLAX
  - DOMAIN-SUFFIX,nsstatic.net,CroLAX
  - DOMAIN-SUFFIX,nssurge.com,CroLAX
  - DOMAIN-SUFFIX,nyt.com,CroLAX
  - DOMAIN-SUFFIX,nytimes.com,CroLAX
  - DOMAIN-SUFFIX,omnigroup.com,CroLAX
  - DOMAIN-SUFFIX,onedrive.com,CroLAX
  - DOMAIN-SUFFIX,onenote.com,CroLAX
  - DOMAIN-SUFFIX,ooyala.com,CroLAX
  - DOMAIN-SUFFIX,openvpn.net,CroLAX
  - DOMAIN-SUFFIX,openwrt.org,CroLAX
  - DOMAIN-SUFFIX,orkut.com,CroLAX
  - DOMAIN-SUFFIX,osxdaily.com,CroLAX
  - DOMAIN-SUFFIX,outlook.com,CroLAX
  - DOMAIN-SUFFIX,ow.ly,CroLAX
  - DOMAIN-SUFFIX,paddleapi.com,CroLAX
  - DOMAIN-SUFFIX,parallels.com,CroLAX
  - DOMAIN-SUFFIX,parse.com,CroLAX
  - DOMAIN-SUFFIX,pdfexpert.com,CroLAX
  - DOMAIN-SUFFIX,periscope.tv,CroLAX
  - DOMAIN-SUFFIX,pinboard.in,CroLAX
  - DOMAIN-SUFFIX,pinterest.com,CroLAX
  - DOMAIN-SUFFIX,pixelmator.com,CroLAX
  - DOMAIN-SUFFIX,pixiv.net,CroLAX
  - DOMAIN-SUFFIX,playpcesor.com,CroLAX
  - DOMAIN-SUFFIX,playstation.com,CroLAX
  - DOMAIN-SUFFIX,playstation.com.hk,CroLAX
  - DOMAIN-SUFFIX,playstation.net,CroLAX
  - DOMAIN-SUFFIX,playstationnetwork.com,CroLAX
  - DOMAIN-SUFFIX,pushwoosh.com,CroLAX
  - DOMAIN-SUFFIX,rime.im,CroLAX
  - DOMAIN-SUFFIX,servebom.com,CroLAX
  - DOMAIN-SUFFIX,sfx.ms,CroLAX
  - DOMAIN-SUFFIX,shadowsocks.org,CroLAX
  - DOMAIN-SUFFIX,sharethis.com,CroLAX
  - DOMAIN-SUFFIX,shazam.com,CroLAX
  - DOMAIN-SUFFIX,skype.com,CroLAX
  - DOMAIN-SUFFIX,smartdnsProxy.com,CroLAX
  - DOMAIN-SUFFIX,smartmailcloud.com,CroLAX
  - DOMAIN-SUFFIX,sndcdn.com,CroLAX
  - DOMAIN-SUFFIX,sony.com,CroLAX
  - DOMAIN-SUFFIX,soundcloud.com,CroLAX
  - DOMAIN-SUFFIX,sourceforge.net,CroLAX
  - DOMAIN-SUFFIX,spotify.com,CroLAX
  - DOMAIN-SUFFIX,squarespace.com,CroLAX
  - DOMAIN-SUFFIX,sstatic.net,CroLAX
  - DOMAIN-SUFFIX,st.luluku.pw,CroLAX
  - DOMAIN-SUFFIX,stackoverflow.com,CroLAX
  - DOMAIN-SUFFIX,startpage.com,CroLAX
  - DOMAIN-SUFFIX,staticflickr.com,CroLAX
  - DOMAIN-SUFFIX,steamcommunity.com,CroLAX
  - DOMAIN-SUFFIX,symauth.com,CroLAX
  - DOMAIN-SUFFIX,symcb.com,CroLAX
  - DOMAIN-SUFFIX,symcd.com,CroLAX
  - DOMAIN-SUFFIX,tapbots.com,CroLAX
  - DOMAIN-SUFFIX,tapbots.net,CroLAX
  - DOMAIN-SUFFIX,tdesktop.com,CroLAX
  - DOMAIN-SUFFIX,techcrunch.com,CroLAX
  - DOMAIN-SUFFIX,techsmith.com,CroLAX
  - DOMAIN-SUFFIX,thepiratebay.org,CroLAX
  - DOMAIN-SUFFIX,theverge.com,CroLAX
  - DOMAIN-SUFFIX,time.com,CroLAX
  - DOMAIN-SUFFIX,timeinc.net,CroLAX
  - DOMAIN-SUFFIX,tiny.cc,CroLAX
  - DOMAIN-SUFFIX,tinypic.com,CroLAX
  - DOMAIN-SUFFIX,tmblr.co,CroLAX
  - DOMAIN-SUFFIX,todoist.com,CroLAX
  - DOMAIN-SUFFIX,trello.com,CroLAX
  - DOMAIN-SUFFIX,trustasiassl.com,CroLAX
  - DOMAIN-SUFFIX,tumblr.co,CroLAX
  - DOMAIN-SUFFIX,tumblr.com,CroLAX
  - DOMAIN-SUFFIX,tweetdeck.com,CroLAX
  - DOMAIN-SUFFIX,tweetmarker.net,CroLAX
  - DOMAIN-SUFFIX,twitch.tv,CroLAX
  - DOMAIN-SUFFIX,txmblr.com,CroLAX
  - DOMAIN-SUFFIX,typekit.net,CroLAX
  - DOMAIN-SUFFIX,ubertags.com,CroLAX
  - DOMAIN-SUFFIX,ublock.org,CroLAX
  - DOMAIN-SUFFIX,ubnt.com,CroLAX
  - DOMAIN-SUFFIX,ulyssesapp.com,CroLAX
  - DOMAIN-SUFFIX,urchin.com,CroLAX
  - DOMAIN-SUFFIX,usertrust.com,CroLAX
  - DOMAIN-SUFFIX,v.gd,CroLAX
  - DOMAIN-SUFFIX,vimeo.com,CroLAX
  - DOMAIN-SUFFIX,vimeocdn.com,CroLAX
  - DOMAIN-SUFFIX,vine.co,CroLAX
  - DOMAIN-SUFFIX,vivaldi.com,CroLAX
  - DOMAIN-SUFFIX,vox-cdn.com,CroLAX
  - DOMAIN-SUFFIX,vsco.co,CroLAX
  - DOMAIN-SUFFIX,vultr.com,CroLAX
  - DOMAIN-SUFFIX,w.org,CroLAX
  - DOMAIN-SUFFIX,w3schools.com,CroLAX
  - DOMAIN-SUFFIX,webtype.com,CroLAX
  - DOMAIN-SUFFIX,wikiwand.com,CroLAX
  - DOMAIN-SUFFIX,wikileaks.org,CroLAX
  - DOMAIN-SUFFIX,wikimedia.org,CroLAX
  - DOMAIN-SUFFIX,wikipedia.com,CroLAX
  - DOMAIN-SUFFIX,wikipedia.org,CroLAX
  - DOMAIN-SUFFIX,windows.com,CroLAX
  - DOMAIN-SUFFIX,windows.net,CroLAX
  - DOMAIN-SUFFIX,wire.com,CroLAX
  - DOMAIN-SUFFIX,wordpress.com,CroLAX
  - DOMAIN-SUFFIX,workflowy.com,CroLAX
  - DOMAIN-SUFFIX,wp.com,CroLAX
  - DOMAIN-SUFFIX,wsj.com,CroLAX
  - DOMAIN-SUFFIX,wsj.net,CroLAX
  - DOMAIN-SUFFIX,xda-developers.com,CroLAX
  - DOMAIN-SUFFIX,xeeno.com,CroLAX
  - DOMAIN-SUFFIX,xiti.com,CroLAX
  - DOMAIN-SUFFIX,yahoo.com,CroLAX
  - DOMAIN-SUFFIX,yimg.com,CroLAX
  - DOMAIN-SUFFIX,ying.com,CroLAX
  - DOMAIN-SUFFIX,yoyo.org,CroLAX
  - DOMAIN-SUFFIX,ytimg.com,CroLAX
  - DOMAIN-SUFFIX,telegram.me,CroLAX
  - DOMAIN-SUFFIX,v2ex.com,CroLAX
  - DOMAIN-SUFFIX,poe.com,CroLAX
  - DOMAIN-SUFFIX,poecdn.net,CroLAX
  - DOMAIN-SUFFIX,quoracdn.net,CroLAX
  - IP-CIDR,91.108.4.0/22,CroLAX
  - IP-CIDR,91.108.8.0/22,CroLAX
  - IP-CIDR,91.108.56.0/22,CroLAX
  - IP-CIDR,109.239.140.0/24,CroLAX
  - IP-CIDR,149.154.160.0/20,CroLAX
  - IP-CIDR,127.0.0.0/8,DIRECT
  - IP-CIDR,172.16.0.0/12,DIRECT
  - IP-CIDR,192.168.0.0/16,DIRECT
  - IP-CIDR,10.0.0.0/8,DIRECT
  - IP-CIDR,17.0.0.0/8,DIRECT
  - IP-CIDR,100.64.0.0/10,DIRECT
  - GEOIP,CN,DIRECT
  - MATCH,CroLAX
```

## 效果

![ ](https://i.postimg.cc/QNfg6xHj/Pix-Pin-2025-11-30-20-04-25.png)


## 通过代理IP结合指纹浏览器上网

## 简单解释

本方式针对于对地理位置高度敏感的应用：claude、paypal。不同的IP不在于连接速度快慢，而在于是否看起来像真人上网。IP看起来像真人上网就越纯净，价格也会越高。大多数数据中心IP因为是和其他人共享的，所以有流量限制。静态IP虽没有流量限制，但会有带宽限速。

* 纯净度：静态住宅IP > 动态住宅IP > 移动IP > 数据中心IP
* IP纯净度检测：https://www.ping0.cc 
* IP检测站点补充：[nodeseek -【分享】几个检测IP的网站，检测结果的准确性可靠性，本人不做解释，供参考](https://www.nodeseek.com/post-107402-1) 

大多数数据中心IP（通常指云服务器、VPS等共享环境下的IP）之所以相对没有带宽限速，但有流量限制，主要源于其资源分配和成本控制模型。在共享环境中，多个用户或实例共享底层物理硬件和网络资源，包括带宽。这意味着单个用户可以根据可用资源“突发”（burst）使用较高的带宽速度，而不会被严格限速到固定值，因为提供商希望最大化资源利用率，避免闲置带宽浪费。同时，为了防止少数用户过度消耗总数据传输量（这会增加提供商的 peering 或上游流量成本），他们通过设置月度或总流量上限来控制整体使用，确保公平性和可持续性。

相比之下，静态IP（往往与专用服务器或固定链路关联）没有流量限制，是因为它分配了专属资源，用户支付了更高的费用来独占固定带宽（如100Mbps或1Gbps端口）。这种专用设置允许无限数据传输（只要不超出物理极限），但带宽会被限速到合同约定的值，以匹配用户付费水平并防止超出硬件容量。如果不限速，可能会导致网络拥塞或额外基础设施投资。这种差异本质上是提供商的商业策略：共享IP强调灵活性和成本效益，通过流量限来平衡；静态IP强调稳定性和性能，通过带宽限来定义服务等级。

## 使用方式

!> 看起来也只是相对纯净一点，但还是不能注册 misskey.io 账号...

上网方式：

1. https://www.kookeey.com 购买 IP
2. https://www.hubstudio.cn 下载指纹浏览器
3. clash 开启 服务模式 和 tun 模式

kookeey操作：

* 静态住宅ISP代理 -> 购买静态住宅ISP代理

指纹浏览器操作：

* 新建环境 -> 代理类型 选择 socks 5 > 代理主机 填写购买的服务器地址
 * 下一步，代理账号和代理密码直接复制kookeey提供的账号及密码就行，并勾选IP变更提醒
 * 点击完成，点击打开创建使用的新环境。

### 关键操作截图

填写方式

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/uploads/2025/PixPin_2025-12-23_07-34-22.webp)

相关原理，详细见：[Clash for Windows 代理工具使用说明](https://docs.gtk.pw/)

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/uploads/2025/PixPin_2025-12-23_08-26-34.webp)

https://www.ping0.cc 检测结果

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/uploads/2025/PixPin_2025-12-23_08-19-59.webp)


## 无法使用Gemini（ipdodo）

> 转载自 ipdodo 团队 - 《2026最新修复指南：解决电脑翻墙后chrome浏览器无法使用谷歌gemini问题》,原文见：https://www.ipdodo.com/news/15150 

## 2026最新修复指南：解决电脑翻墙后chrome浏览器无法使用谷歌gemini问题

明明已经开启了网络代理，并且将节点切换到了美国或英国等Gemini支持的地区，但在Chrome浏览器中访问Google Gemini时，依然弹出“Gemini is not available in your country”的提示，导致gemini无法使用？这种“明明翻了却像没翻”的问题，困扰了无数用户。其实，这往往是Chrome浏览器的某些底层协议“出卖”了你的真实位置。本文将围绕 QUIC 协议、WebRTC、IPv6、浏览器缓存、异常流量和 IP 质量几个方向，帮助你排查并**解决电脑翻墙后 Chrome 浏览器无法使用谷歌 Gemini 的问题**。

![img](https://www.ipdodo.com/news/wp-content/uploads/2026/01/%E8%A7%A3%E5%86%B3%E7%94%B5%E8%84%91%E7%BF%BB%E5%A2%99%E5%90%8Echrome%E6%B5%8F%E8%A7%88%E5%99%A8%E6%97%A0%E6%B3%95%E4%BD%BF%E7%94%A8%E8%B0%B7%E6%AD%8Cgemini%E9%97%AE%E9%A2%98-1024x548.jpg)

### 一、 为什么电脑翻墙后chrome浏览器无法使用谷歌gemini？

在尝试各种复杂的网络设置之前，我们需要先了解一个被90%用户忽视的浏览器特性——QUIC协议。当你发现代理开启后依然**gemini无法使用**，很有可能是因为Chrome默认开启的QUIC协议绕过了你的代理隧道。

#### 1. 什么是QUIC？

QUIC（Quick UDP Internet Connections）是由Google开发的一种基于UDP的传输协议。它的初衷是为了让网页加载更快，通过减少连接建立的延迟来提升用户体验。

#### 2. 为什么它会“出卖”你？

大多数普通的代理工具主要针对TCP流量进行封装和加密。然而，QUIC是基于UDP的。如果你的代理配置没有强制接管所有UDP流量，或者浏览器认为直连速度更快，QUIC协议产生的流量就有可能绕过代理，直接从你的本地网络发送给Google服务器。

这时候，Google看到的不是你代理服务器的IP，而是你本地运营商的真实IP。这就是为什么明明挂了梯子，却依然需要**解决电脑翻墙后chrome浏览器无法使用谷歌gemini问题**的根本原因。

[**领取新用户礼包**](https://www.ipdodo.com/account/register?cid=un97)

### 二、 如何在Chrome中禁用QUIC协议

通过在Chrome的实验性功能中禁用QUIC，可以强制浏览器退回到传统的TCP连接，从而确保所有流量都走代理通道。

以下是详细的操作步骤：

1.**进入设置页面：**
打开你的Chrome浏览器，在顶部的地址栏中输入 chrome://flags/ 并按下回车键（Enter）。这将带你进入Chrome的实验室设置页面。

![img](https://www.ipdodo.com/news/wp-content/uploads/2026/01/%E6%AD%A5%E9%AA%A4%E4%B8%80.png)

 

2.**搜索QUIC选项：**
在页面顶部的搜索框中，输入关键词 QUIC。

3.**定位关键设置：**
在搜索结果中，找到名为 **“**Experimental QUIC protocol**”** 的选项。

![img](https://www.ipdodo.com/news/wp-content/uploads/2026/01/%E6%AD%A5%E9%AA%A4%E4%BA%8C.png)

 

4.**修改状态：**
点击该选项右侧的下拉菜单（默认通常是Default），将其修改为 **“**Disabled**”**（禁用）。

![img](https://www.ipdodo.com/news/wp-content/uploads/2026/01/%E6%AD%A5%E9%AA%A4%E4%B8%89.png)

5.**重启浏览器：**
修改完成后，浏览器底部会弹出一个蓝色的 **“**Relaunch**”** 按钮。点击它，Chrome会自动重启。

重启后，再次尝试访问Gemini。对于很多用户来说，仅仅这一个步骤就能成功解决电脑翻墙后chrome浏览器无法使用谷歌gemini问题。

### 三、 进阶排查：WebRTC与IPv6的潜在泄露

如果禁用了QUIC协议后，**gemini打不开**的情况依然存在，那么我们需要进一步检查其他的“漏网之鱼”。

#### 1. 堵住WebRTC泄露

WebRTC是一种支持浏览器进行实时语音或视频对话的技术，但它有一个著名的副作用：容易泄露用户的真实局域网IP和公网IP。

- **解决方案：** 在Chrome应用商店搜索并安装“WebRTC Leak Prevent”类插件，或者在你的代理软件设置中勾选“阻断WebRTC”。

#### 2. 禁用IPv6

目前很多代理节点仅支持IPv4。如果你的本地网络开启了IPv6，Chrome可能会优先尝试通过IPv6直连Google服务器。由于代理不接管IPv6流量，你的真实位置瞬间暴露。

- **解决方案：** 在操作系统的网络适配器设置中，取消勾选“Internet 协议版本 6 (TCP/IPv6)”。

推荐阅读：[IPv6是什么？一文看懂IPv6，了解IPv6的核心优势](https://www.ipdodo.com/news/13955/?cid=un97)

### 四、 终极防线：IP质量

如果你把QUIC关了、WebRTC堵了、缓存也清了，但依然面临解决电脑翻墙后chrome浏览器无法使用谷歌gemini问题的困境，那么问题大概率不在你的设置，而在你使用的“IP”本身。

#### 1. 为什么IP会被封？

Google的风控系统拥有庞大的黑名单数据库。很多免费的或廉价的代理服务，使用的是“数据中心IP”。成千上万的用户挤在同一个IP地址下访问Gemini，这种异常的流量特征会被Google瞬间识别为“代理/机器人”，从而直接在服务器端拒绝服务，哪怕你的伪装做得再好也没用。

#### 2. 打造纯净的住宅网络环境

为了解决由IP脏、IP复用率高导致的**gemini无法使用**问题，升级网络资源的质量是必经之路。

在这里，推荐大家尝试 [IPdodo](https://www.ipdodo.com/?cid=un97) 的服务。与容易被识别的数据中心IP不同，IPdodo 专注于提供高质量的[住宅IP](https://www.ipdodo.com/product/static-home?cid=un97)。

- **真实住宅IP：**静态住宅IP覆盖约65个国家，提供美国、日本、台湾、韩国、巴西等高质量原生IP，用户可根据目标受众国家选择最佳节点。
- **独享性：** 纯净的IP环境意味着你不会受到“邻居”违规操作的牵连。

通过 [IPdodo](https://www.ipdodo.com/?cid=un97) 构建的高信任度网络环境，配合上述禁用QUIC的操作，可以形成“浏览器设置+底层网络”的双重保障，这是目前攻克Gemini地区限制最稳妥的方案。

[**注册获取原生住宅IP**](https://www.ipdodo.com/account/register?cid=un97)

### 五、 浏览器环境的“大扫除”

在完成了网络层面的优化后，别忘了清理浏览器留下的“痕迹”。

1. **清除Location定位权限：**
   检查Chrome设置，确保没有赋予Gemini网站获取你地理位置的权限。
2. **清理Cookie和缓存：**
   旧的Cookie可能记录了你之前的登录位置。按 Ctrl+Shift+Delete，清除关于 Google 和 Gemini 的所有缓存数据。
3. **语言设置：**
   尝试将Chrome浏览器的首选语言设置为“英语（美国）”，这有时也能作为辅助验证手段，帮助通过Google的检测。

### 六、常见问题FAQ

#### 1. 挂了梯子还是用不了Gemini怎么办？

先关闭 Chrome 的 QUIC 协议，再检查 WebRTC、IPv6、DNS、缓存和 Google 账号环境。如果仍然失败，重点检查当前节点是否为共享高风险 IP。

#### 2.Gemini网页打不开是Chrome的问题吗？

不一定。可能是 Chrome 的 QUIC、WebRTC、IPv6 泄露，也可能是 IP 地区不支持、DNS 异常、缓存冲突或网络质量差。

#### 3. 为什么翻墙后还是无法使用Gemini？

因为 Gemini 不只看你是否“连上代理”，还会综合判断 IP、DNS、浏览器协议、账号地区、缓存和网络请求行为。如果其中一项暴露异常，就可能导致无法使用。

#### 4. Gemini纯净节点有必要吗？

如果只是偶尔使用，普通稳定网络也许够用。但如果你长期使用 Gemini 做工作，或频繁遇到异常流量、地区不可用、网页打不开，干净、稳定、长期一致的网络环境会更可靠。

### 七、 总结

回顾全文，**解决电脑翻墙后chrome浏览器无法使用谷歌gemini问题****，**本质上是一场关于“隐私保护”与“风控检测”的博弈。希望这篇指南能帮助你排除故障，顺利连接Gemini，在AI的浪潮中保持领先。如果你身边的朋友也遇到了gemini无法使用的困扰，不妨将这篇文章分享给他们。


## 无法使用Gemini（自用方案）

> **【提示】** 建议在配置完 ipdodo 团队方案后，再来参考本章节

配置及效果如图

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/uploads/2026/20260815191634.png)

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/uploads/2026/20260815191640.png)

![](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/uploads/2026/20260815191641.png)

> **【重要】** > 为什么浏览器翻墙后，定位也是在台湾、美国，关闭了QUIC协议也没用，clash选择Research+Al ，US Fixed IP，就能正常访问Gemini了呢？ 以下由Manus AI解答。

核心原因是：**“浏览器显示的定位”与“Gemini 用来决定是否放行的地区判定”不是同一件事；关闭 QUIC 也只改变了一种传输协议，无法改变代理出口、DNS、WebRTC、账号和 IP 信誉等因素。**

## 一、为什么翻墙后仍显示台湾或美国

浏览器里的“定位”通常有三种来源，不能简单等同于你的真实物理位置。

| 定位来源           | 实际依据                                | 典型现象                     |
| :----------------- | :-------------------------------------- | :--------------------------- |
| IP 地理库          | 当前出口 IP 的归属数据库                | 显示台湾、美国或其他国家               |
| 浏览器地理定位 API | Wi‑Fi、基站、设备定位；通常需要授权     | 可能接近真实位置，也可能失败 |
| 网站自身推断       | DNS、时区、语言、Cookie、账号、网络特征 | 与 IP 定位结果不一致         |

如果你看到的是搜索页、网站页脚或某个 IP 查询网站显示“台湾/美国”，大概率只是**代理出口 IP 的地理数据库结果**。这些数据库存在滞后、误标和不同步，尤其是云厂商、转售 IP、IPv6 段和 CDN 出口，不同网站显示不同国家很正常。

如果你看到的是浏览器弹出的定位权限结果，则它可能来自浏览器的地理定位 API，而不是代理 IP。代理软件通常不能把 Wi‑Fi 扫描、系统定位或浏览器权限返回的坐标自动改成代理所在地。

## 二、为什么关闭 QUIC 仍然没有改善

QUIC 是基于 UDP 的传输协议，HTTP/3 通常建立在 QUIC 之上。关闭它后，浏览器往往回退到 TCP 上的 HTTP/2 或 HTTP/1.1；这**不等于更换了代理出口，也不等于清除了其他定位和风控信号**。

关闭 QUIC 可能影响的是“某些 UDP 流量是否绕过代理”或“某个连接是否能建立”，但以下因素仍然可能保持不变：

| 仍可能暴露或影响判定的因素 | 说明                                                         |
| :------------------------- | :----------------------------------------------------------- |
| 出口 IP                    | 代理最终从哪个 IP 访问 Google，仍是最重要因素之一            |
| DNS                        | DNS 可能由本地网络、代理节点或远端解析，三者结果不同         |
| IPv6                       | 如果代理只接管 IPv4，而浏览器或系统仍使用原生 IPv6，可能出现出口不一致 |
| WebRTC                     | 某些浏览器或配置可能暴露本地网络接口或候选地址；是否暴露取决于浏览器和策略，[4] |
| Cookie 与账号              | Google 可能依据账号历史地区、登录活动、语言、支付资料等判断环境一致性 |
| TLS/浏览器特征             | 代理链路和浏览器组合可能被用于风险评分，但通常不是单一决定因素 |
| IP 信誉                    | 数据中心 IP、共享 IP、被大量滥用过的 IP，可能触发额外验证或限制 |

因此，**QUIC 不是“翻墙是否成功”的总开关**。它最多解决某一类 UDP/HTTP3 连接问题；如果根因是 IP 被识别、DNS 泄漏、IPv6 泄漏、规则未命中或账号地区不一致，关闭 QUIC 通常不会有效。

## 三、为什么选择 “Research + AI，US Fixed IP” 后 Gemini 能正常访问

从现象看，最可能的变化不是“Research”这个名称本身，而是这个配置组合改变了**Gemini 相关请求的实际路由和出口质量**。

### 1. “AI”规则可能覆盖了更多 Google/Gemini 域名

Gemini 并不只访问一个域名。页面、登录、静态资源、接口、风控和账户服务可能分别使用不同的 Google 域名。如果普通代理规则只代理了主站，其他请求仍可能走直连或走了不合适的节点，就会出现页面能开、功能不能用，或者反复跳转、验证失败的情况。

“Research + AI”这类策略组通常意味着它为研究或 AI 服务预设了更完整的域名规则，可能把 Gemini 相关请求统一送进代理。**真正起作用的可能是规则覆盖范围更完整，而不是标签文字。**

### 2. “US Fixed IP” 提供了稳定、可识别的美国出口

Gemini 的可用性判断通常会综合地区、IP、账号状态和风险信号。固定美国 IP 可能带来三项改善：

第一，IP 地理位置更稳定，减少一次请求显示美国、下一次请求显示台湾或其他地区的情况。第二，同一会话中的页面、接口、登录和资源请求更可能使用同一个国家的出口。第三，固定 IP 的信誉和历史使用情况可能比共享、轮换或被滥用的节点更好。

这里的“Fixed IP”不一定意味着住宅 IP，也不一定代表 Google 认可它是某个真实用户的家庭网络；它通常只表示**出口地址或出口映射相对固定**。能否使用还取决于该 IP 的 ASN、数据中心属性、滥用历史和 Google 的风险评分。

### 3. 其他配置可能同时改变了 DNS 和分流方式

某些 Clash 配置在切换策略组时，会连带改变远程 DNS、Fake-IP/Redir-Host 模式、IPv6 处理、代理规则和 TUN 接管范围。因此你观察到的“换成 US Fixed IP 后恢复”，可能是多个变化同时发生，而不只是 IP 国家从台湾变成美国。

## 四、最可能的因果链

结合你的描述，最合理的解释是：

普通配置下，浏览器或 Gemini 的部分请求没有保持一致的美国代理出口，或者使用了被识别为台湾、共享节点、异常数据中心节点的出口；关闭 QUIC没有改变这个根因。切换到“Research + AI”后，相关域名被更完整地代理，再配合“US Fixed IP”提供稳定的美国出口，Gemini 的地区和风险判定达到了可接受状态，因此恢复正常。

这不一定表示之前的节点“完全不能访问美国服务”，而更可能表示它的**出口一致性、IP 信誉或规则覆盖**不满足 Gemini 的风控要求。

## 五、建议按以下顺序排查

先在同一个 Clash 配置、同一个浏览器窗口中检查出口 IP。分别访问 IP 查询服务，确认 IPv4 和 IPv6 是否都指向预期国家；如果 IPv4 显示美国而 IPv6 显示本地或台湾，说明存在 IPv6 出口不一致问题。

然后检查 DNS。确认 Gemini 相关域名的 DNS 查询是否由代理侧完成，而不是由本地运营商解析。若使用 Fake-IP，需要确认 Fake-IP 与 TUN/系统代理模式之间没有冲突；若使用 Redir-Host，则要确认 DNS 没有被系统或浏览器 DoH 单独接管。

再检查规则命中情况。重点观察 Gemini 页面、登录、账户和静态资源请求是否全部命中同一个 AI/美国策略组，而不是主页面走代理、接口或账户服务走直连。浏览器开发者工具里的 Network 面板，以及 Clash 的连接日志通常可以看到这一点。

最后清理会话变量进行对比测试。可以使用一个全新的浏览器配置文件或隐私窗口，在不改变代理节点的情况下测试；如果新会话可用、原账号不可用，则账号地区、Cookie 或历史风险状态可能参与了判定。不要频繁切换多个国家的节点登录，否则会使地区和登录风险信号更加不一致。

## 结论

台湾、美国定位本身不一定是故障；它可能只是不同 IP 地理库或网站推断结果。关闭 QUIC无效也很正常，因为 QUIC只涉及传输协议。真正让 Gemini 恢复的关键，很可能是“AI 规则把相关请求完整送入代理”与“US Fixed IP 提供稳定、信誉更好的美国出口”这两个变化。


## 离岸爱国、数字侨居、脱钩与双重封锁

## 摘要

本文综合分析近年来中国社会中出现的几类看似分散却内在关联的现象：高净值群体在国内积累资源后转向境外布局成为「食利阶层」、网红式「离岸爱国」的公开表演与私下逃离、VPN的普遍使用与早期「以安全名义」的网络管控，以及中美在AI与高科技领域的双向地理封锁。更普遍的是，大量普通人虽物理空间仍处于境内信息管控环境，却通过数字工具与消费行为将精神与身份部分外置，形成「数字离岸」或「数字侨居」现象。与此同时，曾经喧嚣的网络民族主义声浪在近年来呈现相对收敛趋势；已经完成物理与经济退出的海外华人更普遍表现出对体制的批评态度，同时区分「党」与「人」。然而，跨境华人犯罪网络对同胞的系统性侵害，政策封锁、教育与海外经历所催生的崇洋倾向，以及部分留学生在海外生活后反而强化对中国文化圈生活方式的认同（而非对威权统治的认同），共同提醒我们：身份反应高度复杂，信任赤字与文化归属的张力并存。这些现象共同揭示：在高度不确定性与强叙事环境中，表演型忠诚与结构性风险对冲是理性反应，而真实态度的显现高度依赖于退出成本的高低。

## 一、引言

近年来，中国社会在个体选择、信息环境与国际技术竞争三个层面同时呈现出显著的张力与分裂。一方面，高净值群体在国内利用集中权力结构下的规则与关系快速积累资源，却同步将资产、子女教育与身份配置到境外，形成「国内积累、境外锁定」的双轨策略；网红与普通网民在公开场合高调宣示领土完整与爱国立场，却在签证受阻或私人表达中坦露希望长期居留境外的真实意愿。另一方面，国家以「安全」名义持续强化信息边界——从早期对公共无线网络的限制，到对VPN的常态化打击，再到对境外AI服务的屏蔽——而美国等西方国家的高科技企业则主动对中国IP实施地理封锁，形成「两头堵」的技术脱钩格局。

与此同时，大量普通人虽物理空间仍处于境内信息管控环境，却通过VPN、海外账号、跨境支付与平台区域切换，将数字生活部分迁移至境外规则体系，形成「数字侨居」。曾经高调喧嚣的网络民族主义（「小粉红」）声浪在近年来呈现相对收敛；已经完成物理与经济退出的海外华人更普遍愿意批评体制，同时区分「党」与「人」。然而，跨境华人犯罪网络对同胞的系统性侵害打破了族群内部天然团结的想象；政策封锁与海外经历既催生了崇洋倾向，也让部分留学生在经历文化冲击后，反而强化了对中国文化圈生活方式的认同——这种认同往往指向社会密度、饮食、家庭伦理与效率体验，而非对威权统治或强权政治的拥护。

这些现象看似分散，实则共享同一套逻辑：在强叙事与高不确定性并存的环境中，表演型忠诚成为获取国内资源的必要技能，而真实安全感则通过资产、身份、信息与数字工具的对冲来实现。本文旨在系统梳理这些现象，揭示其内在关联，并分析其社会代价。

## 二、个人层面的对冲：离岸爱国的具体行为逻辑与资产外置

离岸爱国并非抽象概念，而表现为一套可观察的行为模式。其核心是「公开表演忠诚」与「私下准备退出」的并行运作。

具体而言，离岸爱国行为通常包含以下环节：在公开场合（社交媒体、课堂、社群）高调宣示领土完整、国家统一与官方立场，以获取流量、认同与政治安全；同时，积极申请海外签证、留学或工作机会，并在私人对话或后续视频中坦露希望长期居留境外的真实意愿。2026年Rita案例即为典型：她在新西兰语言学校因同学自称「来自台湾」「来自香港」而高分贝强调「台湾是中国不可分割的一部分」，却在澳大利亚签证被拒后崩溃大哭并明确表示不想回国（三立新聞網, 2026）。这种行为模式的本质是将爱国话语工具化——它是进入国内流量与机会场的入场券，而非对生活地点的真实承诺。

高净值群体的资产外置则将这一逻辑系统化：

**1. 风险对冲（最核心的动机）** 政治与政策风险是首要驱动。国内权力结构高度集中，政策可以快速转向；再强势的人也能意识到，今天的资源优势可能明天就变成被清算的对象。把一部分资产、身份、子女教育放在境外，等于购买「政治保险」。法律与产权风险同样显著：国内对私有产权的保护强度与司法独立性，和国际主流发达国家相比仍有差距。一旦出现系统性风险（反腐运动、行业整顿、资本外逃管控等），境外资产更难被直接触及。汇率与资本管制风险也不可忽视——人民币并非完全自由兑换，提前布局境外资产可降低未来兑换与转移成本（Hess, 2016; Chau & Gherghina, 2024; Wong, 2021）。

**2. 财富保值与生活方式** 真正的「食利阶层」追求的是长期稳定的被动收入与高质量生活。许多发达国家在产权保护、法治环境、教育医疗、空气水质、社会秩序等方面仍具优势。把家人安顿在那里，自己可以两边飞，是很多人眼中更「理性」的选择。

**3. 代际传承与身份配置** 很多人为下一代准备的是全球通行的身份与机会（护照、绿卡、国际学校、海外大学）。国内再强势，也难保证下一代还能在同样的环境下继续保持优势。身份多元化本身就是一种对冲。

**4. 「在国内积累资源 + 在境外锁定收益」并不矛盾** 这其实是一种最优策略组合：国内负责积累和变现，境外负责锁定和享受。公开批评外流的人，自己有条件时往往也会做类似安排。

**5. 完整退出后的真实态度显现及其限度** 已经完成物理与经济退出的海外华人，更普遍批评体制，同时区分「党」与「人」（Ding, 2025; Pew Research Center, 2023; Wall Street Journal, 2024）。然而，活跃于东南亚、中东与非洲部分地区的跨境华人犯罪网络，系统性针对同胞实施电信诈骗与强迫劳动，彻底打破了「中国人不骗中国人」的想象。族群内部信任同样脆弱。

**6. 政策封锁、教育与海外经历催生的崇洋倾向** 信息管控与教育叙事将外部世界单向理想化，留学与海外生活进一步强化比较效应，部分人从对体制的批评滑向对本土的贬低与对外国符号的过度崇拜。

**7. 海外生活后的文化圈认同回流** 值得注意的是，部分留学生与海外生活者在经历初期的新鲜感与文化冲击后，反而强化了对中国文化圈生活方式的认同。这种认同通常指向高社会密度、熟悉的饮食与人际节奏、家庭伦理的确定性，以及某些公共服务或商业效率的体验，而非对威权统治或强权政治的拥护。文化冲击、孤独、歧视经历，或对西方社会问题（枪支、无家可归、身份政治撕裂等）的直接观察，都可能促使他们重新评估「哪里更适合自己生活」。这种回流是文化与生活层面的再认同，与政治忠诚之间存在清晰边界。它说明身份反应并非单向的「脱钩」或「崇洋」，而是在具体生活体验中不断校准的复杂过程。

## 三、信息控制的细致逻辑：早期无线网络限制、VPN封锁与数字侨居现象

国家早期以「安全」名义限制公共无线网络，以及持续对VPN的打击，构成了信息层面的系统性对冲。其逻辑可从三个层面理解：

**1. 信息流动的垄断与组织风险防控** 公共无线网络在早期被视为难以实名、难以追溯的入口，可能成为匿名传播敏感信息或组织集体行动的通道。限制或强制实名，本质上是将网络接入纳入可监控体系，降低「不可见」的社会动员风险。VPN则直接挑战防火墙的有效性，使个人能够绕过叙事边界，获取未被审查的信息。持续封锁VPN，是为了维持信息环境的可控性与官方叙事的垄断地位（Hoang et al., 2021）。

**2. 安全叙事的自我强化** 「以安全名义」成为一种万能正当化机制。它将技术限制转化为公共安全议题，使质疑者面临「不重视安全」的道德压力。这种叙事既服务于政治稳定，也服务于产业保护——为本土互联网与AI企业提供免于外部竞争的市场空间。

**3. 数字侨居：物理空间受限下的虚拟退出策略** 在物理迁移成本高昂、签证与资本管制严格的背景下，大量普通人转向一种「虚拟退出」策略。他们的物理存在仍处于境内信息管控环境，却通过VPN、海外账号、跨境支付与区域切换，将数字生活部分迁移至境外规则体系。Steam等平台用户通过切换至低价区域以更低成本获取数字商品的现象即为典型：其实质是在寻求一种「境外消费者」的价格与权限特权。这可被概念化为「数字离岸」或「数字侨居」：在物理边界难以突破时，个体通过技术手段将部分生活世界迁移至境外规则体系，以获取相对优势与心理距离。

## 四、网络民族主义声浪的相对收敛及其意涵

近年来，网络民族主义（「小粉红」）的公开声浪呈现出相对收敛的趋势。相较于2016–2020年高峰期大规模、情绪化的「出征」与集体动员，当前的民族主义表达在频率与烈度上有所下降。

依据Liu（2024）基于2011–2023年Google Trends与百度搜索数据的实证分析，中国民族主义的整体趋势自2018年（甚至更早）以来呈现下降态势。阶段性上升主要由短期事件驱动，而非长期结构性增强。这一收敛有多重原因：经济下行与青年就业压力使民生议题优先级上升，单纯依赖民族情绪动员的空间被压缩；平台生态从公开广场向圈层化、生活化内容迁移，降低了极端言论的传播效率；审查强化与对「过度消极情绪」的整治进一步规训了公开表达的边界；部分经历过现实落差的个体出现「脱粉」转向。

声浪的收敛并不意味着民族主义情绪消失，而是其表达形式发生了变化——从高调、自发的集体表演，转向更可控、更日常或更犬儒的状态。当表演忠诚的收益下降、真实风险感知上升时，个体会调整策略：从高调的民族主义表演，转向更隐蔽的资产、身份或数字外置。这一趋势与全文的核心逻辑一致。

## 五、技术与地缘政治层面的对冲：AI双向封锁

个人与信息层面的对冲，在国家与企业层面被放大为技术脱钩，形成典型的「两头堵」。

中国通过防火墙屏蔽ChatGPT等西方AI服务，既为了信息控制与意识形态安全，也为了保护与扶持本土大模型生态。与此同时，OpenAI、Anthropic、Google等美国AI公司主动屏蔽中国IP。Anthropic态度尤为强硬，明确将中国获取前沿模型视为对美国国家安全的关键威胁，并持续打击「蒸馏」行为（用输出训练自家模型）。其CEO公开将限制中国访问作为维护美国技术优势的关键措施（WIRED, 2026; Financial Times, 2026）。相关研究显示，美国出口管制虽成功切断部分对华技术供应，但也给美国供应商带来显著成本，并加速了全球技术生态的分裂（Crosignani et al., 2026）。

两边的逻辑是对称的：中国不让外部未审查信息与工具自由进入，美国不让最前沿算力与模型能力自由流向中国。结果是普通人被夹在中间——想使用境外先进工具需借助技术绕过手段，想使用境内工具则面临审查与能力差距。技术脱钩与个人层面的资产外置、数字侨居，本质上都是「不把鸡蛋放同一个篮子」的风险对冲，只是行动主体与规模不同。

## 六、局限与未来展望

本研究存在以下局限。第一，现象涵盖面广，但定量数据（尤其是关于数字侨居规模、民族主义声浪精确衰减曲线、海外华人态度分布）仍相对有限，主要依赖二手文献与公开报道。第二，跨境诈骗与崇洋倾向的讨论更多基于现象观察，系统性实证研究有待补充。第三，身份反应的个体差异巨大，本文概括的是主要趋势而非全貌。

未来研究可在以下方向深入：一是结合大数据与问卷调查，更精确测量民族主义表达的频率变化与数字侨居的实际规模；二是开展针对不同退出阶段（短期留学、长期居留、入籍）海外华人的比较研究，细化「文化认同」与「政治认同」的分离机制；三是考察信息开放程度、歧视经历与生活满意度如何共同塑造崇洋或文化回流；四是将跨境华人犯罪网络纳入更广泛的低信任社会研究框架，探讨其与国内社会信任结构的关联。只有在更扎实的经验基础上，才能更准确地理解表演型忠诚与风险对冲的动态演变。

## 七、统一的逻辑与批判性结论

强叙事与高不确定性并存，使表演忠诚成为获取国内资源的必要技能，而真实安全感只能通过私下对冲获得。从离岸爱国的公开表演与私下退出，到数字侨居，到网络民族主义声浪的相对收敛，到完整退出后真实态度的显现，到跨境诈骗所揭示的族群内部信任危机，到崇洋倾向与文化圈认同回流的并存，本质上都是同一套激励结构与信任赤字下的复杂反应。

完整退出后的海外华人态度具有对照意义：当不再需要表演时，批评体制而区分「人」成为常见模式。但跨境华人犯罪网络提醒我们不能将「人」浪漫化；部分留学生的文化圈认同回流则说明，身份反应并非简单的政治忠诚或全面否定，而包含对生活方式的具体评估。

这种模式的代价是深远的。它系统性地奖励口是心非，惩罚真诚表达；它让最有能力的人率先通过物理迁移或数字工具实现退出；它在技术与信息层面制造自我封闭与外部封锁的双重困境；它也侵蚀了人与人之间最基本的信任。只要激励结构不改变，这种撕裂就不会消失。真正危险的不是虚伪本身，而是虚伪已经变成了最理性的生存策略。

## 参考文献

Chau, G. W. F., & Gherghina, S. (2024). Conditional loyalty and exit: Explaining the emigration of wealthy Chinese after the 2012 leadership change. *Diaspora Studies*. https://doi.org/10.1163/09763457-bja10081

Crosignani, M., Han, L., Macchiavelli, M., & Silva, A. F. (2026). Securing technological leadership? The cost of export controls on firms. *Journal of Financial Economics, 175*, 104192. https://doi.org/10.1016/j.jfineco.2025.104192

Ding, S. (2025). New generation brings new challenges for China’s diaspora engagement. *East Asia Forum*. https://eastasiaforum.org/2025/07/12/new-generation-brings-new-challenges-for-chinas-diaspora-engagement/

Financial Times. (2026, July 9). OpenAI and Google sell AI models to blacklisted China groups. https://www.ft.com/content/5d6aafa1-5d47-4585-aa95-6ec06a6cd20f

Hess, S. (2016). The flight of the affluent in contemporary China: Exit, voice, loyalty, and the problem of wealth drain. *Asian Survey, 56*(4), 629–650. https://doi.org/10.1525/as.2016.56.4.629

Hoang, N. P., Niaki, A. A., Dalek, J., Knockel, J., Lin, P., Marczak, B., Crete-Nishihata, M., Gill, P., & Polychronakis, M. (2021). How great is the Great Firewall? Measuring China’s DNS censorship. In *30th USENIX Security Symposium* (pp. 3381–3398). USENIX Association. https://www.usenix.org/conference/usenixsecurity21/presentation/hoang

Liu, Y. (2024). Declining Chinese nationalism: Evidence based on internet search query data. *Nationalism and Ethnic Politics, 30*(4), 533–549. https://doi.org/10.1080/13537113.2024.2359253

Pew Research Center. (2023). How Chinese Americans view China, the U.S. and other places in Asia. https://www.pewresearch.org/2023/07/19/chinese-americans-views-of-china-and-other-places/

Wall Street Journal. (2024, December 1). How a young Chinese nationalist turned her back on Beijing. https://www.wsj.com/world/china/how-a-young-chinese-nationalist-turned-her-back-on-beijing-69bea291

Wang, E. N., & Huang, Q. (2026). *Fandom nationalism: Participatory censorship and performative patriotism in East Asia*. University of Groningen. https://doi.org/10.5040/9798765125175

WIRED. (2026, June 26). How people in China keep outsmarting Anthropic’s geolocation restrictions. https://www.wired.com/story/how-people-in-china-keep-outsmarting-anthropics-geolocation-restrictions/

Wong, A. (2021). Capital flight: The travel channel. *Journal of International Money and Finance, 117*, 102437. https://doi.org/10.1016/j.jimonfin.2021.102437

三立新聞網. (2026, August 22). 高喊台灣是中國的！陸網紅澳簽遭拒崩潰大哭　網酸：祖國這麼好幹嘛不回. https://www.setn.com/news/1893677


## 跨国阶层跃升中的零容错接力与资本特权

向下社会背景下低资本家庭的代际消亡与超高净值阶层的跨境套利研究

> **【重要】** 相关文本由 Gemini 开展分析及总结生成，本文内容已向旅居新加坡、日本的联系群友求证核对，确认该 AI 总结内容无明显较大疏漏与偏差。

## 摘要 (Abstract)

在当今全球经济增速放缓、地缘政治对抗加剧（向下社会）的宏观背景下，跨境人口流动与身份转换呈现出两极分化的极端态势。本文旨在全面系统地解构现代跨境流动的双重图谱：一方面，底层与普通中产家庭面临“零容错率（Zero-Tolerance）”的代际托举长跑，极易因健康、政策或资产泡沫等黑天鹅事件导致几代人的血汗累积瞬间归零，进而在人口学上做出主动断代的理性防御；另一方面，超高净值（UHNW）与顶流巨贾阶层则跨越了传统移民局与签证官的基层审查，进入由跨国律师团、私人银行、国家安全部门与经济特权交织的“幕后博弈”。研究表明，现代跨境流动本质上已演变为一套**对底层实行“工具人筛选”、对中产实行“容错率压榨”、对巨贾实行“国家级利益交换”**的弹性制度矩阵。

## 一、 引言：向下社会的阶层重力与跨境流动的双轨制

在全球化红利边际递减与主要经济体内部阶层固化的时代，“社会代际收入弹性（Intergenerational Income Elasticity, IGE）”在东亚及全球多个发达经济体中持续走高，意味着个体的阶层归宿越来越取决于其原生家庭的先赋性因素。传统依赖高等教育或国内市场红利实现阶层跃升的渠道严重贬值，促使不同阶层的家庭将目光转向海外（以日本、台湾、新加坡等东亚发达经济体为主要观测对象）。

然而，当前的跨境流动并非一条扁平的通道，而是呈现出清晰的**“流动双轨制”**：

1. **生存型/防御型流动（中下阶层）**：试图通过肉体出海或几代人积蓄“梭哈”，对抗国内阶层下滑的重力，其特征是高风险、低容错。
2. **套利型/避险型流动（极顶阶层）**：以顶流巨贾、顶流二代为代表，其核心诉求非福利与生存，而是“全球流动性（Global Mobility）”与“资产安全性”，其特征是资本开路、政治博弈。

## 二、 跨国移居路径的核心资本量化矩阵

根据皮埃尔·布尔迪厄（Pierre Bourdieu）的资本再生产理论，跨境流动的成败取决于经济、文化与社会资本的综合变现。不同阶层在面对日本、台湾、新加坡等地政策时，展现出截然不同的硬性准入矩阵：

### 1. 经济资本（Economic Capital）：硬性准入杠杆与持有成本

- **新加坡（精英/富裕路径）**：
  - **自雇就业准证（自雇EP）**：月薪门槛至少 **5,600新币** [MOM]（金融业为6,200新币），且需通过COMPASS互补专才积分架构（大龄申请者薪资要求可达1万新币/月以上）。每年公司运营、发薪、本地员工社保（CPF）及个人生活开销，最低维持成本在 **100万-150万人民币/年**。
  - **全球商业投资者计划（GIP/家办）**：方案A的投资门槛已大幅拉高至 **1,000万新币**（约740万美元） [EDB]。
- **日本（经营管理/高级人才路径）**：
  - **初始资本**：注册公司需至少 **500万日元**（约合3-4万美元）的资本金，且需维持真实的办公场所 [ISA]。
  - **维持成本**：每年公司运营、雇员、纳税及个人生活费需 **300万-500万日元**。
  - **总计**：在拿到永住（通常需要1-10年）之前，家庭需准备至少 **2000万-3000万日元**（约合13万-20万美元）的流动资金储备。
- **台湾（港澳/外籍移居路径）**：
  - **投资移居**：过去港澳居民投资移民门槛为 **600万新台币**（约合18-20万美元），且需实际开设商店并聘用台籍员工，维持至少3年 [移民署]。
  - **专业/就业金卡**：月薪需达到 **16万新台币**（约5000美元）以上，或在特定领域有杰出成就。

### 2. 文化资本（Cultural Capital）：学术资本与信息差

跨国流动需要极高的政策解读能力与语言资本。中产家庭试图通过留学就业路径移民，意味着家庭必须具备无偿供养子女在海外接受4–6年高额学费与生活费的财力，这本质上是家庭将国内累积的经济资本转化为子女国际化文化资本的过程。

### 3. 社会资本（Social Capital）：跨境信用与商业网络

海外本地的行政书士、协助办理合规税务法务的专业律师团队、真实的商业上下游订单，以及信用担保人（如日本经营管理签证早期需要联合发起人或日本本地居民作为信用担保），构成了跨国落地的润滑剂。低资本家庭在此项资源上几乎为零。

##  三、 “长期打工”与“身份移民”的本质分流：工具人陷阱

在研究中，必须将“长期海外打工（劳工阶层）”与“身份移民”进行严格的政策与学术分流。部分底层家庭试图通过肉体出海（如赴新、赴日、赴台打工）实现改变命运的目的，但各目的地的底层治理逻辑存在巨大差异：

![](https://hoochanlon.github.io/picx-images-hosting/imgs/uploads/2026/20260707202437-1.png)

**学术结论**：国际移民组织（IOM）等机构发布的报告 [ADBI] 证明，长期在外打工对于底层家庭而言，本质上是一种**高强度的家庭财务防御机制**（通过跨国汇款改善母国的居住、防老、防病条件），但它**无法直接转化为目的国的国籍与阶层跃迁**。

## 四、 零容错率：三至四代人极限托举的解构

对于一个没有任何先赋性背景的底层家庭，要抹平上述动辄百万、千万的资本门槛与政策壁垒，在学术模型中需要经历一个**长达50–70年、跨越三至四代人的完美接力链条**：

1. **第一代（肉体筑基期）**：在国内从事高强度体力劳动，或在海外做最脏最累的蓝领（如新加坡WP、日本研修生）。他们6人挤在廉租房里，省吃俭用将90%薪水汇回国内。其历史使命是**消灭家庭负债**，拿血汗换取微薄积蓄，确保第二代能接受完整教育。
2. **第二代（资产放大与阶层跃升期）**：成为城市高级白领、体制内基层或小工商業者。他们承受着巨大的职场压力和内卷，通过买房、理财或创业将资产放大到百万乃至千万级别，完成国际化流动的认知觉醒，并将资产“梭哈”（全额投入）到下一代的教育中。
3. **第三代（身份冲刺期）**：作为国际留学生、跨国精英或高净值投资移民者出海。独自在异国他乡面对文化隔阂、语言障碍、职场隐性歧视以及身份焦虑的心理双重折磨，利用前人准备好的资金或高端学历（如冲刺月薪1万+新币的EP签证），开始漫长的永居排队。
4. **第四代（阶层落地期）**：出生即获得发达国家身份，彻底脱离原有的阶层重力与内卷环境。

### 零容错（Zero-Tolerance）的致命踩空点：

由于低资本家庭的**影子资本（Shadow Capital）**为零，导致其**容错资本（Tolerance Capital）**极低。在这场长跑中，**不能出现任何一次决策或环境失误**：

- **第一代踩空**：一次严重的工伤或大病，全家瞬间失去收入并背负巨额医疗债务，代际积累在起跑线中断。
- **第二代踩空**：若高位接盘房地产、踩中P2P或理财骗局导致资产归零；或者中年遭遇行业周期性裁员，在上有老下有小的年纪房贷断供、断缴社保，不仅无法托举下一代，自身还会滑落回底层。
- **第三代踩空**：精神防线因巨大期盼而崩溃（如重度抑郁导致无法毕业或失业）；或者撞上目的国政策突然改制（如台湾近年极度收紧对大陆背景人士的联审，新加坡COMPASS积分年年水涨船高），差一两分就被迫打包回国，导致前两代人的“梭哈式投入”彻底成为沉没成本。

## 五、 超高净值阶层的跨境套利与审查机制的“分层异化”

与中下阶层在窗口与基层签证官“硬碰硬”的惨烈现状截然不同，以王思聪、房祖名等顶流巨贾、富豪二代为代表的超高净值阶层（UHNW），其跨境流动进入了完全不同的“隐秘剧场”。

### 1. 窗口签证官的“工具化”与幕后“影子审批”

普通人申请签证，生死掌握在窗口签证官手里。但对于超级富豪，窗口签证官没有任何实质裁量权。

- 富豪的案子属于“特批案（Special Cases）”。在材料正式递交前，其背后由顶级大律师事务所与私人银行组成的重装智囊团，早已在幕后与目的国的移民局高级官员、甚至国会议员进行了长达数月的非正式沟通与利益对接。
- 窗口签证官的作用仅仅是核对本人身份与原件，随后将卷宗上报。

### 2. 资金来源（AML）的重装洗白与经济特权

普通移民需提供完税证明与银行流水。巨贾移民则需面对最高级别的**财务法证审计（Forensic Accounting）**，交代数亿资产的最原始源头。

- 巨贾的律师团队会利用复杂的家族信托、离岸外壳公司（开曼、维京群岛）架构，撰写出数千页完美契合反洗钱（AML）合规要求的报告。
- 各国移民法普遍赋予高级官员**“自由裁量权（Discretionary Power）”**。当巨贾能为新加坡带来50个高薪岗位、几亿直接税收，或为日本引入顶级跨国商业资源时，目的国经济部门（如新加坡EDB、日本经济产业省）会主动发函背书，豁免其语言不达标、居住时间不够等常规法规底线。

### 3. 关键政治背景人物（PEP）的“国安联审”与地缘红线

富豪本人或其父辈往往具有鲜明的体制内政治标签（如人大代表、政协委员、或深度参与国家重大战略建设）。在西方及发达经济体眼中，这类背景被自动归类为**PEP（政治关联人物）**，进而触发最高级别的**国家安全筛查（National Security Screening）**。

- 审查的核心不再是经济能力，而是“财富是否涉及国际制裁”、“是否带有特定政治意图”以及“是否与原籍国强力机构存在隐秘联系”。
- **台湾的极端案例**：修正后的《港澳居民进入台湾地区及居留定居许可办法》明确规定，凡出生于大陆、或曾任职于大陆党政军、体制内企事业单位者，定居申请在“国安联审”阶段几乎会被一票否决 [移民署]。即使是具备深厚港台人脉的顶级巨贾，一旦踩中这条政治红线，常规身份通道亦会被彻底封死。
- **富豪的应对机制**：巨贾家族通常不需要狭隘的“换国籍（移民）”，而是追求“全球流动性”。他们通常实行**“国籍分散制”**，让家族不同成员持有美、加、新、日或圣基茨等多国长期签证或护照，利用资本架构在幕后搞定政治审查，实现“风险留给原籍国，利益留给国际化家族”的跨境套利。

## 六、 人口学回应：底层“主动断代”与顶层“跨境永续”的社会学对称

当跨境流动与阶层攀升的通道在底层呈现出“零容错、高投入、低回报”的特征时，底层群体在社会心理上会产生深度的绝望感。基于中国综合社会调查（CGSS）等数据模型证明，代际流动成本的极端化、家庭与学校及机构场域的“三重再生产”失败，会直接催生中下阶层的生育抑郁 [CGSS]。

底层和底层中产清醒地认识到，在缺乏“影子资本（Shadow Capital）”护航的向下的社会中，繁衍只会让孩子重复自身的结构性苦难，沦为时代变迁的代价。因此，**“底层到二代选择主动不婚不育”，并非消极的逃避，而是面对零容错率社会规则时，个体与家庭所能做出的最理性的结构性抗争与制度性退出。**

这种**底层的主动消亡**与**顶层通过资本特权实现的跨境永续**，共同构成了向下社会最为冷酷的社会学景观。

## 七、 结论

现代跨国阶层跃升早已不是依靠一腔热血、空手到异国洗碗就能扎根的温情故事。它是一套高度精准、分层治理的残酷制度矩阵。能够在新加坡、日本或台湾成功落地并改变家族命运的普通人，是几代人极限血汗、精打细算与完美避开所有时代陷阱的“幸存者”；而食物链顶端的巨贾二代，则是在用跨国大律所、私人银行作为重装武器，与目的国政府进行更高层面的政治与利益交换。

对于缺乏容错资本的普通家庭而言，在看清全球跨境流动的冷酷双轨制后，如何保护好自身的健康、现金流等底线资源，避免在政策与资本的双重绞杀中沦为时代的消耗品，是比盲目追求跨境跃迁更为迫切与务实的生命课题。

## 论文权威参考文献与引用的具体数据链接 (References)

1. **新加坡人力部 (MOM) 官方政策**：[Ministry of Manpower Singapore](https://www.mom.gov.sg/) —— 验证自雇EP最低薪资门槛 5,600 新币/月及 COMPASS 互补专才积分架构数据。
2. **新加坡经济发展局 (EDB) 官方政策**：[Economic Development Board Singapore](https://www.edb.gov.sg/) —— 验证全球商业投资者计划 (GIP) 方案A之 1,000 万新币投资硬性指标。
3. **日本出入国在留管理厅 (ISA) 官方指南**：[Immigration Services Agency of Japan](https://www.isa.go.jp/) —— 验证经营管理签证 500 万日圆资本金要求、续签持有成本及高级人才点数制。
4. **中华民国内政部移民署全球资讯网**：[National Immigration Agency Taiwan](https://www.immigration.gov.tw/) —— 验证港澳居民 600 万新台币投资移民法规、3年实体营运聘雇要求，以及近年国安联审针对大陆背景人士的收紧细则。
5. **跨国家庭资本代际传递学术研究**：*Mobility as Capital: A ‘Three‐Step’ Education Pathway of Chinese Transnational Migrant Families* —— [Wiley Online Library 论文页面](https://onlinelibrary.wiley.com/doi/full/10.1002/psp.2873)。论证了华人跨国家庭如何通过多代人将地理移动性转化为文化与社会资本。
6. **日本劳动力市场僵硬性与移工障碍研究**：*Economic achievement of immigrants in Japan: Examining the role of country‐of‐origin and host‐country‐specific human capital in an inflexible labor market* —— [Wiley Online Library 链接](https://onlinelibrary.wiley.com/doi/abs/10.1111/ijjs.12149) | [ResearchGate 讨论页](https://www.researchgate.net/publication/369271004_Economic_achievement_of_immigrants_in_Japan_Examining_the_role_of_country-of-origin_and_host-country-specific_human_capital_in_an_inflexible_labor_market)。论证了缺乏本土社会资本的底层移工极难在日本实现职业晋升。
7. **亚洲低技能劳工移民政策权威报告**：*LABOUR MIGRATION IN ASIA: WHAT DOES THE FUTURE HOLD?* —— 亚洲开发银行研究院 (ADBI) 劳工移民年度报告主页。论证了新加坡 WP 等准证系统在机制上封锁低技能劳工转PR的“工具人”本质。
8. **阶层流动与生育意愿研究框架**：基于 *Social class, intergenerational mobility, and desired number of children* 等基于 **CGSS（中国综合社会调查）** 数据的延伸研究，论证了代际收入弹性（IGE）过高、容错资本匮乏对底层主动选择断代的人口学影响。


# DNS、Hosts

## DNSCrypt

> **【说明】** 目前，多数SS分享站点或是VPN官网均以污染为主，因此可用它来打开绝大部分此类相关网址，并以此下载VPN或是配置代理从而连接互联网；但需注意遇到如谷歌等这类封IP的网站是打不开的。 
多说一句，仅针对一些相对来说大众不很明白或是易混淆的相关概念进行此类提示，若还需较为深入地了解相关的原理细节等，还请自行翻看科普与补充的相关章节（ps：论坛现已封ip，2019）

开启DNSCrypt服务与网卡选项√

<!-- ![](https://ipfs.io/ipfs/Qme3m7pu4qM2RqT7LqtRM6umPZuKhEMBJkCFGr3tAg66Y3?3.png) -->

![](https://i.postimg.cc/ZY289WC0/2018-04-29-031314.png)

启用自动模式

<!-- ![](http://p0.cdn.img9.top/ipfs/Qmd449GEzw6KUvpmcfDxv3e9rYRxYk3dHNuo5ZitD7zEqm?0.png) -->

![](https://i.postimg.cc/VkYFqdcw/2018-04-29-031427.png)

高级设置-&gt;应用设置

<!-- ![](http://p1.cdn.img9.top/ipfs/QmNZ1JEN51T7v5cP8aEVJfYQvBXLcCscAtgXtWf6nhESKL?1.png) -->

![](https://i.postimg.cc/fR2YYCK7/2018-04-29-031418.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmSr8t86BHkoDyofqEMYucg9uAyxCGVjuqzVPE6yGmqf3r?4.png) -->

![](https://i.postimg.cc/qRfhG5CK/2018-04-29-1.png)

> **【说明】** 不过需要注意的是：DNSCrypt 时常将计算机 dns 设置成 `127.0.0.1` 以本地DNS解析服务器作为缓存，从而加快解析效率；关机或关闭 DNSCrypt 时，注意检查计算机 DNS 配置，改成自动获取或原自己配置的 DNS 地址。


## DNS

> **【提示】** 若是对修改DNS只能防劫持但还可以防污染甚至解封IP感到困惑，[请点此查看相关内容](#dns污染)

进入[baidns.cn](https://baidns.cn/)，记住此DNS地址

<!-- ![](https://ipfs.io/ipfs/QmXL5GM1HPZcvsGx8eDKhnNWWJjVNKQ6PQzzdsqYf94FuM?3.png) -->

![](https://i.postimg.cc/vZKD4bnf/2018-05-10-181032.png)

打开`控制面板\网络和internet\网络和共享中心`并点击`WLAN`，接着选择`属性`并进入`internet协议版本4 (TCP/IPv4)`

<!-- ![](https://ipfs.io/ipfs/QmfZFMj1hg7fo1uop8uLoEX9fcMYY4wMNJ1C5aBMNy2GkX?2.png) -->

![](https://i.postimg.cc/v8rYnjm9/2018-05-10-053020.png)

选择`使用下面的DNS服务器地址`并填入相应的DNS地址

<!-- ![](https://ipfs.io/ipfs/QmZFzd8GsXzmLwAfth8X9WFEPk9z83oSHQm3NPbNHhB1iQ?4.png) -->

![](https://i.postimg.cc/DyfTXwHk/2018-05-10-053911.png)

[点击测试](https://my.ishadowx.net/),你可能会对修改DNS只能防劫持但还可以防污染甚至解封IP的感到不解，[请进入传送门](#dns污染)

<!-- ![](https://ipfs.io/ipfs/QmTK8mV8q2sZbUeQXMFj5MCCmASyY1ZyGFy2oAYeQB3k49?0.png) -->

![](https://i.postimg.cc/fR31ctvF/2018-05-23.png)


## hosts

> **【重要】** 早期，GFW屏蔽的网址不是很多且手段也仅限于污染，修改hosts也仅对当前配置所受污染的站点有效。推荐使用 [Ip Switch](https://github.com/hoochanlon/Ip-Switch) 修改 hosts 更为方便。
>
> 有关 ip 地址的计算推荐使用 [network-calculator](https://github.com/hoochanlon/network-calculator)

利用 https://www.ipaddress.com 查询维基百科相关ip，并找到`C:\Windows\System32\drivers\etc\host`，打开它

<!-- ![](http://p3.cdn.img9.top/ipfs/QmeUhmaHpUSiQP9hgA4Y5gEsoufqF5u3o9zVrGftWJQx4T?3.png) -->

![](https://i.postimg.cc/SQdRXsVC/2018-04-30-090747.png)

添加维基的ip地址，`#`是注释

<!-- ![](https://ipfs.io/ipfs/QmfBgmHvkYXor6gJtvpz93psQAvTm4zsFB2qMK2NtNszYR?2.png) -->

![](https://i.postimg.cc/prcPsm1S/2018-04-30-091155.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmT5DKfhyTteW4NWPQfb657YEz2jeuoESmmpZgLXJ3Dkd3?4.png) -->

![](https://i.postimg.cc/sg7RhHyq/2018-04-30-092057.png)


# 浏览应用

## chrome

?> [此chrome扩展下载站点](https://chrome-extension-downloader.com/)需要输入扩展应用的ID，这里以下载[privatix](https://privatix.com/)插件进行演示；额外力荐：[skyzip-proxy](https://chrome.google.com/webstore/detail/skyzip-proxy/hbgknjagaclofapkgkeapamhmglnbphi?utm_source=chrome-ntp-icon)

要想使用扩展插件，首先得去镜像站点[下载chrome](https://repo.fdzh.org/chrome/exe/?C=M&O=D)

![](https://i.postimg.cc/yd0JnRxm/2018-05-31-181314.png)

`https://chrome.google.com/webstore/detail/扩展应用名称`后面即是它的chromeID，打开网址将ID复制

<!-- ![](https://ipfs.io/ipfs/QmXxyd7LKPB7GFD82DGFhHeHo3WAptztEYeHtmnuXzGZud?2.png) -->

![](https://i.postimg.cc/8cP1Wf6P/2018-05-01-153439.png)

接着进入[chrome- extension-downloader](https://chrome-extension-downloader.com/)页面，粘贴ID并点击下载按钮

<!-- ![](https://ipfs.io/ipfs/QmZucqRU4mUnRczUnC7avan6LFiXAsiKzzmDBDoLX6XxeT?3.png) -->

![](https://i.postimg.cc/Vkbzj8dM/2018-05-01-153929.png)

将下载好的`.crx`扩展文件拖动至chrome的扩展程序页面中，便可完成安装

<!-- ![](https://ipfs.io/ipfs/QmXdxTD6RBijvGmfSQK8SenmSqi5bvCWcT2aAdY7ACzped?0.png) -->

![](https://i.postimg.cc/sgSRM4N4/2018-05-01-154821.png)
除此之外，还可使用[Google访问助手](http://www.ggfwzs.com/)并按相关说明进行设置

<!-- ![](https://ipfs.io/ipfs/QmYXeM1YztaipcumewNYqQmNGSjPj6E4uspjGvSwfxYuaE?2.png) -->

![](https://i.postimg.cc/brd7pxnb/2018-04-28-214301.png)
虽然助手只能用于访问Google服务，但有了商店可以下载各式各样的代理插件 

<!-- ![](https://ipfs.io/ipfs/Qmd3XDfNV6QswghKe7nmrP2by3cxzgT1TEMdVTuTunWyfb?4.png) -->

![](https://i.postimg.cc/mg70L2Pd/2018-04-28-220028.png)


## opera

!> 再次提醒，为了有效合理的使用VPN或代理服务，请在系统`国家/地区`选项中改成香港地区；因为一些代理与VPN提供商会采用规避风险的策略，所以最好将地区改为特别行政区；台湾的话，时区和北京并不一致，因此并不建议更改此地区，也没有必要换回内地。
软件功能可能会在较长期间失效，不过此示例用压缩包安装Chrome扩展插件的方法，很好解决了 crx_header_invalid 的问题。
也可以在[173app](https://173app.com/)等插件网或是GitHub，搜寻`skyzip`、[SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega)等相关代理，在Chrome中做此以加载解压缩形式安装插件操作。

更改`国家或地区`换成香港或澳门特别行政区

<!-- ![](http://ipfs.io/ipfs/QmaoGnn2RwRpH5HdDWHBtzJE2kzK3bygkMExAEo2PTgmQR?3.png) -->

![](https://i.postimg.cc/25Gj5x1X/2018-04-28-204541.png)

下载安装opera并打开设置选项中的`隐私和安全`找到`VPN`选项开启便可

<!-- ![](http://ipfs.io/ipfs/QmbPmiD1oWdoKGMt8voGxdy7mxwQcGQngceetoeJ8goZwD?3.png) -->

![](https://i.postimg.cc/Y9j7CBKh/2018-04-28-205527.png)

测试

<!-- ![](http://ipfs.io/ipfs/QmPnbqrUEBboNmUJ3aZYHFbK3cWfGcefz2CxyK2Zj7Ydsx?0.png) -->

![](https://i.postimg.cc/ZK6WSpxX/2018-04-28-210138.png)

打开扩展应用商店，搜索`chrome`关键字，找到[extension-source-viewer](https://addons.opera.com/zh-cn/extensions/details/extension-source-viewer/)，点击进入安装它

<!-- ![](https://ipfs.io/ipfs/QmS1hLEzPNXhcii2dSuX6TkFKE77Stib2y75LWEymxkTTX?2.png) -->

![](https://i.postimg.cc/hjHGFtzS/2018-05-01-160149.png)

下载zip压缩包

<!-- ![](https://ipfs.io/ipfs/QmazGqGpH2Aqt9XedswyX7ZpbdnmZiFjaDkx9dLtHXbBMy?0.png) -->

![](https://i.postimg.cc/KvhYJ4hf/2018-05-01-160509.png)

将opera扩展下载的chrome扩展压缩包，进行解压生成文件夹

<!-- ![](https://ipfs.io/ipfs/QmT7Vn1JUHsgRvzm5AfX7akDBvEB7VcnW1uTfR9QtZQLbc?3.png) -->

![](https://i.postimg.cc/d03QLyGs/2018-05-01-164056.png)

在chrome中的扩展程序中，开启开发者模式，点击加载已解压的扩展程序，找到已解压的扩展程序文件夹，点击确定

<!-- ![](https://ipfs.io/ipfs/QmW44rZLfD9wdmwpUkSmQhhYrGMh3SXvr7xSexyUyXQF9x?1.png) -->

![](https://i.postimg.cc/Zn7VYXmK/2018-05-01-164619.png)


## tor（firefox）

!> tor、i2p都是属于匿名浏览访问[暗网](#abc/darkweb)性质的软件，多数情况结合duckduckgo一起使用

azure已由政府背景的企业所代理，但还是可用的，只是不太建议选择

<!-- ![](https://ipfs.io/ipfs/QmWV4nmWRJL1Yi7jrFdt35tE91fYPTbZ6XMxgV1nqtp1ZU?2.png) -->

![](https://i.postimg.cc/v89G8GPp/2018-04-29-022846.png)

满足你的好奇心这里给出一个暗网地址:point_right:[hdwiki](https://thehiddenwiki.org/)

<!-- ![](http://ipfs.io/ipfs/QmPa9g6SnpvXdDHcy5bYWB3jdkvtiCYe4oU44bznHaKrRX?3.png) -->

![](https://i.postimg.cc/xjGBF8pT/2018-04-29-023357.png)


## puffin

!> 其本质上还是代理浏览器，目前不能安装扩展插件，对简中支持并不是很好；不过，比起tor、i2p这类多层匿名访问的浏览器，网速自然要好很多；像是这类型的浏览器，市场的需求引导下，以后可能还会出现比如说：[yandex browser](https://browser.yandex.com/)；不过，失效的可能性也是随时发生的，所以说，注意观察相关时事新闻动态吧，软件始终是说不完的，掌握方法就行！ヾ(o◕∀◕)ﾉヾ

[下载安装puffin](https://www.puffinbrowser.com/)

![](https://i.postimg.cc/13pwJbdn/2018-06-08-121528.png)

在初始化配置时，需要连接VPN

![](https://i.postimg.cc/B6wKj3jy/2018-06-08-123200.png)

查看服务器与本地IP信息

![](https://i.postimg.cc/d0skn3dp/2018-06-08-123524.png)

断开VPN连接，再重启`启用云服务器`即可

![](https://i.postimg.cc/kDPDSgqj/2018-06-08-123758.png)

测试

![](https://i.postimg.cc/3xBFFdW0/2018-06-08-124837.png)


## zeronet

?> 对zeronet的简单介绍及运作方式概要的说明，[请看这里（见「对零网的简要补充说明」）](#)

下载接着解压缩并打开[Zeronet](https://zeronet.io/)

<!-- ![](https://ipfs.io/ipfs/QmfQdYYVi7h4h3LqVWXFZNkxffHBmjKUGmJbEjr4vJETha?3.png) -->

![](https://i.postimg.cc/ZntPk6H7/2018-05-20-213528.png)

打开ZeroMe

<!-- ![](https://ipfs.io/ipfs/QmavvBF5yT6ANDNETqXPsY3PGWhS96v42ZMvz9Zro1Exaq?3.png) -->

![](https://i.postimg.cc/ZR33LCmr/2018-05-20-225824.png)

允许授权

<!-- ![](https://ipfs.io/ipfs/QmeanoM1b4r94RYPj2UD8T7qJ98Gw1guqFPMpxNQA7zuVz?1.png) -->

![](https://i.postimg.cc/CLvZkj83/2018-05-20-230112.png)

注册新的用户

<!-- ![](https://ipfs.io/ipfs/QmYRJSVT3PpfEqN1KZJ8WsU2DLkAczDu4FdWVuiQreksng?2.png) -->

![](https://i.postimg.cc/xdLTxHkT/2018-05-20-230310.png)

选择获得认证证书

<!-- ![](https://ipfs.io/ipfs/QmaKYaN4GqYGxoU75k33Zv6fHdvXaYG6fMDQ9fh3iy8WZX?0.png) -->

![](https://i.postimg.cc/wv0zZk9H/2018-05-20-233227.png)

创建成功

<!-- ![](https://ipfs.io/ipfs/QmP6oMX3FimFeSvx8oJjYgA7uDtfzCAvF65r1j8fm7AjWE?4.png) -->

![](https://i.postimg.cc/6pnXtKBM/2018-05-20-233251.png)

点击`在用户数据库中搜索`可查看已注册用户并拉入黑名单

<!-- ![](https://ipfs.io/ipfs/QmchciRgEmuS48cPw9TxLH4yq25hy39FbD3ciXvckKbgG3?3.png) -->

![](https://i.postimg.cc/HkGqSNbX/2018-05-20-233508.png)

点击右上角的`0`图标可回到控制台首页，在设置中也可管理屏蔽用户

<!-- ![](https://ipfs.io/ipfs/QmP9FKwvRaVmFs9cEEKYGrvAF4kk5zAst79XybrWVD34ZD?4.png) -->

![](https://i.postimg.cc/FHVh0vw7/2018-05-20-233759.png)

再次进入ZeroMe选择已注册好的账户并下载相关组件，完成之后加入便可

<!-- ![](https://ipfs.io/ipfs/Qmc5CHNk6TebUoyByJvobge1EPTaF53WuLXimNb3TpvG7v?0.png) -->

![](https://i.postimg.cc/DyVhDmTS/2018-05-20-234758.png)

用[零度搜索](https://www.zerogate.tk/lingdu.bit)查找相关感兴趣的论坛可参加讨论

<!-- ![](https://ipfs.io/ipfs/QmVr3A3oWBWxPwbUsiD5gj5JBHxcLYzNaMC6oAYL2YC7Pg?2.png) -->

![](https://i.postimg.cc/FKwCRdGc/2018-05-21-000234.png)

进入[零度导航](https://www.zerogate.tk/0123.bit)可找到，一些你想要的东西

<!-- ![](https://ipfs.io/ipfs/QmZPQQPXincSMcDdovrZbjUuxieqsvQyDsuzcXvVBrFi2z?4.png) -->

![](https://i.postimg.cc/XqksQ2Wc/2018-05-21-001320.png)

另外一些细节方面，右上角`0`图标左拖动可拉取更新还可查看设置相关信息

<!-- ![](https://ipfs.io/ipfs/QmTeLqpubB6F9TNyQJ85XaXXsRKK89t7pDUtA9Fn7Jtq67?4.png) -->

![](https://i.postimg.cc/K8HJqk6V/2018-05-21-003643.png)

若将Zeronet整个文件删除，重新载入则失去对当前账户的所有权且无法找回

<!-- ![](https://ipfs.io/ipfs/QmTCjXEepwdu4wUVW1nw66Hve2iURe939TPaBnF4Vsrs1D?4.png) -->

![](https://i.postimg.cc/50M5TwnP/2018-05-21-005027.png)

因此需备份`users.json`文件

<!-- ![](https://ipfs.io/ipfs/QmcFGnNonp269m2Hc6NAAJfE9mhWqFxNfGy7pomcsdhxZu?2.png) -->

![](https://i.postimg.cc/VvZCfMWP/2018-05-21-005403.png)

将Zeronet整个文件删除且重新载入以后，打开`ZeroNet.exe`让其生成`data`文件夹

<!-- ![](https://ipfs.io/ipfs/QmSo7gVZvDC76Ty8D2w7W4hVCD9KHCbk7gzP9EBHVuY6GT?0.png) -->

![](https://i.postimg.cc/QVLjJdXW/2018-05-21-010901.png)

复制已备份好的`users.json`文件放置在`data`文件夹中

<!-- ![](![](https://ipfs.io/ipfs/QmX9q2EzXcUo1g6x8HJv9qqFi3UJvjoQMVmJrXyh6t8j6p?2.png)) -->

![](https://i.postimg.cc/TPkLqgBL/2018-05-21-011154.png)

重启ZeroNet并打开ZeroMe，下载完数据库点击授权

<!-- ![](https://ipfs.io/ipfs/QmdvwoK2cMM8F6UaVGTrq31bS3pZMZ79jUzCoeZnXNnvVb?1.png) -->

![](https://i.postimg.cc/CLjRrWWV/2018-05-21-011848.png)

再重启ZeroNet打开ZeroMe即可

<!-- ![](https://ipfs.io/ipfs/QmUx6vCMPwhcei5D5HomostAgqBgzGXMftUhNcfrrm7rth?2.png) -->

![](https://i.postimg.cc/SNryMqBj/2018-05-21-012112.png)

若是遇到一些site Blocked或是disable proxy请将`www.zerogate.tk`换成`127.0.0.1:43110`即可

<!-- ![](https://ipfs.io/ipfs/QmV9SdqrZCNdWCpCZLBV4MqUkHg36KWN8UJUnChBNi5YLs?1.png) -->

![](https://i.postimg.cc/RZYx70XC/2018-05-20-221304.png)

<!-- 
打开[零度搜索](https://www.zerogate.tk/lingdu.bit)，并查找相关站点

![](https://raw.githubusercontent.com/hoodiearon/fq-book/master/docs/images/2018-05-20_220806.png)

将`https://www.zerogate.tk`替换成`http://127.0.0.1`

![](https://raw.githubusercontent.com/hoodiearon/fq-book/master/docs/images/2018-05-20_221304.png)

打开站点并设置大小限制到100MB

![](https://raw.githubusercontent.com/hoodiearon/fq-book/master/docs/images/2018-05-20_222037.png)

进入站点

![](https://raw.githubusercontent.com/hoodiearon/fq-book/master/docs/images/2018-05-20_222425.png)

复制特征码

![](https://raw.githubusercontent.com/hoodiearon/fq-book/master/docs/images/2018-05-20_223125.png)

在特征码前加入 `magnet:?xt=urn:btih:`指令复制到迅雷下载即可

![](https://raw.githubusercontent.com/hoodiearon/fq-book/master/docs/images/2018-05-20_224907.png) -->

<!-- ### 磁力链结构

magnet ：协议名。

xt ：exact topic的缩写，表示资源定位点。

BTIH：BitTorrent Info Hash表示哈希方法名

dn ：display name的缩写，表示向用户显示的文件名是选填的。

tr ：tracker的缩写，表示tracker服务器的地址也是选填的。

### 文件校验MD5、SHA1值

每个文件都可以用某种算法得到一个验证码，而文件的MD5和SHA1值就是使用相应的特殊的算法对文件数据进行计算而得到的一串字符。因为这种算法反向推算几乎无法实现，所以我们便可以认为一个文件对应着一个特定的MD5、SHA1值。

于是，我们下载文件的时候可以在下载完成之后算出文件的MD5、SHA1值与文件提供者提供的MD5、SHA1值进行比较，如果计算出来的和提供者注明的不匹配，那么你下载的这个文件就是不完整，或是被别人动过手脚的。 -->


# VPN软件

## Betternet

!> 再次说明：
简单来说VPN与代理的最大区别就在于代理不会虚拟一块独立的网卡
多数的免费VPN与代理有着严格的[NAT类型](#)，以限制游戏与下载等相关操作

点击 `connect` 等一会 PC 即可连接上互联网

<!-- ![](https://ipfs.io/ipfs/QmWFRGy8fQr35qK5RujpWdnHyQjMWvjESRxnQK84uQrhcw?3.png) -->

![](https://i.postimg.cc/x18kPk9D/2018-04-29-022009.png)

打开`移动热点`，创建成功后，并右键选择`设置`

<!-- ![](https://ipfs.io/ipfs/QmfPtCEk3dqjjXeXHW67paE6TuRRm8t144VpweAJzU5Ux5?3.png) -->

![](https://i.postimg.cc/hPbw0jpr/2018-05-08-213716.png)

可设定WiFi热点名称与密码，若系统是win7，[就请看这里](#append/win7-wifi)

<!-- ![](https://ipfs.io/ipfs/Qmb5xZZWGN73dWHXHHfTPTxSPmqZQEsPRkaGwhGgHYG1SS?1.png) -->

![](https://i.postimg.cc/L6RQhS2Z/2018-05-08-214959.png)

`控制面板`->`网络共享中心`->`更改适配器设置`找到VPN软件开启的网卡，右键`属性`

<!-- ![](https://ipfs.io/ipfs/QmRPSE29AQPX37pcKyH6HkWcg18pqAymp66J68ziFTnEie?4.png) -->

![](https://i.postimg.cc/q7tjWMXW/2018-05-08-221121.png)

在`共享`选择`允许其他网络用户通过此计算机的Internet连接来连接`，并在`家庭网络连接`选择热点网卡

<!-- ![](https://ipfs.io/ipfs/QmaWy3yjxn1a88qVjKrinU2wYEyYLpjGausVvG1UdoNSqu?0.png) -->

![](https://i.postimg.cc/B6TcG887/2018-05-08-221920.png)

打开手机`WiFi`设置

<!-- ![](https://ipfs.io/ipfs/QmdUMKKiFa1Fj7wottZXy8zY7wq7m78TudGDGkDinAX1SZ?2.png) -->

![](https://i.postimg.cc/dVg8kRrS/QQ20180508224410.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmfCDDEGWhFb2nD7LrLu2gmVWdhVzBgDc59qDnmGMfaYJE?1.png) -->

![](https://i.postimg.cc/nrV7b3fM/QQ20180508224420.png)


## 典型VPN概览

> 使用 [WireGuard](https://zh.wikipedia.org/zh-cn/WireGuard) 协议的高性能且安全的VPN客户端。TunSafe使在Windows和Linux之间设置极其快速且安全的VPN隧道非常简单。 [摘自官网介绍](https://tunsafe.com)。有兴趣的话，可了解下[虚拟网卡 TUN/TAP 驱动程序设计原理 - IBM dev](https://www.ibm.com/developerworks/cn/linux/l-tuntap/index.html)、[TUN与TAP wiki](https://zh.wikipedia.org/zh-hans/TUN%E4%B8%8ETAP)

进入[tunsafe官网](https://tunsafe.com/)，可以看到此外它还提供独立的虚拟网卡和软件（集合安装器需要全局翻墙环境），然后下载并安装这两个文件。

![](https://i.postimg.cc/1XRCdppx/20190607083401.png)

安装很简单，默认就行；注意勾选下始终信任项目就好了。

![](https://i.postimg.cc/Z5LLG954/20190607083553.png)

在 `user guide` 选择 `using tunsafe windows`接着再选择`free vpn servers`

![](https://i.postimg.cc/7LKsW3r8/20190606205200.png)

点击 `create new account`，选择服务器，然后生成下载该配置文件，**建议下载多个配置文件测试连接效果**。

![](https://i.postimg.cc/63NrzTyJ/20190606205536.png)

也可以在 [mullvad](https://www.mullvad.net) 中选择`取得账户`-> `验证` -> `WireGuard configuration generator`

![](https://i.postimg.cc/C1b528w4/20190607084331.png)

选择服务器并下载

![](https://i.postimg.cc/CxnYmCWV/20190607084522.png)

打开软件在`File`项中选择`browse in explorer` 就会打开软件配置目录源

![](https://i.postimg.cc/hv8Qj0rf/Snipaste-2019-06-06-21-11-36.png)

将下载好的conf导入到该目录

![](https://i.postimg.cc/SRYVwsqj/20190607092202.png)

如果连接不上，那换一个服务器连接测试，即可

!> 也有可能存在恶意禁用的问题，详情请看：[简谈国产杀软 - 恶意禁用连接互联网服务问题](append/guochan-sharuan?id=恶意禁用连接互联网服务问题)

![](https://i.postimg.cc/T3RbDfrP/Snipaste-2019-06-07-08-54-24.png)

## GateVPN

!>重点且易被封杀的对象，需要选择合适的协议与连接方式并时常更新列表与软件，否则连接成功率极低，对协议间的了解与如何选择，[相关细节，请点击这里](#)

> 原列表出处：[泡泡](https://pao-pao.net/article/82)，以及如何设置相关服务器连接方式，[GateVPN官网列表](http://www.vpngate.net/cn/)已有说明

| gateVPN服务器连接方式 | 软件设置 | 平台适用 | 服务器支持 | 翻墙体验 |
| :-: | :-: | :-: | :-: | :-: |
| SSL-VPN | 一般 | 只windows平台 | 全部支持 | 最好 |
| L2TP/Ipsec-VPN | 简单 | win,mac,ios,android | 很少 | 较差 |
| openvpn | 复杂 | win,mac,ios,android | 极好 | 一般 |
| MS-SSTP | 最易 | 只windows平台 | 较好 | 最差 |

<!-- ![](https://ipfs.io/ipfs/QmQc1YoVQvszg1rNZscxwWJ7ZmBMmDZyvALyw3T5iYsRa4?4.gif) -->

![](https://i.postimg.cc/RZFb7zhp/Snipaste-2019-06-06-04-03-52.png)

## OpenVPN

!> 目前，已被GFW特征识别成为重点封杀的对象，连接成功率低，一些SSH站点也提供OpenVPN配置文件下载，因为极大多数国家并没有像中国封锁网络那么严格

进入[freeopenvpn.org](https://www.freeopenvpn.org/)，点击home查看服务器列表，`get access`、`download`皆可进入下载页面

<!-- ![](https://ipfs.io/ipfs/QmbkkgwTLEQGRWNEqWAvhnLkaNB5dVWNmZiLV1HYonVkwQ?1.png) -->

![](https://i.postimg.cc/fRkYHqMb/2018-04-29-012851.png)

导入文件后，运行 openVPN 连接互联网


## wireguard

进入[wireguard](https://www.wireguard.com/install/)，下载

![](https://i.postimg.cc/d0Ny2kxH/Snipaste-2019-10-04-10-49-28.png)

打开wireguard选择 `add empty tunnel`并复制`public key` 公钥键值

![](https://i.postimg.cc/FR2w1Vkf/00-05.png)

进入[cryptostorm.is/wireguard](https://cryptostorm.is/wireguard)，将公钥复制到`your wireguard public key`选项，`add key`继续，并生成的配置文件

![](https://i.postimg.cc/MHB0Ky1p/27-48.png)

将配置文件复制到`public key`下方配置信息框内，并删除如下不必要的字段

```
[Interface]
PrivateKey = YOUR_PRIVATE_KEY
```

![](https://i.postimg.cc/BbRhmSBX/41-15.png)

点击`active`激活

![](https://i.postimg.cc/65gwLTRh/50-10.png)

测试

![](https://i.postimg.cc/zvz1SjPK/56-26.png)

> 参考自油管 [Siemens Tutorials](https://www.youtube.com/channel/UCmvvn2qsP77_7XUB0omMeCw/about?pbjreload=10) 关于wireguard翻墙视频


# 代理工具

## SS/SSR

!>  简单来说代理与VPN的最大区别就在于代理不会虚拟一块独立的网卡
  多数免费代理与VPN是严格[NAT类型](#abc/4nat.md)，以限制游戏与下载等操作
 ssr可以使用ss链接与二维码，反之是不行的，且ss只能连接兼容ss的服务器
 若想较为深入的了解ss链接的含义，[请参考ss、ssr、v2ray链接解析章节](#append/srvurl.md)
 ss与ssr都做了socks代理端口对http协议的兼容，所以并不需要额外的代理转发
 全局模式即被的代理软件所有网络均走代理路线，直连模式即正常访问不走任何代理

## SS

?> 在直接关机而没先将代理关闭的情况下，计算机再次启动时，设置在系统中代理配置还是生效的，这也就是用过代理软件后，却无法上网的原因

### 入门

访问[ss站点](https://free-ss.tk/)，右键扫描二维码

<!-- ![](https://ipfs.io/ipfs/QmWS9eJJi7dnMXjG7jxYAz7NDDCLHnrtSfc6viNRjbBjc9?2.png) -->

![](https://i.postimg.cc/C1v3LX5P/2018-04-30-105508.png)

 此时已经可以连接互联网了，如果你的系统不是自动设置的，请看<a href="#/proxy/ss-ssr?id=配置">配置</a>

右键允许来自局域网的连接

<!-- ![](https://ipfs.io/ipfs/QmbNUAL9vmXcnAkWP15XxevvLqpED2tbAxxnVCeGDs3o9X?1.png) -->

![](https://i.postimg.cc/J0fdsLLq/2018-05-05-032022.png)

`网络和共享中心`-&gt;`wlan`-&gt;`详细信息`查看本机网卡IP地址

<!-- ![](https://ipfs.io/ipfs/QmdwEi4zS8DNWx8gzkykPAoBkocQguEEP4QYhZFQV8Kwj9?4.png) -->

![](https://i.postimg.cc/Vvsxz4Ds/2018-05-05-032400.png)

`高级`设置`代理`选择`手动`，按照如下信息设置

<!-- ![](https://ipfs.io/ipfs/QmfU5EVwSUgyNtKFbetxfR1pvcyQTgbmM1y5Rp7QYkuX1b?1.png) -->

![](https://i.postimg.cc/mkCKNDVq/x1.png)

 一些朋友可能对连接互联网的网速要求较高，也可使用[speedtest](http://www.speedtest.net/)进行测试

<!-- ![](https://ipfs.io/ipfs/QmRfQ2LhCek5jw7UDBxwC2Y9Qm8VLjP17Ehhgh99Kw7Uod?3.png) -->

![](https://i.postimg.cc/zXw9yyyH/x2.png)

### 配置

有些系统如win7，连接服务器后还需在internet属性中手动设置本机地址与sock5代理端口

<!-- ![](https://ipfs.io/ipfs/QmQBdt4QM9GKcgfFdXh1LtKh45ubyrTqhjEgVHUBk9VfG4?4.png) -->

![](https://i.postimg.cc/k4tHqGr4/2018-04-28-224352.png)

PAC模式即脚本配置模式，收录的网址走代理路线，没有收录的地址则不走代理路线即正常访问。例如将Google加入代理访问列表，配置规则如下：

```text
 ".google.com",
"||google.com",
```

在`pac`选项中-&gt;`编辑本地pac文件`即可

<!-- ![](https://ipfs.io/ipfs/QmeHE8dTsEEQhvQRWBjwzKeioyprepRha6vFFYpce4i22o?1.png) -->

![](https://i.postimg.cc/xTP40BZK/2018-04-28-230423.png)

### SS分享

右键-&gt;`服务器`-&gt;`分享服务器配置`，如图

![](https://i.postimg.cc/bv46CPGj/2018-53px8.png)

随后可以看到相关ss链接与二维码生成

![](https://i.postimg.cc/90hL2Bt8/2018-06-09-174922.png)

可将二维码截图或是复制ss链接分享给他人，扫码或粘贴导入都行

![](https://i.postimg.cc/FFyPZ2N2/2018-06-09-181034.png)

## SSR

### 订阅功能

右键->`服务器订阅`->`SSR服务器订阅设置`
<!-- ![](https://ipfs.io/ipfs/QmX4z2VDbj5EDvzRzBHTiyqYsTvvxbgDi3pFwhiLfLLNFL?1.png) -->

![](https://i.postimg.cc/wvKV5kPq/2018-04-28-235146.png)

点击add添加按钮，并导入此条订阅：https://prom-php.herokuapp.com/cloudfra_ssr.txt
<!-- ![](https://ipfs.io/ipfs/QmNbaKnwt9E447xLzndAZvCHDByMbA6rZn4AsdDbeuFDuP?2.png) -->

![](https://i.postimg.cc/YChfJVB2/2018-06-09-215048.png)

<!-- ![](https://ipfs.io/ipfs/QmfXCT9yWSxPq4G7QuU9b1RzmFWZodAkY2Pzrt7iGHko5X?1.png) -->

再右键->`服务器订阅`->`更新ssr服务器订阅（不通过代理）`

![](https://i.postimg.cc/jSpNBShv/2018-04-28-235337.png)

订阅成功后会有如下提示
<!-- ![](https://ipfs.io/ipfs/QmdteWfXcW3NzJrB8gbxmF83eoybYfBoLThFEC6f8CwYCw?1.png) -->

![](https://i.postimg.cc/SQ1nwKS8/2018-04-28-235358.png)

再打开SSR可看到导入了多条账号信息

![](https://i.postimg.cc/TPcwQdNK/2018-06-09-220222.png)

订阅的好处：

* 一键导入多条服务器地址
* 不需要经常打开站点网址即可更新服务器配置（取决于订阅源）

### SSR分享

打开ssr选中ssr链接即可

![](https://i.postimg.cc/SNzx37tF/2018-06-09-190728.png)

<!-- !> ssr可以使用ss链接与二维码，反之是不行的，且ss只能连接兼容ss的服务器
 若想较为深入的了解ss链接的含义，[请参考ss、ssr、v2ray链接解析章节](#append/srvurl.md)
 ss与ssr都做了socks代理端口对http协议的兼容，所以并不需要额外的代理转发
 全局模式即被的代理软件所有网络均走代理路线，直连模式即正常访问不走任何代理 -->
<!-- ps:

* ssr可以使用ss链接与二维码，反之是不行的，且ss只能连接兼容ss的服务器
* ss与ssr都做了socks代理端口对http协议的兼容，所以并不需要额外的代理转发
* 全局模式即被的代理软件所有网络均走代理路线，直连模式即正常访问不走任何代理 -->


## v2ray

!> 若需了解为何使用额外的代理插件以及配置，浏览器才能访问互联网，还请[点击跳转链接](#abc/connection)

## CLI

在使用v2ray前，需要下载[SwitchyOmega插件](https://github.com/FelisCatus/SwitchyOmega)，打开ss分享站点，点击蓝色配置小齿轮，下载`config.json`

<!-- ![](https://ipfs.io/ipfs/QmcEBpCA4L194bXFpYaTLeDqJiypw9577KkuBT5hTLTwim?2.png) -->

![](https://i.postimg.cc/nr1ffr7m/2018-04-29-000906.png)

替换同名源文件

<!-- ![](https://ipfs.io/ipfs/QmPpDSm8oyz7b2oTGVMtYBv63pDeDzQkft5z2vpnSazSvy?4.png) -->

![](https://i.postimg.cc/tT5BXxS9/2018-04-29-001551.png)

打开v2ray.exe程序，即可

<!-- ![](https://ipfs.io/ipfs/QmYh2fcdZyadbTrdNoE7o4uQfUoupiqycJrvNzm6JDem93?4.png) -->

![](https://i.postimg.cc/9Q5Znfbb/2018-04-29-001900.png)

注意`congfig.json`里的端口、协议配置信息

<!-- ![](https://ipfs.io/ipfs/QmSpmZsk2LFMtN3ku7PiNp5Yv9EREtxiJQMuWSPqYbpaz8?3.png) -->

![](https://i.postimg.cc/MTM1LfCs/2018-04-29-002418.png)

SwitchyOmega在情景模式中添加如下设置

<!-- ![](https://ipfs.io/ipfs/Qmd1Gdt7v7PBrmj49mFjMFq2EyZ6H2EpytueRQESbBpCXC?0.png) -->

![](https://i.postimg.cc/ZqyRtPqy/2018-04-29-002210.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmW62TYFQHQqoaJgX65AEKqosrXEpJKgSBgt8kBZw4zGzn?1.png) -->

![](https://i.postimg.cc/yYJ2TLp9/2018-04-29-002706.png)
## GUI

v2ray图形化界面软件与ss操作类似，请留心，以[v2rayN_Pro](https://drive.google.com/drive/folders/1oCt98YHiFdf_uJPB2nRGU2FXDnZxSXVM)为例，将服务器`设为活动服务器`

<!-- ![](https://ipfs.io/ipfs/QmdttdMMn7tbhE3k7KQNnHWPxPeS8CJ2fTXB1NGFs18haa?3.png) -->

![](https://i.postimg.cc/4xWLkt0Z/2018-05-06-211557.png)
自带UDP转发，但你的账号服务器也必须支持UDP转发并开启，才可连接网络游戏

<!-- ![](https://ipfs.io/ipfs/QmTcjcDKmZvGAdER6pmqVGVUYU4Qy6PJ6C2NKiS2U4PpRM?0.png) -->

![](https://i.postimg.cc/L6TvLL2f/2018-05-06-212229.png)

如需共享账户，可将二维码截图或复制v2ray的链接分享给好友，扫描或粘贴导入皆可

![](https://i.postimg.cc/MHY00J2x/2018-06-09-194631.png)


## proxifier

!> 支持网络协议之间的转换，用于打开不同网络协议的软件进行互联，试学一月不收任何费用

 未配置网络协议的情况下，打开telegram，连接是不成功的，此时打开proxifier协议代理软件，在`profile`中选择`proxy servers`

<!-- ![](https://ipfs.io/ipfs/QmXEQikveHVzSXwieaSZQMthKLi2b3Dmrj4CmhbrkKb5bS?4.png) -->

![](https://i.postimg.cc/j5Vbzzvt/2018-05-05-00.png)

点击`add`选项弹出此`proxy server`窗口

<!-- ![](https://ipfs.io/ipfs/QmQZz9AszKY52Rb9b2pGbucYbAhdc1TvnzfSTkR1Kzkv2A?2.png) -->

![](https://i.postimg.cc/BvFWQj3y/2018-05-05-012427.png)

出现提示窗口一直默认即可

<!-- ![](https://ipfs.io/ipfs/QmThWyoMWXtBPH2CRhcn6iuA85M1piYr52ng1hcqVXCG17?3.png) -->

![](https://i.postimg.cc/SQrBsF0y/2018-05-05-013230.png)

这时处于`direct`选项全局模式OK

<!-- ![](https://ipfs.io/ipfs/QmdnvWMZ4r61N4JUijmWSbf8Jwt7i3BzfL1fzo3DWtvFVf?4.png) -->

![](https://i.postimg.cc/W37HhrH9/2018-05-05-015347.png)

勾选` Resolve hostnames through proxy`可防止DNS污染

<!-- ![](https://ipfs.io/ipfs/QmfLdRwcQD1WqC5DfgXzmAyV6T3F3cNyGRLcYAXB6UWMNL?2.png) -->

![](https://i.postimg.cc/y6vGKm9x/2018-05-05-013748.png)

在ss的pac模式下测试telegram

<!-- ![](https://ipfs.io/ipfs/QmXTLirvocLvNXkskAHYuRkfBERQRpeSrM6WspCV8PQvtG?0.png) -->

![](https://i.postimg.cc/28tXbC0f/2018-05-05-01442.png)


## privoxy

!>这是一个http/https协议代理工具，通过它将sock协议转换为http/https协议，以便访问互联网

打开`option`选择`edit main configuration`

<!-- ![](https://ipfs.io/ipfs/QmPcjXUUhr7AAHi3vSHVy6UfsADi1fhhb1Bt4ypYDFRaiR?3.png) -->

![](https://i.postimg.cc/yY4Rp5pz/2018-05-06-200606.png)

在配置文件中末尾处添加`forward-socks5 / 127.0.0.1:1080 .`

<!-- ![](https://ipfs.io/ipfs/QmQfecQdLwrw2xaerNosFDvrrhhdR2WvJozidVNbp1GWw5?2.png) -->

![](https://i.postimg.cc/zf6vbb91/2018-05-06-200824-1.png)

到`代理`中设置privoxy的默认地址与监听端口

<!-- ![](https://ipfs.io/ipfs/QmZ4nnJsvPqsoCeQPRvh7yiun7SiUscGPg5e2KxxFemaFC?4.png) -->

![](https://i.postimg.cc/6qw9ndcF/2018-05-06-201359.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmY185S5pis1Q9rPpg6xH5UjodWT1Zr2qoRMkGj8Gpd4f1?2.png) -->

![](https://i.postimg.cc/1RHSbVJ5/2018-05-06-203158.png)

将网络共享给手机，ss共享局域网也是做了privoxy含有的端口映射功能；按照如下配置将本机环回地址改为任意地址

```
# 可以允许局域网中的连接,0.0.0.0是绑定任意地址
listen-address 0.0.0.0:8118

# 仅当前系统的软件才可以连接到Privoxy的监听端口 
# 127.0.0.1:8118
```
查看本机局域网IP地址

<!-- ![](https://ipfs.io/ipfs/QmdwEi4zS8DNWx8gzkykPAoBkocQguEEP4QYhZFQV8Kwj9?1.png) -->

![](https://i.postimg.cc/Vvsxz4Ds/2018-05-05-032400.png)

`高级`设置`代理`选择`手动`，按照如下信息设置

<!-- ![](https://ipfs.io/ipfs/Qmcw7qqe9euzZ25CX5A9epEi45wAe9hAs5zwrhaK5MkrKU?1.png) -->

![](https://i.postimg.cc/15tkTC8J/QQ20180507165544.png)

测试

<!-- ![](https://ipfs.io/ipfs/Qmb7SwSVo6VMY2og6hZeEYrTcS1KcYNxWckYYkyZifjBSS?0.png) -->

![](https://i.postimg.cc/vHcKX4KK/QQ20180507165554.png)


## SSH-Tunnel

打开[SSH站点](http://www.speedssh.com)，创建SSH账户

<!-- ![](https://ipfs.io/ipfs/QmZEDXe76sAvE9f55jcqyj2gSQWhGjhAY19SFerks4AZD4?1.png) -->

![](https://i.postimg.cc/DwFBH5y8/2018-05-07-020641.png)

在[Bitvise SSH Client](https://www.bitvise.com/)上输入相关信息，`22`为SSH默认端口，登录

<!-- ![](https://ipfs.io/ipfs/QmVZU3eTnUMt3AjduBZwMFixaotncWgSf3K4aZ1iasFqhU?0.png) -->

![](https://i.postimg.cc/FKCpf4bL/2018-05-07-031612-1.png)

关闭

<!-- ![](https://ipfs.io/ipfs/QmV3y5DGfVHasLdjzhEktHYNycQBDqFRgdZKbcGqbbWdAK?3.png) -->

![](https://i.postimg.cc/vmTLwKRH/2018-05-07-021221.png)

<!-- ![](https://ipfs.io/ipfs/QmfVXq1NvcVC2gqrFq3yLvWkHhFMmxwzG2y1NqnVh2TmaP?0.png) -->

![](https://i.postimg.cc/T1VncMbQ/2018-05-07-021255.png)

设置`SOCKS/HTTP proxy forwarding`

<!-- ![](https://ipfs.io/ipfs/QmYje4D3Sc5KDpZy1hJnD1QmEgKA4UP9dds7mNTZh21QvT?1.png) -->

![](https://i.postimg.cc/HLF5Ds4B/2018-05-07-021327.png)

设置代理

<!-- ![](https://ipfs.io/ipfs/QmS5Y8qBjE8aUxGUM9Cz2Wm9dgh7DGYoPfFBNXDmhbDvqf?0.png) -->

![](https://i.postimg.cc/6qfGvVsm/2018-05-07-021118.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmdjxGqsaSRsGdKdUx77fafgstHuR4basXDac42jiLARzS?4.png) -->

![](https://i.postimg.cc/fbStKQnX/2018-05-07-021103.png)


# 使用网站

## 搜索站点

> 其搜索引擎的特点是对语义搜索支持较优，同时结合了传统的关键字搜索，技术实现上介于谷歌和[W|A](https://zh.wikipedia.org/wiki/Wolfram_Alpha)之间。
>
> 雅虎、微软搜索业务合并之后，Ask.com是美国第三，世界第六大公网搜索引擎，仅次于谷歌、必应和百度、[NAVER](https://zh.wikipedia.org/wiki/NAVER)、[Yandex](https://zh.wikipedia.org/wiki/Yandex)。据一份调查报告表明，Ask.com是谷歌用户首选的替代搜索引擎。
>
> ——摘自 维基百科

现今IP被封禁

<!-- ![](https://ipfs.io/ipfs/QmY2qrPY83q7qU4KHPC2D4tynwgj3ikCnNmPtEHzXfa3SH?1.png) -->

![](https://i.postimg.cc/3xDQ39nS/2018-04-30-140950.png)

## DuckDuckGo

> DuckDuckGo是一个互联网搜索引擎，其总部位于美国宾夕法尼亚州保利市。DuckDuckGo着重在传统搜索引擎的基础上引入各大Web 2.0网站的内容，主张维护用户的隐私权，并承诺不监控、不记录用户的搜索内容。
>
>—— 摘自 维基百科

目前已被封IP

<!-- ![](http://ipfs.io/ipfs/QmUGinkyFHMaec77wF72s5qz9rh1YBJvzC4ZiMjY5XGjri?4.png) -->

![](https://i.postimg.cc/C5K9X4R4/2018-04-30-135848.png)

## Ecosia

> Ecosia是一个网页搜索引擎，他们将至少80%的剩余所得公益捐献，目前正关注植树。 Ecosia支持全财务透明。 Ecosia由B-labs认证为公益企业，B-labs称“搜索引擎自2009年12月成立以来，将80%的广告收入捐出，筹资超过1.5百万美元用了保护雨林”。 它发布了免费网页浏览器，叫做EcoBrowser（Chromium的改版）。
>
>—— 摘自 维基百科

主要搜索源是bing，必应国内版返回的数据和谐较多

<!-- ![](https://ipfs.io/ipfs/QmNQ5qgTaaT1A4q7cwqYinbvi3nzC4qaA4reEhZfnBaFGa?4.png) -->

![](https://i.postimg.cc/NFLPpfnJ/2018-04-28-210623.png)

## Qwant

> **Qwant**是一家法国公司，它于2013年7月推出了同名网络搜索引擎。它声称不使用[用户跟踪](https://en.wikipedia.org/wiki/Website_visitor_tracking)，不要将搜索结果个性化，以避免陷入[过滤器泡泡](https://en.wikipedia.org/wiki/Filter_bubble)中的用户。
>
> 该网站每天处理超过1000万次搜索请求，全球每月超过5,000万个人用户，分布在三个主要入口点：普通主页，简化版本和针对儿童的Qwant Junior门户过滤结果 
>
> ——摘自 维基百科

搜索效果很不错，数据很全面

<!-- ![](https://ipfs.io/ipfs/QmZbGQihNC8zKhBxFxNc7jWtF3qML4jfjXE7aCwozQRQPg?1.png) -->

![](https://i.postimg.cc/GhWSxRxK/2018-05-01-084517.png)

但会不会同[startpage](https://www.startpage.com/)被GFW封杀，也是有点悬的问题，也许它只想让我们不准看、不准听、不准说，喜迎油价上涨地着老大哥的[www.baidu.com](https://www.baidu.com)


## 网页时光机

> 网站时光机（英语：Wayback Machine）[4]是万维网或互联网上传播的其他信息的一个数字文件网站，是美国加利福尼亚州旧金山的非营利组织——互联网档案馆最重要的服务之一。—— 摘自：[网站时光机 - wikiwand](https://www.wikiwand.com/zh-cn/%E7%BD%91%E7%AB%99%E6%97%B6%E5%85%89%E6%9C%BA#/overview)

!> 当对于相关技术讨论封锁越来越严，网站内容随时有丢失的可能，利用这个网页时光机，做个永久网页档案备份，方便下次再次查询与恢复思路继续联想。

进入 https://web.archive.org 输入想要永久备份的网址页面，再点击 `save this url in the wayback machine` 便可生成备份站点。

![](https://i.postimg.cc/CMbyc8K2/Snipaste-2019-06-09-19-13-00.png)

对于已经备份过的网页该网站是存有记录的，不过对于显示css、image并不理想，还是存在一定的局限性。

![](https://i.postimg.cc/1X6P8R9K/Snipaste-2019-06-09-19-45-23.png)

愿意离线保存的话，在Chrome设置中`更多工具 -> 网页另存为 -> 网页全部(*.htm;*.html)`或者`ctrl + p`打印PDF（建议使用[wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf)针对网页打印PDF，相关参数官网有详细说明）；也可以保存成一个概览整图，在`f12`（开发者工具）中，`ctrl + shift + p`（控制台）输入：`screen` 如图示

![](https://i.postimg.cc/fTR7x34y/Snipaste-2019-06-09-20-03-18.png)

btw，当网页无法打开或者失效不久，没有时光机的话，也可以通过快照临时查看，[灵感来自：coderschool](https://coderschool.cn/2348.html)。

?> 在补一刀：使用 [similarsitesearch](https://www.similarsitesearch.com/cn/) 可查询相似网站，你懂的，ヾ§ ￣▽)ゞ2333333


## 利用个人博客及视频平台

!> 方法有很多，同时每个人的主要的活跃平台及相关着重点的不同，比方说：有的人在YouTube、Twitter，也有的人在GitHub、个人网站（博客、分享论坛）等等，或是都有涉及。由此，搜集情报并不要局限某一平台而是要多层探索。
一些私人博客出于某种目的（技术分享，客流营销），为了吸引更多的访客，也会开放几个代理节点分享，当然他们中也有纯粹是为了连接互联网的。
如果封锁临时邮箱，那么就注册个qq小号、outlook（可销户），创建一个专用于试用摸底的邮箱；手机号码就用虚拟电话textnow、Google voice，国内的阿里小号也可以试试。
有些站点为了推广也会在GitHub上发放每日更新的节点，之后便附上他的个人站点链接；现在也存在一些机会主义者跟风吸引流量获得更多的关注，也在GitHub上搞相似甚至完全一样独立的repo。

两会以及高考的一段时间，都可以算国内的敏感时期，爱国上网的难度是很高的，节点被封锁一大批，部分代理网站及虚拟系统站点都受到不同程度的封锁，就更难获取到时常更新节点信息网站的有效节点了；说难听点：国内基本就是互联网的孤岛 — 局域网。因此，这些人的个人站点恰恰可以成为一个访问互联网的中转站（获取节点的中转站）。

在搜索引擎上搜索如：“ss/ssr、v2ray节点分享”等相关关键词，总会找到被爬取到一些个人博客网站；当然，也可以在GitHub上输入这些关键词，如图所示。

![](https://i.postimg.cc/fTjTxqCM/Snipaste-2019-06-08-14-25-52.png)

进入 [youneed.win](https://www.youneed.win) 即可观察到这些重点信息，他的个人站点类似于 [free-ss.site](https://free-ss.site) 的国内镜像；因此，将此站点所示的ss节点信息填入 shadowsocks 即可；与之类似的还有：[nulastudio/Freedom](https://github.com/nulastudio/Freedom) 等等

![](https://i.postimg.cc/MpMPCNLS/Snipaste-2019-06-08-14-28-28.png)

不过也得注意的是：关注的人越来越多，自然会引起五毛以及内部的觉察，他们只要动些手脚比如人海举报、或是gfw等级封锁，自然又访问不成了。使用 watching 留意观察他提供ss节点访问更新就好了。btw，他这站点借助 [weirch (free-ss的站长)](https://github.com/free-ss) 的 free-ss.site 提供的节点，看来引流量不少；但不可否认，以此方式提供节点信息，确实帮助了不少人，这个是值得肯定的。

和 weirch 聊到相关话题，我也把 [WebSiteOutlook](https://github.com/hoodiearon/WebSiteOutlook) 的issue功能关了，因为...如图...当然我也删去一些人发着玩的 issue 以及广告，由此还是将存储库的issue功能关闭算了...

![](https://i.postimg.cc/4y6xdWy2/Snipaste-2019-06-08-14-56-44.png)

## YouTube 油管订阅

搜索相关关键字查看相关视频，如果觉得up主多数视频有实际帮助的话，订阅他的频道，即可

![](https://i.postimg.cc/YC43TXsG/Snipaste-2019-06-13-21-20-00.png)

顺便推荐几个技术分享站点，也顺带着安利一个网盘 [mega](https://mega.nz/)

* [技术拉近你我](https://coderschool.cn)
* [如有乐享](https://51.ruyo.net)
* [坚果极客](https://www.nutgeek.com)

?> 说一些题外话：
真正良心的机场主也不容易，记得我在写到邮件获取ss并导入outline的机场好像倒了...中国号码普遍注册难度很高，稍不注意填写验证码时效过期，再验证时，发现验证过多无法验证了...
解决方案：用原生手机的gmail注册或换个浏览器试试，但这都没法解决的话...还是搜索下提供此注册服务的淘宝或是微商吧。


## 网页代理的使用

!> [rabbit](https://www.rabb.it/)是视频应用社交分享平台，由于内置了连接外网的Ubantu系统，所以能够科学上网，这个就相当于使用网页代理；像这些提供内置操作系统服务的站点，可以直接用它来注册textNow、Google voice

点击资料旁在右上角头像那点击`My Room`，然后并选择任意项

<!-- ![](https://ipfs.io/ipfs/QmYon74j1A3bpv5BgESkuxmKg3Fsnt2aDC6aByQ89iLGH1?4.png) -->

![](https://i.postimg.cc/1zTmKfdQ/5cf8ccb934d9511615.png)

点击优土小图标

<!-- ![](https://ipfs.io/ipfs/QmYddfvgPnXZ3NhpxsqU9MXwrAtyi2xTjpy99aUEnAeWzb?4.png) -->

![](https://i.postimg.cc/cJKZ6dL5/5cf8cd00b088751477.png)

网速比香港记者还快，刷梅林路由这类修电脑动手实操性较强的，也可在这进行在线观看

<!-- ![](https://ipfs.io/ipfs/QmRLuupq19dKy7dRKy2zkdo6kqSSAFCrbnHq7wXqjKvhh4?3.png) -->

![](https://i.postimg.cc/ZKLs4Jf6/2018-04-29-170242.png)

## demo.glyptodon

打开 [demo.glyptodon](https://demo.glyptodon.com)，一直 `OK` 确认并等待开机即可

![](https://i.loli.net/2019/06/06/5cf8cd8d9936b39088.png)

测试，也试着玩一下简单的网页代理吧：[anyproxy](https://www.anyproxy.cn/)

![](https://i.loli.net/2019/06/06/5cf8cacec80aa67102.png)

当然，也可使用[netptop/siteproxy](https://github.com/netptop/siteproxy)在heroku平台上搭建代理网页自行使用，部署方式该代理网页项目已说明，不再重复叙述。在线代理地址：[proxy.netptop](https://proxy3.netptop.com/)

![](https://i.loli.net/2020/06/07/dVDnFw5fvNiuobR.png)


## heroku搭建ss服务器

> **免费配额与限制：**
> * Network Bandwidth/流量: 2TB/month – Soft
> * Shared DB processing/并发数: Max 200msec per second CPU time – Soft
> * Dyno RAM usage/使用运行内存: 512MB – Hard
> * Slug Size/存储空间: 300MB – Hard
> * Request Length/请求时间: 30 seconds – Hard

> 在正确部署的情况下提示Application error，是由于访问量各项配额耗尽而停止服务

 fork！github项目：

* [shadowsocks-heroku](https://github.com/onplus/shadowsocks-heroku)

创建App

<!-- ![](https://ipfs.io/ipfs/QmUXxiPhVKLX446nyc7Z6pdSw8WQ8F1wA37sBnSfC7wCgM?2.png) -->

![](https://i.postimg.cc/NFKxzR93/2018-04-29-195722.png)

起个可用名称，默认美国服务器就行，总之不要选网络有限制国家的服务器

<!-- ![](https://ipfs.io/ipfs/QmUNHKLumDEBb4XdxydVEenRauihPnwuA3bTtcCZKizJZh?1.png) -->

![](https://i.postimg.cc/T3TvZP0k/2018-05-16-013449m.png)

在`deploy`点击github图标，并搜索fork过来的项目名称`shadowsocks-heroku`

<!-- ![](https://ipfs.io/ipfs/Qma4mAJVrjEC8nVKos6Eb44CbKFppJm6fqnB4ieVhyaoVn?0.png) -->

![](https://i.postimg.cc/RVQjQBmw/2018-05-16-014155.png)

点击`Connect`按钮

<!-- ![](https://ipfs.io/ipfs/QmSGRCqZ25Kr9kZCFhetdfTMJgKvYmxEHsCCN53WzmrUhE?1.png) -->

![](https://i.postimg.cc/C5C6Nj3w/2018-05-16-014818.png)

转到`settings`点击` reveal config vars`

<!-- ![](https://ipfs.io/ipfs/QmdvghVLwd7std3mSFauDrdVMv4h4V3mmHvMRKiSvdXq61?2.png) -->

![](https://i.postimg.cc/FR3Prys0/2018-05-16-015444.png)

填入`METHOD`与`KEY`并设置其相关参数，关于各项加密算法请看此章结尾处

<!-- ![](https://ipfs.io/ipfs/QmeaPP1aktxNH297tUu8NCu1eTcQwpZ5TwXQLJLQ4D1hN7?2.png) -->

![](https://i.postimg.cc/50B3dfn3/2018-05-16-020104.png)

回到`deploy`选项

<!-- ![](https://ipfs.io/ipfs/QmWuBvjMhmMK2igG3Y7LjZJcfv7bRysTaCYstxLgq7FVrt?0.png) -->

![](https://i.postimg.cc/QdvkFFzm/2018-05-16-020653.png)

下拉点击`enable automatic deploys`完成后再点击`deploy branch`

<!-- ![](https://ipfs.io/ipfs/QmVVTUPaB96knLXLjcMvF6dRiqrfGxnEn3NLBFe7CNxRGK?2.png) -->

![](https://i.postimg.cc/05ZYpW3b/2018-05-16-020817.png)

此时已经部署成功了

<!-- ![](https://ipfs.io/ipfs/QmRbbbFZmsVLoyTNSHhPrg8CRs5QCdXFedK6fST8H9q1Ri?4.png) -->

![](https://i.postimg.cc/9f3ZWv4N/2018-05-16-021041.png)

[下载相关客户端](https://github.com/onplus/shadowsocks-heroku/releases)

<!-- ![](https://ipfs.io/ipfs/QmdCvNxsKYfuxDSjnrtbu4capqkMuw1TWHP2TPHoJgcnN7?4.png) -->

![](https://i.postimg.cc/59PzHHYz/2018-05-16-021835.png)

下载完成后解压缩，并打开`config.json`配置文件

<!-- ![](https://ipfs.io/ipfs/QmS9CrJeuaAeBVz9eK8SLE4iX4bgMRizucuFkS6Uvd6j8F?2.png) -->

![](https://i.postimg.cc/ZRb9nZJj/2018-05-16-022113.png)

配置`config.json`填入页面生成的地址以及在heroku上设置好的加密与密码参数

<!-- ![](https://ipfs.io/ipfs/QmeYnigQFmkN2AbL2Xbqxnvsjaq57LKuxTesWHkUSRNVkM?3.png) -->

![](https://i.postimg.cc/tCZsYBH0/2018-05-16-022758.png)

再打开`ss-h.exe`与配置chrome代理插件`switchyomega`的各项参数，并应用选项

<!-- ![](https://ipfs.io/ipfs/QmQXAw2mEYqVe5RDnypvkSr61FdWX5kxU2fFndq9UE161Z?1.png) -->

![](https://i.postimg.cc/xC1CYRP4/2018-05-16-023617.png)

再选择已配置好的情景代理模式`proxy`

<!-- ![](https://ipfs.io/ipfs/QmP2RX3fpMDNDqyzqGyJB6nNxWhZH9UsckEzrxuBs4JWHp?1.png) -->

![](https://i.postimg.cc/htRthgrx/2018-05-16-024447.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmXYPPXw95AHRsXPTUndycXNKjyQZQu5F8Zx6ZvBn9CS4E?3.png) -->

![](https://i.postimg.cc/7ZNJkfkb/2018-05-16-025046.png)

加密算法

* rc4
* rc4-md5
* table
* bf-cfb
* des-cfb
* rc2-cfb
* idea-cfb
* seed-cfb
* cast5-cfb
* aes-128-cfb
* aes-192-cfb
* aes-256-cfb
* camellia-256-cfb
* camellia-192-cfb
* camellia-128-cfb


## heroku搭建v2ray服务器

!> 由于国家日渐强盛在国际上的地位及影响不断的提升，搭建此服务器存在有很大封禁风险！[参见 issue #63](https://github.com/onplus/v2hero/issues/63)

 fork！github项目：

* [v2hero](https://github.com/onplus/v2hero)

使用现成的[模板](https://heroku.com/deploy?template=https://github.com/onplus/heroku_go-getting-started)，默认的uuid有冲突所以需要更改

<!-- ![](https://ipfs.io/ipfs/QmYMotFhdsdFK2nbro8psM9DrfPuGfoR1UW6Wcfhyp8e9u?2.png) -->

![](https://i.postimg.cc/wxstBWpC/2018-05-16-073517.png)

使用[uuidgenerator](https://www.uuidgenerator.net/)刷新一次页面每次均生成不同uuid

<!-- ![](https://ipfs.io/ipfs/QmdosJDGsEi9aXg9J42BgaRdV4qrEE7BCRCh1HuxwVt2Uc?3.png) -->

![](https://i.postimg.cc/jqN5TL6K/2018-05-16-073839.png)

复制uuid粘贴进入uuid填写空中并确定

<!-- ![](https://ipfs.io/ipfs/QmZ2jV6DEyoAaAQ45gAsfYZUnYnqjSfPpLqWhVYWGg4cL7?3.png) -->

![](https://i.postimg.cc/Xq0nqkKW/2018-05-16-080047.png)

授权登录[travis-ci](https://travis-ci.org/profile)中开启按钮并设置

<!-- ![](https://ipfs.io/ipfs/QmTvirGSXtuXiBJNjKBeUAQZqvZT4qy9YNVqTSX11BPQKj?0.png) -->

![](https://i.postimg.cc/q7hrG5j0/2018-05-16-074407.png)

在`setting`选项中找到`Environment Variables`

<!-- ![](https://ipfs.io/ipfs/QmPXP33L7Pr9zRLykptoKcvviJuRypviVTLfmensgQxkBG?4.png) -->

![](https://i.postimg.cc/xT6SV2Zn/2018-05-16-080618.png)

环境变量相关参数

|name|value|
|:-:|:-:|
|HEROKU_APPNAME|heroku应用名称|
|HEROKU_EMAIL|注册heroku的邮箱|
|HEROKU_APIKEY|heroku的apikey| 

添加写入相应键值数据
<!-- ![](https://ipfs.io/ipfs/QmPGKFVeEbPb8x2hkTDnx4X1RwEWiV7FpsKZr22n6gpqyb?1.png) -->

![](https://i.postimg.cc/8kb2LGNM/2018-05-16-081238.png)

关于`api key`的位置，点击头像选择`account setting`往下拉即可看到

<!-- ![](https://ipfs.io/ipfs/QmbricYnEEoG4sn3tCnqVidrHdcaioWjiPZbXgfjKBZUyd?1.png) -->

![](https://i.postimg.cc/nhXN8Q7G/2018-05-16-081848.png)

按步骤构建即可

<!-- ![](https://ipfs.io/ipfs/Qmc93xvtPjj3fFgfGPX9kppM8tr8LdBTgg4hniNe4sAKpg?0.png) -->

![](https://i.postimg.cc/qqBZ1t4n/2018-05-16-082146.png)

等待片刻，黄色变成绿色即可

<!-- ![](https://ipfs.io/ipfs/QmYko1LSWdnnAGFcuijvxP7WesjBuUU3eQ5XmMnSU45CMK?2.png) -->

![](https://i.postimg.cc/DyMYcyDJ/2018-05-16-082553.png)

在heroku的`more`选项中选择`Restart Dynos`并再次选择就行

<!-- ![](https://ipfs.io/ipfs/QmYkUkyuG6UzPrYBqSAdMR12VFoA5kyf1ANSWVvMG45QDo?0.png) -->

![](https://i.postimg.cc/ZRHwvTpq/2018-05-16-083502.png)

`view logs`确认启动成功

<!-- ![](https://ipfs.io/ipfs/QmRCMqygTFgB8HRsfUD5zyQH33tkE2RnExCGjrDP7RA3Bk?2.png) -->

![](https://i.postimg.cc/tJftF7T9/2018-05-16-083035.png)

以v2rayN为例

<!-- ![](https://ipfs.io/ipfs/QmbQQ2im8gdNKfLtQ6WPv1YTZ448EsRuLgP3hSSP8gpqqq?3.png) -->

![](https://i.postimg.cc/jdp45WmX/2018-05-16-090353.png)

填入相应的配置参数并确定，id就是你的uuid，也可写入`80`端口，底层传输安全留空

<!-- ![](https://ipfs.io/ipfs/QmRoBPBGmWPRMHYhq2YAAhtfUJKRLYLPo3iy8GsvtbyNrv?2.png) -->

![](https://i.postimg.cc/5t3Bns07/2018-05-16-090615.png)

右键设置为活动服务器

<!-- ![](https://ipfs.io/ipfs/QmbDyHz2frv4nEgt4xz1V5TLkg8qc5JjvVnZ2PJSNuYPJF?1.png) -->

![](https://i.postimg.cc/fWFx2tzN/2018-05-16-091318.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmPkj4HZVJT6QHQVUP4R9yyxk7yhbcSd2zQaRh8PB5Skcr?1.png) -->

![](https://i.postimg.cc/cC88yhxN/2018-05-16-093822.png)


## heroku搭建ss分享站点

fork！github项目：

* [ShadowSocks-Share](https://github.com/zc-zh-001/ShadowSocks-Share)
* [ShadowSocksShare-OpenShift](https://github.com/the0demiurge/ShadowSocksShare-OpenShift)

创建App

<!-- ![](https://ipfs.io/ipfs/QmUXxiPhVKLX446nyc7Z6pdSw8WQ8F1wA37sBnSfC7wCgM?3.png) -->

![](https://i.postimg.cc/NFKxzR93/2018-04-29-195722.png)

在`deploy`点击github图标

<!-- ![](https://ipfs.io/ipfs/Qmd1K1ZU8EsF8mXi9hevXBMMTdb8U45a5G7gZE36ufdJYm?1.png) -->

![](https://i.postimg.cc/7hJgVDjD/2018-04-29-200459.png)

如图设置

<!-- ![](https://ipfs.io/ipfs/QmYJwnhwpqswgePB4i3HEqYtdAefHcu8ZzuTd1wUWzTRpY?2.png) -->

![](https://i.postimg.cc/gJnMfC1t/2018-04-29-200843-1.png)

?> 有些相关ss/ssr等其他节点分享站点搭建项目，需要自己手动配置相关环境变量；`settings -> buildpacks -> add buildpack` 再选择如：nodejs、java等项目所依赖的相关语言环境。

![](https://i.postimg.cc/q7cLhp8x/Snipaste-2019-06-09-13-04-49.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmaGX1PxhzqxFkVxfwb4VXGrK4RESZSuMfC8FBXapjbpAh?3.png) -->

![](https://i.postimg.cc/SKKV90QQ/2018-04-29-201525.png)

修改样式可点击find file选项，查找`.html`、`.css`文件

<!-- ![](https://ipfs.io/ipfs/QmdowFYWqJ9RnDYGkRxVPm3w2Z9xZp3NE23AsRoNzkZ25T?3.png) -->

![](https://i.postimg.cc/SN7GtQJN/2018-04-29-201800.png)

如有其他问题，可查看或发起issues

<!-- ![](https://ipfs.io/ipfs/QmeFUMF4SCtyzbmWExpvp4MbdpgbxCgcT12Sn4kLG7KBoZ?3.png) -->

![](https://i.postimg.cc/CKtCfz6J/2018-04-29-202117.png)


# ipfs专题

## ipfs

> 原文：[IPFS](https://ipfs.io/ipfs/QmV5ZVQxXURKPDcVDW8WjpLCiQYvNzg173XcB6rYFevoXm/#!index.md) 作者： [Mr.Maple](https://github.com/daijiale)

### IPFS简介

IPFS全称InterPlanetary File System，中文名：星际文件系统，是一个旨在创建持久且分布式存储和共享文件的网络传输协议。

它是一种内容可寻址的对等超媒体分发协议。在IPFS网络中的节点将构成一个分布式文件系统。它是一个开放源代码项目，自2014年开始由Protocol Labs （协议实验室）在开源社区的帮助下发展。其最初由Juan Benet设计。

IPFS是点对点的超媒体协议，可以让网络更快、更安全、更开放。它是一个面向全球的、点对点的分布式版本文件系统，试图将所有具有相同文件系统的计算设备连接在一起

<!-- ![](https://ipfs.io/ipfs/QmUSeaFSDkhz82dDfE1XbVZ7GEb7WntiZNYKRg3wfMN3kp?1.png) -->

![](https://i.postimg.cc/ncyQ97xG/ipfs-io.png)

IPFS—又称“星际文件系统”。简单点说，它是一个点对点的分布式文件系统（和比特币技术一样），通过底层协议，可以让存储在IPFS系统上的文件，在全世界任何一个地方快速获取，且不受防火墙的影响（无需网络代理）。

我们现在所使用的互联网协议被称作——超文本协议HTTP。这种协议具有超中心化特性。

也就是说，你从互联网上下载文件或者是浏览网页，一次只能从一个数据中心获取你所需要的资料。如果这个数据中心出现故障，或者被限制或是攻击，就会出现文件丢失或者网页无法打开的问题。比如你存在某云盘的资料突然无法下载，或者你想浏览的网页因为某些政策原因无法打开。

而IPFS的目的就是解决这些问题。在某些方面，IPFS类似Web，你一样可以基于IPFS进行互联网地址的链接。但IPFS是去中心化的，它不存在Web的主网故障问题。所以，**IPFS完全取代掉HTTP也并非天方夜谭**。

### IPFS与HTTP的区别

#### HTTP的四大痛点

<!-- ![](https://ipfs.io/ipfs/QmU6CuRkqHETWhoSi8JV4SUAPKADhLBUkva7kUvnp4DGb3?0.png) -->

![](https://i.postimg.cc/ht8hJ5pK/ipfs-is-the-distributed-web.png)

> HTTP效率低下，服务器成本昂贵

使用HTTP协议从一台计算机服务器上一次只能下载一个文件，而不是同时从多台计算机中获取文件。通过P2P方式的视频传输可以节省带宽成本的60％。

> 历史文件被删除

网页的平均使用寿命为100天，大量的网站文件不能得以长期保存。有些重要的文件因操作不当，也有可能永远在互联网消失。

> 中心化的网络限制了机会

互联网一直是人类进步的催化器，但中心化的网络容易被控制，是对互联网良性发展的的威胁。

> 网络应用太依赖骨干网

为保证数据的可靠性，我们开发的应用程序太依赖大型的中心服务器，并通过大量的备份来保证数据的安全。

HTTP协议已经用了20年的历史，从HTTP 1.0 到现在的HTTP5，网页的展示越来越美观丰富，**但它背后的Browser/Server 模式是从来没变的**。

#### IPFS区别于HTTP痛点的特质

> 互联网信息永久存储

IPFS像是一个分布式存储网络（类似于SIA），任何存储在系统里的资源，包括文字、图片、声音、视频，以及网站代码，通过IPFS进行哈希运算后，都会生成唯一的地址。今后，你只要通过这个地址就可以打开它们。并且这个地址是可以被分享的。

而由于加密算法的保护，该地址具备了不可篡改和删除的特性（在某种意义上，如果破解密码还是有可能被篡改或删除，但概率极低）。所以，一旦数据存储在IPFS中，它就会是永久性的。比如我们经常会遇到的某个资源删除无法访问的问题。

这种情况，在IPFS上就不会发生。即便是把该站点撤销，只要存储该站点信息的网络依然存在，该网页就可以被正常访问。存储站点的分布式网络越多，它的可靠性也就越强。

与SIA不同的是，IPFS存储的一般是公共信息，普通大众都可以获得的。有一种说法认为，**如果IPFS完全取代HTTP，那么此后，人类历史将会被永久保存，且不会被篡改**。

这也就意味着，人类所做的每一件事情都会被记录，不管是正确的、抑或是错误的。

> 解决过度冗余问题，实现共享经济

如果你喜欢某部电影，又担心电影资源丢失，通常的做法是，你会把这部电影下载在自己的电脑上。比如电影《阿凡达》，在2016年一年的下载次数就达到了1658万次，总下载数量更是惊人。那么一个无法避免的问题是：同样的一部电影被反复储存，造成了内存资源极大浪费。这就是HTTP协议的弊端。同样的资源备份的次数过多，就会造成过度冗余的问题。

而IPFS的出现可以很好的解决这个问题。IPFS会把存储文件，做一次哈希计算，只字不差的两个文件哈希值相同。所以，用户只需要使用相同的哈希值，就可以访问那个文件，这个哈希值就是文件的地址。只要获取这个地址，就可以共享资源了。

基于上面的永久存储特性，你再也不用担心某个电影找不到了，也不用备份，**因为全球电脑上只要有那么几个人存储着，你就能拿到它。而不是重复存储几十万份**。

> 同时基于内容寻址，而非基于域名寻址。

IPFS的网络上运行着一条区块链，即用来存储互联网文件的哈希值表，每次有网络访问，即要在链上查询该内容（文件）的地址。

文件（内容）具有存在的唯一性，一个文件加入了IPFS的网络，将基于计算对内容赋予一个唯一加密的哈希值。这将改变我们使用域名访问网络的习惯。

提供文件的历史版本控制器（类似Git），并且让多节点使用保存不同版本的文件。

> 节点存储激励，代币分成

通过使用代币（FileCoin）的激励作用，让各节点有动力去存储数据。 Filecoin 是一个由加密货币驱动的存储网络**。矿工通过为网络提供开放的硬盘空间获得Filecoin，而用户则用Filecoin来支付在去中心化网络中储存加密文件的费用**。

### IPFS工作原理

<!-- ![](https://ipfs.io/ipfs/QmZ7t61ZkJESFhJCsifMAkXtof6dZvcczyx7J4WQDnBsAf?0.jpg) -->

![](https://i.postimg.cc/yYc0Pnvb/ipfswork.jpg)

* 每个文件及其中的所有块都被赋予一个称为加密散列的唯一指纹。
* IPFS通过网络删除重复具有相同哈希值的文件，通过计算是可以判断哪些文件是冗余重复的。并跟踪每个文件的版本历史记录。
* 每个网络节点只存储它感兴趣的内容，以及一些索引信息，有助于弄清楚谁在存储什么。
* 查找文件时，你通过文件的哈希值就可以在网络查找到储存改文件的节点，找到想要的文件。
* 使用称为IPNS（去中心化命名系统），每个文件都可以被协作命名为易读的名字。通过搜索，就能很容易地找到想要查看的文件。
* 从IPFS的介绍可以看出，IPFS设想的是让所有的网络终端节点不仅仅只充当Browser或Client的角色，其实人人都可以作为这个网络的运营者，人人都可以是服务器。


## ipfs简单使用

## 前言

在看了读者的邮箱来信后，确实，若是被勒令这不可抗拒的因素删除仓库也是毫无办法；何况，我也是各种担心也因其他缘由与相关操作不当导致删除重建好几次该书项目，而这次就需要着手使用ipfs这类去中心化的网络应用了。

这其中也遇到一些问题就是上传文件后，关闭了ipfs的进程，其他人却无法有效访问这个站点了。为此特意搜索相关相关问题内容，找到了一个合理的解释：

> 我还特意找了一个VM安装ipfs，并添加同样内容（"hello world"）的文件到ipfs，发现hash是一样的。相信全球大量的人员在测试ipfs时都可能会使用"hello world"作为文件内容。  

> 所以当访问地址`https://ipfs.io/ipfs/QmT78zSuBmuS4z925WZfrqQ1qHaJ56DQaTfyMUF7F8ff5o`时，访问的不见得是你自己的电脑上的这个hello.txt文件，除非这个文件的内容独特到全球只有你的电脑上有。  

> 文档`https://ipfs.io/ipfs/QmXZXP8QRMG7xB4LDdKeRL5ZyZGZdhxkkLUSqoJDV1WRAp`的内容比较独特，恐怕只有我自己的电脑上有，如果我不开机并启动ipfs进程，估计别人访问不了。

> —— 摘自 [王伟兵的博客](https://github.com/wbwangk/wbwangk.github.io/wiki/IPFS)

也就是说，打不开对方提供的已发布在网上的IPFS节点链接，很可能是资源仅他独有且关闭了ipfs的进程。

## 安装

打开[ipfs](https://ipfs.io/docs/install/)，选择[getting started with ipfs](https://ipfs.io/docs/getting-started/)

<!-- ![](https://ipfs.io/ipfs/QmVqhqctR8HaHEaLBsT8oCy5u2cDWH3xp5nWSgCjMGJTJJ?0.png) -->

![](https://i.postimg.cc/Y0SyFZ1Z/2018-05-27-092613.png)

[install ipfs now](https://ipfs.io/docs/getting-started/)

<!-- ![](https://ipfs.io/ipfs/QmT8nWpg14T2Vts7LRWiNMi4ZcXd3q96DYAYq8cFB3vF5j?2.png) -->

![](https://i.postimg.cc/vHg0dWXr/2018-05-27-093125.png)

[download ipfs for your platorm](https://dist.ipfs.io/#go-ipfs)

<!-- ![](https://ipfs.io/ipfs/QmTDGnkpwcuN6tQjnP7R7XpTjLxr9MXwGYKBBbAqXN7ako?3.png) -->

![](https://i.postimg.cc/fLqfGL9q/2018-05-27-093548.png)

点击即可下载

<!-- ![](https://ipfs.io/ipfs/QmSTjFqRHEjtW6LWYmE9eLy2YRGjKUmUQgX8JznX6N28Ui?2.png) -->

![](https://i.postimg.cc/XvVKXFKD/2018-05-27-093946.png)

解压并用CLI进入当前文件夹，输入`ipfs.exe init`完成初始化操作

<!-- ![](https://ipfs.io/ipfs/QmbAL6HMqHTc8stSxQRhowh5WBcVEiW4i4NsmTe6hcjS78?4.png) -->

![](https://i.postimg.cc/0yCWt9cF/2018-05-27-095305.png)

`ipfs.exe daemon`开启守护进程

<!-- ![](https://ipfs.io/ipfs/QmRQf6jx8U9VeFfu2gr8T7JhQX5zRdSPgaWmF7BipWrjvn?0.png) -->

![](https://i.postimg.cc/D0s51hSC/2018-05-27-095836.png)

输入`http://localhost:5001/webui`进入主界面，在`connection`版块中可以看到全球共有267个节点，这一数字也是动态变化的

<!-- ![](https://ipfs.io/ipfs/Qmf2iphYYZbzoZXisJB6rfGTdEU5MGzRwbPLaoobzA1Nkt?2.png) -->

![](https://i.postimg.cc/T2rrjCkH/2018-05-27-100854.png)

## 上传文件

在`files`版块中点击`create folder`创建文件夹，目前除图片外，若要正确上传文件，必须用文件夹的`hash`加载

<!-- ![](https://ipfs.io/ipfs/QmTWV2wo9on5oqgcgQq5N4hRyfLrNY3RXgcvtGfE13Shjb?2.png) -->

![](https://i.postimg.cc/vZpBNdT7/2018-05-27-113127.png)

选择需要上传的文件，右键`copy hash`，转到DAG板块中粘贴进输入框GO

<!-- ![](https://ipfs.io/ipfs/QmUMhW3H3ApEPihJs9gHxfAG1SExeyUuWZtoM2VmtCpQz7?3.png) -->

![](https://i.postimg.cc/qq5068Cc/2018-05-27-114055.png)

<!-- ![](https://ipfs.io/ipfs/QmeoED47NpN6HHEkiSnz4Mt32XJpoWtX1AQDuC1LaojUA8?2.png) -->

![](https://i.postimg.cc/dQbJF9wv/2018-05-27-114452.png)

将如上hash连接复制，并在前面加上`htttps://ipfs.io`

<!-- ![](https://ipfs.io/ipfs/QmRAbdqGsKiZjScrztkftxx9XTArenE8toKkvCZfLhvP8M?3.png) -->

![](https://i.postimg.cc/BvVdgqvs/2018-05-27-114812.png)

hash链接始终是太长了，就需要使用[tinyURL](https://tinyurl.com/)生成短链接

<!-- ![](https://ipfs.io/ipfs/QmfSA2veGGcndSWXpmxhn3zBNux4i1JMHv8Wm3fRr9nmbz?3.png) -->

![](https://i.postimg.cc/QCrY4VZL/2018-05-27-120243.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmVTmfExQdvVjrosgsmqKT5hk4wABW756V7pA6YcoN9hCu?2.png) -->

![](https://i.postimg.cc/9f7B6Vpc/2018-05-27-121017.png)

你愿意把它当作无限存储的网盘也可以，只不过任何人包括你在内不能删除它罢了；速度的话，聊天群、问答社区以及贴吧各种宣传，人多了应该自然也就会快一些。

## 部署静态网站

在这里我已预先提供了一份基于gitbook生成的静态网站文件夹

<!-- ![](https://ipfs.io/ipfs/Qmf337dkc4u8Vvz3afx6hVQwDutSagkEh1nPW7dRtSCpEC?2.png) -->

![](https://i.postimg.cc/J4FZMvt0/2018-05-27-164203.png)

命令行定位到文件夹的上层文件夹，执行`ipfs add -r web-book`上传整个目录

<!-- ![](https://ipfs.io/ipfs/QmYAHqw57WUfvTyLEd8EgAVE6gN38ykrZJg1bV7ci5z4de?0.png) -->

![](https://i.postimg.cc/X7BXcJ7N/2018-05-27-171923.png)

`web-book`文件夹的指令输出的最后一行的哈希值，就是你的网站的根目录

<!-- ![](https://ipfs.io/ipfs/QmSqfSqZCjZ2BGr75sK816cRGHksoESnYK8CPXfg6cjKUF?2.png) -->

![](https://i.postimg.cc/fLkMz2VW/2018-05-27-172511.png)

复制最后一行的hash值

<!-- ![](https://ipfs.io/ipfs/QmcP41JKtYrq7TuS3pdU2Hmh5zpTQsDKdmniFgQyJcgwb9?4.png) -->

![](https://i.postimg.cc/VkD6zbKR/2018-05-27-173142.png)

输入`localhost:8080/ipfs`后面追加已复制的哈希值即可

<!-- ![](https://ipfs.io/ipfs/QmW7yPmdmZXPanUrDfVFm7C38TjdB3B3gMWQXjXoU2iCf4?1.png) -->

![](https://i.postimg.cc/G2YdTBx6/2018-05-27-173114.png)

虽数据已添加到当前的ipfs节点中，但是并没有同步到ipfs网络；此时还只是离线部署，现在要将它发布在互联网上。

运行了`ipfs add -r` 的指令的窗口不要关闭，新建一个cmd命令行窗口，进入ipfs文件夹再输入`ipfs.exe daemon`便发布成功了

![](https://i.postimg.cc/mrC5Q7K3/2018-05-27-175819.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmdPPXYVMJ2JTMFChQbdQy2eApMiD6Dr763s27YD46n35b?3.png) -->

![](https://i.postimg.cc/3wXtyYDn/2018-05-27-181051.png)

## IPNS同步更新

由于去中心化的缘故，一但上传也就不能更改了，为此需要ipns的新目录以及节点id映射在新的hash值，用户只需访问`ipfs.io/ipns/节点id`查看相关的更新，也就是说以前的`ipfs.io/ipfs/目录hash值`被废弃了；这也看出来去中心化一个弊端就是产生大量垃圾，虽然链接很长很长...

为了演示方便在`book.json`文件中添加了新的插件，并再次使用了`ipfs add -r web-book`指令使其生成新的hash值。

<!-- ![](https://ipfs.io/ipfs/QmUokTS9iEMAvcBf2r4AuGXkgHzmoC97LuPLtnS3Tc3miz?4.png) -->

![](https://i.postimg.cc/YSR1K9FK/2018-05-27-213304.png)

使用`ipfs name publish`后面跟上站点根目录的hash值进行发布操作

<!-- ![](https://ipfs.io/ipfs/QmPrEGfXt53aZdXwkRgPC9qFLaziKZKXjy2sXgXQmTDdPk?2.png) -->

![](https://i.postimg.cc/65Z1vDg2/2018-05-27-220829.png)

使用`ifps id`查看节点id

<!-- ![](https://ipfs.io/ipfs/Qma7Ww1tWrrdX4aauMqYueeNnhuXR1Ms16JDkDCcSofYM1?1.png) -->

![](https://i.postimg.cc/ZqWN9hsX/2018-05-27-221733.png)

`ipfs name resolve`后面追加已查到的节点id

<!-- ![](https://ipfs.io/ipfs/QmaL3MCdyBbBS5n5X2sweyMj1pKW2UgZka4jY9rSQKtd3F?0.png) -->

![](https://i.postimg.cc/ZRhqTkG8/2018-05-27-222850.png)

此时，已经可以本地访问了，`localhost:8080/ipns/节点id`

<!-- ![](https://ipfs.io/ipfs/QmULUBN4wRUSQ5NquDxXwAyvGuXogymDBCbQbXQsB8BhvR?1.png) -->

![](https://i.postimg.cc/Zn54RJVd/2018-05-27-223735.png)

关掉之前的使用`ipfs daemon`指令的窗口，再打开命令行窗口重新运行该指令即可，由于访问人数不多再加上GFW的干扰，可能会很慢。

测试

<!-- ![](https://ipfs.io/ipfs/QmUe1eWwnUFPDpjiSu75Gyv3QxpaHm8Xb2aVJMmuydwXxk?2.png) -->

![](https://i.postimg.cc/qMY4JVnN/2018-05-27-225417.png)

## 备份

备份这很重要，但也很简单，在`C:\Users\lorem\.ipfs`下找到`config`文件并将其拷贝至云盘即可，lorem是我的用户名

<!-- ![](https://ipfs.io/ipfs/QmWdvB4mskcD6oPEWJLHB16JspxxdSQh9uog4JoaSgUR2v?3.png) -->

![](https://i.postimg.cc/xTkVFx7n/2018-05-27-232208.png)


## 对去中心化网络的信仰

> 原文：[对去中心化网络的信仰](https://www.kawabangga.com/posts/2226) 作者：[卡瓦邦噶！](https://www.kawabangga.com/)

美剧《硅谷》中提到了一种去中心化的网络：人们不再是从网络的中心的服务器上获得资源，网络的资源存在于每个人的设备上。

我比较认同这种互联网，人才是互联网的真正用户而不是服务器。互联网连接的应该是人与人，而不是人与服务器。

目前的中心化网络存在很多问题。**比如审查**，在现在的中国基本上不可能在国内的网络上讨论任何政治问题，在知乎、微博等国内社交媒体上存在大量“被删除的内容”，这已经让互联网失去和很大一部分意义。互联网为了分享知识和沟通而诞生，一个理想的互联网应该是可以自由发布任何内容、并且任何资源都不会被删除的。但是目前的互联网却走了一条错误的道路，集中化的网络让政府或者网站所有人对删除资源有了可能。但是设想一下，如果我们的网络是分布式的呢？如果网络存在于任何一个人的机器上，这样任何东西都不会被删除，一份资源可能有无数个冗余备份。Git和Bt就是一个成功的例子，github上有[被勒令删除的仓库](https://github.com/shadowsocks/shadowsocks)，但是因为git是分布式的，如果一个仓库足够流行，那么就会有无数份fork，官方仓库可以删除，项目却会永远存在。另外，去中心化的网络有着与生俱来的匿名性，资源从一台计算机到另一台计算机，发布者隐藏自己的身份轻而易举，如果不能保证匿名，如果保证言论自由呢？

**安全问题。**首先是文件的安全。一切存储介质都是有寿命的，目前可以想像到的最安全的存储方式就是放到云上。个人存储无论有多少冗余备份都觉得不安全，比如说家里着火，就可能把所有的磁盘损坏了。但是如果把文件通过BT的方式加密存储在别人的设备上（或者将适合共享的资源共享出去），可以免费使用很多备份，如果要使这份资源消失，基本上是不可能的（可能有一些隐患，但是这不正是互联网的构想吗？）。对于网站运营者来说，集中式的（比如说一台网站服务器）总有可能沦陷，通过各种各样的漏洞拿到服务器权限，那么攻击者基本上是占有了所有的内容。但是分布式[提供了完全不同的另一种的认证机制](https://zh.wikipedia.org/zh-cn/ZeroNet)。除此之外，还有DDoS的问题。DDoS目前基本上是不可解的，无论你有怎么样的策略，机房上层网络发现有巨大流量攻击的时候会采取最笨、也是最暴力的方式应对：将发送给你的网络包直接丢掉，让你的网站下线一段时间，等攻击结束，再恢复响应。如果你的业务足够大，可能还有和机房或运营商谈判的筹码，但是对于中小业务，人家根本不理你，直接给你切断。但是分布式的网络不会存在DDoS，况且如果网络涉及的优秀，你可以去离你最近的节点获取资源，相当于一个无形的超级CDN了（个人设想）。

**节省资源。**云存储是很昂贵的，带宽也很贵。集中化的网络避免不了要将所有的流量发往一处，将资源存放在一处，比如Google目前维护DC（数据中心）的[一年费用大约是120亿](https://gigaom.com/2015/02/04/google-had-its-biggest-quarter-ever-for-data-center-spending-again/)，虽然有文章说，[个人存储的成本更高](https://leonax.net/p/8267/zeronet-will-be-the-next-failure/)，但是不要忘了，分布式的存储是利用的空闲空间！相比于集中式，去中心必然需要更多的冗余，但是却可以利用个人的空闲空间，个人与个人之见的空闲带宽。我认为成本肯定比集中的数据中心低。

目前，很多去中心化项目已经证实了分布式的成功：比特币证明了去掉中心服务器核准交易是可行的，Git证明了分布式的版本控制是可靠、成本低的，BT虽然在很多国家被禁止，但是目前依然有相当多的用户在使用，并且速度也尚可。

我也承认，去中心化的网络会带来一系列的社会问题，例如[地下交易](https://zh.wikipedia.org/wiki/%E7%B5%B2%E8%B7%AF_%28%E8%B3%BC%E7%89%A9%E7%B6%B2%E7%AB%99%29)。技术是有两面性的，同时也是无罪的，但是不能因为社会问题而阻止技术的发展，当然这也是不现实的。

我相信将来，随着个人存储成本继续降低（摩尔定律），网络带宽越来越大（4G，5G），以及压缩技术、分布式技术的发展，总有一天，我们会看到一个理想的、完美的、真正的互联网。


## 为什么说去中心化很重要

> 原文：[Why Decentralization Matters](https://medium.com/@cdixon/why-decentralization-matters-5e3f79f7638e)  作者：[Chris Dixon](https://www.cdixon.org/about)

去中心化是与中心化相对的一个概念，简单的来说中心化的意思，是中心决定节点。节点必须依赖中心，节点离开了中心就无法生存。去中心化恰恰相反，在一个分布有众多节点的系统中，每个节点都具有高度自治的特征，每一个节点都是一个“小中心”。

<!-- ![](https://ipfs.io/ipfs/Qmcvrheq3DvMow9RKwtha145WaCztdYNszvTbKi1UzwHMj?3.jpg) -->

![](https://i.postimg.cc/kXRLyV65/6cmad.jpg)

随着网络服务形态的多元化，去中心化网络模型越来越清晰，也越来越成为可能。本文从**互联网的发展阶段，去中心化的优势，以及对去中心化趋势的预测**等角度，解释了去中心化的重要性。

### 互联网的前两个阶段

在互联网的第一个时代——也就是20世纪80年代到21世纪初，互联网服务建立在互联网社区控制的开放协议上。当了解到互联网固定的规则后，用户和组织就增加了他们在互联网中的存在感。同时期，包括雅虎，谷歌，亚马逊，Facebook，LinkedIn和YouTube在内的大公司都建立了大量的网络资产。在这个过程中，像AOL这样的集中式平台的重要性大大降低了。

在互联网的第二个时代，即从21世纪初到现在，盈利的科技公司中最有名的几家：苹果，Facebook和亚马逊（Google, Apple, Facebook, Amazon，即GAFA）构建了快速超越开放协议功能的软件和服务。**智能手机的爆炸式增长加速了这一趋势，移动应用成为了大众使用互联网的主要方式。**最终，用户从开放式服务迁移到这些更复杂的集中式服务上。即使用户仍然会用开放协议访问网络，他们也多半会通过GAFA四家公司提供的软件和服务进行访问。

这么做的好处是，通过出色的技术让数十亿人获得了非常好的体验，而且其中多数应用都可以免费使用。坏处是，初创公司、创业者和其他组织想在互联网领域分一杯羹就变得非常困难，**当然这种集中式平台并不会带走他们的用户和利润。**这一事实反过来又扼杀了创新趋势，使互联网不再那么有趣和活跃了。中心化系统也会造成社会紧张关系的普遍化，包括假新闻，系统机器人，没有用户言论自由的平台，欧盟隐私法和算法偏见等等。这些具有争议的情形在未来几年将会加剧。

### 互联网第三阶段

中心化系统的用途之一就是有利于政府对大型互联网公司施加监管。这样的监管建立在新出现的网络和过去的通讯网络（电话，广播和电视网络等）非常相似的基础上。但事实上，基于硬件的通信网络与新出现的基于软件的网络有本质上的不同。基于硬件的网络一旦建立，几乎无法重新架构，而基于软件的网络可以通过企业创新和市场力量进行重新架构。

互联网是基于软件的高级网络，其核心层相对简单，由数十亿个完全可编程的计算机组成。**软件只是将人类思维进行编码，因此具有几乎无限的设计空间。**连接到互联网的计算机都可以自由运行用户选择的软件。任何你想要表达的内容，加上正确的激励措施，都可以通过互联网迅速传播。所以说，互联网就是技术创新和设计碰撞产生火花的地方。

互联网仍处于发展初期：互联网核心服务在未来几十年内将进行重新架构。这一点将会通过加密经济网络（crypto-economic networks）实现。这种网络最开始在比特币中初步形成，通过以太坊的出现得到了进一步的发展。加密网络结合了互联网前两个时代的最佳特性：由社区管理的网络以及去中心化的分布式网络。最终，新型网络的功能将超过眼下最先进的中心化互联网服务。

### 为什么要去中心化？ 

**通常，大众对去中心化这一概念存在着广泛的误解。**例如有时会说，加密网络主张去中心化的原因是为了抵制政府审查，或者是因为自由主义的政治观点，然而这并不是去中心化如此重要的主要原因。

我们先来看看中心化平台的问题。这样的平台遵循着可预测的生命周期。最开始，互联网创业公司会尽其所能吸引用户和第三方人员，比如开发人员，企业和媒体组织，通过这种方式让他们的服务更有价值，因为“平台”的定义是具有多边网络效应的系统。在下图中，随着平台影响力的扩大使S曲线不断上升，这些平台对用户和第三方的掌控力也稳步增长。

<!-- ![](https://ipfs.io/ipfs/QmSe3ztTjKYc8trh9KP3daZABHdD6DNzuYBP3faEPsM8mh?0.png) -->

![](https://i.postimg.cc/Y2vtJCG5/xx001x.png)

当互联网创业公司的影响力到达S曲线的顶端时，他们与媒体、开发者等参与者的关系将从正和变为零和。最容易让公司继续升值的方法是从用户那里收集数据，并与竞争对手争夺潜在用户和利润。历史上曾有不少这样的先例，比如微软与Netscape，谷歌与Yelp，Facebook与Zynga以及Twitter与其第三方客户端。像iOS和Android这样的操作系统表现较好，虽然使用某些Apps仍需要支付30％的税费，但应用商店有权下架部分第三方的Apps，监管方面有绝对的话语权。

对于第三方来说，这种从合作到竞争的转变像是一场骗局。随着时间的推移，最优秀的企业家，开发商和投资者在中心化的平台上构建自己的网络时变得小心翼翼。现在数十年的证据已经表明，基于中心化的平台网络会以失望告终。另外，用户放弃隐私，下放私人数据的控制权，很容易受到来自安全漏洞的攻击。在未来，中心化平台的这些问题将更加明显。

### **进入加密网络时代**

加密网络是建立在互联网基础上的网络，它具有两个特点，其一，加密网络使用诸如区块链的共识机制来维持和更新状态。其二，加密网络使用加密货币（比如coins 或者tokens）去激励分享共识的参与者（比如矿工/验证者）。以太坊等加密网络，就是一个通用的程序编写平台，可以开发各种用途的分布式应用。其他加密网络就有一些特殊用途，例如比特币主要用于电子储值，Golem用于执行计算，Filecoin用于分布式文件存储等等。

**早期的互联网协议是由专门的团队或非营利组织创建的技术规范，而他们的生存则依靠互联网社区中的利益协调。**这种方法在互联网的早期阶段运行良好，但从20世纪90年代初以来，很少有新协议能够以上述方式进行普及。加密网络通过以令牌（token）形式向开发者，维护者和其他网络参与者提供经济激励，从而解决这些问题。加密网络在技术上也更加强大。例如，他们能够保持某种状态并对该状态进行任意转换，这是过去的网络协议无法做到的。

加密网络使用多种机制来确保它们在增长时保持中立，防止中心化平台的骗局。首先，加密网络和参与者之间的合同通过执行开源代码完成。其次，他们通过“退出—呼吁” 机制（“voice and exit”）进行网络检查。一方面，参与者通过社区治理获得呼吁，既可以是“链上”（通过协议）也可以是“链下”（通过协议周围的社会结构）。另一方面，参与者可以通过离开网络并出售他们的货币退出，或者在极端情况下通过分叉协议退出。

简而言之，加密网络让网络参与者一起努力实现共同目标 - 网络的扩大和令牌（token）的升值。这种一致性是比特币无视质疑一直保持繁荣的主要原因之一，像以太坊这样的新型加密网络都随其有了一定的发展。

如今的加密网络因对中心化网络产生过大的威胁而受到限制。其中最严重的包括对加密网络性能和可扩展性的限制。未来几年加密网络的发展主要是减少或者消除这些限制，并且构建组成加密堆栈基础结构层的网络。再往后，加密网络的主要任务将会是在这样的平台上建立应用程序。

### 去中心化的优势

说去中心化的网络会占据市场是一回事，如何占据市场就是另一回事了。 让我们看看具体的理由，对此持乐观态度。

软件和Web服务是由开发人员构建的。世界上有几百万的高级开发者，但是他们当中只有小部分在大型IT企业工作，还有小部分专注于研发新产品。历史上许多最重要的软件项目都是由创业公司或独立开发者社区创建的。

> “无论你是谁，大多数最聪明的人都会为别人工作。” - Bill Joy

去中心化网络可以赢得互联网的第三个时代，这与互联网当时胜出的原因是一致：赢得企业家和开发者的热情和想法。

在本世纪初，维基百科与Encarta等对手之间的竞争可以说明问题。在21世纪初，如果你比较这两种产品，Encarta其实做得更好，因为它主题覆盖范围更广，准确性更高。但维基百科改善的速度更快，因为它有活跃的志愿者贡献者社区。这些志愿者这种被分散的，去中心化的社区管理精神所吸引。到2005年，维基百科是互联网上最受欢迎的参考网站。Encarta网站于2009关闭。

**从这个案例中得到的教训是，当比较中心化的和去中心化的系统时，需要将它们看作一个动态过程，而不是静态、生硬的产品。**中心化的系统通常在开始的时候表现良好，但它改善的速度完全取决于所属公司的员工。相比之下，去中心化的系统虽然开始不完善，但在适当的条件下，它们的特点会吸引大量新的贡献者，产品的表现也就会成倍增长。

加密网络中存在多个涉及各方人员的复合反馈回路，包括核心协议开发者，互补加密网络的开发者，第三方的应用开发者以及运营网络的服务提供商。这些反馈回路通过相关令牌（token）的激励进一步放大，正如我们在比特币和以太坊所看到的那样 - 可以提高加密社区发展的速度（不过有时会导致负面结果，比如挖比特币将消耗大量电力资源）。

去中心化或中心化系统是否会赢得互联网下个时代，其实可以归结为谁将构建最具吸引力的产品，简单来说就是谁能够获得更多高质量的开发人员和企业家。 GAFA四家公司有许多优势，包括现金储备，庞大的用户基础和运营基础设施。加密网络对开发人员和企业家在价值主张方面更具吸引力。**如果加密网络能够赢得开发人员和企业家的青睐，他们将会调动比GAFA更多的资源，并在产品开发上迅速超过GAFA。**

> ”如果你在1989年问人们为了改善自己的生活需要什么东西，那他们不可能说使用超文本链接访问去中心化网络的信息节点。“ — Farmer & Farmer

中心化的平台通常会在推出应用程序时捆绑销售其他产品：Facebook具有其核心社交功能，iPhone拥有许多关键应用程序。相比之下，去中心化的平台通常开发出不完整，且用途不明确的应用案例。因此，这些案例需要经历两个产品—市场相适应的阶段：

* 平台与开发人员/企业家之间的产品市场匹配，他们将共同构建生态系统，完成平台搭建; 
* 产品市场在平台本身和终端用户之间的匹配。

这个两阶段过程导致许多人 - 包括很有经验的技术人员 - 低估了去中心化平台的潜力。

### **互联网的下一时代**

**去中心化网络并不是一个能够解决互联网上所有问题的万能灵药。**但是，它们可以提供比中心化系统解决问题更好的方法。

我们可以比较一下垃圾推文和垃圾邮件的问题。自从Twitter关闭了第三方开发者的入口后，唯一能向用户发送垃圾推文的公司其实一直是Twitter本身。相比之下，有数百家企业试图通过数十亿美元的风险投资和企业融资致力于开发过滤垃圾邮件的业务。虽然过滤垃圾邮件尚未解决，但现在的情况已经有所改善，因为第三方开发者知道电子邮件协议是去中心化的，所以他们可以在此基础上建立业务，而不用担心后期这些规则会改变。

或者我们也可以考虑网络治理问题。如今，决定信息排名和过滤的往往是大型平台上那些不负责任的员工们，例如哪些用户该升级，哪些用户该禁止，以及其他重要的治理决策。在加密网络上，这些决策由社区制定，并且使用完全公开和透明的机制。正如我们的线下世界，民主制度虽不完美，但比其他替代方案要好得多。

中心化平台长时间地占据着主导地位，以至于许多人忘记了建立互联网服务还有更好的方法。**加密网络是一种以社区为主导的强大网络，还为第三方开发人员，创业者和企业提供了一个公平的竞争环境。**在互联网的第一个时代，我们看到了去中心化系统的价值。希望在互联网的下一个时代，我们会再次遇见它。


# 特别篇

## 不止于APN

## APN 与移动网络的连接流程（简化版）

1. 手机开启移动数据 → 向运营商网络发送连接请求，附带 APN 配置。
2. 运营商的核心网（SGSN/MME）收到 APN → 通过 DNS 解析找到对应的网关（GGSN/PGW）。
3. 网关根据 APN 决定：
    * 连接公网互联网（普通上网）
    * 连接企业专网（私有 APN）
    * 分配 IP、QoS（服务质量）、计费规则等

连接成功 → 手机获得 IP 地址，开始上网。

| 作用             | 说明                                                                 |
|------------------|----------------------------------------------------------------------|
| 标识接入路径     | 告诉运营商的网关（GGSN/PGW）设备要连接哪个外部网络（如互联网、MMS、WAP、企业专网等） |
| 分配 IP 地址     | 决定设备获得公网 IP 还是私网 IP，以及 IP 地址类型（动态/静态）       |
| 决定服务类型     | 区分普通上网、MMS、多媒体消息、定位服务等                           |
| 控制安全与路由   | 私网 APN 可实现数据直连企业内网、加密传输、防火墙隔离等             |
| 运营商区分       | 每个运营商的 APN 不同（如中国移动常用 cmnet、cmwap，中国联通 3gnet、uniwap，中国电信 ctnet、ctwap） |

没有正确的 APN 配置 → 无法使用移动数据（即使信号满格）。APN 是移动网络数据服务的“入口”，直接决定了设备能访问什么网络、速度、安全性、计费方式。大多数情况下，插入 SIM 卡后手机会自动配置正确的 APN（运营商推送），但换卡、换设备、用物联网卡、去国外漫游、需要专网时，可能需要手动设置或修改。

## 两张不同的网络传递

固定宽带网络

```mermaid
graph LR
    A[电脑] --> B[网线/Wi-Fi];
    B --> C[路由器];
    C --> D[光猫];
    D --> E[光纤];
    E --> F[运营商机房];
    F --> G[互联网];
    
    style A fill:#e1f5fe
    style G fill:#f1f8e9
```

移动通信网络

```mermaid
graph LR
    A[电脑带移动模块] --> B[无线信号];
    B --> C[基站];
    C --> D[移动核心网];
    D --> E[互联网];
    
    style A fill:#ffe0e0
    style C fill:#fff3e0
```

## 架构梳理

电脑、手机通过有线网络上网的完整技术架构图，涵盖了从设备到互联网的全过程

```mermaid
flowchart TD
    subgraph UserZone["用户区域"]
        direction LR
        Device1["电脑/智能设备操作系统网络栈"]
        Device2["智能手机双模：Wi-Fi+蜂窝"]
    end
    
    %% ========== 路径1：有线网络 ==========
    Device1 -->|"路径①: 有线网络以太网帧/RJ45接口"| WiredPath
    
    subgraph WiredPath["有线接入路径"]
        Router1["家庭/企业路由器NAT/DHCP/防火墙"]
        Modem["光猫/调制解调器光电转换"]
    end
    
    Router1 -->|"网线PPPoE/DHCP"| Modem
    
    %% ========== 路径2：Wi-Fi网络 ==========
    Device1 & Device2 -->|"路径②: Wi-Fi连接802.11ac/ax协议"| WiFiAP["Wi-Fi接入点/路由器"]
    
    WiFiAP --> Router1
    
    %% ========== 路径3：移动数据网络 ==========
    Device2 -->|"路径③: 移动数据需SIM卡/USIM"| MobilePath
    
    subgraph MobilePath["移动网络路径"]
        Radio["手机射频模块"]
        BS["基站4G:eNodeB / 5G:gNB无线信号覆盖"]
        RAN["无线接入网基站控制器/汇聚"]
        MobileCore["移动核心网MME:移动管理 HSS:用户数据库SGW/PGW:数据网关"]
    end
    
    Radio -->|"无线信号LTE/NR协议"| BS
    BS --> RAN
    RAN --> MobileCore
    
    %% ========== 运营商网络汇聚 ==========
    Modem -->|"光纤/DSL线接入网"| ISP_A["运营商宽带接入网OLT/DSLAM"]
    MobileCore -->|"通过PGW连接"| ISP_B["运营商IP核心网"]
    
    ISP_A --> BRAS["宽带接入服务器BRAS认证/计费/分配IP"]
    ISP_B --> BRAS
    
    %% ========== 互联网与VPN ==========
    BRAS --> Internet["公共互联网Internet"]
    
    Internet --> Target["目标服务器网站/应用/服务"]
    
    %% ========== VPN叠加层 ==========
    subgraph VPNLayer["VPN安全隧道（可选）"]
        V_Client["设备VPN客户端"]
        V_Tunnel["加密隧道IPSec/OpenVPN/WireGuard"]
        V_Server["VPN服务器/网关"]
    end
    
    Device1 & Device2 --> V_Client
    V_Client --> V_Tunnel
    V_Tunnel --> V_Server
    V_Server --> Target
    
    %% ========== 关键协议栈 ==========
    subgraph ProtocolStack["关键协议栈（分层模型）"]
        P7["应用层HTTP/HTTPS/DNS"]
        P4["传输层TCP/UDP（端口）"]
        P3["网络层IP（IPv4/IPv6）/路由"]
        P2["数据链路层以太网/MAC/Wi-Fi/PPP"]
        P1["物理层光纤/网线/无线电波"]
    end
    
    ProtocolStack -.->|"每层对应不同设备"| UserZone
    
    %% ========== 特殊连接方式 ==========
    subgraph SpecialPaths["特殊连接方式"]
        SP1["手机USB共享网络手机作为调制解调器"]
        SP2["蓝牙网络共享PAN"]
        SP3["卫星互联网Starlink等"]
    end
    
    SP1 -->|"USB RNDIS协议"| Device1
    SP2 --> Device1
    SP3 -->|"卫星信号"| Satellite["卫星终端"]
    Satellite --> Internet
    
    %% ========== 认证与标识 ==========
    subgraph AuthSystem["认证与标识系统"]
        Auth1["有线/Wi-Fi认证:PPPoE/802.1X/密码"]
        Auth2["移动网络认证:SIM卡(IMSI/Ki)/5G-AKA"]
        Auth3["IP地址分配:公网IP/CGNAT私网IP"]
    end
    
    Auth1 --> BRAS
    Auth2 --> MobileCore
    Auth3 --> BRAS
    
    %% ========== 设备标识 ==========
    subgraph DeviceID["设备唯一标识"]
        ID1["MAC地址数据链路层"]
        ID2["IP地址网络层"]
        ID3["IMSI（SIM卡）移动网络"]
    end
    
    ID1 --> Device1
    ID2 --> Device1
    ID3 --> Device2

    %% ========== 样式美化 ==========
    classDef user fill:#e3f2fd
    classDef wired fill:#e8f5e8
    classDef mobile fill:#fff3e0
    classDef isp fill:#f3e5f5
    classDef internet fill:#e8eaf6
    classDef vpn fill:#ffebee
    classDef protocol fill:#f5f5f5
    classDef special fill:#fff8e1
    
    class UserZone,Device1,Device2 user
    class WiredPath,Modem,WiFiAP wired
    class MobilePath,Radio,BS mobile
    class ISP_A,ISP_B,BRAS isp
    class Internet,Target internet
    class VPNLayer vpn
    class ProtocolStack,AuthSystem,DeviceID protocol
    class SpecialPaths,SP1,SP2,SP3 special
```


## 最後のTag

24岁那年，我的高级工程师证变成了废纸，不过放现在成了厕纸，可类比为 80S 的中专...考到大厂里高级工程师证书的那天，我拍了照发朋友圈，配文是“熬出来了”。当时自以为是觉得自己终于攒够了“不可替代”的筹码，以为从此能喘口气，不用再像30多岁时那样年年担心被优化。结果没过两年，公司来了新一轮“组织优化”。

我开始怀疑这些年到底在卷什么。在校拼命学编程，毕业后996桌面运维，周末自学新技术，熬夜做开源项目，攒钱，写博客，考证……我一度以为“只要技术够硬，就不会被抛弃”。后来才明白，在大部分中国工厂和传统大厂的职场里，真正决定你能不能留下的排序大概是这样的：

1. 你能不能让领导觉得“没有你不行”
1. 你会不会来事、会不会汇报、会不会站队
1. 你技术到底有多牛

而我常年排在第三位，甚至连第二位都没及格。

最讽刺的是，那些同期入职、代码写得稀烂、文档都懒得写的同事，反而活得更滋润。他们擅长在周会上讲PPT、擅长在茶水间传递情绪价值、擅长在关键时刻出现在领导视线里。他们被裁的风险，比我低得多。我不是在酸，我是真的困惑：

1. 为什么热爱写代码、愿意把周末贡献给开源的人，到最后反而成了最容易被替换的那一拨？
1. 为什么真正“吃香”的，是那些把人际关系玩得炉火纯青的人？

亲身经历两过裁员，我不再相信“有一份长久的工作”这种鬼话了。

以前总觉得稳定是努力的副产品，现在才看清：稳定从来不是靠技术堆出来的，而是靠“被需要”的感觉堆出来的。而“被需要”这四个字，技术只能占30%，剩下70%是人情、是包装、是站位、是运气。

现在我心态已经躺平了，做什么都好，做零工也好、回老家开个小店也好……只要别再让我相信“只要我再卷一点就能安全”这种幻觉就行。

热爱是奢侈品，生存才是必需品。我把热爱暂时收起来了，等哪天活得稳一点，再慢慢捡回来。

我们这代人，正像日本泡沫破灭后的那一代——以为努力卷技能、攒经验，就能换来一辈子的安稳饭碗，结果时代一转弯，一切都变了味。


# 科学普及

## 软件互联协议

软件使用网络协议取向：

* 客户端间歇性的发起无状态的查询且允许发生延迟，使用http/https，如：浏览器
* 客户端和服务器都可独立发包的情况下： 
    * 可容忍延迟但对数据来说一个字节都不能改变，使用tcp，如：在线斗地主
    * 有实时性要求，准许部分字节错误，但不能容忍延迟，使用udp，如：即时动作类游戏

TCP/IP协议拓扑图

<!-- ![](https://ipfs.io/ipfs/QmWu85jmMDSfWNRDtX2JrtRtkqpWDvAWj9XQhXmY85p6Bv?0.png) -->

![](https://i.postimg.cc/RhB8t1rj/171651525642888.png)

所以VPN能连接TCP与UDP协议，是因为虚拟网卡以及其生成的IP比TCP与UDP更为底层；sock处于OSI模型中的会话层，负责在数据传输中设置和维护电脑网络中两台电脑之间的通信连接，并不关心是何种应用协议，以至于sock代理不能互联用于其他协议的软件。典型的例子：v2ray需要switchyomega在表示层做中继代理打开被封锁的站点。

由于游戏外挂使用Socks代理的也较多，为了防止外挂，封禁也是最立竿见影的办法，Proxifer这类转换网络协议的软件也卻遭到鱼池之殃；当然，最好的办法还是刷梅林路由器，路由器本身就是小型linux系统，因此可以从物理层的路由器内嵌SS转发UDP，因为外挂识别主要针对PC操作系统而不是路由器，所以并不会被游戏厂商认为是外挂。


## DNS劫持与污染

## DNS

域名是Internet上某一台计算机或计算机组的名称，用于数据传输时标识计算机的电子方位，有时也指地理位置。域名是由一串用点分隔的名字组成的，通常包含组织名，而且始终包括两到三个字母的后缀，以指明组织的类型或该域所在的国家或地区。

DNS是计算机域名系统 \(Domain Name System 或Domain Name Service\) 的缩写，它是由域名解析器和域名服务器组成的。域名服务器是指保存有该网络中所有主机的域名和对应IP地址，并具有将域名转换为IP地址功能的服务器。其中域名必须对应一个IP地址，一个IP地址可以有多个域名，而IP地址不一定有域名。域名系统采用类似目录树的等级结构。

域名服务器通常为客户机/服务器模式中的服务器方，它主要有两种形式：

* 主服务器和转发服务器
* 将域名映射为IP地址的过程就称为“域名解析”

## DNS劫持

通过劫持DNS服务器，通过某些手段取得某域名的解析记录控制权，进而修改此域名的解析结果，导致对该域名的访问由原IP地址转入到修改后的指定IP，其结果就是对特定的网址不能访问或访问的是假网址，从而实现窃取资料或者破坏原有正常服务的目的。DNS劫持通过篡改DNS服务器上的数据返回给用户一个错误的查询结果来实现的；[具体详情请参考此搜索链接](https://www.google.com/search?newwindow=1&ei=dljzWqzhDNCYsAfUwKewAQ&q=%E5%8A%9F%E5%A4%AB%E7%BD%91%E5%8E%9F%E7%90%86%E4%B8%8D%E9%9D%A0%E8%B0%B1%E7%9A%84DNS&oq=%E5%8A%9F%E5%A4%AB%E7%BD%91%E5%8E%9F%E7%90%86%E4%B8%8D%E9%9D%A0%E8%B0%B1%E7%9A%84DNS&gs_l=psy-ab.3...76416.76416.0.76712.1.1.0.0.0.0.0.0..0.0....0...1c.1.64.psy-ab..1.0.0....0.vXslcuUhfQQ)。

综上所述，因此手动修改DNS是能实现防止域名劫持的。

## DNS污染

通常的DNS查询没有任何认证机制，而且DNS查询通常基于的UDP是无连接不可靠的协议，非常容易被篡改，通过对UDP端口53上的DNS查询进行入侵检测，GFW发现与关键词相匹配的请求则立即伪装成目标域名的解析服务器给查询者返回虚假结果。因此也被称为DNS欺骗或叫投毒。由于巨量的IP请求被GFW的DNS污染分别指向各个不同IP让其各项资源快速耗尽，导致正常用户无法访问，致使部分网站屏蔽中国IP而防止这种DDoS攻击。从DNS服务器端投毒，所以手动改了DNS也没用，也有例外情况如下文。

通常情况下无论使用设置在中国大陆的DNS服务还是使用设置在外国的DNS服务，因为解析结果都需要穿过GFW，所以都会被GFW污染。但是仍有一些设置在中国大陆的小型DNS使用dnsmasq+stunnel+sniproxy等技术手段回避GFW的污染或是封IP并提供正常的结果。

[原理图来源](http://www.cnblogs.com/yanxinjiang/p/7486314.html)

<!-- ![](https://ipfs.io/ipfs/Qmdf4EHCYHXm9mQVZVwqknR9Apbw8jNLrtgQmQmte5Ncjf?1.png) -->

![](https://i.postimg.cc/cLTznNCB/95001.png)

## Host

Hosts是负责将主机名映射到相应的IP地址的文件，通常用于补充或取代网络中DNS的功能；与DNS不同，计算机的用户可以直接对hosts文件进行控制指定IP访问的网址。

Hosts文件本来是用来提高解析效率的。在进行DNS请求以前，系统会先检查自己的Hosts文件中是否有这个地址映射关系，如果有则调用这个IP地址映射，如果没有再向已知的DNS服务器提出域名解析。也就是说Hosts的请求级别比DNS高。当你的Hosts文件里面有对应的IP时，它就会直接访问那个IP，而不用通过DNS。

所以，当我们直接将SS分享之类的站点IP放入Hosts文件后，就可以跳过DNS的解析这一步直接就行，IP访问不受GFW的DNS污染干扰了，但封IP那就没辙了；如果是[CDN](https://baike.baidu.com/item/CDN) 的IP被封的话，则需要站点站长提供主IP地址，也可以说是真实IP添加进hosts即可。


## 数字证书攻防概述

## 数字证书

?> 推荐浏览 [阮一峰-数字签名是什么？](https://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature.html)

### 证书简介

公开密钥认证（英语：Public key certificate），又称数字证书（digital certificate）或身份证书（identity certificate）。是用于公开密钥基础建设的电子文件，用来证明公开密钥拥有者的身份。此文件包含了公钥信息、拥有者身份信息（主体）、以及数字证书认证机构（发行者）对这份文件的数字签名，以保证这个文件的整体内容正确无误。

拥有者凭着此文件，可向电脑系统或其他用户表明身份，从而对方获得信任并授权访问或使用某些敏感的电脑服务。电脑系统或其他用户可以透过一定的程序核实证书上的内容，包括证书有否过期、数字签名是否有效，如果你信任签发的机构，就可以信任证书上的密钥，凭公钥加密与拥有者进行可靠的通信。

### 弱点与防御

证书的弱点，一旦证书机构被入侵，黑客可以在人们不知情下签发了伪冒他人身份的证书，以中间人攻击进行欺诈。业界已研发不同的防御策略，例如证书机构公开新签发的电子证书，让大众检查手上收到的电子证书是否可能未被正式授权，网站管理员也可以定期检查是否有不明机构发出了未被授权的证书。另一方面，HTTPS网站也可以指明其固定的公钥，让中间人的欺诈证书无法使用。另外，可透过第三方用户安全软件检查证书是否有效。

> 摘抄自 [wiki-公开密钥认证](https://zh.wikipedia.org/wiki/%E5%85%AC%E9%96%8B%E9%87%91%E9%91%B0%E8%AA%8D%E8%AD%89)，并作了一定的大众化改写叙述，我个人建议是仔细阅读下维基

## SNI、RST

### 服务器名称指示（SNI）

大型网点通常会加入CDN加速的队伍满足用户秒开网页的需求，当用户访问某个网站，域名解析到距离用户最近的CDN服务器的公网IP，浏览器于是与公网IP对应的CDN服务器建立连接。CDN服务器一个公网IP，可能hosted多个客户网站（x.com,y.net,z.cn)。当浏览器主动连接时，CDN服务器如何知道是连接哪个客户网站呢？答案是SNI，用户输入a.com回车，CDN服务器可以根据SNI的值判定，用户原来想连接a.com，并建立这样的连接，把资源返回浏览器。

这也可以解释，为什么ping域名得到的IP无法访问该站点的问题。因为，用户不使用域名进行IP地址访问，但CDN服务器并不知道用户是想进入虚拟主机对应多个域名的哪一个，所以，就造成IP地址无法访问该站点的原因。

为了使SNI协议起作用，绝大多数访问者必须使用实现它的Web浏览器。使用未实现SNI浏览器的用户将被提供默认证书，因此很可能会收到证书警告。尽管SNI已经被多数浏览器和服务器支持，但目前现状还是会造成部分用户不兼容的现象。这个时候，可以选择我们多域名证书来完美解决这个问题。

由于SNI信息并非加密的，允许审查者区分出“真实”和“虚假”的服务或者识别出用户访问的网站域名。现已被中国用于互联网审查。当前，Cloudflare、Mozilla、Fastly和苹果的开发者已开始制定关于加密服务器名称指示（ESNI）的草案。

### TCP重置攻击

TCP重置攻击指的是使用伪造的TCP重置包干扰用户和网站的连接。因GFW识别SNI，运用这个技术进行TCP关键字阻断，将对站点进行TCP重置攻击，访问网页将出现此类 ERR_CONNECTION_RESET 异常。所以，就会出现这样的问题：我能ping通网站域名、IP地址，但就是访问不了网页。

使用[IPsec](https://zh.wikipedia.org/wiki/IPsec)进行安全数据源、与数据完整性认证等可以避免，因SNI被识别的域名，带来的TCP重置攻击。也有研究认为通过连接双方配置适当的过滤来丢弃用于阻断的重置包来也可以维持连接的创建。

连接重置是TCP协议的一种消息。一般来说，例如服务器端在没有客户端请求的端口或者其他连接信息不符时，系统的TCP协议栈就会给客户端回复一个RESET通知消息，可见连接重置功能本来用于应对例如服务器意外重启等情况。而发送连接重置包比直接将数据包丢弃要好，因为如果是直接丢弃数据包的话客户端并不知道具体网络状况，基于TCP协议的重发和超时机制，客户端就会不停地等待和重发。

### 域名前置

域前置（英语：Domain fronting），又译为域名幌子，是一种隐藏连接真实端点来规避互联网审查的技术。在应用层上运作时，域前置使用户能通过HTTPS连接到被屏蔽的服务，而表面上像在与另一个完全不同的站点通信。

此技术的原理为在不同通信层使用不同的域名。在明文的DNS请求和TLS服务器名称指示（SNI）中使用无害的域名来初始化连接、公布给审查者，而实际要连接的被封锁域名仅在创建加密的HTTPS连接后发出，使其不以明文暴露给网络审查者。

此技术利用审查者通常很难区分被伪装流量与合法流量的特点，迫使审查者选择放行所有看似无害的流量，或者选择彻底封锁此域的流量。而彻底封锁可能带来显著的附加损害。


## 代理上网准入检测实验

情景：按照代理软件默认的安装方式，登录帐号连接节点发现软件报错，并提示乱码，软件日志难以找到，去切实排查原因...第一想法是软件字符编码及兼容性问题，可win7、win10测试无效，即使设置了UTF-8编码，情况依旧；从以前经验想当然认为“乱码不影响使用（连接、功能逻辑操作）”，这个时候也是一头雾水。

![image-20201215112132923.png](https://i.loli.net/2020/12/15/MXQB5KS8s4UgnDi.png)

在这个时候联系了售后才了解到不能含特殊字符、空格的目录如常见的：

```cmd
C:\Program Files
C:\Program Files (x86)
```

....O__O "…，按照软件说明安装，登录连接服务器确实成功的。虽然连接成功，但访问Google还是被阻断了有些异常，联系了厂商客服，他们也表示他们的提供服务器没有问题，页面空白如下图现象...为了临时能让同事连接上网，使用ss连接依旧如此。（该图为过程复盘）

![Catch_12-03-11-39-37_.jpg](https://i.loli.net/2020/12/03/o81uC4zR6LipQYd.jpg)

然而在管理员主机这边却是可以的，这又是怎么回事呢？

![image-20201203114350647.png](https://i.loli.net/2020/12/03/QtNTdDCWUV4BAMO.png)

**初步了解**原来是上网帐号权限问题，管理员访问网站是不受限的；所带来的疑问点是为什么实验同学明明勾选了代理工具，但用代理工具却又访问不了Google这般类型的搜索页面呢？

防火墙对代理、VPN程序的协议识别机制有关，由于年限原因一些新型代理、VPN使用新型的协议导致无法识别相关的代理工具，也是存在这种可能性。

![2020-12-03_120742.png](https://i.loli.net/2020/12/03/K5FiSZtICswgycp.png)

**通过深入发现**设置LAN->WAN并制定端口范围的访问方式，限制代理、VPN翻墙。

![2020-12-03_121845.png](https://i.loli.net/2020/12/03/1PbhsDdxj3nKwQE.png)

不在上图中准入系统设置的端口范围内的实验同学，该同学代理界面节点端口信息如下。

![089EF.png](https://i.loli.net/2020/12/05/KI65dAZFyeWDaOm.png)

所以这就是此次访问异常的原因所在；泛泛来说，学校学生一般有百来个，不同专业班级也有十几个左右及以上，根据相关需求也得制定不同的上网规则。将上网规则集合在一起组成策略，将各组的上网行为规范应用于策略，极大方便了对校园学生的上网行为管理。

**浏览器页面的启用端口疑惑**

深信服访问准入设备的开放端口限制，浏览器所打开的各个站点是是否端口各不相同？于是参考[知乎-浏览器对于每个网页会使用不同的端口号吗？](https://www.zhihu.com/question/401686199)的两篇回答得出结论：

各个站点的网址服务器端口不会变，默认设置443、80，加端口号都是额外设置的；客户端，也就是我们的浏览器 ，本质上是启用多个独立程序打开相应所访问的多个页面，与此同时， 也就有了相应进程与多个端口。并不是访问各个网址的端口各不相同。

## 代理上网逻辑网络

大家对我校学生及组织难以理解，也是，那么我就以毕业的社会人视角比方吧，最开始用户是通过互联网联系到能够直连外网的代理商访问外网

![image-20201203142709439.png](https://i.loli.net/2020/12/03/4kM5mL2Dyv9IWhQ.png)

用户与代理商双方建立连接关系，也是需要相互之间信任验证的，不建立信任验证，谁都可以建立连接就乱套了。于是就有了客户端与服务器端完成帐号登录与密码验证这一过程。建立信任关系后，代理商就如同用户的下手助理，接代用户的意愿去完成一系列的行为操作。

代理上网拓扑流程如下：

![image-20201203162752377.png](https://i.loli.net/2020/12/03/TjZLyhg1vBxuAVs.png)

### 附：网页代理原理

网页代理服务器又称为在线代理或者叫线上代理，是一种在网页上运行的代理服务器程序，其不用任何设置，输入网址选择好代理服务器便可以访问的优点已经成为时下最流行的代理访问方式。网页代理是常见的一种代理程序。网页代理给客户端提供远程网站上的网页和文件的高速缓存，使客户端可以更加快速安全的浏览远程网站。一些网页代理网站保持每天更新以保证速度。

浏览器客户端提交网址的时候，代理程序开始在当前服务器寻找远程网站的缓存网页和网站，找到目标网站后，代理程序马上将网站数据返回到用户的浏览器客户端；如果当前服务器没有该远程服务器的缓存，代理程序则会自动读取远程网站，将远程网站的资料提交给客户端，同时将资料缓存提供给下一次的浏览需求。

代理程序会根据缓存的时间、大小和提取记录自动删除缓存。删除的方法有两种，一种是删除保存最久的资料，一种是删除最少提取的缓存。这两种方法也可以结合使用。

![2018-05-10-192753.png](https://i.loli.net/2020/12/15/6TeZqCQ3c2gxous.png)


## VPN隧道协议

> 原文：[VPN隧道协议](https://blog.csdn.net/cymm_liu/article/details/16889457)&emsp;作者：[长眼慢慢](https://blog.csdn.net/cymm_liu)

**整理自网络：**

VPN \(虚拟专用网\)发展至今已经不在是一个单纯的经过加密的访问隧道了，它已经融合了访问控制、传输管理、加密、路由选择、可用性管理等多种功能，并在全球的 信息安全体系中发挥着重要的作用。也在网络上，有关各种VPN协议优缺点的比较是仁者见仁，智者见智，很多技术人员由于出于使用目的考虑，包括访问控制、 安全和用户简单易用，灵活扩展等各方面，权衡利弊，难以取舍;尤其在VOIP语音环境中，网络安全显得尤为重要，因此现在越来越多的网络电话和语音网关支 持VPN协议。

目前比较常见的VPN隧道协议有[PPTP VPN](http://web.xieshenglin.com/tag/pptp-vpn/)、[L2TP  VPN](http://web.xieshenglin.com/tag/l2tp-vpn/)、[OpenVPN](http://web.xieshenglin.com/tag/openvpn/)、[SSH代理](http://web.xieshenglin.com/tag/ssh/)等多种协议选择，可在不同的平台和环境下使用。每一种协议均有独特的功能和优势。在选择使用哪种协议时，需要考虑你的设备支持什么协议，在安全性和速度之间权衡，以及有没有协议被你的网络阻塞。

PPTP、L2TP、OpenVPN三种隧道协议的优缺点对比：（SSH不列入比较）：

* 易用性：
    * PPTP &gt; L2TP &gt; OpenVPN

* 速度：
    * PPTP &gt; OpenVPN UDP &gt; L2TP &gt; OpenVPN TCP

* 安全性：
    * OpenVPN &gt; L2TP &gt; PPTP

* 稳定性：
    * OpenVPN &gt; L2TP &gt; PPTP

* 网络适用性：
    * OpenVPN &gt; PPTP &gt; L2TP

下面简单介绍下PPTP、L2TP、OpenVPN、SSH协议的特点：

1. PPTP VPN协议

    PPTP协议是点对点隧道协议，其将TCP控制包与数据包分开，适合在没有墙限制的网络中使用。

2. L2TP VPN协议

    L2TP是国际标准隧道协议，它结合了PPTP协议以及第二层转发L2F协议的优点，能以隧道方式使PPP包通过各种网络协议，包括ATM、SONET和帧中继。但L2TP没有任何加密措施，更多是和IPSec协议结合使用提供隧道验证。

    支持PPTP的设备基本都支持L2TP，设置略复杂，需要选择L2TP/IPSec PSK方式且设置预共享密钥PSK

    L2TP使用UDP协议，一般可穿透防火墙，适合在有防火墙限制的局域网用户，如公司、网吧、学校场合等使用；PPTP和L2TP二个连接类型在性能上差别不大，如果使用PPTP不正常，那就更换为L2TP。

3. OpenVPN隧道协议

    OpenVPN是一个基于SSL加密的纯应用层VPN协议，是SSL VPN的一种，支持UDP与TCP两种方式。UDP和TCP是2种通讯协议，这里通常UDP的效率会比较高，速度也相对较快。所以尽量使用UDP连接方式，实在UDP没法使用的时候，再使用TCP连接方式。

    由于其运行在纯应用层，避免了PPTP和L2TP在某些NAT设备后面不被支持的情况，并且可以绕过一些网络的封锁（通俗点讲，基本上能上网的地方就能用OpenVPN）。

    OpenVPN客户端软件可以很方便地配合路由表，实现不同线路（如国内和国外）的路由选择，实现一部分IP走VPN，另一部分IP走原网络。

    目前已被GFW用流量特征识别等技术手段侦测并受到严重封杀

4. SSH隧道协议

    SSH原本用于UNIX类系统的远程登录和管理。由于SSH可以通过客户端软件，在本地做一个SOCKS代理进行加密转发，因此也被用于网络代理。

    一些人喜欢用SSH的代理，配合浏览器插件（如Firefox的AutoProxy，Chrome的Switchy）和自动列表，可实现对不同网址有选择性地代理。


## 科学上网原理

> 原文：[科学上网原理](https://segmentfault.com/a/1190000011485579)&emsp;作者：[Pines_Cheng](https://segmentfault.com/u/pines_cheng)

## 背景

在很久很久以前，我们访问各种网站都是简单而直接的，用户的请求通过互联网发送到服务提供方，服务提供方直接将信息反馈给用户。

<!-- ![](https://ipfs.io/ipfs/QmS6LwXYMGw8mtY4sMrnbtsNVSwbUfAQG6uuQiJwcqf95p?1.png) -->

![](https://i.postimg.cc/Kj0bfpD6/whats-shadowsocks-01.png)

后来，[GFW](https://zh.wikipedia.org/wiki/%E9%98%B2%E7%81%AB%E9%95%BF%E5%9F%8E) 就出现了，他像一个收过路费的强盗一样夹在了在用户和服务之间，每当用户需要获取信息，都经过了 GFW，GFW将它不喜欢的内容统统过滤掉，于是客户当触发 GFW 的过滤规则的时候，就会收到 `Connection Reset` 这样的响应内容，而无法接收到正常的内容。

<!-- ![](https://ipfs.io/ipfs/QmZU3aC45PRKweNYxbtN1Dn69nEMmw5Cfs1MitiXHBF4TS?2.png) -->

![](https://i.postimg.cc/gcS1MhWb/whats-shadowsocks-02.png)

GFW 内部结构：

<!-- ![](https://ipfs.io/ipfs/QmWuT9BfsYt9efzir5mYUck46gL92FfXS6VzAT1hHQr3Yi?0.jpg) -->

![](https://i.postimg.cc/NGzP8w6g/fiyya.jpg)

GFW 列表可以参考这里：[gfwlist](https://github.com/gfwlist/gfwlist)

<!-- ![](https://ipfs.io/ipfs/QmX2kmam3QVEBESZvKFi6kST23BAbXzsNqBhz4eUKsWkPn?1.png) -->

![](https://i.postimg.cc/Vs2PftHB/image.png)

聪明的人们想到了利用境外服务器代理的方法来绕过 GFW 的过滤，其中包含了各种HTTP代理服务、Socks服务、VPN服务等。

## SSH Tunnel

SSH（Secure Shell）是一个提供数据通信安全、远程登录、远程指令执行等功能的安全网络协议，由芬兰赫尔辛基大学研究员Tatu Ylönen，于1995年提出，其目的是用于替代非安全的Telnet、rsh、rexec等远程Shell协议。之后SSH发展了两个大版本SSH-1和SSH-2。

想深入了解SSH的原理，可以查看 O‘RELLY的 [《SSH: The Secure Shell - The Definitive Guide》](http://openyoudao.org/_media/ssh_second_edition.pdf)，这是一本非常不错的书。

那么我们来看看搭建一个SSH隧道翻墙，究竟有多简单。首先你需要有一台支持SSH的墙外服务器，此服务器啥都不需要，只要能SSH连接即可。

客户端SSH执行如下命令：

```text
ssh -D 7001 username@remote-host
```

上述命令中-D表示动态绑定，7001表示本地SOCKS代理的侦听端口，可以改成别的，后面的 `username@remote-host`就是你登录远程服务器的用户名和主机。当然，这个命令后会提示输入密码，就是username这个用户的密码（除非你配置了SSH公钥认证，可以不输入密码），这样隧道就打通了。

<!-- ![](https://ipfs.io/ipfs/QmZK59U5PoQgKjuBTA1PmXwfo8xzkCwsY3DnpARtETUvh9?3.png) -->

![](https://i.postimg.cc/85rwt7BN/whats-shadowsocks-03.png)

1. 首先用户和境外服务器基于 ssh 建立起一条加密的通道 \(1\)
2. 用户通过建立起的隧道进行代理，通过 ssh server 向真实的服务发起请求 \(2-3\)
3. 服务通过 ssh server，再通过创建好的隧道返回给用户 \(4-5\)

由于 ssh 本身就是基于 [RSA 加密技术](https://zh.wikipedia.org/wiki/RSA%E5%8A%A0%E5%AF%86%E6%BC%94%E7%AE%97%E6%B3%95)，所以 GFW 无法从数据传输的过程中的加密数据内容进行关键词分析，避免了被重置链接的问题，但由于创建隧道和数据传输的过程中，ssh 本身的特征是明显的，所以 GFW 一度通过分析连接的特征进行干扰，导致 ssh 存在被定向进行干扰的问题。

至于干扰的原理，shadowsocks的作者 [@clowwindy](https://github.com/clowwindy) 认为：

> 从[校长](https://zh.wikipedia.org/wiki/%E6%96%B9%E6%BB%A8%E5%85%B4)最近的论文上上看，GFW 最近弄的是先检测首部特征判断 SSL 和 SSH，然后统计包长度和方向，用实现训练好的模型去判断承载的流量是否为 HTTP。如果你用 SSH 翻墙，或者你的操作行为发的数据包过于接近 HTTP，就会被 reset。反过来，如果你想用 SSH 翻墙，只要在用来翻墙的那个 ssh 连接里做些别的操作（比如反复 tail 一个长文件，这样会不停的输出；或者用管道不停的往 ssh 里写命令，这样会不停的输入），就可以让这个模型失效，从而不会被判定为翻墙。

## VPN

随着时代的发展以及企业规模的发展壮大，企业网络也在不断发生变化。例如，一家总部设在北京的企业，可能会在上海、广州和深圳等地都设有分支机构，因此需要把各个分支机构连接在一起，以便共享资源、协同工作，提高工作效率。但传统的专线联网方式价格昂贵，一般中小企业难以负担。这时低成本的VPN技术就孕育而生了。`VPN（Virtual Private Network）`即`虚拟专用网络`，它可以利用廉价接入的公共网络（主要使用Inter-net）来传输私有数据，相较于传统的专线连网方式具有成本优势，因此被很多企业和电信运营商采用。

VPN 比shadowsocks更加底层，它通过操作系统的接口直接虚拟出一张网卡，后续整个操作系统的网络通讯都将通过这张虚拟的网卡进行收发。这和任何一个代理的实现思路都差不多，应用层并不知道网卡是虚拟的，这样vpn虚拟网卡将以中间人的身份对数据进行加工，从而实现各种神奇的效果。具体来说，vpn是通过编写一套网卡驱动并注册到操作系统实现的虚拟网卡，这样数据只要经过网卡收发就可以进行拦截处理。

<!-- ![](https://ipfs.io/ipfs/QmR3HHgE8LKyyAvAhy93D2UxdeRPJv62PzBvTZDVZQqbhP?2.png) -->

![](https://i.postimg.cc/NFDX4tVQ/2018-05-28-163626.png)

VPN和SSH隧道翻墙有如下区别：

* VPN的设置是全局的，即电脑一旦挂上VPN，所有的联网程序都将自动使用VPN；而建立好SSH隧道后，需要程序设定使用隧道才会使用隧道联网。
* 如果使用商用的VPN一般要花钱，如果自己搭，VPN的搭建难度大于SSH隧道。因为SSH隧道只要一台可以SSH的服务器即可，根本不需要在服务器上配置任何东西。
* vpn在IP层工作，而shadowsocks在TCP层工作。

## shadowsocks

简单理解的话，shadowsocks 是将原来 ssh 创建的 Socks5 协议拆开成 server 端和 client 端，所以下面这个原理图基本上和利用 ssh tunnel 大致类似。

<!-- ![](https://ipfs.io/ipfs/QmU3iBDrP1R72ZKrKHP5QBQ7K33vPPNssQsSxzUBvdvYyF?0.png) -->

![](https://i.postimg.cc/9MWFB9jq/whats-shadowsocks-04.png)

* 1、6\) 客户端发出的请求基于 Socks5 协议跟 ss-local 端进行通讯，由于这个 ss-local 一般是本机或路由器或局域网的其他机器，不经过 GFW，所以解决了上面被 GFW 通过特征分析进行干扰的问题
* 2、5\) ss-local 和 ss-server 两端通过多种可选的加密方法进行通讯，经过 GFW 的时候是常规的TCP包，没有明显的特征码而且 GFW 也无法对通讯数据进行解密
* 3、4\) ss-server 将收到的加密数据进行解密，还原原来的请求，再发送到用户需要访问的服务，获取响应原路返回

## PAC

`代理自动配置（Proxy auto-config，简称PAC）` 是一种网页浏览器技术，用于定义浏览器该如何自动选择适当的代理服务器来访问一个网址。

一个PAC文件包含一个JavaScript形式的函数 `FindProxyForURL(url, host)`。这个函数返回一个包含一个或多个访问规则的字符串。用户代理根据这些规则适用一个特定的代理其或者直接访问。当一个代理服务器无法响应的时候，多个访问规则提供了其他的后备访问方法。浏览器在访问其他页面以前，首先访问这个PAC文件。PAC文件中的URL可能是手工配置的，也可能是是通过网页的 `网络代理自发现协议（Web Proxy Autodiscovery Protocol）` 自动配置的。

上面是从维基百科摘录的关于PAC的解释，我做了一个简单的图片解释什么是PAC：

<!-- ![](https://ipfs.io/ipfs/QmWz6Q97MWa5mKZeBR8tbikczwkjr1ULKwigC6zkZAoY4C?2.png) -->

![](https://i.postimg.cc/MHgSgMg5/yEvu2aF.png)

简单的讲，PAC就是一种配置，它能让你的浏览器智能判断哪些网站走代理，哪些不需要走代理。点击 Shadowsocks 的菜单，选择 `编辑自动模式的 PAC`，如下图

<!-- ![](https://ipfs.io/ipfs/QmcxE9dbPLTCbmSKxFvLvCBHQ9dQCpaLt8dxTJUqqEk5PK?3.png) -->

![](https://i.postimg.cc/9Xs06rds/1nkq1h.png)

<!-- ![](https://ipfs.io/ipfs/QmYArbNR1F6paD6Zutp5Fvpb3YewCwwyroNNndyLpGKryX?4.png) -->

![](https://i.postimg.cc/PxphyQRJ/18ie14.png)

在上面的目录下有两个文件，一个是 gfwlist.js，还有一个是   
user-rule.txt,确保当前的模式为自动代理模式，打开系统设置--&gt;网络，点击高级，查看代理选项卡，如下图

<!-- ![](https://ipfs.io/ipfs/QmdCqRf9CdE9ZzuPidsuPFdpiRmUgpW2eLnsSqd1rX8MsJ?2.png) -->

![](https://i.postimg.cc/mgmsGnxh/13p1u.png)

## SS全局模式与PAC模式的区别 

Shadowsocks 的全局模式，是设置你的系统代理的代理服务器，使你的所有http/socks数据经过代理服务器的转发送出。而只有支持 socks 5或者使用系统代理的软件才能使用 Shadowsocks（一般的浏览器都是默认使用系统代理）。

而PAC模式就是会在你连接网站的时候读取PAC文件里的规则，来确定你访问的网站有没有被墙，如果符合，那就会使用代理服务器连接网站，而PAC列表一般都是从 GFWList 更新的。GFWList 定期会更新被墙的网站（不过一般挺慢的）。

简单地说，在全局模式下，所有网站默认走代理。而PAC模式是只有被墙的才会走代理，推荐PAC模式，如果PAC模式无法访问一些网站，就换全局模式试试，一般是因为PAC更新不及时（也可能是GFWList更新不及时）导致的。

还有，说一下Chrome不需要 `Proxy SwitchyOmega` 和 `Proxy SwitchySharp` 插件，这两个插件的作用就是，快速切换代理，判断网站需不需要使用某个代理的（shadowsocks已经有pac模式了，所以不需要这个）。如果你只用shadowsocks的话，就不需要这个插件了！

经过代理服务器的IP会被更换。连接 Shadowsocks 需要知道IP、端口、账号密码和加密方式。但是Shadowsocks因为可以自由换端口，所以定期换端口就可以有效避免IP被封！

## Socks代理和http代理的区别 

**Socks代理**

本地浏览器SOCKS服务器通常是用来做代理的，它通过TCP连接把目标主机和客户端连接在一起， 并转发所有的流量。SOCKS代理能在任何端口，任何协议下运行（额，好想有点不对， 这货是运行在session层，所以在他之下的层他就无法代理了）。SOCKS V4只支持 TCP连接，而SOCKS V5在其基础上增加了安全认证以及对UDP协议的支持（也就是说， SOCKS5支持密码认证以及转发UDP流量，注意，HTTP是不支持转发UDP的）。

SOCKS代理在任何情况下都不会中断server与client之间的数据（这是由这种协议的 特性决定的，毕竟非明文，但是在SOCKS代理服务器上还是可以还原出TCP和UDP的原始 流量的），当你的防火墙不允许你上网的时候，你就可以通过SOCKS代理来上网（这里的 意思是，如果GFW把google屏蔽了，你就可以通过一台海外的SOCKS代理服务器上谷歌）。

大多数的浏览器都支持SOCKS代理（这篇文章是三年前的，抱歉，谷歌第一条就是它）。（ 浏览器上网的时候需要与目标主机建立TCP连接，这个时候浏览器就会告诉SOCKS代理，它想 与目标主机进行通讯，然后SOCKS代理就会转发浏览器的数据，并向目标主机发出请求，然 后再把返回的数据转发回来。）（关于shadowsocks的一点题外话：虽然github上的源码 没了，但是耐不住民间私货多呀。shadowsocks有server端和client端，这两个都是用 来转发数据的，但是由于其所处的位置不同，所以功能也不同，client即本地运行的程序， 监听1080端口，并将数据转发到远在他乡的SOCKS服务器，由于这种转发是加密的，在会话层， 所以GFW过滤的难度很大，所以才派人巴拉巴拉让作者删除源码，嗯，一定是这样的。然后server 那边收到数据后，会原原本本的把数据再向目标请求，收到反馈后再返回给本地client的1080端口， 这样，我们向本地的1080请求资源，本地向SOCKS服务器请求资源，SOCKS服务器向目标请求资源， 这一条TCP连接就这样建立起来了。）但是，但是，但是，SOCKS代理原则上是可以还原真实数据的， 所以，第三方的代理也许不是很可靠。

**HTTP代理**

HTTP代理跟上面原理类似，用处也基本相同，都是让处于防火墙下的主机与外界建立连接，但是它与SOCKS代理不同的是，HTTP代理可以中断连接（即在中间截断数据流），因为HTTP代理是以HTTP请求为基础的 而这些请求大多以明文形式存在，所以HTTP代理可以在Client和下游服务器中间窃听，修改数据。但也正 由于HTTP代理只能处理HTTP请求，所以它对HTTP请求的处理也是很舒服的（原文中是smart）。而也由于 HTTP代理可以获取你的HTTP请求，所以HTTP代理服务器那边就可以根据你提交的数据来把那些资源缓存下来，提升访问的速度（用户亲密度+1）。有好多ISP都用HTTP代理，而不管用户那边的浏览器是怎样配置的，因为不管用户们怎么配置，他们总是要访问80端口，而这些80端口们又掌握在ISP们的手中。（原文完全不是这样说的= =。原文是说，互联网提供商们把流量都通过了HTTP代理，这样代理服务器中就有了缓存，访问的速度会快一些。）

（我来举个栗子：假如你的HTTP代理是Goagent，监听本地127.0.0.1:8080，此刻假设你已经把浏览器 的代理设置为：127.0.0.1:8080，那么你在浏览器中，所有的POST，GET，以及其他的请求，都会通过 本地的代理转发给远程的服务器，然后再通过远程的服务器去请求你所请求的这些资源，大家知道，HTTP协议是通过明文传输的，无论是在本地还是远程的服务器上，都是可以监听到这些流量的，所以才会有GFW的存在……HTTP协议属于应用层，而SOCKS协议属于**传输层**，ps：传输层在网络层之下，这就决定了两者的能力大小。）

## 参考 

* [shadowsocks 源码阅读](https://0x01.io/2016/02/28/shadowsocks-%E6%BA%90%E7%A0%81%E9%98%85%E8%AF%BB/)
* [Shadowsocks 源码分析——协议与结构](https://loggerhead.me/posts/shadowsocks-yuan-ma-fen-xi-xie-yi-yu-jie-gou.html)
* [写给非专业人士看的 Shadowsocks 简介](https://vc2tea.com/whats-shadowsocks/)
* [SSH原理简介](http://erik-2-blog.logdown.com/posts/74081-ssh-principle)
* [RSA算法原理（一）](http://www.ruanyifeng.com/blog/2013/06/rsa_algorithm_part_one.html)
* [详解代理自动配置 PAC](http://www.barretlee.com/blog/2016/08/25/pac-file/)
* [科学上网漫游指南](https://lvii.gitbooks.io/outman/content/)
* [Socks代理和http代理的区别](https://wrfly.kfd.me/SOCKS%E4%BB%A3%E7%90%86%E5%92%8CHTTP%E4%BB%A3%E7%90%86%E7%9A%84%E5%8C%BA%E5%88%AB/)


## GFW原理和封锁技术

> 原文：[GFW原理和封锁技术](https://xuranus.github.io/2017/10/09/GFW%E5%8E%9F%E7%90%86%E5%92%8C%E5%B0%81%E9%94%81%E6%8A%80%E6%9C%AF)&emsp;作者：[XUranus](https://xuranus.github.io/)

GFW是Great Fire Wall的缩写，即“长城防火墙”。这个工程由若干个部分组成，实现不同功能。长城防火墙主要指TG监控和过滤互联网内容的软硬件系统，由服务器和路由器等设备，加上相关的应用程序所构成。

首先，需要强调的是，由于中国网络审查广泛，中国国内含有“不合适”内容的的网站，会受到政府直接的行政干预，被要求自我审查、自我监管，乃至关闭，所以GFW的主要作用在于分析和过滤中国境内外网络的资讯互相访问。GFW对网络内容的过滤和分析是双向的，GFW不仅针对国内读者访问中国境外的网站进行干扰，也干扰国外读者访问主机在中国大陆的网站。

## 一 关键字过滤阻断

关键字过滤系统。此系统能够从出口网关收集分析信息，过滤、嗅探指定的关键字。主要针对HTTP的默认端口：80端口，因为HTTP传播的内容是明文的内容，没有经过加密，而GFW是一个IDS(Intrusion detection system)。普通的关键词如果出现在HTTP请求报文的头部(如`Host: www.youtube.com`)时，则会马上伪装成对方向连接两端的计算机发送RST包(reset)干扰两者正常的TCP连接，进而使请求的内容无法继续查看。如果GFW在数据流中发现了特殊的内文关键词(如轮子，达赖等)时，其也会试图打断当前的连接，从而有时会出现网页开启一部分后突然停止的情况。在任何阻断发生后，一般在随后的90秒内同一IP地址均无法浏览对应IP地址相同端口上的内容。

## 二 IP地址封锁 

IP地址封锁是GFW通过路由器来控制的，在通往国外的最后一个网关上加上一条伪造的路由规则，导致通往某些被屏蔽的网站的所有IP数据包无法到达。路由器的正常工作方式是学习别的路由器广播的路由规则，遇到符合已知的IP转发规则的数据包，则按已经规则发送，遇到未知规则IP的数据，则转发到上一级网关。

而GFW对于境外(中国大陆以外)的XX网站会采取独立IP封锁技术。然而部分XX网站使用的是由虚拟主机服务提供商提供的多域名、单(同)IP的主机托管服务，这就会造成了封禁某个IP地址，就会造成所有使用该服务提供商服务的其它使用相同IP地址服务器的网站用户一同遭殃，就算是正常的网站，也不能幸免。其中的内容可能并无不当之处，但也不能在中国大陆正常访问。现在GFW通常会将包含XX信息的网站或网页的URL加入关键字过滤系统，并可以防止民众透过普通海外HTTP代理服务器进行访问。

## 三 特定端口封锁 

GFW会丢弃特定IP地址上特定端口的所有数据包，使该IP地址上服务器的部分功能(如SSH的22、VPN的1723或SSL的443端口等)无法在中国大陆境内正常使用。

在中国移动、中国联通等部分ISP\(手机IP段\)，所有的PPTP类型的VPN都被封锁。

2011年3月起，GFW开始对Google部分服务器的IP地址实施自动封锁(按时间段)某些端口，按时段对`www.google.com`(用户登录所有Google服务时需此域名加密验证)和`mail.google.com`的几十个IP地址的443端口实施自动封锁，具体是每10或15分钟可以连通，接着断开，10或15分钟后再连通，再断开，如此循环，令中国大陆用户和Google主机之间的连接出现间歇性中断，使其各项服务出现问题。GFW这样的封锁手法很高明，因为Gmail并非被完全阻断，这令问题看上去好像出自Google本身。这就是你们认为Google抽风的原因。

## 四 SSL连接阻断 
GFW会阻断特定网站的SSL加密连接，方法是通过伪装成对方向连接两端的计算机发送RST包(RESET)干扰两者间正常的TCP连接，进而打断与特定IP地址之间的SSL(HTTPS，443端口)握手(如Gmail、Google文件、Google网上论坛等的SSL加密连接)，从而导致SSL连接失败。

当然由于SSL本身的特点，这并不意味着与网站传输的内容可被破译。

## 五 DNS劫持和污染

GFW主要采用DNS劫持和污染技术，使用Cisco提供的IDS系统来进行域名劫持，防止访问被过滤的网站，2002年Google被封锁期间其域名就被劫持到百度。中国部分ISP也会通过此技术插入广告。

对于含有多个IP地址或经常变更IP地址逃避封锁的域名，GFW通常会使用此方法进行封锁。具体方法是当用户向DNS服务器提交域名请求时，DNS返回虚假\(或不解析\)的IP地址。

全球一共有13组根域名服务器\(Root Server\)，目前中国大陆有F、I这2个根域DNS镜像，但现在均已因为多次DNS污染外国网络，而被断开与国际互联网的连接。

DNS劫持和污染是针对某些网站的最严重的干扰。

干扰的方式有两种：

一种是通过网络服务提供商(Internet Service Provider)提供的DNS服务器进行DNS欺骗，当人们访问某个网站时，需要要把域名转换为一个IP地址，DNS服务器负责将域名转换为IP地址，中国大陆的ISP接受通信管理局的屏蔽网站的指令后在DNS服务器里加入某些特定域名的虚假记录，当使用此DNS服务器的网络用户访问此特定网站时，DNS服务便给出虚假的IP地址，导致访问网站失败，甚至返回ISP运营商提供的出错页面和广告页面。

另一种是GFW在DNS查询使用的UDP的53端口上根据blacklist进行过滤，遇到通往国外的使用UDP53端口进行查询的DNS请求，就返回一个虚假的IP地址。


## meek网桥的技术原理

> 转载自[网络](https://www.google.com/search?q=meek%E6%B5%81%E9%87%8F%E6%B7%B7%E6%B7%86&oq=meek%E6%B5%81%E9%87%8F%E6%B7%B7%E6%B7%86&aqs=chrome..69i57.7285j0j9&sourceid=chrome&ie=UTF-8)，并做了相应修改

首先，tor从使用者本机直到出口节点的传输是强加密的，别人无法偷窥你的真实网络流量。除非tor软件本身出现严重安全漏洞或者碰到的出口节点是[蜜罐](https://baike.baidu.com/item/%E8%9C%9C%E7%BD%90%E6%8A%80%E6%9C%AF/9165942?fromtitle=%E8%9C%9C%E7%BD%90&fromid=5390254)。

虽然无法偷窥你的真实上网内容，但是如果有ISP、GFW监控你的流量，可以判断出你在使用tor，判断流量类型不等于解密内容；而流量混淆把tor流量伪装成其它的上网流量，让监控者看不出你在用tor。

出于软件架构方面的考虑，流量混淆的功能不是做到tor的核心软件中，而是以插件的方式来提供。因为混淆流量的方式是多种多样的，用插件来扩展就无需频繁改动核心模块的代码。

在meek之前，tor开源社区已经出过好几款流量混淆插件。以obfsproxy为例：

<!-- ![](https://ipfs.io/ipfs/QmWbJAtptajEo98PHticEVyGDQewFyEYuq7hv6w9AbE8uh?3.png) -->

![](https://i.postimg.cc/bv8fkjQ6/2018-05-10-164713.png)

图中的tor client和obfsproxy client在你本机，他们要正常工作就需要先连接到obfsproxy server。虽然GFW无法区分被obfsproxy混淆过的流量，但是因为全球的obfsproxy server数量是有限的，GFW可以把所有的obfsproxy server都加入IP黑名单。如此一来，就足以让obfsproxy失效。  
  
meek client也是跟tor client

一起运行在你本机。下面这张是meek的示意图：

<!-- ![](https://ipfs.io/ipfs/QmRD4PGd2W2PotzuukKbMnbU5gHAijrnXzTxpCbUQT5fGq?1.png) -->

![](https://i.postimg.cc/XJJhkNXg/2018-05-10-171318.png)

从图中可以看出，meek跟obfsproxy的主要差异在于meek server 并不是直接暴露出来的。换句话说，你本机不需要直连meek server，而是直接连接云计算平台的服务器。如此一来，即便GFW知道meek server的IP，封杀这些IP也没有意义。

只因aws、azure云计算平台绑定国内各个公司业务较多，GFW又不敢轻易封杀。这就是meek插件可以突破GFW的关键所在。关于更多tor原理细节请搜索：[tor的常见问题解答](https://www.google.com/search?q=TOR+%E7%9A%84%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E8%A7%A3%E7%AD%94&oq=TOR+%E7%9A%84%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E8%A7%A3%E7%AD%94&aqs=chrome..69i57j69i60.535j0j7&sourceid=chrome&ie=UTF-8)


## VMware的3种网络模式

> 原文：[根本区别在哪里 VMware的3种网络模式](http://net.zol.com.cn/115/1158058.html)&emsp;作者：孙鹏

## 桥接模式

桥接网络是指本地物理网卡和虚拟网卡通过VMnet0虚拟交换机进行桥接，物理网卡和虚拟网卡在拓扑图上处于同等地位（虚拟网卡既不是Adepter VMnet1也不是Adepter VMnet8）。

桥接网络拓扑图

<!-- ![](https://ipfs.io/ipfs/QmaM994hn7RC2gT8qd3ubxqrTiURzsUrhYCwu2JJc68ERN?3.png) -->

![](https://i.postimg.cc/D0m3YyN6/2018-05-13-161016.png)

那么物理网卡和虚拟网卡就相当于处于同一个网段，虚拟交换机就相当于一台现实网络中的交换机。所以两个网卡的IP地址也要设置为同一网段。

物理网卡IP地址

<!-- ![](https://ipfs.io/ipfs/QmTksR6g9wBZptxJzXcVspXtzUppUFfSj9d5W2k74iGWv8?3.png) -->

![](https://i.postimg.cc/zBccvwdw/2018-05-13-161401.png)

虚拟网卡IP地址

<!-- ![](https://ipfs.io/ipfs/QmemKU954PgTQaBQ4jg3Wa8A7tk74wAAHf4XLEpMiqg1ZW?4.png) -->

![](https://i.postimg.cc/ZRHyxVk3/2018-05-13-161708.png)

我们看到，物理网卡和虚拟网卡的IP地址处于同一个网段，子网掩码、网关、DNS等参数都相同。两个网卡在拓扑结构中是相对独立的。

ping结果

<!-- ![](https://ipfs.io/ipfs/QmcwWPpLZXN7yU5KmPgA9pJNV3gPefNH3ot87GjDQxZUUp?3.png) -->

![](https://i.postimg.cc/Gpr2gGxj/2018-05-13-161826.png)

我们在192.168.15.111上ping192.168.15.96，结果显示两个网卡能够互相通信。如果在网络中存在DHCP服务器，那么虚拟网卡同样可以从DHCP服务器上获取IP地址。所以桥接网络模式是VMware虚拟机中最简单直接的模式。安装虚拟机时它为默认选项。

## NAT模式

在NAT网络中，会用到VMware Network Adepter VMnet8虚拟网卡，主机上的VMware Network Adepter VMnet8虚拟网卡被直接连接到VMnet8虚拟交换机上与虚拟网卡进行通信。

NAT网络模式拓扑图

<!-- ![](https://ipfs.io/ipfs/QmT4kUS8cMC7g9VoZMmro4rf3vjRc84f6MagkYuZQcmY3u?2.png) -->

![](https://i.postimg.cc/zvjZBHgq/2018-05-13-162012.png)

VMware Network Adepter VMnet8虚拟网卡的作用仅限于和VMnet8网段进行通信，它不给VMnet8网段提供路由功能，所以虚拟机虚拟一个NAT服务器，使虚拟网卡可以连接到Internet。在这种情况下，我们就可以使用端口映射功能，让访问主机80端口的请求映射到虚拟机的80端口上。

VMware Network Adepter VMnet8虚拟网卡的IP地址是在安装VMware时由系统指定生成的，我们不要修改这个数值，否则会使主机和虚拟机无法通信。

NAT虚拟网卡IP地址

<!-- ![](https://ipfs.io/ipfs/Qmd2KUrSiviXCv34mUha2dfV7MzSbGi9foPm5yiKK7ATF1?4.png) -->

![](https://i.postimg.cc/63JDffV9/2018-05-13-162216.png)

物理网卡IP地址

<!-- ![](https://ipfs.io/ipfs/QmXWg73AiRBuE5i2auxwPicmfYUwsnFd4GhbH1qGuhhDxi?3.png) -->

![](https://i.postimg.cc/sXLGL1XD/2018-05-13-162302.png)

虚拟出来的网段和NAT模式虚拟网卡的网段是一样的，都为192.168.111.X，包括NAT服务器的IP地址也是这个网段。在安装VMware之后同样会生成一个虚拟DHCP服务器，为NAT服务器分配IP地址。

当主机和虚拟机进行通信的时候就会调用VMware Network Adepter VMnet8虚拟网卡，因为他们都在一个网段，所以通信就不成问题了。

实际上，VMware Network Adepter VMnet8虚拟网卡的作用就是为主机和虚拟机的通信提供一个接口，即使主机的物理网卡被关闭，虚拟机仍然可以连接到Internet，但是主机和虚拟机之间就不能互访了。

## 仅主机模式

在Host-Only模式下，虚拟网络是一个全封闭的网络，它唯一能够访问的就是主机。其实Host-Only网络和NAT网络很相似，不同的地方就是Host-Only网络没有NAT服务，所以虚拟网络不能连接到Internet。主机和虚拟机之间的通信是通过VMware Network Adepter VMnet1虚拟网卡来实现的。

host-only模式拓扑图

<!-- ![](https://ipfs.io/ipfs/QmdsKse5xP3BRDMy7dGQPWmGNcCrFF9RVYtgyYzPVPqoE9?1.png) -->

![](https://i.postimg.cc/0yvnnXFX/2018-05-13-162359.png)

同NAT一样，VMware Network Adepter VMnet1虚拟网卡的IP地址也是VMware系统指定的，同时生成的虚拟DHCP服务器和虚拟网卡的IP地址位于同一网段，但和物理网卡的IP地址不在同一网段。

 Host-Only虚拟网卡IP地址

<!-- ![](https://ipfs.io/ipfs/QmeBhyZXNcraRFGp2evnAK74NRSYNpgKgeo2g5M26mG63g?2.png) -->

![](https://i.postimg.cc/8zwRHphs/2018-05-13-162504.png)

物理网卡IP地址

<!-- ![](https://ipfs.io/ipfs/QmUn6ZwscVPmigSNfxABezVX8A3Qeekqt7Ss4pDGYKGrR7?0.png) -->

![](https://i.postimg.cc/LXjhxDrv/2018-05-13-162617.png)

Host-Only的宗旨就是建立一个与外界隔绝的内部网络，来提高内网的安全性。这个功能或许对普通用户来说没有多大意义，但大型服务商会常常利用这个功能。如果你想为VMnet1网段提供路由功能，那就需要使用RRAS，而不能使用XP或2000的ICS，因为ICS会把内网的IP地址改为192.168.0.1，但虚拟机是不会给VMnet1虚拟网卡分配这个地址的，那么主机和虚拟机之间就不能通信了。

## 综述

在VMware的3中网络模式中，NAT模式是最简单的，基本不需要手动配置IP地址等相关参数。至于桥接模式则需要额外的IP地址，如果是在内网环境中还很容易，如果是ADSL宽带就比较麻烦，ISP一般是不会大方地多提供一个公网IP的。


## nat类型科普以及提升方法

> 原文：[NAT类型科普及一些简单提升NAT类型的方法](http://www.right.com.cn/forum/thread-199299-1-1.html)&emsp;作者：iSkyun

首先百度了解到什么是“[**NAT**](http://baike.baidu.com/item/nat)”，看了那么多我们大概也知其一些的基本知识，比如说[**定义**](http://baike.baidu.com/item/nat)、[**功能**](http://baike.baidu.com/item/nat#1)、[**实现方式**](http://baike.baidu.com/item/nat#2)及[**类型**](http://baike.baidu.com/item/nat#7)
  
提升NAT类型的好处：  

* 浏览网页、观看视频、游戏等更顺畅，下载速度更稳定快速，  
* 特别是对那些玩ED2K/PT下载、PS4/XBox主机游戏的，  
* 提升NAT类型后更有可能获取到HigtID、更容易进入游戏房间连线等。  
  
要提升NAT类型，我们必须知道NAT的4个类型它们分别对应：  

* **NAT1 **→ **Full Cone**&emsp;  NAT1这是最宽松的网络环境，你想做什么
* **NAT2 **→ **Address-Restricted Cone** &emsp;浏览网页与游戏及下载都没过多限制
* **NAT3 **→ **Port-Restricted Cone** &emsp;同上，但游戏厂商会限制此NAT类型的联机
* **NAT4 **→ **Symmetric** &emsp;这是最严格的网络环境，可能会玩不了游戏、下载都没速度
  
说些比较重要的前话，路由器少一层是一层，这样越有可能得到NAT1和NAT2这两类NAT类型，一般建议家里的网路是以下两种拓扑类型：  
1. 光猫桥接→主路由（拨号连接外网用）→副路由（纯AP模式，扩展信号）  
2. 光猫拨号（直接充当主路由）→副路由（纯AP模式，扩展信号）  

这样的好处是桥接和纯AP是不进行NAT的，而是SWitch，所以不会导致多一层NAT。
  
现在个别网络游戏严格要求你的网络环境必须是**NAT2**或以上才能进行游戏。而你的网络环境又是NAT3及NAT4,那到底该怎么办呢？下面我们介绍一些简单提升NAT类型的方法，其实就是进行[**NAT穿透**](http://baike.baidu.com/item/nat#3_3)

* 路由器有启用**Full Cone、STUN、TURN、ICE、uPnP**等功能都果断启用了；若没有该换了，因为**uPnP**基本是标配

* 一般建议有Full Cone、uPnP等就不要开DMZ了，除非你是PS4/XBox这类游戏主机要提升NAT类型

* 如果没有以上功能，那可以找下有没有**[DMZ](http://baike.baidu.com/item/dmz)**功能并启用它，将你要提升NAT类型的主机IP地址设置好。

* 在Windows上把以下三个服务设置为自动启动，并启动该服务：   

    * SSDP Discovery  
    * Function Discovery Provider Host  
    * Function Discovery Resource Publication  
  
* 在Windows防火墙，放行你需要提升NAT类型的软件或者游戏程序，也可以直接关闭

* 如果你的设备是通过电脑共享网络的形式上网的，建议把这个服务也打开：
    
    * UPnP Device Host  

以上能弄的都弄了，网络环境就会越好甚至NAT1都没有问题。这是我通过以上设置，进行NAT穿透+公网IP一枚。

测得的结果： 

![](https://i.postimg.cc/NFMFQtKC/132059dd4rfiilqz4e4s4p.jpg)

<!-- ![](https://ipfs.io/ipfs/QmZNLVAGW4wUrd1qpRKhj4JzXei9PhKJ7z9HTnjvp3qYbw?0.jpg)    -->

<!-- ![](http://www.right.com.cn/forum/data/attachment/forum/201611/10/132059dd4rfiilqz4e4s4p.jpg)   -->
最后附上NAT类型测试工具：  

![](https://i.postimg.cc/257n6z5C/zip.gif) [NAT类型测试.zip](http://down7.pc6.com/xy3/NatTypeTester.zip) 

<!-- ![](http://www.right.com.cn/forum/static/image/filetype/zip.gif) [NAT类型测试.zip](http://www.right.com.cn/forum/plugin.php?id=imc_attachad:ad&aid=MTQzODYzfDQxMGQxODFmfDE1MjU4MzkxMjZ8MHwxOTkyOTk%3D)  -->
PS:  
如果能找运营商要到外网IP，这是最好的；没有公网IP的话，可以打电话给客服态度强硬点、最好一开始就把客服的工号也要了并说“我家宽带怎么没公网IP啊，我需在家里装远程监控，没有公网IP的话不行，如果不给我公网IP，我只好退宽带换别家的了，不给就投诉你”；但如果还是要不到公网IP，能提升到NAT2也不错了。

还有一种最笨的就是直接电脑拨号上网，Windows 直接把防火墙关了，只要你的是公网IP，妥妥的NAT1。想要提升PS4/XBox这类游戏主机的NAT类型，建议以上能做的都做了。


## 浅析正向、反向、透明代理

> 原文：[浅析正向代理、反向代理、透明代理](https://www.logcg.com/archives/929.html)&emsp;作者：[R0UTER](https://www.logcg.com/archives/author/admin)

一般我们上网，都是插上网线即可，顶多需要拨号。但是在企业应用上网络的环境可能就要复杂的多，这是一般家庭网络所无法体会的。所以，代理这个功能就应运而生了。

在维基百科上的定义是这样的：

> 代理（英语：Proxy）也称网络代理，是一种特殊的网络服务，允许一个网络终端（一般为客户端）通过这个服务与另一个网络终端（一般为服务器）进行非直接的连接。一些网关、路由器等网络设备具备网络代理功能。

> 一般认为代理服务有利于保障网络终端的隐私或安全，防止攻击。

在代理当中，一般会把代理分为三种，即正向代理、反向代理还有透明代理。接下来，我们就依次818这些代理。

## 正向代理

正向代理就是我们接触最多的代理模式，一般来讲，很多企业以前（现在也有不少）是不允许员工随便访问外网的，有一些则是部分外网，如果你想要或者需要访问外网资源，那你很可能会希望在自己家里搭建一个代理服务器。这时候你就发现，正向代理一般都是 C/S 架构的，它通过客户端，将你要访问某站的请求打包，然后发给代理服务器，而代理服务器负责将你的请求发送给目标站。——通过这样的方式，便可以绕过防火墙的屏蔽了。

另外，如果你想悄悄地访问某站，不想让别人知道，你也可以使用代理，通过高度匿名的代理访问，这样你的踪迹就完全被隐藏了，别人只会找到代理服务器的访问信息而不是你的，从而达到了隐藏痕迹的目的。

由于需求的不同，就肯定催生了一批不同用途的代理，比如说我们最常见的HTTP代理、FTP代理、SSL代理等等。

哦对了，还有比较低层的socks代理，这个比较特殊一些，它不会关心你代理什么协议，它统统会将你的IP包撸走，不过，我们常用的 shadowsocks 虽然使用了sock5代理，但是对于UDP的支持并不是很完善。

**正向代理又会根据高度匿名与否来区分：**

* 高度匿名代理

    这样的服务器会把你的数据包原封不动的来转发，就好像自己的一样；这样对目标站来讲，根本就会以为是代理服务器在访问它而不是你；

* 普通匿名代理

    相对于高度匿名代理来讲，这样的服务器会被目标站认出来是代理服务器，因此很有可能还会追踪到你的真实IP

* 透明代理

    这个其实不能和正向、反向代理并列，因为它是正向代理中的一种；它不会加密你的信息，而是明明白白的告诉目标站你是通过代理访问的！当然好处是允许缓存，以及一些规则来让你的访问变得更加安全——典型应用就是内网硬件防火墙上的透明代理。
    
    不过，我们常说的ss透明代理与此定义不同，前者表示相对电脑访问，代理是透明的；后者表示相对目标站点，代理是透明的。

## 反向代理

说完了正向代理，我们来818与之相对的反向代理，相对于正向代理来说，反向代理的技术含量更高一些，应用的范围也更加广泛，从小到你代理访问网站 ，大到网站内部负载均衡都会使用到这种技术。

其实这个技术最典型的应用是在服务后端。比如说某大型网站服务器有一台，然后后端负责计算的服务器有N台，其实真正的服务器在这N台服务器上，这N台服务器通过某些机制同步内容，然后前端的服务器只负责收发数据，那么前端接收到请求之后就会根据后台某服务器的空闲资源来决定将请求反向代理给谁，从而达到了负载均衡的目的。

![](https://i.postimg.cc/rFXTMWDX/imagesppx.png)

> 比如说淘宝以前访问速度一般，后来就是革新了负载均衡的系统，对于反向代理都需要这个代理的过程。而淘宝把这个代理过程砍掉一半，也就是上文中的N台服务器中的某台收到前端的请求之后，并不会将数据返回给前端，而是直接反馈给了用户。（这个案例具体的忘记了，两年前朋友讲给我听的……求斧正。）

总之呢，后来这个反向代理就已经被人们给玩坏了，从搭建缓存服务器到钓鱼攻击，再到后来的变成了我们经常用的梯子……

它的特点就是绝对可以保护代理后边的东西，用户只能访问到代理服务器，而代理服务器后边发生的事情你绝对不会知晓，这样一来就让它变得很危险，这绝对是个黑箱。比如说用来钓鱼，悄悄篡改你的访问链接之类的，完全没有问题。所以，如果你要使用反向代理的梯子，那一定要找绝对信任的人提供的服务——或者干脆自己动手搭建一个只给身边的人用。

反向代理就讲这么多吧，它一般还是用在开发环境的多，反代的最大特点就是一个域名一个站，比如我们常见的那些谷歌的跨境反代，明明访问的是谷歌，但域名却不尽相同。还有其实你访问的淘宝、京东都是反代网站，只不过应用的技术更多，而且他们只反代他们自己的站点。

## 透明代理

前边讲过，透明代理本应该是正向代理的一个级别分支，但为什么还是要任性地将它单独拎出来扒一扒呢？正如上文所说，此透明代理非彼透明代理！

我们这里要讲的透明代理，特指装在我们家用小路由器上的各种代理，这样一来，就实现了电脑正常上网但实际上是被代理出去的效果——即相对电脑来说代理是透明的。

> 这样一来，就要把VPN囊括进来，说起VPN其实不属于代理，简单讲一句就是它们被开发出来的初衷不太相同，这么讲，你家、防火墙、公司这三个地方，虽然代理和VPN的手段都是穿墙，但代理的目的是从公司出去，而VPN则是从家里连到公司。

> 所以代理只会转发某些对应的数据包，而VPN则是在逻辑上让你“穿越”到了目的地，从而实现在那里上网。

不过，这对于我们的“透明代理”来讲都不重要，在路由器上使用透明代理，一般是使用socks5代理或vpn；通过特制的路由器让它们来实现代理，这样你上网所发出的数据包就会被路由器“自动”地代理。

你看相对你的电脑、手机、iPad来讲，这个代理是不是变得“透明”了呢？


## 深网和暗网的区别及基础扫盲

> 原文：[深网和暗网的区别及基础扫盲](http://chitanda.me/2016/08/19/difference-between-deepweb-and-darkweb/) 作者：[Chitanda Akari](http://chitanda.me/2016/08/19/difference-between-deepweb-and-darkweb/)

## 什么是深网

根据[维基百科相关词条](https://zh.wikipedia.org/wiki/%E6%B7%B1%E7%BD%91)的解释:  

| 深网（英语：Deep Web、Dark Web，又称：不可见网、隐藏网）是指互联网上那些不能被标准搜索引擎索引的非表面网络内容。 |
| --- |

可以看出这**深网**并不仅仅是指网络站点，它的范围远大于一般的网站，它包括所有不能被搜索引擎抓取到的网络内容，比如：你的QQ聊天记录，你微博私信记录，MC私服，诸如SSH、VPN等非标准80或443端口且不走标准HTTP/HTTPS协议的内容等等。因此对于普通用户来说他们每时每刻都在和深网打交道，所谓”深网深不可测”自然是个笑话。而且实际上深网这个概念对用户来说毫无意义，因为不同用户”能抓取到的内容不同”，A的聊天记录被B来说就是”深网”；你女神对你屏蔽的朋友圈对你来说也是”深网”，而对她自己来说自然就是个普通的表层网络。所以讨论”深网”的时候只能取绝对参照物——搜索引擎，**深网其实是一个仅针对搜索引擎的概念，表示不能被其抓取到的私有内容**

## 什么是暗网

暗网是深网的子集，根据维基上的解释：暗网（英语：Darknet或Dark Web）是指只使用非常规协议和端口以及可信节点进行连接的私有网络,暗网是不能通过”常规方式”访问的——当然你用TOR浏览器就不算常规方式了。而根据wiki还有别的方式比如Freenet、RetroShare、GNUnet、OneSwarm、Tribler等等就不一一列举了。

对普通大众来说最简单的方法还是Tor浏览器，暗网的重点在于”暗”。属于网络上的黑市，这里面有很多暴力，色情，黑产等相关的东西，比如军火、假护照、信用卡、用户信息、0day等等。网络上大部分阴谋论相关的文章也都是从暗网这些阴暗点做切入点进行发散创作。

## 谣言

由于进入暗网需要的一点点技术门槛（国外是TOR国内是VPN+TOR）导致很多文章都开始搞阴谋论和超自然分析夺人眼球。这里选几个比较经典的做下解释

## 暗网和深网是同一个东西

这个是最常见的，往往标题里写着”深网”结果写着写着就成了”暗网”。比如这两篇，就是典型的误导人：  

* 《[一篇关于 DEEP WEB 的简易指南](http://www.vice.cn/read/a-brief-guide-to-deep-web)》
* 《[暗网，一个比你想象中恐怖100倍的互联网世界](http://www.admin5.com/article/20151004/625784.shtml)》

前面也说过，暗网是深网的子集，但深网里的绝大多数网站都是普通用户可以直接接触到的内容；和暗网这种必须借助第三方工具才能访问的不一样。

## 暗网的内容占了互联网全部内容的96%

这个是上面那个谣言的变种。其实也是”深网””暗网”弄混了而已。这句话原话出自[纸牌屋](http://www.slate.com/articles/technology/bitwise/2014/02/house_of_cards_season_2_what_s_up_with_all_the_deep_web_stuff.html)：”Deep Web is 96 percent of the Internet, with us plebes only seeing a mere 4 percent.”,可见原文说的是”深网的内容占了互联网内容的4%”而不是”暗网”。

事实上这个谣言本身也是相当好反驳的：

1. 因为暗网本身的用户量就是相当少，可能只占网民的x万分之一，这种比例下他们的内容产出不可能超越作为大多数的普通网民所构建的普通网络

2. Apple、Google、Facebook、Amazon等公司每年在硬件和带宽上的成本至少加起来上百亿人民币，如果暗网本身内容是表层网络的几十倍的话，那他们的成本就更可怕了。然而全部暗网的流水加起来估计都覆盖不了这里的零头。而如果是深网的话这句话是没有多少问题的，这里先不论4%这个数字是否准确（因为按照有些人的计算google收录的不只4%，然而这点不好证伪，所以姑且认为是4%吧）。因为互联网大部分用户数据对搜索引擎而言都是不公开的。

## 暗网是非公开的，一般人很难进去

这个其实是很难证伪的论点，因为有个”没有真正的苏格兰人”的诡辩点在：你举出的例子对方都可以用”这不是真正的暗网”来死缠烂打，所以具体不深入。  

单纯说下”非公开”这点：这是个认知错误。其实暗网依旧是公开站点，它只是与普通的公网相隔绝而已。真正的非公开站点应该是那些纯局域网内的站点。而”普通人很难接触这点”，由于通过TOR浏览器就可以直接访问了，因此也是故意夸大难度好渲染阴谋论而已。网上很多帖子只说自己看到的各种光怪陆离的东西而从来不给链接可能也就是因为给了后大概立马就要被打脸了。

事实上访问**暗网真正的难点其实在于获取URL**,因为很多网站都是过几天就换一个域名。对于大众来说只能依靠**hidden wiki**的帮助，而真正的暗网深度人士大概会有其他的获取渠道，比如IRC聊天室，专门的发布页面等等。（这个只是个人猜测而已）

## 暗网上有相当多的血腥恐怖的内容 

这个本质上其实不能算谣言。但我拿出来就是因为**这部分内容被媒体过于渲染，把少数当多数**，这个说法的问题在于**相当多**，虽然暗网上确实有部分血腥暴力的站点，但是就和表站里也有很多小众站点如食人，撒旦教等等一样，这部分站点在暗网里也只是占了极少数。从暗网的大部分**hidden wiki**页面来看，暗网的主流内容还是各种交易市场：比特币、毒品、枪支、信用卡等等；再就是色情站点等，买凶相关的站点也有，但是非常血腥主题的确实基本上看不到（有些人大概会认为这说明他们藏的更深，找不到不代表就没有。但是这也从侧面证明了它们的小众，由这种极小部分人群作为暗网代表，我觉得相当缺乏说服力） 

而根据wiki上[Dark web](https://en.wikipedia.org/wiki/Dark_web)里的相关数据表明，暗网站点里数量前三的是”Drugs”、”Market”、”Fraud”,即药品、交易、欺诈前三，可以说明那些极度血腥反人类的真的只是极少

<!-- ![](https://ipfs.io/ipfs/Qmd2gda91yrCpzfNMu8LKEjPaV8WcBpa7SXSH5iM5Tp9rx?2.jpg) -->

![](https://i.postimg.cc/c6qJwb1d/hidden-web-category.png)

## 总结

首先是需要TOR打开[The Uncensored Hidden Wiki](http://uhwiki36pbooodfj.onion/wiki/index.php/Main_Page)，另外这种导航页其实有很多，各位可以自行挖掘

<!-- ![](https://ipfs.io/ipfs/QmaX8fmm2pBGNRQ9WU3xuPDdiB4wtyGd18oPpZ16mu3Bxc?0.jpg) -->

![](https://i.postimg.cc/1373KX3W/hiddenwiki.jpg)

<!-- ![](https://ipfs.io/ipfs/QmRzrEfCk1Rxo6opZbidCyNnStFBhhzmszsbq517NC3E1K?0.jpg) -->

![](https://i.postimg.cc/RZ2zFHFz/hiddenwiki-list.jpg)

另一个导航站点：

<!-- ![](https://ipfs.io/ipfs/QmYfBSP66ToswbWvm44JwAYg6jsSrxPS3TrrMzxC2jzX3m?3.jpg) -->

![](https://i.postimg.cc/90wdcKN2/hdwiki.jpg)

其次是某些站点的截图。有军火、Drug、假护照、信用卡

<!-- ![](https://ipfs.io/ipfs/QmcdFpt8HEUsPTGgw9zASrUbNZZCg9pzFuazRBZcPCJoQW?0.jpg) -->

![](https://i.postimg.cc/bY0b90c3/gun.jpg)

<!-- ![](https://ipfs.io/ipfs/QmabaP9oANr2MyKBf9igUJn3pj3KtrTSsYbmaGWXpzUuCa?2.jpg) -->

![](https://i.postimg.cc/TwVyQxSp/fake.jpg)

不过也不是所有站点都是违法犯罪的，也有些画风比较清奇如下图，这说明其实你也完全可以在暗网搭个网站放动画片，不过有没有人看就是另一回事了。

<!-- ![](https://ipfs.io/ipfs/Qmdye3d2Ct3AhAnJUYgLpUTnRtUie2uJkd74gfRvx3PjF7?2.jpg) -->

![](https://i.postimg.cc/q7fMFY2n/ps4.jpg)

## 参考文档

[深网-中文维基](https://zh.wikipedia.org/wiki/%E6%B7%B1%E7%BD%91)  
[Darknet-Wikipedia](https://en.wikipedia.org/wiki/Darknet)  
[Dark\_web](https://en.wikipedia.org/wiki/Dark_web)  
[The Uncensored Hidden Wiki](http://uhwiki36pbooodfj.onion/wiki/index.php/Main_Page)


## 为什么纯净IP这么重要？

## 万人骑的 IP 可能引发的后果

纯净IP的重要性主要体现在以下几个高风险场景下，使用“不干净”的IP往往会导致严重后果：

1. **账号安全与防关联（最常见场景）**
   - 跨境电商（如亚马逊、eBay、Shopify）、社媒运营（如TikTok、Instagram、Facebook、Twitter/X）等平台严禁一人多账号。
   - 如果多个账号用同一个或关联的IP登录，平台风控系统很容易判定为“同一人操作”，导致**批量封号**。
   - **纯净IP（尤其是住宅IP或原生IP）** 看起来像普通家庭宽带，能有效隔离账号，降低封号风险。
   - 案例：很多卖家用共享数据中心IP开店群，几天内全军覆没；换成纯净静态住宅IP后，半年0封号。
2. **数据爬虫与采集**
   - 大量爬虫请求同一个IP，网站很容易识别为机器人并封禁。
   - 纯净IP + 合理轮换，能大幅提高采集成功率和速度，避免被限流、验证码轰炸或永久封禁。
3. **广告投放与审核**
   - Google Ads、Facebook Ads、TikTok Ads等平台对IP有严格审核。
   - 使用被标记的IP，广告可能直接被拒审，或投放效果差（限流、无法精准定位）。
   - 纯净本土IP能让广告看起来更像真实用户，提高通过率和投放效果。
4. **访问稳定性与体验**
   - 不纯净的IP常被网站加入黑名单，导致频繁出现验证码、连接超时、访问被拒。
   - 纯净IP连接更快、更稳定，减少操作中断。
5. **SEO与网络安全**
   - 低纯净IP可能影响搜索引擎排名（被视为垃圾流量）。
   - 也能降低被黑客利用的风险。

**一句话总结**： 在风控越来越严的今天，**纯净IP就是你的“网络身份证”**。它不是“可有可无”的工具，而是决定业务能否长期稳定运行的生死线。

## 纯净IP应用场景

纯净IP未被用于垃圾邮件、网络攻击、欺诈、PAN口（东南亚盘口）博彩等违规活动，因此未被列入国际黑名单（如Spamhaus、谷歌黑名单等）。

纯净IP主要用于以下场景：

* 企业邮件系统：确保客户邮件送达，避免进入垃圾箱。
* 跨境电商与支付：防止支付网关因IP风险拒绝交易。
* API服务与云平台：避免AWS、谷歌云等平台因IP风控限制访问。
* 学术研究：访问学术数据库（如PubMed、IEEE）时避免IP封锁。

### 常见纯净IP类型（从高到低推荐）：

- **原生住宅IP（Native Residential IP）**：由当地运营商直接分配，从未被代理污染，纯净度最高，适合长期养号。
- **静态住宅IP**：固定不变的住宅IP，适合绑定账号。
- **动态住宅IP**：轮换使用，适合爬虫、批量操作。

### 怎么判断一个IP是否纯净？

可以用免费工具快速检测：

- **IPQualityScore** / **Scamalytics** / **AbuseIPDB** → 看欺诈分数（Fraud Score），越低越好（<25分较安全）。
- **Whoer.net** / **WhatIsMyIP** → 看是否被标记为Proxy/VPN、是否在黑名单。
- **Ping0.cc** → 国内常用，显示欺诈值和历史行为。

**建议**：

- 不要贪便宜买共享IP（容易被多人用脏）。
- 优先选择正规代理商的**独享/静态住宅IP**，虽然贵，但长期算下来最划算。

总之，**纯净IP不是锦上添花，而是必须的基础设施**，尤其在2025年平台风控空前严格的背景下。


## 集群、分布式、负载均衡区别

> 原文：[集群、分布式、负载均衡区别](https://www.cnblogs.com/xzwblog/p/7255364.html) &nbsp;|&nbsp; 作者：[何必等明天](https://home.cnblogs.com/u/xzwblog/)

?> 另外这篇 [菜鸟教你如何通俗理解——>集群、负载均衡、分布式](https://www.cnblogs.com/guanshan/p/guan2018_3_8_001.html) 说的比较通俗化

## 集群

### 集群的概念

计算机集群通过一组松散集成的计算机软件和/或硬件连接起来高度紧密地协作完成计算工作。在某种意义上，他们可以被看作是一台计算机。集群系统中的单个计算机通常称为节点，通常通过局域网连接，但也有其它的可能连接方式。集群计算机通常用来改进单个计算机的计算速度和/或可靠性。一般情况下集群计算机比单个计算机，比如工作站或超级计算机性能价格比要高得多。

比如单个重负载的运算分担到多台节点设备上做并行处理，每个节点设备处理结束后，将结果汇总，返回给用户，系统处理能力得到大幅度提高。一般分为几种：

**高可用性集群：** 一般是指当集群中有某个节点失效的情况下，其上的任务会自动转移到其他正常的节点上。还指可以将集群中的某节点进行离线维护再上线，该过程并不影响整个集群的运行。

**负载均衡集群：** 负载均衡集群运行时，一般通过一个或者多个前端负载均衡器，将工作负载分发到后端的一组服务器上，从而达到整个系统的高性能和高可用性。

**高性能计算集群：** 高性能计算集群采用将计算任务分配到集群的不同计算节点而提高计算能力，因而主要应用在科学计算领域。

## 分布式

**集群：** 同一个业务，部署在多个服务器上。分布式：一个业务分拆成多个子业务，或者本身就是不同的业务，部署在不同的服务器上。

简单说，分布式是以缩短单个任务的执行时间来提升效率的，而集群则是通过提高单位时间内执行的任务数来提升效率。举例：就比如新浪网，访问的人多了，他可以做一个群集，前面放一个均衡服务器，后面几台服务器完成同一业务，如果有业务访问的时候，响应服务器看哪台服务器的负载不是很重，就将给哪一台去完成，并且一台服务器垮了，其它的服务器可以顶上来。分布式的每一个节点，都完成不同的业务，一个节点垮了，那这个业务可能就失败了。

## 负载均衡

### 概念

随着业务量的提高，现有网络的各个核心部分访问量和数据流量的快速增长，其处理能力和计算强度也相应地增大，使得单一的服务器设备根本无法承担。在此情况下，如果扔掉现有设备去做大量的硬件升级，这样将造成现有资源的浪费，而且如果再面临下一次业务量的提升时，这又将导致再一次硬件升级的高额成本投入，甚至性能再卓越的设备也不能满足当前业务量增长的需求。

负载均衡技术通过设置虚拟服务器IP（VIP），将后端多台真实服务器的应用资源虚拟成一台高性能的应用服务器，通过负载均衡算法，将用户的请求转发给后台内网服务器，内网服务器将请求的响应返回给负载平衡器，负载平衡器再将响应发送到用户，这样就向互联网用户隐藏了内网结构，阻止了用户直接访问后台（内网）服务器，使得服务器更加安全，可以阻止对核心网络栈和运行在其它端口服务的攻击。并且负载均衡设备（软件或硬件）会持续的对服务器上的应用状态进行检查，并自动对无效的应用服务器进行隔离，实现了一个简单、扩展性强、可靠性高的应用解决方案，解决了单台服务器处理性能不足，扩展性不够，可靠性较低的问题。

系统的扩展可分为纵向（垂直）扩展和横向（水平）扩展。纵向扩展，是从单机的角度通过增加硬件处理能力，比如CPU处理能力，内存容量，磁盘等方面，实现服务器处理能力的提升，不能满足大型分布式系统（网站），大流量，高并发，海量数据的问题。因此需要采用横向扩展的方式，通过添加机器来满足大型网站服务的处理能力。比如：一台机器不能满足，则增加两台或者多台机器，共同承担访问压力。

**负载平衡最重要的一个应用是利用多台服务器提供单一服务**，这种方案有时也称之为服务器农场。通常，负载平衡主要应用于Web网站，大型的Internet Relay Chat网络，高流量的文件下载网站，NNTP（Network News Transfer Protocol）服务和DNS服务。现在负载平衡器也开始支持数据库服务，称之为数据库负载平衡器。

服务器负载均衡有三大基本Feature：负载均衡算法，健康检查和会话保持，这三个Feature是保证负载均衡正常工作的基本要素。其他一些功能都是在这三个功能之上的一些深化。下面我们具体介绍一下各个功能的作用和原理。

在没有部署负载均衡设备之前，用户直接访问服务器地址（中间或许有在防火墙上将服务器地址映射成别的地址，但本质上还是一对一的访问）。当单台服务器由于性能不足无法处理众多用户的访问时，就要考虑用多台服务器来提供服务，实现的方式就是负载均衡。负载均衡设备的实现原理是把多台服务器的地址映射成一个对外的服务IP（我们通常称之为VIP，关于服务器的映射可以直接将服务器IP映射成VIP地址，也可以将服务器IP:Port映射成VIP:Port，不同的映射方式会采取相应的健康检查，在端口映射时，服务器端口与VIP端口可以不相同）,这个过程对用户端是不可见的，用户实际上不知道服务器是做了负载均衡的，因为他们访问的还是一个目的IP，那么用户的访问到达负载均衡设备后，如何把用户的访问分发到合适的服务器就是负载均衡设备要做的工作了，具体来说用到的就是上述的三大Feature。

我们来做一个详细的访问流程分析:

![](https://i.postimg.cc/FHfH5gPn/1156565-20170729153452566-2008499549.png)

用户(IP:207.17.117.20)访问域名`www.a10networks.com`，首先会通过DNS查询解析出这个域名的公网地址：199.237.202.124，接下来用户207.17.117.20会访问199.237.202.124这个地址，因此数据包会到达负载均衡设备，接下来负载均衡设备会把数据包分发到合适的服务器，看下图：

![](https://i.postimg.cc/63KWZsBD/85133083.png)

负载均衡设备在将数据包发给服务器时，数据包是做了一些变化的，如上图所示，数据包到达负载均衡设备之前，源地址是：207.17.117.20，目的地址是：199.237.202.124，当负载均衡设备将数据包转发给选中的服务器时，源地址还是：207.17.117.20，目的地址变为172.16.20.1，我们称这种方式为目的地址NAT(DNAT，目的地址转换)。一般来说，在服务器负载均衡中DNAT是一定要做的（还有另一种模式叫做服务器直接返回-DSR，是不做DNAT的，我们将另行讨论），而源地址根据部署模式的不同，有时候也需要转换成别的地址，我们称之为：源地址NAT(SNAT)，一般来说，旁路模式需要做SNAT，而串接模式不需要，本示意图为串接模式，所以源地址没做NAT。

我们再看服务器的返回包，如下图所示，也经过了IP地址的转换过程，不过应答包中源/目的地址与请求包正好对调，从服务器回来的包源地址为172.16.20.1，目的地址为207.17.117.20，到达负载均衡设备后，负载均衡设备将源地址改为199.237.202.124，然后转发给用户，保证了访问的一致性。

![](https://i.postimg.cc/Xq7n2wGL/12538.png)

### 负载均衡算法

一般来说负载均衡设备都会默认支持多种负载均衡分发策略，例如：

**轮询（RoundRobin）**将请求顺序循环地发到每个服务器。当其中某个服务器发生故障，AX就把其从顺序循环队列中拿出，不参加下一次的轮询，直到其恢复正常。

**比率（Ratio）：** 给每个服务器分配一个加权值为比例，根椐这个比例，把用户的请求分配到每个服务器。当其中某个服务器发生故障，AX就把其从服务器队列中拿出，不参加下一次的用户请求的分配，直到其恢复正常。

**优先权（Priority）：**给所有服务器分组，给每个组定义优先权，将用户的请求分配给优先级最高的服务器组（在同一组内，采用预先设定的轮询或比率算法，分配用户的请求）；当最高优先级中所有服务器或者指定数量的服务器出现故障，AX将把请求送给次优先级的服务器组。这种方式，实际为用户提供一种热备份的方式。

**最少连接数（LeastConnection）：**AX会记录当前每台服务器或者服务端口上的连接数，新的连接将传递给连接数最少的服务器。当其中某个服务器发生故障，AX就把其从服务器队列中拿出，不参加下一次的用户请求的分配，直到其恢复正常。

**最快响应时间（Fast Reponse time）：**新的连接传递给那些响应最快的服务器。当其中某个服务器发生故障，AX就把其从服务器队列中拿出，不参加下一次的用户请求的分配，直到其恢复正常。

**哈希算法( hash):** 将客户端的源地址，端口进行哈希运算，根据运算的结果转发给一台服务器进行处理，当其中某个服务器发生故障，就把其从服务器队列中拿出，不参加下一次的用户请求的分配，直到其恢复正常。

**基于数据包的内容分发：** 例如判断HTTP的URL，如果URL中带有.jpg的扩展名，就把数据包转发到指定的服务器。

### 健康检查

健康检查用于检查服务器开放的各种服务的可用状态。负载均衡设备一般会配置各种健康检查方法，例如Ping，TCP，UDP，HTTP，FTP，DNS等。Ping属于第三层的健康检查，用于检查服务器IP的连通性，而TCP/UDP属于第四层的健康检查，用于检查服务端口的UP/DOWN，如果要检查的更准确，就要用到基于7层的健康检查，例如创建一个HTTP健康检查，Get一个页面回来，并且检查页面内容是否包含一个指定的字符串，如果包含，则服务是UP的，如果不包含或者取不回页面，就认为该服务器的Web服务是不可用（DOWN）的。比如，负载均衡设备检查到172.16.20.3这台服务器的80端口是DOWN的，负载均衡设备将不把后面的连接转发到这台服务器，而是根据算法将数据包转发到别的服务器。创建健康检查时可以设定检查的间隔时间和尝试次数，例如设定间隔时间为5秒，尝试次数为3，那么负载均衡设备每隔5秒发起一次健康检查，如果检查失败，则尝试3次，如果3次都检查失败，则把该服务标记为DOWN，然后服务器仍然会每隔5秒对DOWN的服务器进行检查，当某个时刻发现该服务器健康检查又成功了，则把该服务器重新标记为UP。健康检查的间隔时间和尝试次数要根据综合情况来设置，原则是既不会对业务产生影响，又不会对负载均衡设备造成较大负担。

### 会话保持

如何保证一个用户的两次http请求转发到同一个服务器，这就要求负载均衡设备配置会话保持。

会话保持用于保持会话的连续性和一致性，由于服务器之间很难做到实时同步用户访问信息，这就要求把用户的前后访问会话保持到一台服务器上来处理。举个例子，用户访问一个电子商务网站，如果用户登录时是由第一台服务器来处理的，但用户购买商品的动作却由第二台服务器来处理，第二台服务器由于不知道用户信息，所以本次购买就不会成功。这种情况就需要会话保持，把用户的操作都通过第一台服务器来处理才能成功。当然并不是所有的访问都需要会话保持，例如服务器提供的是静态页面比如网站的新闻频道，各台服务器都有相同的内容，这种访问就不需要会话保持。

绝大多数的负载均衡产品都支持两类基本的会话保持方式：源/目的地址会话保持和cookie会话保持，另外像hash，URL Persist等也是比较常用的方式，但不是所有设备都支持。基于不同的应用要配置不同的会话保持，否则会引起负载的不均衡甚至访问异常。我们主要分析B/S结构的会话保持。

**基于B/S结构的应用：**

对于普通B/S结构的应用内容，例如网站的静态页面，可以不用配置任何的会话保持，但是对于一个基于B/S结构尤其是中间件平台的业务系统来说，必须配置会话保持，一般情况下，我们配置源地址会话保持可以满足需求，但是考虑到客户端可能有上述不利于源地址会话保持的环境，采用Cookie会话保持是一个更好的方式。Cookie会话保持会把负载均衡设备选择的Server信息保存在Cookie中发送到客户端，客户端持续访问时，会把该Cookie带来，负载均衡器通过分析Cookie把会话保持到之前选定的服务器。Cookie分为文件Cookie和内存cookie，文件cookie保存在客户端计算机硬盘上，只要该cookie文件不过期，则无论是否重复关闭开放浏览器都能保持到同一台服务器。内存Cookie则是把Cookie信息保存在内存中，Cookie的生存时间从打开浏览器访问开始，关闭浏览器结束。由于现在的浏览器对Cookie都有一定默认的安全设置，有些客户端可能规定不准使用文件Cookie，所以现在的应用程序开发多使用内存Cookie。

然而，内存Cookie也不是万能的，比如浏览器为了安全可能会完全禁用Cookie，这样Cookie会话保持就失去了作用。我们可以通过Session-id来实现会话保持，即将session-id作为url参数或者放在隐藏字段中，然后分析Session-id进行分发。

另一种方案是：将每一会话信息保存到一个数据库中。由于这个方案会增加数据库的负载，所以这个方案对性能的提高并不好。数据库最好是用来存储会话时间比较长的会话数据。为了避免数据库出现单点故障，并且提高其扩展性，数据库通常会复制到多台服务器上，通过负载均衡器来分发请求到数据库服务器上。

基于源/目的地址会话保持其实不太好用，因为客户可能是通过DHCP，NAT或者Web代理来连接Internet的，其IP地址可能经常变换，这使得这个方案的服务质量无法保障。

**NAT(Network Address Translation，网络地址转换):** 当在专用网内部的一些主机本来已经分配到了本地IP地址(即仅

在本专用网内使用的专用地址)，但现在又想和因特网上的主机通信(并不需要加密)时，可使用NAT方法。这种方法需要在专用网连接到因特网的路由器上安装NAT软件。装有NAT软件的路由器叫做NAT路由器，它至少有一个有效的外部全球IP地址。这样，所有使用本地地址的主机在和外界通信时，都要在NAT路由器上将其本地地址转换成全球IP地址，才能和因特网连接。

### 负载均衡的其他好处

**高扩展**

通过添加或减少服务器数量，可以更好的应对高并发请求。

**（服务器）健康检** 

负载均衡器可以检查后台服务器应用层的健康状况并从服务器池中移除那些出现故障的服务器，提高可靠性。

**TCP 连接复用（TCP Connection Reuse）**

TCP连接复用技术通过将前端多个客户的HTTP请求复用到后端与服务器建立的一个TCP连接上。这种技术能够大大减小服务器的性能负载，减少与服务器之间新建TCP连接所带来的延时，并最大限度的降低客户端对后端服务器的并发连接数请求，减少服务器的资源占用。

一般情况下，客户端在发送HTTP请求之前需要先与服务器进行TCP三次握手，建立TCP连接，然后发送HTTP请求。服务器收到HTTP请求后进行处理，并将处理的结果发送回客户端，然后客户端和服务器互相发送FIN并在收到FIN的ACK确认后关闭连接。在这种方式下，一个简单的HTTP请求需要十几个TCP数据包才能处理完成。

采用TCP连接复用技术后，客户端（如：ClientA）与负载均衡设备之间进行三次握手并发送HTTP请求。负载均衡设备收到请求后，会检测服务器是否存在空闲的长连接，如果不存在，服务器将建立一个新连接。当HTTP请求响应完成后，客户端则与负载均衡设备协商关闭连接，而负载均衡则保持与服务器之间的这个连接。当有其它客户端（如：ClientB）需要发送HTTP请求时，负载均衡设备会直接向与服务器之间保持的这个空闲连接发送HTTP请求，避免了由于新建TCP连接造成的延时和服务器资源耗费。

![](https://i.postimg.cc/8zTxL1vd/266.png)

在HTTP 1.1中，客户端可以在一个TCP连接中发送多个HTTP请求，这种技术叫做HTTP复用（HTTP Multiplexing）。它与TCP连接复用最根本的区别在于，TCP连接复用是将多个客户端的HTTP请求复用到一个服务器端TCP连接上，而HTTP复用则是一个客户端的多个HTTP请求通过一个TCP连接进行处理。前者是负载均衡设备的独特功能；而后者是HTTP 1.1协议所支持的新功能，目前被大多数浏览器所支持。

**HTTP缓存**

负载均衡器可以存储静态内容，当用户请求它们时可以直接响应用户而不必再向后台服务器请求。

**TCP缓冲**

TCP缓冲是为了解决后端服务器网速与客户的前端网络速度不匹配而造成的服务器资源浪费的问题。客户端与负载均衡之间采用的链路具有较高的时延和较低的带宽，而负载均衡与服务器之间采用时延较低和高带宽的局域网连接。由于负载均衡器可以暂存后台服务器对客户的响应数据，再将它们转发给那些响应时间较长网速较慢的客户，如此后台Web服务器就可以释放相应的线程去处理其它任务。

**SSL加速**

一般情况下，HTTP采用明文的方式在网络上传输，有可能被非法窃听，尤其是用于认证的口令信息等。为了避免出现这样的安全问题，一般采用SSL协议（即：HTTPS）对HTTP协议进行加密，以保证整个传输过程的安全性。在SSL通信中，首先采用非对称密钥技术交换认证信息，并交换服务器和浏览器之间用于加密数据的会话密钥，然后利用该密钥对通信过程中的信息进行加密和解密。

SSL是需要耗费大量CPU资源的一种安全技术。目前，大多数负载均衡设备均采用SSL加速芯片（硬件负载均衡器）进行SSL信息的处理。这种方式比传统的采用服务器的SSL加密方式提供更高的SSL处理性能，从而节省大量的服务器资源，使服务器能够专注于业务请求的处理。另外，采用集中的SSL处理，还能够简化对证书的管理，减少日常管理的工作量。

**内容过滤**

有些负载均衡器可以按要求修改通过它的数据。

**入侵阻止功能**

在防火墙保障网络层/传输层安全的基础上，提供应用层安全防范。

**分类**

下面从不同层次讨论负载均衡的实现：

**DNS 负载均衡**

DNS负责提供域名解析服务，当访问某个站点时，实际上首先需要通过该站点域名的DNS服务器来获取域名指向的IP地址，在这一过程中，DNS服务器完成了域名到IP地址的映射，同样，这样映射也可以是一对多的，这时候，DNS服务器便充当了负载均衡调度器，将用户的请求分散到多台服务器上。使用dig命令来看下”baidu”的DNS设置：

![](https://i.postimg.cc/ZKwxDZgx/baidu.png)

可见baidu拥有三个A记录。

这种技术的优点是，实现简单、实施容易、成本低、适用于大多数TCP/IP应用，并且DNS服务器可以在所有可用的A记录中寻找离用户最近的一台服务器。但是，其缺点也非常明显，首先这种方案不是真正意义上的负载均衡，DNS服务器将Http请求平均地分配到后台的Web服务器上（或者根据地理位置），而不考虑每个Web服务器当前的负载情况；如果后台的Web服务器的配置和处理能力不同，最慢的Web服务器将成为系统的瓶颈，处理能力强的服务器不能充分发挥作用；其次未考虑容错，如果后台的某台Web服务器出现故障，DNS服务器仍然会把DNS请求分配到这台故障服务器上，导致不能响应客户端。最后一点是致命的，有可能造成相当一部分客户不能享受Web服务，并且由于DNS缓存的原因，所造成的后果要持续相当长一段时间(一般DNS的刷新周期约为24小时)。所以在国外最新的建设中心Web站点方案中，已经很少采用这种方案了。

**链路层（OSI 第二层）负载均衡**

在通信协议的数据链路层修改mac地址，进行负载均衡。

数据分发时，不修改ip地址（因为还看不到ip地址），只修改目标mac地址，并且配置所有后端服务器虚拟ip和负载均衡器ip地址一致，达到不修改数据包的源地址和目标地址，进行数据分发的目的。

实际处理服务器ip和数据请求目的ip一致，不需要经过负载均衡服务器进行地址转换，可将响应数据包直接返回给用户浏览器，避免负载均衡服务器网卡带宽成为瓶颈。也称为直接路由模式（DR模式）。如下图：

![](https://i.postimg.cc/T2q9gnJS/974.png)

性能很好，但是配置复杂，目前应用比较广泛。

**传输层（OSI 第四层）负载均衡**

传输层是 OSI 第四层，包括 TCP 和 UDP。流行的传输层负载均衡器有 HAProxy（这个也用于应用层负载均衡）和 IPVS。
**主要通过报文中的目标地址和端口**，再加上负载均衡设备设置的服务器选择方式，决定最终选择的内部服务器。

以常见的TCP为例，负载均衡设备在接收到第一个来自客户端的SYN 请求时，即通过上述方式选择一个最佳的服务器，并对报文中目标IP地址进行修改(改为后端服务器IP），直接转发给该服务器。TCP的连接建立，即三次握手是客户端和服务器直接建立的，负载均衡设备只是起到一个类似路由器的转发动作。在某些部署情况下，为保证服务器回包可以正确返回给负载均衡设备，在转发报文的同时可能还会对报文原来的源地址进行修改。

![](https://i.postimg.cc/HLq242KG/maxk.png)

**应用层（OSI 第七层）负载均衡**

应用层是 OSI 第七层。它包括 HTTP、HTTPS 和 WebSockets。一款非常流行又久经考验的应用层负载均衡器就是 Nginx[恩静埃克斯 = Engine X]。

所谓七层负载均衡，也称为“内容交换”，也就是主要通过报文中的真正有意义的应用层内容，再加上负载均衡设备设置的服务器选择方式，决定最终选择的内部服务器。注意此时可以看到具体的http请求的完整url，因此可以实现下图所示的分发：

![](https://i.postimg.cc/HnC6H240/5615.png)

以常见的TCP为例，负载均衡设备如果要根据真正的应用层内容再选择服务器，只能先代理最终的服务器和客户端建立连接(三次握手)后，才能看到客户端发送的真正应用层内容的报文，然后再根据该报文中的特定字段，再加上负载均衡设备设置的服务器选择方式，决定最终选择的内部服务器。负载均衡设备在这种情况下，更类似于一个代理服务器。负载均衡和前端的客户端以及后端的服务器会分别建立TCP连接。所以从这个技术原理上来看，七层负载均衡明显的对负载均衡设备的要求更高，处理七层的能力也必然会低于四层模式的部署方式。那么，为什么还需要七层负载均衡呢？

七层负载均衡的好处，是使得整个网络更"智能化"，比如上面列举的负载均衡的好处，大部分都基于七层负载均衡。例如访问一个网站的用户流量，可以通过七层的方式，将对图片类的请求转发到特定的图片服务器并可以使用缓存技术；将对文字类的请求可以转发到特定的文字服务器并可以使用压缩技术。当然这只是七层应用的一个小案例，从技术原理上，这种方式可以对客户端的请求和服务器的响应进行任意意义上的修改，极大的提升了应用系统在网络层的灵活性。

另外一个常常被提到功能就是安全性。网络中最常见的SYN Flood攻击，即黑客控制众多源客户端，使用虚假IP地址对同一目标发送SYN攻击，通常这种攻击会大量发送SYN报文，耗尽服务器上的相关资源，以达到Denial of Service(DoS)的目的。从技术原理上也可以看出，四层模式下这些SYN攻击都会被转发到后端的服务器上；而七层模式下这些SYN攻击自然在负载均衡设备上就截止，不会影响后台服务器的正常运营。另外负载均衡设备可以在七层层面设定多种策略，过滤特定报文，例如SQL Injection等应用层面的特定攻击手段，从应用层面进一步提高系统整体安全。

现在的七层负载均衡，主要还是着重于应用广泛的HTTP协议，所以其应用范围主要是众多的网站或者内部信息平台等基于B/S开发的系统。 四层负载均衡则对应其他TCP应用，例如基于C/S开发的ERP等系统。


## 为什么翻了墙，也无法访问某网站？

* 杜绝主观情绪化因素
* 多方面考虑原因（多种可能）
* 查找及建立两者关联（共同点）

主观情绪化会失去客观分析判断能力，正确率几乎忽略不计，必须杜绝主观情绪化再去分析！

### RST

网络封锁重置、hosts IP-DNS映射指向问题

### SSL_ERR_SYSCALL 

调用传输层自行设置的代理套接字，出现的无法访问的问题。可能存在代理配置或是网址有问题，网址问题则涉及到hosts映射设定内容。

### 汇总

RST与SSL_ERR_SYSCALL有一个共同的问题：hosts IP-DNS映射

应用层的Hosts通过IP-DNS映射，网址解析被指向特定IP地址。而代理只是转达客户端这特定指向访问IP请求，并不会对IP进行路径转换。若Hosts映射IP、DNS任一方不存在，则会造成即使翻墙配置了代理也无法进行访问的情况。所以代理也被称作[应用网关](https://baike.baidu.com/item/%E5%BA%94%E7%94%A8%E7%BD%91%E5%85%B3/6324513)，也是有原因的。

![](https://i.postimg.cc/SKjbkkk8/008.png)

由于Hosts比远程的DNS优先级高，主机最先进入Hosts查询DNS映射，只有在hosts中没查到该条访问映射才进行远程DNS服务器查询，VPN方面虽建立一条专用隧道进行外部服务器访问，但主机给到外部服务器解析的DNS映射还是错误的，所以还是会造成主机不可达，依旧无法访问。

![](https://i.postimg.cc/fT1p9pnn/009.png)

有时就算进行Host设定重定向也能短时间内也正常访问站点，这与keep-alive、浏览器及系统DNS缓存有关，参考 [小胡子哥-修改Hosts为何不生效，是DNS缓存？](https://www.cnblogs.com/hustskyking/p/hosts-modify.html)

#### 小插曲

对GitHub进行ping测试，发现虽然ping不通，但还是能访问。处于网络安全的考量，应该是网站禁用了ICMP回应或者开启了ICMP过滤。

参考 [kunlunmountain-为什么有些网站PING不通但又能访问.](https://www.cnblogs.com/kunlunmountain/p/5945756.html)

由此从ping转向curl测试，因为该工具也提供了很直观的信息。

![](https://i.postimg.cc/brH28KhX/010.png)


# 仅作了解

## accesser

我们开始是不能打开[wiki主页 https://wikipedia.org](https://wikipedia.org)

![](https://i.postimg.cc/WbbqtFZ4/2020-04-13-114900.png)

现在，[点进入Accesser证书下载页面](https://urenko.github.io/Accesser/)，选择下载相应系统版本的程序。

![](https://i.postimg.cc/MGwBYs4W/2020-04-13-114303.png)

运行下载好的程序，接受弹窗提示的安装证书操作，选择 **`是`**

![](https://i.postimg.cc/Bb6RyBjy/old-3.png)

测试成功，该操作支持较多数被DNS污染和SNI（服务器名称指示）、RST（TCP重置攻击）的站点。

![](https://i.postimg.cc/KvtCWjjm/new2-acc.png)

证书+代理的脚本程序，将被CSP限制。这也就是用此类工具也不能访问P站的原因。有关[内容安全策略( CSP )的了解阅读](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CSP)

![](https://i.postimg.cc/Gm1mXvBd/piv.png)

## ping

可能部分读者会对下图站点、IP都能ping通，但就是访问不了网页的这一现象，而感到奇怪。

![](https://i.postimg.cc/50gC6Nkz/54.png)

ping不处于应用层http协议内，而是网络层ICMP的协议，所以，站点、IP都能ping通，但就是访问不了网页。这与TCP重置攻击有关，相关原理[请看对数字证书的相关概要说明（见「数字证书攻防概述」）](#)

> 图摘自 [TCP/IP、HTTP协议的区别](https://www.jianshu.com/p/f4db4eb065bd)

![](https://i.postimg.cc/50XytRx1/tcpxiyiceng.png)


## goagent

!> goagent已停止维护并清空了相关仓库，基于此的相关衍生项目xx-net自身问题颇多，且含有服务质量低下的付费功能，并不推荐使用

GoAgent通过使用GAE的服务器作为中转绕过了GFW。它的运作流程是浏览器代理设置将请求的数据重定向到client，对数据加密后并发送到GAE的server，再将数据解密并请求需要的数据回传给client。

![](https://i.postimg.cc/nrqdmmrj/goagengstuture.jpg)


## gatherproxy

!> 如今，代理服务器列表测试时效性过低，连接互联网也并不理想（属于中彩票的那种呃...），因此，那就仅当做了解就好了。

进入 [gatherproxy](http://www.gatherproxy.com/) 网址代理服务器列表

![](https://i.postimg.cc/bJ7bFNmk/Snipaste-2019-06-14-13-24-29.png)

选择 `proxy checker` 并下载 GatherProxyer

![](https://i.postimg.cc/T1cwqRFR/Snipaste-2019-06-14-13-25-26.png)

在`gather proxy  from` 中选择 `gatherproxy.com` 勾选 `filter proxy` 点击 `start`；等会就如图所示该站点的代理服务器列表。

![](https://i.postimg.cc/FK1DMzVB/Snipaste-2019-06-14-13-54-a28.png)

在 proxy checker 下方 `checking for` 中勾选 socks代理 ，并点击`start` 开始。

![](https://i.postimg.cc/bvJp4xMf/Snipaste-2019-06-14-14-01-15asd.png)

右键选中一个绿色 ip （随机）测试， `set as proxy for ie chrome`

![](https://i.postimg.cc/sgWNxvhG/Snipaste-2019-06-14-14-10-32.png)

此时提示设定已经完成

![](https://i.postimg.cc/sXbn3zg4/Snipaste-2019-06-14-14-14-23.png)

打开ie 浏览器测试，捎带安利一个ip查询站点: [ip-adress](https://www.ip-adress.com/)

?> 选择相关代理服务器，绿色代表服务器状态相对良好，红色也就是很差的；当然，显示绿色也未必连接状态就很好；多数时候，得多测试好几个代理服务器ip，红色恶心的，那就更不用说了。

![](https://i.postimg.cc/Gh04ymgn/Snipaste-2019-06-14-14-37-09.png)

## bing翻译用作web代理

!> 现在，必应搜索和翻译，需要国际互联网环境才能浏览到真正的内容；说一句废话吧：国际互联网其实就是互联网，中国互联网实际上是局域网，只是换了个名词而已。

利用连接到的代理服务器ip，必应也可当做代理网站使用

![](https://i.postimg.cc/25zMtC1q/Snipaste-2019-06-14-14-22-00.png)

sure thin' 你得还需将英文转换中文浏览 `English -> Chinese` 即可所示如图效果

![](https://i.postimg.cc/pdSTVcbB/Snipaste-2019-06-14-14-29-20.png)


## CoNET

!> 该项目存在一些邮箱验证不完善与滥用收发邮件等问题，以至于无法有效使用相关翻墙服务，故不建议使用

> 编译原文：[QTGate/CoNET](https://github.com/QTGate/CoNET)&emsp;作者：[CoNET](https://github.com/QTGate)

CoNET是对抗网络监控的工具。用户通过连接第三方公众邮件服务器，接入CoNET的匿名虚拟网络，它的技术被称为[折射网络](https://zh.wikipedia.org/zh-cn/%E6%8A%98%E5%B0%84%E7%BD%91%E7%BB%9C)，可以帮助用户逃避被网络监控，访问被网络屏蔽的服务器。

![](https://i.postimg.cc/Qd86BH3C/conet-refraction1.png)


## brook

!> brook也可以使用ss的ip地址、端口、密码进行连接互联网，type类型选择shadowsocks即可

进入[逗比ss分享站点](https://doub.io/sszhfx/)，在服务器列表找到brook，打开控制台输入`decodeuricomponent("需要解码URL")`

<!-- ![](https://ipfs.io/ipfs/QmVyHu3fJZNiWXaFL6FcNx2LXDh6rASN4uQVxrjkLc1Ems?4.png) -->

![](https://i.postimg.cc/RZWHbB1G/2018-04-29-004340.png)

将解码的信息填入`setting`选项中，保存后，右键brook程序打开`toggle`选项即可

<!-- ![](https://ipfs.io/ipfs/QmV54Pz3apqZFaiVcnq3K7L2fUXEdciR6XRANcMMr3qphw?4.png) -->

![](https://i.postimg.cc/13V8rKPj/2018-04-29-004903.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmVRpEBVCKUWUBZguT2TYnmxmV4asZtGG7ryHaGwuRCHdn?0.png) -->

![](https://i.postimg.cc/cH06Zy3p/2018-04-29-005228.png)


## reqrypt

!> 目前，reqrypt由于软件原理构造无法应对墙大的处理机制，在国内已经没有使用它的必要了；不过，在其他网络审查不像中国那么严格的地区，常搭配着DNSCrypt一起使用进行穿墙。

> 编译原文：[basil00/reqrypt](https://github.com/basil00/reqrypt) 

ReQrypt是一种隧道和加密Web浏览器请求的工具，可以将它们从本地（例如路由器级别或ISP级别）窥探和拦截中隐藏起来。ReQrypt可用于绕过ISP级别的URL审查/过滤/日志记录系统。

ReQrypt的工作方式与其他旁路方法完全不同。ReQrypt基于称为“三角路由”的技术。简而言之，ReQrypt的工作原理是这样的：

```text
(1) Tunneled request      +----------------+      (2) Forwarded request
           +------------->| ReQrypt server |-------------+
           |              +----------------+             |
           |                                             |
           |                                             V
   +----------------+                             +----------------+
   | PC web browser |<----------------------------|   Web server   |
   +----------------+                             +----------------+
                        (3) Web-page response
```

基本上：

1. 您的Web浏览器向Web服务器发出一个HTTP请求，该请求被加密并隧道传输到ReQrypt服务器
2. ReQrypt服务器解密隧道数据包，并将其转发给网络服务器
3. Web服务器响应HTTP请求，就好像它直接来自您的计算机，并且网页响应通过正常路由发回

通常，HTTP请求直接发送到Web服务器未加密；这意味着它可能会被如您的ISP、工作场所或共享家庭路由器读取或拦截。但在使用ReQrypt时，传出的HTTP请求会被加密并隧道传输，使得它们无法被任何本地窃听者读取。

对于只攻击出站HTTP请求并忽略入站HTTP响应的系统，ReQrypt是有效的。这种系统非常常见的是ISP级别的审查和日志记录系统，因为处理URL流量（HTTP请求）比处理网页响应要容易得多。

最后，与VPN或代理、Tor等不同，ReQrypt不是一个匿名工具。它不会更改隧道数据包的IP地址。这可能是件好事：它意味着Web响应直接发送到您的PC，这意味着ReQrypt通常比其他系统更快。

> 图表来源：[reqrypt官网](https://reqrypt.org/reqrypt.html)

| Filter/Proxy | ReQrypt? | Explanation |
| --- | --- | --- |
| DNS poisoning | ✗ | ReQrypt is overkill for DNS poisoning. Instead reconfigure your system to use a different DNS server, such as [Google Public DNS](https://developers.google.com/speed/public-dns/). |
| DNS blocking | ✓ | This occurs when your provider blocks access to alternative DNS servers. In this case reconfigure your system to use a different DNS server then run ReQrypt with Hiding modeset to "Off" and "DNS Hiding" enabled. |
| IP address blocking | ✓ | Provider blocks certain IP addresses. Use ReQrypt with "Active-Highest" mode enabled. |
| Proxy-ing | ✓ | Provider forces all HTTP traffic through proxy servers. In some cases ReQrypt can completely bypass the proxy servers with "Active-Highest" mode enabled. |
| Hybrid proxy-ing | ✓ | Provider forces some HTTP traffic through proxy servers based on IP address. As above use ReQrypt with "Active-Highest" mode enabled. |
| Hybrid filtering | ✓ | Provider blocks access to certain URLs at the Network level using Deep Packet Inspection \(DPI\). For Network-level filtering only the URLs need to be hidden. Use ReQrypt with "Passive", "Active-Low" or "Active-Medium" modes enabled. |
| Mirror filtering | ✓ | This is similar to hybrid filtering except the provider copies \(mirrors\) rather than selectively redirects packets. As above, use ReQrypt with "Passive", "Active-Low" or "Active-Medium" modes enabled. |
| URL sniffing | ✓ | Provider is sniffing packets to extract URLs for logging or data-retention purposes. User ReQrypt with "Active-Medium" mode enabled. |
| Strong filtering | ✗ | The various strong filtering methods used in countries like China or Iran. ReQrypt is generally ineffective against such systems since they typically block or severely restrict inbound traffic. |

> 编译原文：[issues#15](https://github.com/basil00/reqrypt/issues/15#issuecomment-363946075) 

ReQrypt是一种特殊的技术（单向隧道技术），而且这项技术（大部分）对检测入境流量的强大过滤系统（如在中国和伊朗部署的那些过滤系统）无效。

在多数其他地区，由于政策不同的原因，检查入站流量在ISP级别是不常见的，即：跟踪TCP状态的成本，Web响应流量高，Web响应流量中没有URL，以及基于IP愚蠢的方法进行大规模过度阻塞。但在中国和伊朗等地，他们愿意为此付出代价。

我也听说过一些传闻，ReQrypt确实对中国的一些ISP有效，以及伊朗还做了一些额外的伎俩。据报道，除了审查HTTP之外，还会限制非HTTP流量以阻止规避工具。像[BarbaTunnel](https://github.com/BarbaTunnelCoder/BarbaTunnel/)这样的项目通过HTTP隧道传输以获得全速。

要通过双向隧道强制所有流量，这对ReQrypt来说将是一个不同的项目。这更像是[Tallow](https://github.com/basil00/TorWall)所做的，它是一种通过Tor网络强制所有流量的工具。Tallow可能适用于其他类型的隧道，特别是支持Socks5的任何东西。

> 编译原文：[issues#27](https://github.com/basil00/reqrypt/issues/27#issuecomment-394153872)

是的，见[#15](https://github.com/basil00/reqrypt/issues/15)。ReQrypt从未设计为规避“严格”ISP级过滤器，主动监控入站和出站流量。ReQrypt主要用于在许多国家（包括英国等西方国家）普遍使用更轻量级的基于URL黑名单过滤；因为他们也不希望降低互联网的性能，所以重量级的双向过滤通常是一个禁忌。

对于中国与伊朗的用户，建议基于双向隧道技术寻找更强大的规避技术并保护匿名。

<!-- 
!> 目前，reqrypt由于软件原理构造无法应对墙大的处理机制，在国内已经没有使用它的必要了；不过，在其他网络审查不像中国那么严格的地区，常搭配着DNSCrypt一起使用进行穿墙。
至于barbaTunnel已有多年没更新了，再加上VPN服务器可能自身存在些许问题，使得这款软件不怎么好用；我测试了一下也不是很满意，直白的说就是连接OpenVPN的操作并不成功。
所以，关于这些软件与其所涉及到的一些科学上网相关方面的知识，做个了解也就行了
 -->


## barbaTunnel

!>barbaTunnel已有多年没更新了，再加上VPN服务器可能自身存在些许问题，使得这款软件不怎么好用；我测试了一下也不是很满意，直白的说就是连接OpenVPN的操作并不成功。

BarbaTunnel是点对点非独立的隧道，应在运行BarbaTunnel后运行隧道应用程序或使用标准的VPN连接。如果防火墙阻止VPN连接或防止VPN连接速度降低，那么它可能会对此有所帮助。

> 图片来源：[BarbaTunnelCoder/BarbaTunnel](https://github.com/BarbaTunnelCoder/BarbaTunnel/#barbatunnel-diagram) 

![](https://i.postimg.cc/vmmSKDqk/home-barbatunneldiagram.png)


# 细节补充

## ss#1130

<!-- ![](https://ipfs.io/ipfs/QmZ2145UzK4PSkXcs49sWEwpqksWZb6wRJKioNbd97skSW?4.png)

![](https://ipfs.io/ipfs/QmV4U7c4zZbYaH7vWWWeLfRLshhbC1UwQrmwr6PfWz8yHD?4.png)

![](https://ipfs.io/ipfs/QmQh1CwQzf7Aqfyi9YAcNYhbk7pdwgDHxhLHctGYkUQBm5?3.png) -->

![](https://i.postimg.cc/d095hhm0/2018-05-02-012348.png)

![](https://i.postimg.cc/tg95GXQG/2018-05-02-012640.png)

![](https://i.postimg.cc/FFknZHhT/2018-05-02-012818.png)


## 难封锁的草榴

一个IP指向多个地址，污染一个域名还有另一个域名指向。

<!-- ![](https://ipfs.io/ipfs/QmPkd76acmkTYoi92Bxtb5G5QezHzAoQN8YSmJSz4f2G1v?3.png) -->

![](https://i.postimg.cc/9QzzqZY8/2018-05-02-002837.png)

IP被列入黑名单后，需通过迎春楼贵宾通道，就是VPN隧道协议访问。

<!-- ![](https://ipfs.io/ipfs/Qmf8D6wegWbtbKviSJU1w5tzhn7sYDqJJ7fDtWze77vGaF?0.png) -->

![](https://i.postimg.cc/XNHbBh1W/2018-05-02-002021.png)

若是浏览器不支持远程DNS解析，访问网站很多时候就会先通过ISP默认的DNS解析服务器进行解析，这样ISP就会知道你访问了哪个网站。对于VPN来说DNS很多时候都是本地解析的，所以常有人反映即使用了VPN一些被DNS污染的网站依旧上不了，把默认DNS解析服务器设置为国外的DNS解析服务器就能解决问题。

尽管现在对这类网站打击很严厉，色情网站只能打一枪换一个网址；但在这个圈子里，狼友们会“友爱”互相分享最新网址；这也难怪央视编辑也使用fqrouter顺带着收藏草榴社区还将这个收藏夹在新闻频道分享出来，不过事后重播时已经打马赛克了；相对来说，每次查封黄网都是加强对网络控制。

> 但是，还是回到老问题，大量色情网站把服务器放在国外，而很多人也以外籍身份寻求保护。知乎上也曾经有这么一个提问：“情色网站把服务器放在香港或者美国，警察除了封域名 IP，能抓他们吗？”
>
> 用户 lyac 对此的回答有一定参考意义：
>
> 理论上肯定属于违法，主要手段还是封 IP，因为服务器是境外租用的，所以根本上还是要拆除境外服务，但这个问题又涉及到境外执法，国内警察肯定不能去国外执法了，需要服务器所在国协助，这又涉及到双方国家法制制度，自己合作协议，处理起来比较困难，这就是很多色情网站为何很难清理很干净，色情网站被封后只需再申请一个 IP，指向原来的网站即可，网站数据还是原来的，当然理论上也是能清理的，只是成本高
>
> —— 摘自雷锋网  [草榴社区这类色情网站为什么封不掉 ](https://www.leiphone.com/news/201612/isY4iUwVGppRMsZA.html)


## 简谈杀毒软件

!> 正如前言所说，出现任何VPN、proxy相关软件就挨个演示一遍，这做不到，且真的没必要；**我只能尽量写出思路，提供读者参考，借此而探索以认知，这才是真正的重点。**

如opera这般，其他各类型软件商(不仅仅只限于杀软)为了推广附加了VPN，以此达到使用人数更多的目的，例如：panda、avast等；再比方说以“改善网络及游戏加速为目的”xx加速器为名义卖VPN的等等。

倒是像极了那句话：没有做不到，只有想不到...

![](https://i.postimg.cc/NjpHZTTV/QQ-20190612093300.jpg)

火绒做法比较精明罢了，刚入市的时候以广告推广是以提供浏览器首页的形式，而并不锁定首页；它的[营销方式](#一些题外话-（可看可不看）)很像一加，有兴趣的话，可以在问答网站搜寻下其火热原因，这里不在过多赘述；反正，所有举动背后都是在原有市场上，自己能占有一席之地，分一杯羹；处处都一个德行，人家本来就已经占领了庞大的市场，那为什么还用你的呢？倒不如形成一股清流，让“少数极客及电脑高手”来带动大众，以此做良性的口碑推广。

## 恶意禁用连接互联网服务问题

预先禁用互联网服务是国产杀软也是企业或网吧网管的普遍手法，他们一般会以[注册表](https://baike.baidu.com/item/%E6%B3%A8%E5%86%8C%E8%A1%A8)注入代码的形式到策略组，这里给个参考链接：[bat 启用禁用浏览器代理-通过修改注册表数值](https://cuityang.iteye.com/blog/2438902)；看些官方文档以及相关博客，学习及操作注册表也是很快能入手的；说回重点，如何再改回来。

首先 `windows + r` 输入 `gpedit.msc`， 在`用户配置->管理模板->Windows组件->Internet Explorer`找到`阻止更改代理设置`，进行相关配置即可。

![](https://i.postimg.cc/fR6Ht6qD/Snipaste-2019-06-12-11-06-32.png)

若是 VPN 的话，好多时候有可能是禁用 `Remote Access Connection Manager` 与 `DHCP Client` 服务

!> 注意下方图片荧光笔标记部分的说明

`win + r -> cmd -> services.msc  -> Remote Access Connection Manager`

![](https://i.postimg.cc/XNpDqPNx/Snipaste-2019-06-30-00-22-10.png)

`win + r -> cmd -> services.msc -> DHCP Client`

![](https://i.postimg.cc/C16PJG7j/2019-06-30-002835.png)

只要客户端状态是自动获取IP地址，开启DHCP后，服务器端就会对客户端动态分配IP。如果客户端是手动配置好的IP，那么它就不会再到服务器端申请IP地址了；关闭DHCP后，客户端自动获取IP地址的请求没有服务器响应，自然无法远程分配的IP。

这也就是连上了 VPN 也上不了网的原因，连局域网（中国互联网）都连接不上，更别说进 Google 了。顺带安利两篇关于DHCP的文章：

* [扫盲：DHCP分配形式](http://server.51cto.com/sCollege-147540.htm)
* [dhcp应该开启还是关闭_dhcp关闭会怎么样](http://www.elecfans.com/baike/wangluo/luyouqi/20180307644000.html)

?> 觉得还不够的话，cmd 键入 `ipconfig /flushdns`； `netsh winsock reset` 此指令对不能打开作业系统之外的其他任何软件也有奇效 :-Oヾ(o◕∀◕)ﾉヾ！

![](https://i.postimg.cc/sXfNPbS8/Snipaste-2019-06-12-11-28-17.png)

ps：这里都是设置网络相关服务配置，说不准以后又会在哪，动些手脚呢？

![](https://i.postimg.cc/xCT9kxdj/Snipaste-2019-06-12-11-39-47.png)

还好，现在（其实早就有了）win10在设置中有比重装更可靠的还原功能！或者直接以压缩文件打开原版系统.ISO 再接着双击 `setup` 也可找到！当然，最好把国产杀软卸了吧 @_@


## 谈谈手机的选择及使用

手机厂商为了捆绑各类全家桶APP占据市场份额，以及国内政府严禁使用谷歌各类服务，又因很多爱国工具需要在Google Play商店运行。在这个前提下，想要root是相当困难且不断加强刷机难度，以及手机厂商夸大对刷机危害与对服务保障权益的警告甚至威胁，这也促使了很多人愿意购买国外版的安卓手机。

这让我想到以前使用Nokia逛天网论坛用公牛破塞班软件证书权限那份怡然自得的轻松，与如今刷机还需去官网解除强限制口令，并要大费功夫地去找刷机包以及各种翻来覆去地倒腾很是苦难折磨；而且现在也没心思去花时间刷机，苹果这一块我也懒得砸壳、使用巨魔，这真是一次强烈又深刻的对比。

手机网络热点的网卡可能无法与VPN虚拟网卡类似电脑共享网卡的操作相互绑定在一块，导致共享不了互联网；另外手机共享代理软件给电脑网络需要设置添加端口映射才能访问互联网，何况花生壳不是免费的甚至使用该软件还需要备案，所以也懒得去写手机代理网络给共享电脑相关操作，用热点网络下载一个VPN或代理，电脑自己用就是了何必这么麻烦。
 
在严法监控的制度之下，国内软件公司不可能做出好的软件产品，这也是某些软件搞出国际版的原因之一，当然他们也很想在国外市场分一杯羹，以及在相对自由与完善的法律制度之下，他们会把一些符合国情与垄断国内市场的特色功能去掉，所以国际版软件要比国内版稍好一些，江山易改本性难移，不过未必见得有多良心。

手机使用受限与厂商广告不断在通知栏中出现的各种糟心，软件使用又是强迫各种捆绑的各种无奈，两年之后的安卓手机卡到飞起真不知说什么好。

## 试用并选择爱国软件

!> 建议更安卓手机地区首选项语言，例如修改成含有中文的国家：新加坡；另外“原生”国产机需在设置中开启 GMS 功能。ps：手机没有刷权限的话，选择免费翻墙工具进行科学上网，那就请使用谷歌空间、Turbo、ssr吧，另外 SamsungMax 一直很稳定。

原生安卓手机与共享PC互联网，也可以直接进入[GitHub](https://github.com/)等相关网站搜索此类软件并下载其安装包，然后依此下载Google商店安装并下载相关代理或VPN软件。

相比于PC，手机的代理或VPN时效性要高出不少且软件丰富很多。因此，查找此类软件可以说是一件很简单的事情，主要的难度是在刷机；国产刷机因品牌的不同而步骤不一，以至于过于繁杂，且刷机不是本书主要内容，故不再演示说明。

这里推荐一个Google商店软件下载站:[uptodown](https://www.uptodown.com/android)

## 科技铁幕·赛博朝缅

迟早有一天，为了在国内自由使用集成AI的苹果手机，就和当初初能在国内使用WiFi自由上网一样，不得不找海外代购，又回到了水货时代。买海外版的手机也容易，在B站、youtube 搜索 “如何购买港版苹果设备？” 类似于这种一站式教学一搜就出来了，可不像当初信息收集那般麻烦。

## 徘句·最上川

<dd>今はまさにサイバー朝緬の時代だ。</dd>
<dd>この「潔癖」とは、実は無意識の傲慢にほかならない——</dd>
<dd>歴史とはもはや客観的に起こった出来事ではなく、</dd>
<dd>好き勝手に切り貼りされる栄光の壁でしかない。</dd>
<dd>気に入らないものは抹消する。</dd>
<dd>欲しくないものは存在しなかったことにする。</dd>
<dd>指鹿為馬など、日常の何でもない操作にすぎない。</dd>
<dd>ここでは客観的事実はどうでもよくなり、</dd>
<dd>本当に重要なのは、語りの「純潔さ」なのだ。</dd>
<dd>記憶はフォーマット可能であり、</dd>
<dd>文書は自由に編集でき、</dd>
<dd>歴史と現実の二重の独占権は、</dd>
<dd>こうして語り手の手に握られる。</dd>
<dd>これは単なる改ざんではない。</dd>
<dd>もっと深い虚無である。</dd>
<dd>すべてが書き換えられ、定義され、忘却されることが可能になったとき、</dd>
<dd>残されるのは、空虚で自己慰撫的な「正しい」バージョンだけだ。</dd>


## 关于封锁IP的认为

GFW采用IP地址屏蔽，所有的骨干路由器和国际出口的路由器都添加上了和Google服务有关的IP黑名单，带有相关IP地址的数据包直接在半路就被丢包了，这会给路由器带来很大负担且成本非常高。

GFW采用这种策略多数针对的是社交通讯网站与有政治倾向性的组织党派或组织的站点，这当然也有频繁连接互联网的个人或提供商的服务器IP地址；对于自认为有违和谐且传播面并不是很广的网站，封锁策略并没有采用这种手段，而是采用了一种廉价很多又很有效的DNS污染。

* 网站换一个IP地址，用户基本上感觉不到有什么变化，但换域名会流失大量用户

* 路由器只负责伪造查询结果，比起基于路由器工作的IP地址屏蔽资源消耗要低上很多

尤其是很多国外主流互联网门户网站，根本就不会因为国内用户看不到自己的网站而更换域名失去其他大量用户，这样就使得GFW的DNS污染长期有效了。

不过党的主观能动性调动相当的强，可以说的上是不惜一切代价；毕竟用纳税人的钱造墙，有这强大的经济后盾支持提供技术保障，家国也并不在乎对于他来说也就这点小钱，所以该封的还是会封IP绝不手软，而且没有任何可商榷回旋的余地。

目前来看，从gfwlist更新的`pac.txt`文件得知被屏蔽的域名站点有6969个，这一数字随着时间也仍在不停地增加，也可以说国内基本上已经是一个彻底的局域网了。

通过以下网站可检测IP、域名、端口是否被中国封锁。不过，GFW很少直接封IP，更多是封域名或触发封禁（端口特定被阻）。但一旦IP被封，通常是永久的，除非服务商换IP。端口被封 ≠ IP被封：有些IP只封特定端口（如80/443），其他端口正常。这些工具基于国内服务器节点测试，受GFW影响，偶尔有误判；但结合多个工具结果基本准确。

域名：

* https://viewdns.info/chinesefirewall
* https://www.top10vpn.com/tools/blocked-in-china

IP

* https://www.vps234.com/ipchecker
* https://www.itdog.cn

IP及端口

* https://www.toolsdaquan.com/ipcheck
* https://ping.pe


## 对于校园网的解读

> Dr.com客户端的认证报文分为登录、保持在线和注销等几种，登录报文中含有机器的物理地址、用户名、密码等信息并包括绑定的IP地址；报文的构造是不可控的，这是物理地址绑定的一部分保证，使用校园网客户端时会把所有的子网IP全部发送，若我们连接了路由器或者使用电脑的WiFi共享功能，子网IP就会暴露我们干了什么，服务器会让这个客户端掉线。

> 每过一段时间，客户端会向服务器发送一个维持在线的数据包，所以当我们使用全局的VPN时，这个包会被路由到外网,导致服务器无法按时收到维持在线的请求之后就会开始掉线。

> 摘自及演绎原文：[突破Dr.com校园网客户端对于热点和路由器的限制](https://blog.csdn.net/Angle_Cal/article/details/78249612) 作者：[angle_cal](https://blog.csdn.net/angle_cal)

可以说校园网是集权垄断网络的集中意志的体现，有着更为封闭的局域网网络系统，又一次极大的提升了科学上网的难度；不过，她的文章也提到使用第三方修改报文的客户端与刷路由是可行的。家庭与企业网络难以实施校园网的网络构造的原因，我个人分析为如下几点：

* 企业自身无法完全形成垄断
* 大批的资本家为了自身的利益反对
* 普通平民对此限制的躁动而导致社会强烈的不稳定

当然，若是国家愿意这么不顾一切去做这肥猪赛大象的事，只要它喜欢，它高兴就好。

<!-- 很久没做所谓的学生了，加上当时相关文献资料很少，所以对这块也不是特别清楚只能转载摘录了； -->

<!-- 
我想若是将校园网运用在家庭以及企业网络中，再来个夜晚十一二点断网，那也是对网络先进创新性地改造提升，以及全国人民喜迎夜晚断网，应该不会有人反对且质疑正确的声音，哈哈哈。 -->


## 论及游戏的看法

在国内的法律审查制度催生下的行内企业乃至个人，很多科技事物、文化产业与娱乐行业有怎么可能真的繁荣发展得起来，不过都是外强中干；科技事物有几个是国内在全球领先的，不过多是造轮子骗经费、文化产业是上下五千年对党的到来歌功颂德不得有半点任何不和谐的产物、ps4/xbox等内容毫无建树可言，实在多得不胜枚举。

GFW目前对游戏这块干涉比较少，多数游戏是可以连接各国家/地区的服务器，只不过ping值有些过高而已；倒是游戏厂商很热衷封锁中国IP，连接受到各种限制，港澳台除外了。

这其中的原因，一是国内法律不允许出现任何违背光伟正的事物，二是GFW的DDoS攻击实在太过于恶心了，三是为了规避法律条文的风险，含有歧视成分的因素还是相对较少。谷歌hk就是很好的例子，简体中文强制安全搜索，类似于一国两制了。

一些代理为了更高的销量打着VPN的旗号售卖，而代理与VPN都具有连接外网功能，这也导致了一些人对代理与VPN的认知不清。有良心的代理还会帮你在服务器端做转发UDP，若没有那也只能自认倒霉了，吸取教训下次注意点。

 购买SS账号的有很多也是奔着摆脱封锁与加速游戏去的，结果却需要着手于UDP转发与net类型网络穿透的各种折腾，就显得有些得不偿失了；毕竟代理不是VPN，代理软件不会虚拟一块网卡分配一个IP地址，让所有软件走全局网络。而且此类涉及到socks代理的软件，太容易被游戏厂商当作外挂封杀了。

所以，想爽快体验游戏的话，还是建议购买大厂的VPN服务，各个方面来说比个人或小组织代理的可靠度要高得多。


## 对零网的简要补充说明

ZeroNet中文被译为零网，是一个以[对等网络](https://zh.wikipedia.org/wiki/%E5%AF%B9%E7%AD%89%E7%BD%91%E7%BB%9C)用户为基础构成的类互联网的[分布式](https://zh.wikipedia.org/wiki/%E5%8E%BB%E4%B8%AD%E5%BF%83%E5%8C%96)网络。现该平台上托管了很多热门网站，而新闻与邮件客户端、文件管理器等专有功能也为其生态系统增加了价值。

网站由特殊的"ZeroNet URL"可以被使用一般的浏览器通过ZeroNet程序浏览，就像访问本地主机一样。由于ZeroNet去中心化的原因,用了ZeroNet后,并没有一台服务器是真实的服务器,任何访客都有可能成为服务器,还有些访客使用了Tor,更找不到真正的物理地址。

ZeroNet利用比特币加密和BT技术提供不受审查的网络与通信的BT平台，ZeroNet网络功能已经得到完整的种子的支持和加密连接，保证用户通信和文件共享的安全；但zeronet默认不匿名，用户可以通过内置的Tor功能进行匿名化。

采用比特币形式的账号很安全，只要不是个人泄露证书几乎完全盗不走；基于p2p原理只要建立网站并有人浏览过，即使是服务器关闭的网站也依然在全球存在。

原理细节方面，其所涉及的各方面的知识过多，技术实现也是相当的复杂，且目前暂无完整的相关中文文档对此的说明；本人学识远远不够，也只能勉强补充做个关于zeronet的简要说明了。

另外多说几句，由于国内的审查制度以及GFW无法有效的干扰拦截其内部网络，该软件在中国被封禁，需通过科学上网进行下载与初步的使用；不过，近期相关消息来看，GFW特征识别貌似察觉到了什么，看来这真的是一个喜迎油价上涨的好消息...


## 宿主机使用VM的代理

!> 虚拟机使用宿主机代理，不用设置额外VMware的转发，只需添加代理的地址与端口
手机也能使用虚拟机所配置的本机代理服务器，不需要同宿主机设置专属的VMware转发
除默认配置的仅主机模式外，宿主机使用VPN会影响全局网络，虚拟机可以直接访问互联网
虚拟机采用的是非全局性的独立网络，也因此在虚拟机使用VPN并不能使宿主机也能够访问互联网

在NAT模式中，虚拟机通过宿主机器所在的公网网络来访问互联网（目前在墙内），vm使用代理软件转发端口监听任意地址，主机在代理中配置同一公网内的局域网IP与端口，完成网络之间的互联共享。以下是具体实例：

在NAT模式中不考虑使用VPN或代理的情况下，IP地址是完全一致的

<!-- ![](https://ipfs.io/ipfs/QmPgX1CEGGAkCGiG6eD5ujWysQ9iBhV2iTqn8hNmZV4upT?2.png) -->

![](https://i.postimg.cc/y6nWLsnS/2018-05-13-005931.png)

在vm中开启v2ray以及配置privoxy相关参数`0.0.0.0:8118`监听任意地址开启的`8118`端口，将所有http流量再转发至本机代理

<!-- ![](https://ipfs.io/ipfs/QmVvZ3tL2jX5NizhrctG7FFFBDYJVDu3pbgB8JGDrrduvj?2.png) -->

![](https://i.postimg.cc/2SnDXxmX/2018-05-12-065612.png)

在vm设置代理本机地址与privoxy代理的监听端口

<!-- ![](https://ipfs.io/ipfs/QmZHt9U6eiYkSrjiU3npR7pCuTi8HVTcEFGy26p5uY9JU7?1.png) -->

![](https://i.postimg.cc/rFrXK9dF/2018-05-13-013525.png)

查看vm局域网地址

<!-- ![](https://ipfs.io/ipfs/QmPPBiFHzDh7crMrLCfvDc9f6B5v13P4zygPhdDhBxg2Wj?0.png) -->

![](https://i.postimg.cc/wBT9ym8f/2018-05-13-014622.png)

VMware设置端口映射

<!-- ![](https://ipfs.io/ipfs/QmZhNJ9bMbuSp9DSPpZHyzmkbBD3DAZNLKqdAYNLhh4814?1.png) -->

![](https://i.postimg.cc/fy44K3ph/2018-05-13-0153pxcx.png)

宿主机中设置代理，填入vm的IP地址与端口

<!-- ![](https://ipfs.io/ipfs/QmTJ8f5AAMX3ak1u78sBXPzYyBUTVoxwSYfsy4ixfcdnKT?2.png) -->

![](https://i.postimg.cc/P57SZg0g/2018-05-13-02xsdf.png)

测试

<!-- ![](https://ipfs.io/ipfs/QmaREa4sCZgTLZ7xqdUh45TuSieGbtyvHp6P9JXGRkqv9Q?2.png) -->

![](https://i.postimg.cc/bJ906WFN/2018-05-13-021830.png)


## SS二级（前置）代理设置

> 原文：[SS二级（前置）代理设置实现中转加速观看BBC iPlayer](https://www.itengli.com/ss-relay/) 作者：[夏天](https://www.itengli.com)

有些时候，我们的shadowsocks代理直连速度比较慢。例如，我们想要用英国代理来观看BBC iPlayer，如果直接用shadowsocks连接英国节点，在很多网络下速度并不理想。这个时候，如果我们有其他节点速度非常快，比如香港节点（阿里云）、维也纳节点等，就可以利用这些速度快的代理作为中转，加速我们的目标代理的连接速度。在这里，我们以维也纳节点作为前置代理，以英国节点作为目标代理来说明一下如何用shadowsocks实现中转。原理如下图：

![](https://i.loli.net/2019/06/06/5cf8d8e90b7b017028.png)

了解原理之后，下面的设置就很简单了。
第一，由于需要两个代理，你需要同时打开两个shadowsocks客户端，所以，你要需要复制一份。为了避免冲突，请将两个客户端分别放入两个不同的文件夹内。
第二，先打开一个客户端，连接维也纳节点。（系统代理模式选择不修改系统（IE）代理）
第三，再打开另外一个客户端，此时会提醒你端口被占用，先点击确定，连接伦敦节点。端口占用的原因是shadowsocks默认本地端口都是1080，两个同时打开必然会冲突。所以你需要修改这一个客户端的本地端口为1081（可以任意选择端口，只要不和其他程序占用相同端口即可）。同时填写二级（前置）代理信息。这部分参数设置为：右键小飞机→选项设置 。 请参照下图填写：

![](https://i.loli.net/2019/06/06/5cf8d9178597669922.png)

第四，启用这个伦敦节点客户端代理就行了（这里系统代理模式选择全局模式） ，然后就大功告成了！
打开 https://www.bbc.co.uk/iplayer 测试：

![](https://i.loli.net/2019/06/06/5cf8d983a308d69299.png)


## ss、ssr、v2ray链接解析

?> 网上有很多人会分享一些免费的 ss、ssr 免费账号，也有少数分享v2ray的；有的会直接把服务、端口、ip、协议等展示出来，直接手动输入相应参数就可以了，有的则直接显示二维码，直接用客户端软件扫一下就可以使用。
不过，也有很多是直接以链接的形式展示出来，比如 ss://xxxxx 或 ssr://xxxx,对于这种链接的方式，复制链接后，直接使用ss 、ssr客户端右键从粘贴板导入url链接即可。

## SS链接

以ss链接为例，链接如下：

`ss://YWVzLTI1Ni1jZmI6S1NYTmhuWnBqd0M2UGM2Q0A1NC4xNjkuMzUuMjI4OjMxNDQ0`

用[base64解码站长工具](http://tool.chinaz.com/Tools/Base64.aspx)（此工具存在和谐因素，仅为演示方便）进行解码

![](https://i.postimg.cc/W3Vkrt3d/2018-06-07-131159x.png)

![](https://i.postimg.cc/ZKny6GTx/2018-06-07-132540.png)

从这两幅图也不难看出格式其实是这样的 `ss://method:password@server:port`，按照这个格式的写法并进行base64编码，就能将ss分享给对方使用。

![](https://i.postimg.cc/fT1kmkqM/2018-06-07-142343.png)

若是分享二维码，可以用[二维码生成器](https://www.qrstuff.com/)将ss链接嵌入二维码中扫描分享

![](https://i.postimg.cc/7hGwZnk0/2018-06-07-141818.png)

## SSR链接

再来看ssr的url，链接如下：

```text
ssr://NjQuMTM3LjIyOC4zNTo1NzYwOmF1dGhfc2hhMV92NDpjaGFjaGEyMDp0bHMxLjJfdGlja2V0X2F1dGg6Wkc5MVlpNXBieTl6YzNwb1puZ3ZLalUzTmpBLz9yZW1hcmtzPTVweXM1WVdONkxTNTZMU201WS0zNXAybDZJZXFPbVJ2ZFdJdWFXOHZjM042YUdaNEx3
```

使用[base64工具](https://1024tools.com/base64)解码

![](https://i.postimg.cc/cJzsyzq0/2018-06-07-145222.png)

 字符串包含`–`，需在解码前把`–`这个字符通通替换为`+`字符

![](https://i.postimg.cc/3wzHbDpw/2018-06-07-150006.png)

效果如下

![](https://i.postimg.cc/Jzgg1Ch6/2018-06-07-150327.png)

再来看ssr链接导入的截图

![](https://i.postimg.cc/4NyBn2qr/2018-06-07-150608.png)

由此得知，格式如下

`ssr://ip:port:protocol:method:blending:password/?remarks=other text`

有时也会看到部分解码后，这样的格式

```
159.65.1.189:5252:auth_sha1_v4:rc4-md5:http_simple:NTJzc3IubmV0/?obfsparam=&protoparam=&group=d3d3LnNzcnNoYXJlLmNvbQ&remarks=RE1fTm9kZQ
```

这其中`obfsparam`、`protoparam`、`group`、`remarks`等都是可选的，也可不填。

![](https://i.postimg.cc/76PSdfyp/2018-06-07-160125.png)

## v2ray链接

其实v2ray链接与相关二维码生成与上述方法是差不多的，只是配置参数格式大同小异而已。v2ray不像ss那样有统一规定的url格式，所以各个v2ray图形客户端的分享链接或是二维码不一定通用

v2ray的链接如下

```
vmess://ew0KICAicHMiOiAicnVzc2lhbi1jbG91ZCIsDQogICJhZGQiOiAiMTg1LjE3Ny4yMTYuMTM0IiwNCiAgInBvcnQiOiAiMjI1MzUiLA0KICAiaWQiOiAiNTIwNTAwNTctZjVlMS00YjllLWI3OGItNWY0OWI1NDlmZDIxIiwNCiAgImFpZCI6ICI2NCIsDQogICJuZXQiOiAia2NwIiwNCiAgInR5cGUiOiAic3J0cCIsDQogICJob3N0IjogIiIsDQogICJ0bHMiOiAiIg0KfQ==
```

进行base64解码之后再对比v2ray客户端的参数配置就显得一目了然

![](https://i.postimg.cc/85sbKtW2/2018-06-08-223349.png)

可以说大体是这么一个格式

```json
{
  "ps": "别名",
  "add": "ip地址",
  "port": "端口",
  "id": "uuid",
  "aid": "alterid",
  "net": "传输协议",
  "type": "伪装类型",
  "host": " http header参数",
  "tls": "底层传输安全"
}
```

 除别名外，可以说服务器与客户端的参数必须要相互对应，别名、留空的是可以省略的。按照这个相关格式生成base64编码。

![](https://i.postimg.cc/pXBnjK5z/2018-06-08-233637.png)

在base64编码首部加上`vmess://`协议头

```text
vmess://ewogICJhZGQiOiAiMTg1LjE3Ny4yMTYuMTM0IiwKICAicG9ydCI6ICIyMjUzNSIsCiAgImlkIjogIjUyMDUwMDU3LWY1ZTEtNGI5ZS1iNzhiLTVmNDliNTQ5ZmQyMSIsCiAgImFpZCI6ICI2NCIsCiAgIm5ldCI6ICJrY3AiLAogICJ0eXBlIjogInNydHAiCn0=
```

将其导入至v2ray客户端，在服务器未作其他相关变更时，即可成功连接服务器。

![](https://i.postimg.cc/mDTvPxvQ/2018-06-08-235033.png)

当然添加别名更好，这样就能v2ray客户端就能自动生成相应的v2ray链接

![](https://i.postimg.cc/cLX9FK28/2018-06-08-235553.png)

## SSR对SS的兼容

至于ssr与ss兼容性的问题参考逗比的解答

> 原文：[关于Shadowsocks的小白常见问题](https://doub.io/ss-jc35/) 作者：[逗比](https://doub.io/author/toyo/)

> **取消协议兼容原版后，**当你的ShadowsocksR服务端配置了**协议**后，只能ShadowsocksR的客户端**选择对应的协议才可以连接**\(SSR客户端选择原版协议也是无法连接\)，而使用Shadowsocks原版客户端无法连接。

> 只有你设置ShadowsocksR服务端的协议为**原版\(origin\)**，那么才能ShadowsocksR客户端\(选择原版协议\)和Shadowsocks客户端都能链接你的ShadowsocksR服务端\(账号\)。

> 目前ShadowsocksR服务端是，**auth\_aes128\_\*** 及以后的协议 都不支持兼容原版了，之前的协议可以兼容原版，混淆也都可以兼容原版。

> 当然了，这只针对 ShadowsocksR的协议，对于混淆参数是无所谓的，协议和混淆是可以分开的，你可以协议不设置兼容原版，而混淆设置兼容原版，或者不设置协议，而只设置混淆兼容原版，都可以，不存在协议开了，混淆也必须开的问题。

总而言之，ssr可以使用ss的服务器，但ss使用ssr的服务器的话，却未必行得通；顺便也多说一句：ssr是可使用ss链接与扫描二维码的（别没事整什么动态的短链接就行了...），反之则不生效。

我个人认为ssr倒像一个ss的升级版，是这样的一个关系：

![](https://i.postimg.cc/1RrpGkL8/2018-06-08-011429.png)

在了解这些，那么开始进行演示，打开[ssrshare论坛的小工具网页](https://tool.ssrshare.com/tool/free_ssr)

![](https://i.postimg.cc/7hjDGsMw/2018-06-08-014905.png)

图中的origin协议、plain混淆都是支持原版ss的，选择其中一个进行复制ss链接

![](https://i.postimg.cc/t70QC1pg/2018-06-08-020234.png)

将其解码

![](https://i.postimg.cc/VN58gPGm/2018-06-08-023014.png)

由于我们得知ss与ssr的链接格式：

`ss://method:password@server:port`

`ssr://ip:port:protocol:method:blending:password`

将解码后的ss的格式转成ssr的格式

![](https://i.postimg.cc/vZ2RcSQj/2018-06-08-024019.png)

对其编码

![](https://i.postimg.cc/zfhd8d3T/2018-06-08-024834.png)

加入`ssr://`链接协议头，再导入至ssr并不成功，原因是密码都套上一层base64编码...因此需要对密码进行一次编码

![](https://i.postimg.cc/jdJn8B16/2018-06-08-030909.png)

之后，按照原有格式将部分参数配置粘贴至密码前，进行编码

![](https://i.postimg.cc/d0J7V3Vn/2018-06-08-031437.png)

再加入`ssr://`链接协议头，导入至ssr即可如：

`ssr://MTM5LjU5LjE2Ny4yNDY6NjIwMzpvcmlnaW46YWVzLTI1Ni1jZmI6cGxhaW46YVM1M2RYY3VjbVZr`

![](https://i.postimg.cc/x1nHctsK/2018-06-08-032054.png)

## v2ray对ss的兼容

ss连接v2ray的服务器，需在v2ray服务端做相应的ss兼容配置；至于v2ray连接其本身兼容ss的服务器，可能需要配置uuid等验证机制。

> 配置参数摘录自：[V2Ray替换shadowsocks服务器详解](https://www.daehub.com/archives/2156.html) 作者：[大隐中心](https://www.daehub.com/)

```json
"inboundDetour": [
{
    "protocol": "shadowsocks", // 开启 Shadowsocks
    "port": 30001, // 监听 30001 端口
    "settings": {
    "method": "aes-256-cfb", // 加密方式，支持 aes-256-cfb 和 aes-128-cfb
    "password": "v2ray", // 密码，必须和客户端相同
    "udp": false // 是否开启 UDP 转发
  }
  },
  {
    "protocol": "shadowsocks", // 开启 Shadowsocks
    "port": 30002, // 监听 30002 端口，由于 Shadowsocks 的限制，多用户的时候只能开多个端口
    "settings": { // 配置和上述类似
    "method": "aes-256-cfb",
    "password": "v2ray-2",
    "udp": false
  }
}
],
```


## 用Win7，电脑就是路由器

> 原文：[用Win7，电脑就是路由器](http://blog.sina.com.cn/s/blog_6286984e0100kujt.html) 作者：[微软Windows的博客](http://blog.sina.com.cn/s/blog_6286984e0100kujt.html)

在平常上网过程中，难免会遇到一些网络方面的问题，这时候我们就需要查看网络连接的状态，查找问题根源。

<!-- ![](https://ipfs.io/ipfs/QmQtXLa5xLbqNsdv82cVYJA8hE9greNXR34FUfkENjoDND?4.jpg) -->

![](https://i.postimg.cc/tCYPPsyg/a12d690.jpg)    
在WinXP中，大家这时候都会从开始菜单或控制面板打开“网络连接”窗口来检查网络问题，但对于一个Win7新手来说，找到这个窗口似乎有点困难，在控制面板中搜索“网络连接”也找不到它。这时候，大家应该想到的就是上次介绍过的“网络和共享中心”，因为这里集中了网络相关的常规配置，在这里能不能找到线索呢？

试试点击左上方的“更改适配器设置”任务吧，瞧，“网络连接”窗口原来藏在这里，这时候我们就可以和XP中一样查看到计算机中网卡的设置和状态了：

<!-- ![](https://ipfs.io/ipfs/QmPQopQc63jx7VJ6x5DVzAShK3XbfsDLA2ZMictCSdWMcx?0.jpg)   -->

![](https://i.postimg.cc/Nf3yHbpN/e88p690.jpg) 

但有的同学可能会发现，在这些网卡当中多了一个叫“Microsoft Virtual WiFi Miniport Adapter”的东西，按名字来看似乎是微软的虚拟Wifi网卡。电脑中怎么会无缘无故多了这么一个东西呢？难道又一个Win7的隐藏功能被发现啦？

没错，这的确是Win7中深藏不漏的新功能——“虚拟Wifi”，不好意思在前面给大家卖了很大一个关子。简单来说，Win7能在现有无线网卡的基础上再虚拟出一块无线网卡，支持网络共享，让我们的电脑变成无线路由器哦！看来如今“虚拟”真是无处不在啊。

有的同学可能知道，在此之前，其实也可以建立临时网络向其他Wifi设备共享互联网啊，虚拟 Wifi 网卡有什么新的优势呢？

<!-- ![](https://ipfs.io/ipfs/QmbDefgaVGHeDwmMdbS4BGi27r8wpYNwzNHJZpWWUBXTQJ?0.jpg)   -->

![](https://i.postimg.cc/Jz3hB8yn/a3et690.jpg) 

传统的临时无线网（即Ad Hoc模式）是一种点对点网络，类似于有线网中的“双机互联”，虽然也能实现互联网共享，但主要用于两个设备临时互联，并且有的设备（如采用Android系统的设备）并不支持连接到临时无线网。还有一个很严重的问题，由于一块无线网卡只能连接到一个无线网络，因此如果通过无线网卡连接到Internet，就不能再使用这个无线网卡建立临时网络，共享Internet了。

而Win7中的虚拟Wifi功能可以在一块真实无线网卡基础上再虚拟出一块网卡，实现无线路由器的 AP功能，解决了临时网络的所有问题。

这么诱人的功能，现在赶紧教给大家：

1. **以管理员身份运行命令提示符**

    因为下面的步骤必须在管理员权限下运行，因此我们从开始菜单找到“命令提示符”，或直接键入cmd快速搜索，右键单击它，选择“以管理员身份运行”，在弹出的用户控制窗口中单击“是”。还有一种方法就是按住Ctrl和Shift键直接单击该快捷方式，更简单哦。

2. **启用并设定“虚拟Wifi网卡”模式**

    运行以下命令启用虚拟无线网卡（相当于打开路由器）：

    `netsh wlan set hostednetwork mode=allow ssid=”Win7 AP WOW!” key=wifimima`

    <!-- ![](https://ipfs.io/ipfs/QmaMeEgS3zw7VeCXrcxAyRdiQPhynYVaanbWJT6Q1Y2bYo?1.jpg)  -->
    
    ![](https://i.postimg.cc/9QB7HZYJ/cd41e690.jpg) 

    这个命令中有三个参数：

     * Mode：是否启用虚拟Wifi网卡，改为`disallow`则为禁用，虚拟网卡即会消失。

     * Ssid：指定无线网络的名称，最好为英文。

     * Key：指定无线网络的密码。该密码用于对无线网进行安全的WPA2加密，能够很好的防止被蹭网。

3. **启用“Internet连接共享（ICS）”**

    为了与其他计算机或设备共享已连接的互联网，我们需要启用“Internet连接共享”功能。打开“网络连接”窗口，右键单击已连接到Internet的网络连接，选择“属性”，切换到“共享”选项卡，选中其中的复选框，并选择允许其共享Internet的网络连接在这里即我们的虚拟Wifi网卡：

    ![](https://i.postimg.cc/jSvLFKR1/d1de690.jpg)
    
    确定之后，提供共享的网卡图标旁会出现“已共享”标志，表示“Internet连接共享”向虚拟无线网卡开通了：
    
    ![](https://i.postimg.cc/5tYbSMyL/e2f690.jpg)

4. **开启无线网络**

    继续在命令提示符中运行以下命令：

    `netsh wlan start hostednetwork`

    即可开启我们之前设置好的无线网络（相当于打开路由器的无线功能。同理，将start改为stop即可关闭该无线网）。

    <!-- ![](https://ipfs.io/ipfs/QmZGdo9UjyEKx5v3pSzKaTvTeFonGRwVs6wR7NdXinfraw?0.jpg) -->

    ![](https://i.postimg.cc/ZKMQFvds/et6ae690.jpg)

    可以看到，虚拟无线网卡已经开启了我们所指定的无线网络，其IP地址等属性是由“Internet连接共享”服务分配的，因此比较特别：

    <!-- ![](https://ipfs.io/ipfs/QmSykUE1kpTVbUiiGnn3QoSyokGfpsTR7mwSE3HiSTr1SL?4.jpg) -->

    ![](https://i.postimg.cc/Qtfm8vgY/c17ec690.jpg)

    一切准备就绪，最后只要在需要联网的的电脑或手机上连接该无线网络，就可以直接畅游互联网了：

    <!-- ![](https://ipfs.io/ipfs/QmR3wMDpsf4MngKbRWuiw8s8BAednxzGWhUcCpqy3tn2Ed?1.jpg) -->

    ![](https://i.postimg.cc/RZmgT10R/dcd690.jpg)
    
需要多说一点的是，虚拟Wifi网卡需要真实网卡的驱动程序专门针对Windows 7设计开发。所幸只要通过Win7徽标认证的无线网卡驱动程序都支持该模式，我们在选购无线网卡时直接寻找是否带有该标志即可。如果在运行`mode=allow`命令后，网络连接中没有出现虚拟无线网卡，就说明真实网卡不支持该功能。大家可以将网卡驱动升级到最新的Win7版本试试看，只要提供共享的电脑不休眠不关机，就可以和路由器一样提供网络共享。

除了使用命令设置虚拟WIFI功能，微软还将其编程接口公开了出来，为开发图形化设置程序提供了可能，例如免费小软件Connectify就能直观的设置虚拟Wifi功能，同学们可以在其官方网站下载使用：[www.connectify.me](http://www.connectify.me/)

<!--分别替换启用“Internet连接共享（ICS）的图片即可  -->
<!-- ![](https://raw.githubusercontent.com/hoodiearon/fq-book/master/docs/images/d1de690.jpg)-->

<!-- ![](https://raw.githubusercontent.com/hoodiearon/fq-book/master/docs/images/e2f690.jpg) -->

<!-- ipfs 启用“Internet连接共享（ICS）的图片-->
<!-- ![](https://ipfs.io/ipfs/QmQkAtXoff2tp8uiRbpGNwAA4hTbCqm8uRGjXmayWP1RcN?4.jpg)   -->

 <!-- ![](https://ipfs.io/ipfs/QmagdtNek1pwCGB6syXtf46WY6MuJFcrJieS9W623NFUik?0.jpg) -->


## 初次搭建网站多次失败后的成功记录

内容包含了相关参考站点的链接，部分操作细节有所省略，旨在提供参考和说明，而非作为手把手的教程。

## VPS与环境选择

2U / 2G / 50GB / 5Mbps，年费约 800–1000 元；域名年费 250–280 元。常见 VPS 平台：LightNode、DigitalOcean、Hostinger、Vultr。

* [VPS 带宽选择指南](https://vpszhijia.com/服务器带宽多少合适)
* [注册域名与 Cloudflare 托管](https://doc.laopobao.online/domain)
* [自托管平台对比：Cloudron / YunoHost / Sandstorm](https://www.bayescafe.com/tools/self-hosting-platform-comparison.html)（推荐使用 Cloudron）
* [1Panel 管理面板](https://1panel.cn/)
* [Nginx UI](https://nginxui.com/zh_CN/)
* [Micro 编辑器](https://github.com/zyedidia/micro)
* [Caddy 简介](https://blog.motorbottle.site/archives/168)
* [Docker 中文参考](https://dockerdocs.xuanyuan.me/reference)

免费主机：

* https://run.claw.cloud
* https://www.serv00.com

**关于 VPS 与无服务器部署的思考**

如今已经不太推荐使用 VPS。原因如下：

1. 无服务器（Serverless）平台已经相当成熟，不仅提供免费额度，超出部分的计费也十分友好。对于大多数中小型项目而言，这些服务完全能够满足日常需求。
1. 在部署策略上，无服务器最理想的场景是静态化服务，例如静态博客或前端页面；若确实需要运行后端服务，国内的云服务商同样提供了价格低廉、性能稳定的选择。
1. 国外云服务器虽然可以免备案直接使用，但访问速度远不如国内。而若是为了科学上网等用途，选择机场服务通常比自建 VPN 更划算。

综合来看，在当前环境下，VPS的性价比已经大幅下降，不再是首选方案。

## bluesky建站部署

目前有两大协议去中心化社交：AT协议的bluesky和ActivityPub的mastodon，但mastodon实在太烂了。

bluesky启动地址：https://bsky.app

参考内容：

* [[軟體教學] 自架 Bluesky PDS 伺服器，促進去中心化社群發展](https://tedliou.com/software/bluesky-pds-server-deploy/#bluesky-pds-%E4%BC%BA%E6%9C%8D%E5%99%A8%E6%9E%B6%E8%A8%AD%E5%BF%83%E5%BE%97)
* [自己架設Bluesky PDS 並使用自己的Domain建立帳號](https://avantiblog.tw/self-hosting-a-bluesky-pds/#%E8%A8%AD%E5%AE%9ADNS_domain%E8%88%87%E7%AE%A1%E7%90%86%E5%93%A1%E4%BF%A1%E7%AE%B1)
* https://github.com/bluesky-social/atproto/issues/1752

SMTP 服务邮箱:

* https://resend.com
* https://www.brevo.com

bsky.app第三方启动器：https://tabtter.jp

在使用 Resend 发送邮件时，如果出现“域名未验证”的错误，通常是因为 域名验证流程未完成。要正确验证域名，需要注意两点：

1. DNS 记录对应：在自己的 DNS 服务商中添加 Resend 提供的域名记录时，必须确保记录的域名（主机名/网域）与 Resend 要求完全一致。
2. 控制台验证：添加完 DNS 记录后，还需要回到 Resend 控制台点击 “Verify DNS Record” 进行验证，Resend 才能确认域名已经生效。

只有满足这两步，域名验证成功后，才能正常使用该域名发送邮件。

```env
#將YOUR_API_KEY_HERE換成上一部給你的 API Keys
PDS_EMAIL_SMTP_URL=smtps://resend:re_your_key@smtp.resend.com:465/
#將 admin@example.com 替換成 SMTP 發信地址
PDS_EMAIL_FROM_ADDRESS=admin@hoochanlon.space
# 测试效果时，取消邀请机制
PDS_INVITE_REQUIRED="false"
# 编辑完，重启服务
systemctl restart pds
```

## Memos 搭建记录

Memos 是轻量级的自托管笔记系统。新版 UI 不太合我意，因此我选择回退旧版。

### Docker 原理图

```
+-------------------------------------------------+
|                  宿主机                         |
|                                                 |
| 访问地址: http://服务器IP:5230                   |
|                                                 |
|  +-----------------------------------------+    |
|  |             容器: MEMOS                  |    |
|  | 应用: MEMOS                             |     |
|  | 内部端口: 5230                          |     |
|  | 数据存储卷: /data                     |       |
|  +-----------------------------------------+    |
| 本地挂载路径: /var/opt/memos ------------------> |
+-------------------------------------------------+
```

### 部署命令

```yaml
version: "3.8"
services:
  memos:
    image: neosmemo/memos:0.24.0
    container_name: memos
    ports:
      - "5230:5230"
    volumes:
      - ./data:/var/opt/memos
    restart: unless-stopped
```

切换版本命令：

```bash
cd /opt/1panel/www/memos
docker compose down
docker stop memos
docker rm memos
docker compose up -d
```

旧版 UI 截图：

![旧版 Memos UI](https://cdn.jsdelivr.net/gh/hoochanlon/picx-images-hosting@master/imgs/uploads/2025/PixPin_2025-11-05_18-11-00.webp)

虽然有不少衍生项目，但个人兴趣不大：

- [Vespa314/cflow](https://github.com/Vespa314/cflow)
- [blinkospace/blinko](https://github.com/blinkospace/blinko)
- [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)

### Nginx 反代注意事项

若访问反代域名时提示“无法访问”，说明浏览器可能强制使用 HTTPS（443 端口）。  
而你只配置了 HTTP（80 端口）。

**解决办法：**
1. 申请 HTTPS 证书（可用 Cloudflare 或 Let’sEncrypt 免费申请）。  
2. 若浏览器缓存了 HSTS，需清理缓存或使用隐身模式访问。

参考教程：  
[如何申请 Cloudflare 免费 SSL 证书](https://kerrynotes.com/apply-ssl-certificate-from-cloudflare/)

### 域名绑定参考

- [Vercel 域名绑定官方指南](https://docs.tangly1024.com/article/vercel-domain)
- [使用 1Panel 自动申请和续签通配符证书](https://hin.cool/posts/sslfor1panel.html)
- [GitHub Pages 绑定域名问题](https://blog.csdn.net/jinweilin/article/details/79607349?)
- [github.io 绑定域名](https://blog.csdn.net/weixin_45961774/article/details/108402406)


## 关于目前 GFW(墙) 的封锁方式TCP封锁(阻断)猜想

> 原文：[关于目前 GFW(墙) 的封锁方式TCP封锁(阻断)猜想](https://doubibackup.com/wkcjzpyd-2.html) 作者：[逗比](https://dbgjd.com/toyo.html)

对于翻墙界来说，今年真不是个顺利年。从年初的 SSR 停更并删除项目，到后来的数次大规模封禁代理服务器，甚至发展到现在已经成为日常了（GFW 2.0），几乎每天都有人的代理服务器被墙，经常听到各个群组讨论，也是。。哎！好了，说正题。

## 简单说明

自从今年初开始，墙的封锁方式就从**全部协议封锁**改为了**TCP封锁(阻断)**，该封锁方式主要特征为：

**Ping IP正常连通(ICMP协议)，而 TCPing IP连接超时无回应(TCP协议)。**

!> 脑洞：这也挺好的，因为相比以前，现在可以更准确的判断服务器被墙，而不是网络、服务器问题了。 😲 以前你发现代理账号连不上了，你会去 Ping ，然后发现 Ping不通，接着你会怀疑是不是网络问题、服务器问题等，然后验证半天后发现：的确是被墙了。😲
而现在，你只需要 Ping IP 一下，TCPing IP 一下，就能肯定是被墙了。😥

基本上你测试你的服务器 IP 出现这种情况，99%的几率就是被墙了。剩下的 1% 就是防火墙没开放端口之类的配置问题。

## TCP封锁(阻断) 简单解释：

当你的海外服务器 IP 被TCP封锁(阻断)后，你依然可以正常的**向海外代理服务器发送数据**（客户端连接服务端），但是海外代理服务器上的代理服务端在**向你返回数据**的时候，肯定是要经过墙的，而墙发现发送者IP(代理服务器)在黑名单中，于是就会**阻断、拦截**，这样你的**客户端就收不到来自服务端的返回数据了**（SSR上表现为：超时或空连）。

而目前的代理软件基本都是使用 TCP 协议传输的，而TCP协议要传输数据，则先要进行握手环节，而握手自然要有来有回，所以当**墙对海外代理服务器回程TCP阻断**的时候，就会导致**代理客户端与服务端无法完成握手**，自然也无法使用代理了。

## 我认为GFW的封IP原理大概是：

墙是通过分析流量特征，通过各种方法、证据来判断该链接为代理的可能性，当可能性达到不同的程度时，墙做出不同的处理。**假设：**

|首先|墙现在都是实时扫描检测的，检测到一个链接是代理的可能性低于10%，那么就无视。|
|:---|:---|
|其次|检测到一个链接是**代理的可能性高于10%**，则将IP的相关信息（及收集的证据、特征等）记录到数据库中，当下次再发现这个链接时，继续去收集证据判断是否为代理，**最后是代理的几率降低，则无视，是代理的几率增加，则进一步关注。**|
|最后|当检测到一个链接是**代理的可能性高于50%**的时候，可能就会考虑**单独封一个端口**（代理端口），这时候如果你换个端口继续做代理，那么往往很快就会所有端口被封，这就是因为墙根据你这个IP链接以往的几率判断，认为你这个IP链接是代理的可能性进一步增加，例如到了80%，所以就给你TCP所有端口封禁了。|

其实，GFW之所以单独封一个端口，可能原因就是吃不准到底是不是代理，如果你很快就换了端口继续做代理，那么GFW就认为很大概率是代理，于是就可以封禁了。

## 如何补救

而目前这种非一锅端的封禁方式，让一些人脑洞大开，比如：

|ICMP|有人把 TCP 协议数据转换为 ICMP 协议数据传输，能用，**但是缺陷很明显，速度太慢了**，因为协议的限制意味着速度捉急。。。|
|:-:|:-:|
|UDP|有人想 TCP 协议封禁了，那我可以用 UDP 呀，于是就有人尝试 TCP 协议转为 UDP 协议传输，目前这类软件都比较成熟了，以前往往都是拿来做加速或者游戏优化用的，而现在拿来正好！不过国内很多运营商往往都会对** UDP QOS限速**，而想要解决 UDP QOS限速，则需要把 **UDP协议 伪装成 TCP协议**，然而这又是一个**死循环**了，TCP 协议被阻断。|

能把TCP转为UDP的软件有：[KCPTun](https://github.com/xtaci/kcptun)、[Dragonite](https://github.com/dragonite-network/dragonite-java)、V2ray(自带KCP协议)。

**那么除了上面说的两者有缺陷的，还有没有能复活被墙IP的服务器继续做代理呢？**

有的，比如：Goflyway 的WS+CDN模式 和 **8V2ray 的WS+CDN模式。**这两种方法都是依赖于CDN，而想要让 CDN 来中转代理，就需要 WebSocket 技术，Goflyway V2ray 都支持 WebSocket；但光有 WebSocket+CDN 只能算复活被墙IP，无法保证 CDN IP 的安全性(被墙方面)，所以还都需要**HTTP、HTTPS伪装。**

所以在使用 Goflyway 时往往搭配 HTTP伪装，而使用 V2ray 时往往搭配 HTTP HTTPS伪装。这里 HTTP HTTPS伪装可不是 SS SSR 里的 **伪 · HTTP HTTPS伪装**，而是实实在在的网站（或者反向代理来的）。

也就是你浏览器打开域名(这种复活方法必须有域名)**会看到正常的网页**，而代理客户端访问则是建立代理链接。

?> `注意：`CDN 特别是免费套餐的 CDN，国内链接速度往往不如意，如果不在意 或 当备用的可以搭建试试。

## 如何解封？

**有人又会问，IP被墙是永久的吗？会解封吗？**

当然会解封，IP的数量是有限的，封一个就少一个，如果只封不解，**那不成貔貅了？**更何况，换位思考想一下，假设你买了一个月付的海外服务器搭建代理，因为什么原因导致被墙了，那么到期的时候，**你还会续费下去等待墙解封吗？自然不会，半年付、年付同样。**

既然你不会为了等待IP解封而续费下去，那么这个服务器到期后，别人在购买的时候却不一定会是搭建代理的，他可能是正常做网站什么的。

墙考虑到 **海外大量的IDC 和 国内购买海外服务器正常使用者 的体验和情绪**，那就必须要定期解封。

以前还是全协议封禁的时候，我不清楚墙的解封流程，但是今年换成 TCP协议封锁(阻断) 后，经过实验和大量网友的反馈，能猜个大概了。

每个做代理被墙的海外服务器IP，墙都会根据不同情况设定一个**解封时间**（根据情况时间可能不同）。

如果解封时间内该海外服务器IP没有向国内发送数据或者尝试建立代理连接，那么**墙就会解封该IP**。当然解封该IP后不代表就可以继续做代理了，根据实验和大量网友反馈，**被解封的海外服务器IP，短时间内再用于代理用途，往往很快就又会封禁**（非100%，另外间隔时间越长，理论再次封禁几率越低）。

所以大家应该明白了吧？

**如果你的海外服务器 IP 被TCP封禁(阻断)，那么请关闭或者删除服务器上面的代理软件（墙还可能定期对被墙IP的服务器主动探测，所以必须要关闭代理软件。），然后一段时间不理这个服务器，应该就会解封了（不是100%，而且各IP的封禁时间也可能不一样）。**

**这时候又有人问了：我被墙的海外服务器都吃灰两个月了，怎么还没有解封？😵**

这个问题除了我上面最后说过的**几率问题 和 解封时间问题**外，还有个可能导致该情况的原因是：**你是不是有空没空就去试试代理账号能不能用？或者有事没事 TCPing 测试一下解封了没有？**

这个无意的行为，可能会导致墙对你被墙的海外服务器IP **重置解封时间或者说延长解封时间。**

!> `就是说：`当墙发现你被墙的海外服务器IP向国内发送数据或者尝试建立代理连接时，就可能会重置解封时间或延长解封时间。
`另外：`墙还可能定期对被墙IP的服务器主动探测，看看代理软件是否还在运行，所以必须要关闭代理软件。
`注意：`被墙IP解封后，尽量不要再做代理了，否则还是容易被墙IP。如果还要做代理，那么建议更换个代理软件，不要再用以前导致该IP被墙的代理软件了，毕竟能检测封禁一次，就能再封禁第二次，更何况你这个IP还有短时间内被墙过的前科，这更会增加被墙的几率。你要是用习惯了不想换，那么你最起码换个代理端口，至少能多活几天。。。

## 如何避免被墙

目前没有任何一个代理软件可以保证代理服务器IP不会被墙（emm 除了 WS+CDN+伪装），顶多减少被墙几率。以前流行的 SSR 因为已经停更大半年了，没有更新就意味着没办法抵御墙的检测，目前已经不推荐使用了。**建议使用 V2ray、Brook、Goflyway 等代理软件。**

**如果你用习惯了SSR，不想更换，那么：** `

首先 SSR 目前依然是可以正常使用的，不过在热门地区（日本、美国等）被墙几率会高一些。

很多人都是默认只用的 HTTP HTTPS 混淆插件 ，或者客户端写个混淆参数 ，但是这样属于**伪混淆** ，仅仅是将流量伪装成 HTTP HTTPS 流量，并没有实体网站，所以可以被主动探测识破。

因此，在热门地区（日本、美国等）搭建 SSR 代理的，建议要么搭配服务端的 **redirect** 参数做个真实网站（教程），要么就干脆用**原版混淆插件（ plain ）**。

毕竟，对于可以被主动探测的伪混淆，不做混淆反而被墙几率更低，只靠协议来降低流量特征 减少被墙几率。

除了代理软件的选择之外，服务器地区也对被墙几率有很大影响。经过实验和大量网友反馈，目前**日本、美国**等热门地区均是重灾区，**被墙几率远高于其他较冷门地区**的服务器，所以不管你当前用的是什么地区的服务器，如果该地区服务器IP频繁被墙，那么你应该考虑使用**其他地区的服务器**来继续搭建代理了。

而且，不说别人，就我这半年不管自用的服务器还是我网站分享的免费代理账号服务器，美国的永远是被墙最频繁的。

而我免费账号中的四个加拿大，都是 **SSR账号( auth_sha1_v4 + tls1.2_ticket_auth 兼容原版，混淆参数什么的全都没搞)，全天24小时都有人使用，实时链接 30~80 独立IP，实时速度 1MB/s~3MB/s，就这样都没有被墙过。**而美国免费账号，除了 Goflyway 的是 CDN模式，其他的都是几天就GG了。

**简单来说就是：**

要么搭配服务端 **redirect** 参数做个真实网站，要么就用**原版混淆插件 plain。**
建议避开**日本、美国**等热门地区。

另外，**请不要或者尽量减少让国内网站(或服务器)走代理的情况出现**，因为该方式会增加被墙几率。你想一下就知道了，假设你是A，代理服务器是B，你要访问的国内网站是C，那么：

**A通过B访问C，那么A会向B发送数据，B向C发送数据，然后C返回数据给B，B返回数据给A。**

这个过程实际上全程时间很短的，**在墙看来你这个行为很符合使用代理的行为。**

最后，本文你只需要关注的重点为：

* **Goflyway、V2ray 等软件可以复活被墙IP 。**
* **被墙IP有解封时间概念。**
* **被墙IP的服务器，请关闭代理软件并不理服务器一段时间，有几率解封IP。**
* **被墙IP解封后，如果还要做代理，请更换代理软件，否则短时间内可能还会被墙。**
* **墙可能会定期对被墙IP的服务器主动探测代理，所以必须关闭代理软件。**
* **日本 美国等热门地区服务器被墙几率更高，建议避开日本 美国热门地区。**
* **以上均为个人猜测（猜测+实验），不保证准确性，仅供参考。如发现不准确，请与 GFW 相关部门联系。**

———— 本文章由 逗比根据地 战略合作伙伴 GFW 提供实验数据


## 浅谈HTTP劫持、DNS污染的影响及解决办法

> 原文：[浅谈HTTP劫持、DNS污染的影响及解决办法（仅个人理解）](https://doubibackup.com/6t3mypbm-5.html) 作者：[逗比](https://dbgjd.com/toyo.html)

首先我们说一下“墙：防火长城”，它是由 互联网科学家（比如：方滨兴）、工作人员、五毛、分布式超级计算机、三大运营商组成的。

我们可以看到，墙并不是一个独立的单独存在的一个组织，而是由国内各领域的互联网重要结构组成的。

!> `互联网科学家：`专门研究如何低成本高效率的更有效的过滤审核。
`工作人员：`一些非机器替代的人工操作，比如人工审核。
`五毛：`五毛。
`分布式超级计算机：`要知道每一秒经过大陆各国际出口经过的流量是非常庞大的，需要很多超级计算机进行运算过滤。
`三大运营商：`这个是最重要的组成部分，没有运营商的支持，墙就是个屁。大陆各国际出口都是三大运营商建立和控制的，如果他们不点头，墙又如何在“大门口”（国际宽带出口处）建立“过滤审核检查站”，当然运营商也是国家控制的，所以还是一家人。

所以，墙就相当于在 **大陆的各个国际宽带出口处建立的 过滤审核检查站。**

还有我发现一个很有趣的事情，很多人以为**只有中国和朝鲜存在墙，这很无知。**

如果你把 屏蔽Google、Facebook、Youtube、Twitter的国家 就当作这个国家存在墙的话，那我无话可说。

**墙或者说 互联网防火长城，是任何一个拥有互联网主权国家的必备组成。**

如果你的国家没有墙，没有信息审核过滤机制，那政权随时可能推翻，这不是吹牛，有好几个国家的总统或者总理因为不注重这个问题，导致不仅下位还坐牢了。

美国是个自称最自由的国家，所以他就没有墙了吗？不，他们对盗版网站，儿童色情网站等也是屏蔽。

还有韩国，在互联网方面最发达的国家之一，同样也是针对色情行业大力清理屏蔽。就算是越南、缅甸、泰国，这种互联网相对不发达的国家，依然存在墙。

墙是必然的，你不可能阻止墙的存在，只是我们的墙更高一些，我并不是为 中国防火长城 开脱什么，我只是阐述墙必须存在的事实。

我们之所以感觉我们的墙更高，一是，我们生活在这个国家的墙内，我们经常碰触到墙；二是，我们也是属于审查最严格的那一类国家。

**同时墙也是一种变相的保护国内互联网产业的发展，否则微博，百度哪那么容易发展起来。**

**因为一些话太敏感，不能说的太直白，否则就要拆水表了，理解不了就反过来站在领导人的角度思考，所以上面说的你们能理解多少那就是多少吧。**

## HTTP劫持

大家都知道，我的 dou-bi.com 域名在前段时间的G20期间被HTTP劫持和DNS污染了，而我也简单的研究了一下这两个。

HTTP劫持很容易理解，因为HTTP传输协议是明文的，并且我的网站服务器是在海外，要访问我的网站就要通过中国的国际宽带出口，出去与我的网站建立连接。

但是那G20期间因为戒严，所以加强了HTTP关键词审查，我的网站也是因为关键词的原因在经过出口的时候，被“**检查站：墙**”扫描到了违规关键词，于是掐断了TCP链接。

所以当时用户访问网站会遇到：**链接已重置、该网站已永久移动到其他地址等等。**

## 解决方法

而HTTP劫持很容易解决，那就是**加上SSL证书，网站链接全部内容加密**，这样“检查站：墙”就无法解密数据分析关键词了。

但是这不是绝对能解决这个问题的，如果你的网站只是误杀或者违规擦边球，那还好，如果是大型网站，就会特殊对待了。

HTTPS在建立加密连接的时候，需要一次握手，也就是达成链接协议建立加密连接，但是这次握手是明文的（建立加密链接首先就是链接双方信任，比如网站的SSL证书是自己签的，或者SSL证书到期或伪造的，在访问这个网站的时候浏览器就会进行提示，表示此网站不安全啥的。）

握手是明文的就意味着，如果你的域名被重点关注，**即使你加上了SSL证书，也会在首次握手的时候，被关键词匹配然后掐断链接。**

**还有一种方式，就是域名备案，使用国内服务器。**这样用户在访问你的网站时，根本不需要经过墙，自然也没有了拦截。

## DNS污染

**DNS污染，又称为域名服务器缓存污染**（DNS cache pollution）或者**域名服务器快照侵害**（DNS cache poisoning）。

**DNS污染**是指一些刻意制造或无意中制造出来的域名服务器分组，把域名指往不正确的IP地址。

一般来说，网站在互联网上一般都有可信赖的域名服务器，但为减免网络上的交通，一般的域名都会把外间的域名服务器数据暂存起来，待下次有其他机器要求解析域名时，可以立即提供服务。一旦有相关网域的局域域名服务器的缓存受到污染，就会把网域内的电脑导引往错误的服务器或服务器的网址。

## 原理解析

我们假设**A为用户端也就是你的电脑设备，B为DNS服务器，C为A到B链路中一个节点的网络设备**（路由器、交换机、网关等）。

然后我们模拟一次被污染的DNS请求过程。

A访问一个网站，比如 `google.com` ，然后，A向B通过UDP方式发送查询请求，比如查询内容 `A google.com` ，这个数据库在前往B的时候要经过数个节点网络设备比如C，然后继续前往DNS服务器B。

然而在这个传输过程中，C针对这个数据包进行特征分析，（DNS端口为53，进行特定端口监视扫描，对UDP明文传输的DNS查询请求进行特征和关键词匹配分析，比如“google.com”是关键词，也或者是“A记录”），从而立刻返回一个错误的解析结果（比如返回了 `A 233.233.233.233` ）。

众所周知，作为链路上的一个节点，**网络设备C 必定比真正的 DNS服务器B 更快的返回结果到 用户电脑A**，而目前的DNS解析机制策略有一个重要的原则，就是**只认第一**。因此 节点网络设备C所返回的查询结果就被 用户电脑A当作了最终结果，于是用户电脑A因为获得了错误的IP，导致无法正常访问 `google.com `。

验证污染
我的 doub.ssrshare.usm 主域名虽然在大部分地区解除了DNS污染，但是我的两个SS站域名并没有，所以我尝试对我的SS 子域名进行nslookup测试。

```bash
C:\Users\Administrator>nslookup ss.dou-bi.com 8.8.8.8
服务器: google-public-dns-a.google.com
Address: 8.8.8.8
 
非权威应答:
名称: ss.dou-bi.com
Addresses: 200:2:9f6a:794b::
8.7.198.45
```

我使用的是谷歌的 8.8.8.8 DNS，但是我得到的A记录 IP却是8.7.198.45，这个明显不是我的IP，看一下其他被DNS污染的域名就会发现都会有这个IP。

所以很明显，我的 ss.dou-bi.com 域名受到了DNS污染。

## 解决办法

**使用加密代理**，比如Shadowsocks，在加密代理里进行远程DNS解析，或者使用VPN上网。

**修改hosts文件**，操作系统中Hosts文件的权限优先级高于DNS服务器，操作系统在访问某个域名时，会先检测HOSTS文件，然后再查询DNS服务器。可以在hosts添加受到污染的DNS地址来解决DNS污染和DNS劫持。

**通过一些软件编程处理**，可以直接忽略返回结果是虚假IP地址的数据包，直接解决DNS污染的问题。

如果你是Firefox用户，并且只用Firefox，又懒得折腾，直接打开Firefox的远程DNS解析就行了。在地址栏中输入：`about:config`找到 `network.proxy.socks_remote_dns` 一项改成true。

**使用DNSCrypt软件**，此软件与使用的OpenDNS直接建立相对安全的TCP连接并加密请求数据，从而不会被污染。
对于被DNS污染的网站站长来说，最有效的方法就是 换域名或者IP 了。

对于被DNS污染的网站站长来说，最有效的方法就是 **换域名或者IP** 了。

## 污染攻击大事记

!> 2010年3月，当美国和智利的用户试图访问热门社交网站如 http://facebook.com 和 http://youtube.com 还有 http://twitter.com 等域名，他们的域名查询请求转交给中国控制的DNS根镜像服务器处理，由于这些网站在中国被封锁，结果用户收到了错误的DNS解析信息，这意味着防火长城的DNS域名污染域名劫持已影响国际互联网。
2010年4月8日，中国大陆一个小型ISP的错误路由数据，经过中国电信的二次传播，扩散到了整个国际互联网，波及到了AT&T、Level3、Deutsche Telekom、Qwest Communications和Telefonica等多个国家的大型ISP。
2012年11月9日下午3点半开始，防火长城对Google的泛域名 http://google.com 进行了大面积的污染，所有以 http://google.com 结尾的域名均遭到污染而解析错误不能正常访问，其中甚至包括不存在的域名，而Google为各国定制的域名也遭到不同程度的污染（因为Google通过使用CNAME记录来平衡访问的流量，CNAME记录大多亦为 http://google.com 结尾），但Google拥有的其它域名如 http://googleusercontent.com 等则不受影响。有网友推测这也许是自防火长城创建以来最大规模的污染事件，而Google被大面积阻碍连接则是因为18大 。
——摘取自：知乎

当然，DNS污染的大事件肯定不会只有这几个，但是这也说明了DNS污染的力量和危害之大。

## ip黑名单

即使没有DNS污染 或者 你获得了正确的IP，你就能正常访问这些被屏蔽的网站了吗？

不，墙目前已经有了IP黑名单，针对谷歌这种网站已经不再是普通的DNS污染了，因为总会有办法访问被DNS污染的网站（比如指定Hosts）。

那么就直接把所有的谷歌IP拉黑不就好了？就算你获得了正确的谷歌IP，但是当你去访问这个IP的时候，墙会发现这个IP存在于黑名单中，于是直接阻断，于是浏览器就会提示：www.google.com的响应时间过长等等。

当然谷歌的IP非常多，而且有很多都是隐藏的。

像Goagent、XX-NET、Hosts方式访问谷歌或者其他被屏蔽的网站，都是使用的谷歌IP，当大量谷歌IP被拉黑后，这三种方式就会衰败。

现在这三种方式依然在不停的扫描那些隐藏的谷歌IP，但是谷歌IP再多也不是无穷无尽的，迟早会消耗完毕，坐吃山空。到时候就是这几种方法的死期了。

在普通用户扫描的时候，“墙”中的工作人员和超级计算机何尝也不是在扫描？正是看到了这种依赖于谷歌IP方式的末路，所以我网站到现在也没有一篇和这几种方式有关的教程和文章。

以上的言论仅为个人理解，只为共享以方便讨论交流，具体事实是如何，自行探索。


# 此书后记

## 后记

本书名灵感来自于[Allen Carr](https://en.wikipedia.org/wiki/Allen_Carr)所撰写的[《Only Way to Stop Smoking Permanently》](https://g.co/kgs/PFMMeG)，中文译为“这本书能让你戒烟”。虽然译名有夸大之嫌，但确实，作为长不长短不短已有六年烟龄的我通过此书的帮助下成功地戒掉烟瘾。当然，也离不开戒烟群管理员老陆与老蒙对我的辅导帮助。

连接互联网成为可能，信息加密与流量混淆有着密切的关系，至少目前不敢封根域名服务器；但瓷若条件成熟的话，说不准会建成真正的局域网:-O

网络是填不完复杂到极点的坑，GFW长城应该说是分布式入侵信息监控系统，原理及手法相当高明，再加上各种屏蔽词条与相关技术讨论的封锁等；由此，我觉得对一个非专业且追求免费自由连接互联网的人来说，面对一个强大的POWER与high tech集于一身的GFW，本身就是极为不公平的存在，自然也就毫无justice可言了。

其实这些事物本来是用来享受畅玩乐趣的，如今对我们而言，却需要掌握足够的专业知识与拥有较长的实操经验，变成了耗时耗精力且极其折腾的一件事，不得不说这是种无Fa可说的悲哀...

有人认为造墙是为了挡住和我们同需使用互联网产品的“愚民”，还有些人也想当然的认为：连这个都不会，还做什么程序员、运维员 blablabla；我觉得这些想法都是非常愚蠢至极的认知，只是着重点不同而已，他们只是没花大量时间专留心这一方面罢了，并不代表其他领域要比这些想当然的家伙弱多少，甚至要超出很多。这和我之前即兴翻译 《I am the best》 的故事，本质上是差不多的。


# 参考文献

## 文献列表

!> 文献列表顺序排名不分先后，由于参考文章实属过多，难免有些遗漏，对此表示诚挚的歉意

* [维基模板-突破网络封锁技术](https://zh.wikipedia.org/wiki/Template:%E7%AA%81%E7%A0%B4%E7%BD%91%E7%BB%9C%E5%B0%81%E9%94%81%E6%8A%80%E6%9C%AF)
* [网络封锁技术方案与反网络封锁技术方案](https://docs.google.com/document/d/1n79DOFLdUTSUtzASiN1TaxSF7SWuXqoZvwyM-SO6W7c/preview)
* [别以为有vpn我找不到你（网警抓人全过程）](http://www.91ri.org/3599.html)
* [GFW原理和封锁技术](https://xuranus.github.io/2017/10/09/GFW%E5%8E%9F%E7%90%86%E5%92%8C%E5%B0%81%E9%94%81%E6%8A%80%E6%9C%AF/)
* [翻墙路由器的原理与实现](https://docs.google.com/document/d/1mmMiMYbviMxJ-DhTyIGdK7OOg581LSD1CZV4XY1OMG8/mobilebasic?pli=1)
* [详解防火墙ISA策略元素](http://blog.51cto.com/yiding/272872)
* [TCP/IP四层模型和OSI七层模型](https://www.debugrun.com/a/RNeZIpB.html)
* [meek流量混淆原理](https://www.google.com/search?q=meek%E6%B5%81%E9%87%8F%E6%B7%B7%E6%B7%86&oq=meek%E6%B5%81%E9%87%8F%E6%B7%B7%E6%B7%86&aqs=chrome..69i57.7285j0j9&sourceid=chrome&ie=UTF-8)
* [功夫网原理不靠谱的DNS](https://www.google.com/search?newwindow=1&ei=dljzWqzhDNCYsAfUwKewAQ&q=%E5%8A%9F%E5%A4%AB%E7%BD%91%E5%8E%9F%E7%90%86%E4%B8%8D%E9%9D%A0%E8%B0%B1%E7%9A%84DNS&oq=%E5%8A%9F%E5%A4%AB%E7%BD%91%E5%8E%9F%E7%90%86%E4%B8%8D%E9%9D%A0%E8%B0%B1%E7%9A%84DNS&gs_l=psy-ab.3...76416.76416.0.76712.1.1.0.0.0.0.0.0..0.0....0...1c.1.64.psy-ab..1.0.0....0.vXslcuUhfQQ)
* [上网限制和翻墙基本原理](http://blog.021xt.cc/archives/85) 
* [科学上网的原理](https://segmentfault.com/a/1190000011485579) 
* [科学上网的软件原理](https://fanzheng.org/archives/2)
* [dnsmasq+Stunnel+sniproxy加密代理](http://www.cnblogs.com/yanxinjiang/p/7486314.html)
* [VPN隧道协议PPTP、L2TP、IPSec和SSLVPN](https://blog.csdn.net/cymm_liu/article/details/16889457)
* [写给非专业人士看的Shadowsocks简介](https://vc2tea.com/whats-shadowsocks/) 
* [[计算机网络]简易http server程序](http://www.hoohack.me/2016/10/28/lcn-simple-server)
* [端口映射和端口转发的区别？](http://www.elecfans.com/dianzichangshi/20171204593654.html)
* [用Win7，电脑就是路由器](http://blog.sina.com.cn/s/blog_6286984e0100kujt.html)
* [NAT类型科普及一些简单提升NAT类型的方法](http://www.xuxiaobo.com/?p=4243)
* [四种NAT的iptables实现](http://os.51cto.com/art/201103/249324.htm)
* [NAT 类型及检测方法](https://my.oschina.net/u/945874/blog/371562)
* [VMware的3种网络模式](http://net.zol.com.cn/115/1158058.html)
* [“深网”和“暗网”的区别及基础扫盲](http://chitanda.me/2016/08/19/difference-between-deepweb-and-darkweb/)
* [草榴社区这类色情网站为什么封不掉](https://www.leiphone.com/news/201612/isY4iUwVGppRMsZA.html)
* [突破Dr.com校园网客户端对于热点和路由器的限制](https://blog.csdn.net/Angle_Cal/article/details/78249612)
* [浅析 正向代理 反向代理 透明代理](https://www.logcg.com/archives/929.html)
* [岳昕：致北大师生与北大外国语学院的一封公开信](https://github.com/sikaozhe1997/Xin-Yue)
* [Why Decentralization Matters](https://medium.com/@cdixon/why-decentralization-matters-5e3f79f7638e)
* [王伟兵的博客](https://github.com/wbwangk/wbwangk.github.io/wiki/IPFS)
* [对去中心化网络的信仰](https://www.kawabangga.com/posts/2226)
* [IPFS+IPNS+个人博客搭建](http://www.liyuechun.org/2017/11/21/ipfs-blockchain-blogger/#52-%E8%8A%82%E7%82%B9ID%E6%9B%BF%E6%8D%A2)
* [ipfs](https://ipfs.io/ipfs/QmV5ZVQxXURKPDcVDW8WjpLCiQYvNzg173XcB6rYFevoXm/#!index.md)
* [CoNET](https://github.com/QTGate/CoNET#conet)
* [reqrypt](https://github.com/basil00/reqrypt#reqrypt)
* [what is barbatunnel?](https://github.com/BarbaTunnelCoder/BarbaTunnel/#what-is-barbatunnel)
* [Deploy V2ray To Heroku](https://github.com/onplus/v2hero/wiki/Deploy-V2ray-To-Heroku)
* [shadowsocks-heroku](https://github.com/onplus/shadowsocks-heroku#shadowsocks-heroku)
* [hadowSocksShare Heroku部署方法](https://github.com/the0demiurge/ShadowSocksShare-OpenShift#heroku-%E9%83%A8%E7%BD%B2%E6%96%B9%E6%B3%95)
* [ss、ssr链接解析，查看对应密码、端口、协议](https://coderschool.cn/2498.html)
* [V2Ray替换shadowsocks服务器详解](https://www.daehub.com/archives/2156.html)
* [关于Shadowsocks的小白常见问题](https://doub.io/ss-jc35/)
* [SS二级（前置）代理设置实现中转加速观看BBC iPlayer](https://www.itengli.com/ss-relay/)
* [浅谈HTTP劫持、DNS污染的影响及解决办法（仅个人理解）](https://doubibackup.com/6t3mypbm-5.html)
* [关于目前 GFW(墙) 的封锁方式TCP封锁(阻断)猜想](https://doubibackup.com/wkcjzpyd-2.html)
* [计算机网络基础知识](https://blog.csdn.net/A993852/article/details/90954068)
* [集群、分布式、负载均衡区别](https://www.cnblogs.com/xzwblog/p/7255364.html)
* [扫盲：DHCP分配形式](http://server.51cto.com/sCollege-147540.htm)
* [dhcp应该开启还是关闭_dhcp关闭会怎么样](http://www.elecfans.com/baike/wangluo/luyouqi/20180307644000.html)
* [亚洲诚信-什么是服务器名称指示](https://www.trustasia.com/fwqmczs)
* [TCP/IP、HTTP协议的区别](https://www.jianshu.com/p/f4db4eb065bd)
* [Mozilla-内容安全策略( CSP )](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CSP)
* [阮一峰-Content Security Policy 入门教程](http://www.ruanyifeng.com/blog/2016/09/csp.html)
* [Youtube - 星环无限「Rinfinity」](https://www.youtube.com/@%E6%98%9F%E7%92%B0%E7%84%A1%E9%99%90)
* [ipdodo - 2026最新修复指南：解决电脑翻墙后chrome浏览器无法使用谷歌gemini问题](https://www.ipdodo.com/news/15150/)


