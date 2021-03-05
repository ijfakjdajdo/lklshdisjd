Android
lan-tianxiang edited this page 6 days ago · 4 revisions
申明
经测试，受到手机电量管理策略的影响，安卓下的定时任务似乎有点抽风，有时候能准时运行，有时候又不能准时运行。

如果被手机杀掉了进程，那么所有定时任务都不会执行了。

每次重启手机或重启Termux后需要重新手动启动crond程序。

绝大部分手机在一段时间不使用以后，将进行低功耗状态，这个状态下，所有程序都将受限，那么自然定时任务也就不会运行了。这种情况在晚上睡觉时尤其明显。

建议安卓运行脚本只做为其他脚本运行方式的一种补充，比如在有类似家电星推官时，可以在手机上运行以达到手动准时运行的效果。

手机无需Root即可使用本方法，只是不Root时，看日志可能不是特别方便，Root后可以通过手机的文件管理器查看。

更新说明
2021-2-18 已经重写安卓Termux的教程部分并做了更新，90%以上的正常安卓手机都能够运行（配置达到Termux的安装要求即可）
准备工作
想办法安装好谷歌服务框架，注意：需要科学上网条件。

从谷歌商店搜索并安装 Termux。

从这里学习 Termux 的基础用法，这其中介绍的 termux-ohmyzsh 一定要装，能显著减少手机上的输入活动。另外，也建议按照该教程进行：切换为国内源、美化终端、允许访问手机外置存储等操作，其他部分也建议多看多学。

安装依赖
切换为国内安装源后，在Termux中输入：

pkg upgrade
pkg install git perl nodejs-lts wget curl nano cronie
针对Termux输入麻烦，多多使用Tab键自动补全是个好习惯。termux-ohmyzsh也是一个神器，启用后可以帮助输入。

下载脚本
前提：

Termux的家目录为：/data/data/com.termux/files/home，一般家目录用~这个符号代替，这个家目录位于手机的内置存储中。

按照上面Termux教程中允许访问手机外置存储的操作后，家目录下会有一个storage的软连接（~/storage），storage中有个shared文件夹（~/storage/shared），连接的就是手机的外置存储。

在手机没有进行root的情况下，一般的文件管理器仅能查看外置存储的文件，无法查看内置存储的文件。

经测试，在没有ROOT时，本脚本只能在内置存储中运行，在外置存储中无法正常运行。而在ROOT以后，脚本可以在外置存储运行，但需要额外安装一个包：

  ```
  pkg install tsu
  ```
在手机没有ROOT时，只能在Termux命令行中查看日志，或者将日志使用cp命令复制到外置存储后查看。

脚本下载：

一键克隆（可能需要科学上网条件）：
git clone https://github.com/lan-tianxiang/jd_shell jd
脚本会自动在jd下克隆下脚本并创建日志文件夹，分别如下：

log: 记录所有日志的文件夹，其中跑js脚本的日志会建立对应名称的子文件夹，并且js脚本日志会以年-月-日-时-分-秒的格式命名。

scripts: 从 lxk0301/jd_scripts 克隆的js脚本。

scripts2: 从 lan-tianxiang/jd_scripts 克隆的js脚本。

修改参数
cd ~/jd
mkdir config/
cp sample/termux.list.sample config/crontab.list     # 复制computer.list.sample从sample到config目录下crontab.list(此为定时文件)
cp sample/config.sh.sample config/config.sh      # 复制config.sh.sample从sample到config目录下config.sh(此为参数文件)

nano config/config.sh                   # 编辑config.sh，内含详细的注释.如果不习惯，请直接使用可视化编辑器编辑这个文件
nano config/crontab.list                # 编辑crontab.list，内含详细的注释.
注意：

请不要直接修改config.sh.sample！而只修改config.sh。

config.sh和crontab.list都内含详细的注释，请按照流程编辑后切记保存

参数清单，如何修改请仔细阅读config.sh中的注释。 参数清单：Parameter，如何修改请见git_pull.sh中的注释。

你可以按上面方式直接在nano中修改参数，但可通过其他途径将必要的信息复制过来粘贴（Ctrl + O 保存，Ctrl + X 退出）；

也可以将config.sh复制到外置存储卡，用其他可视化文件编辑器修改好后，再复制回来；

甚至还可以参考上述Termux教程，在运行sshd服务程序后，通过局域网内的电脑，使用WinSCP软件连接手机进行修改。

初始化
在编辑好config.sh这个文件后，请务必手动运行一次git_pull.sh，不仅是为检查错误，也是为了运行一次npm install用以安装js指定的依赖。

完成所有信息修改以后，先检查一下git_pull.sh能否正常运行。

cd ~/jd
chmod +x *.sh
bash git_pull.sh
注1：.sh脚本如果没有可执行权限，虽然手动执行可以运行，但定时任务将无法正常运行。

注2：首次运行的日志很重要，如果过程中有任何错误，请参考错误提示来解决问题。主要包括两类问题：一是无法访问github，请想办法改善网络；二是git_pull.sh会运行npm install，用来安装js指定的依赖，如果你网络不好，日志中会有提示，请注意观察。如果npm install失败，请尝试手动运行，可按如下操作，如果失败，可运行多次：

cd ~/jd/scripts
npm install || npm install --registry=https://registry.npm.taobao.org
看看js脚本的信息替换是否正常。

cd ~/jd/scripts
git diff    # 请使用上下左右键、Page Down、Page Up进行浏览，按q退出
然后你可以手动运行一次任何一个以jd_开头并以.sh结尾的脚本（有些脚本会运行很长时间，sh本身不输入任何内容在屏幕上，而把日志全部记录在日志文件中）。

cd ~/jd
bash jd.sh jd_bean_change
去~/jd/log/jd_bean_sign文件夹下查看日志，查看结果是否正常，如不正常，请从头检查。

cd ~/jd/log/jd_bean_sign
ls   # 列出文件
cat 2020-11-13-12-00-00.log  # 假如ls列出的文件名是这个的话
如需要使用手机的文本编辑器打开这些日志，在没有ROOT时，可以先将其复制到外置存储后，在文本编辑器中打开。假如要查看上面这个日志~/jd/log/jd_bean_sign/2020-11-13-12-00-00，可按如下操作：

cp ~/jd/log/jd_bean_sign/2020-11-13-12-00-00.log ~/storage/shared/Documents/
上述命令会将这个日志文件复制到外置存储的Documents文件夹下（这个文件夹必须事先存在）。文件名长就多使用Tab~~

如果不想写入日志文件，想直接在Termux中看到输出，那么可以如下操作：

cd ~/jd/scripts
node jd_bean_sign.js
添加定时任务
在添加定时任务之前，请先熟悉一下手机上cronie这个软件的用法（你也可以随时输入crond -h查看此帮助）：

~/jd crond -h
Usage:
crond [options]

Options:
-h         print this message
-i         deamon runs without inotify support
-m <comm>  off, or specify preferred client for sending mails
-n         run in foreground
-p         permit any crontab
-P         use PATH="/data/data/com.termux/files/usr/bin"
-s         log into syslog instead of sending mails
-V         print version and exit
-x <flag>  print debug information

Debugging flags are: ext,sch,proc,pars,load,misc,test,bit

根据帮助文档，如果想要以deamon形式启动cronie，那么可以输入：

crond -ipP
请注意：每次重启手机或重启Termux后需要重新输入上述命令。

如果输入上述命令后显示类似以下内容的错误，那么表示cronie已经启动好了，无需再次启动：

crond: can't lock /data/data/com.termux/files/usr/var/run/crond.pid, otherpid may be 3087: Try again
启动好cronie后，再按以下流程添加定时任务。

复制一份crontab.list到~/jd目录下。

cd ~/jd
cp sample/termux.list.sample config/crontab.list
编辑定时任务并自己根据你的需要调整，

nano config/crontab.list
请注意将crontab.list这个文件中的/root目录替换为/data/data/com.termux/files/home/jd。 路径主要还是为PC考虑的，手机就请自己修改下吧。以下命令可以批量修改：

perl -i -pe "s|/root|/data/data/com.termux/files/home/jd|g" crontab.list
添加定时任务。

crontab config/crontab.list
做到这里，请再次回过头去查看申明部分，请理解在安卓手机下，定时任务不一定准时运行，并且还要注意不要被手机杀掉Termux后台进程。

如何测试定时任务的运行情况。

先在家目录创建一个文件：

touch ~/date.log
然后在你编辑好的crontab.list中再编辑一下，额外增加一条定时任务如下：

* * * * * date >> ~/date.log
更新crontab:

crontab ~/jd/config/crontab.list
增加的这一条定时任务如果正常运行，会在每分钟的第0秒将当前时间写入~/date.log这个文件。你可以在手机在各种情况下都存在过一段时间以后，查看这个文件：

cat ~/date.log
仔细看看定时任务的运行情况。

说明

crontab.list这个文件必须存放在~/jd/config下。

第一条定时任务/data/data/com.termux/files/home/jd/git_pull.sh会自动更新js脚本和shell脚本，并完成Cookie、互助码等信息修改，这个任务本身的日志会存在/data/data/com.termux/files/home/jd/log/git_pull.log中。更新过程不会覆盖掉你已经修改好的git_pull.sh文件。

第二条定时任务/data/data/com.termux/files/home/jd/rm_log.sh用来自动删除旧的js脚本日志，如果你未按下一节自动删除旧日志中操作的话，这条定时任务不会生效。

划重点：电量优化策略
这就是手机上运行定时任务的难点了，请各位各显神通，授予Termux无限制的后台策略，常见的有：允许常驻后台，允许后台联网，无限制的电量优化等等。至于做了这些操作以后，Termux是否仍然偶尔抽风，那我就不得而知了。

但即使这样，遇到特殊情况时，不仍然可以进入~/jd/scripts/后手动运行js脚本吗？

如果有个旧的安卓手机，是不是可以考虑一直充电放家中，无限制地运行此脚本？

补充说明
物理机如需多账号并发，需要创建多个jd.sh，然后分别重命名后如jd2.sh后修改内里面config文件地址运行上述命令，然后也复制并重命名config下的config.sh都按下面说明配置一下，并且在制定定时任务时，你配置了多少个jd.sh，那么同一条定时任务就要重复几次（因为.sh脚本文件不一样）。
如果想要重新调整定时任务运行时间，请不要直接使用crontab -e命令修改，而是编辑~/jd/crontab.list这个文件，然后使用crontab /home/myid/jd/crontab.list命令覆盖。这样的好处脚本会自动依靠这个文件来增加新的定时任务和删除失效的定时任务。

如果shell脚本有更新，需要你手动复制一份config.sh.sample，并重新修改必须的信息，然后命名为config.sh，流程如下（以docker为例）：

cd ~/jd
cp sample/config.sh.sample config/config.sh

# 然后修改config.sh，也可使用其他可视化工具修改
nano config.sh

# 不要忘记赋予修改后的.sh脚本可执行权限
chmod +x git_pull.sh
手机上的git在运行时总会弹出一个警告如下：

warning: Pulling without specifying how to reconcile divergent branches is discouraged. You can squelch this message by running one of the following commands sometime before your next pull:

git config pull.rebase false  # merge (the default strategy)
git config pull.rebase true   # rebase
git config pull.ff only       # fast-forward only

You can replace "git config" with "git config --global" to set a default preference for all repositories. You can also pass --rebase, --no-rebase, or --ff-only on the command line to override the configured default perinvocation.
如果想要永久消除这个提示，按它说明的操作方式输入一下命令即可：

git config --global pull.rebase true
如有帮助到你，请点亮 star 。
