## 以下为v3版脚本的更新日志

2020-12-19，重写v3版脚本：

    ```txt
    1. 减少了代码量；

    2. 降低了配置复杂度；

    3. 减少了操作步骤，v3版脚本任何平台任何时候修改配置，修改完就可以了，不用再运行什么东西，修改配置后的所有定时任务将自动读取修改后的配置；

    4. 增加了使用gitee代替github去同步lxk0301大佬的jd_scripts脚本；

    5. 针对不需要准点运行的任务，增加了随机延迟，随机延迟上限由用户自行确定；

    6. 现在手动运行也可以看到输出日志了；

    7. 原有的重要功能自动增加删除定时任务仍然在的，同样也仍然允许用户自行修改自己的定时任务，脚本只增加或删除定时任务条目，不会修改定时任务。
    ```

2020-12-23，晚20点多更新错误造成bug，有可能造成后面无法再自动更新脚本，如果发现存在此问题（现象是git_pull.log中没有新的日志内容了），解决办法附下：

- 如果是docker，在docker宿主机运行一下：docker exec -it jd git pull， 即可解决此问题。不过也因此建议docker用户一定要安装watchtower来自动更新，这样我会在出错后重新更新容器才让大家直接自动完成容器更新。

- 如果是物理机或手机termux，cd到脚本存放目录后运行一次：git pull， 即可解决此问题。

- 下次我一定先测试好没问题再发布，以避免类似问题发生。

2020-12-24，增加导出互助码的一键脚本`export_sharecodes.sh`，老用户需要参考仓库的sample文件添加自己的cron方可使用。

2020-12-30，增加自动挂机功能，如需使用，在运行过一次`bash git_pull.sh`以后，输入`bash jd.sh hangup`即可（docker要进入容器后输入），然后挂机脚本就会一直运行。如果你希望每天终止旧的挂机进程，然后启动新的挂机进程，请参考sample文件夹下各个平台 的list中的挂机定时任务，添加到自己的`crontab.list`中。目前仅一个`jd_crazy_joy_coin.js`为挂机脚本。

2020-12-30，增加`config.sh`和`config.sh.sample`文件差异智能比对的脚本，使用方法详见WIKI。

2021-01-04，Docker启动时即自动启动挂机程序，Docker允许将`/jd/scripts`映射出来。

2021-01-06，Docker用户增加在线编辑`config.sh`和`crontab.list`功能，启动容器时直接启动，详见最新WIKI。

2021-01-15，如果本机上安装了pm2，则挂机程序以pm2启动，否则以nohup启动。

2021-01-21，增加shylocks/Loon脚本。

## 以下为原v2版脚本的更新日志，后续将不再维护

> 只记录大的更新，小修小改不记录。

- **2020-11-10：lxk0301/scripts 已被封，新的库为 [lxk0301/jd_scripts](https://github.com/LXK9301/jd_scripts)，所有在这时间之前的老用户请按 [#26](https://github.com/EvineDeng/jd-base/issues/26) 重新配置一下！！**

- 2020-11-11：已构建多平台docker镜像，包括：linux/amd64, linux/arm64, linux/ppc64le, linux/s390x, linux/arm/v7, linux/arm/v6。树莓派、N1小钢炮等arm设备均可使用。

- 2020-11-13：重新用Perl语言改写sed命令，脚本已经可以兼容Android、MacOS。

- 2020-11-15：为保持跨平台兼容性，把`Docker`的`shell`也更换为`bash`，Docker用户需要删除原来的镜像重新部署方可正常使用。
    ```shell
    docker stop jd
    docker rm jd 
    docker rmi evinedeng/jd-base
    ```
    无需重新配置，直接按原来的`docker run`命令重新部署即可恢复原有内容。

- 2020-11-20：增加 [799953468](https://github.com/799953468) 大佬开发的脚本，原地址：https://github.com/799953468/Quantumult-X ，需要按照新的`git_pull.sh.sample`重新配置为`git_pull.sh`方可使用。另外，游戏未开通的需要先开通：京东app首页搜索“边玩边赚”，进去后找“东东工厂”和“泡泡大战”。

- 2020-11-23：增加每日签到接口延迟时间自定义功能；增加每日签到关闭通知和简洁通知的控制开关；增加`User-Agent`自定义功能。如需要使用上述功能，需要按照新的`git_pull.sh.sample`重新配置为`git_pull.sh`方可使用。

- 2020-11-24：1.增加摇钱树是否发送通知的控制开关；2.增加摇钱树是否自动卖出金果的控制开关；3.修改安卓相关代码。前两项新功能需要按照新的`git_pull.sh.sample`重新配置为`git_pull.sh`方可使用。

- 2020-11-25：1.删除额外的脚本功能；2.lxk0301大佬已经增加东东工厂脚本，跟随上游，添加两个控制参数：定义东东工厂是否静默运行、定义东东工厂心仪的商品。需要按照新的git_pull.sh.sample重新配置为git_pull.sh方可使用新功能。首页搜索“边玩边赚”，进去找东东工厂查阅具体玩法。

- 2020-11-26：增加京喜工厂、东东工厂助力码相关功能，需要按照新的`git_pull.sh.sample`重新配置为`git_pull.sh`方可使用新功能，或者将本次增加的内容增加到你已有的git_pull.sh中也可以使用。

- 2020-12-09：将部分临时活动InviteCode修改为我的互助码，已得到lxk0301大佬同意。

- 2020-12-13：rm_log.sh增加删除指定时间以前的git_pull.sh和crond运行日志的功能。

- 2020-12-14：增加定义宠汪汪参加比赛类型的功能，如果需要使用此功能，请重新将`v2.3.11`版本的git_pull.sh.sample配置为git_pull.sh，或者直接在你原来的git_pull.sh中增加`teamLevel`参数。

- 2020-12-16：1. 增加jd_jdzz（京东赚赚）和jd_joy_run（宠汪汪赛跑）的长期定时任务，当`AutoAddCron=true`时，短期任务会自动添加的。2. 将用户提供的所有Cookie中的PIN附加在`jd_joy_run.js`文件中，这样你的各个账号之间将相互助力宠汪汪赛跑，在助力完成你的账号以后，再给我和lxk0301大佬的账号助力，每个Cookie助力可得30g狗粮。

- 2020-12-17：增加jd_watch（京东发现-看一看）的初始任务，该脚本内置了80个body，不过建议有能力者自行抓包，以防止有可能的黑号，抓包教程及使用方法详见该脚本内的注释说明，引用如下：

> 使用 Charles 抓包，使用正则表达式：functionId=disc(AcceptTask|DoTask) 过滤请求
> 选中所有请求，将所有请求保存为 JSON Session File 名称为 watch.chlsj，将该文件与jd_watch.js放在相同目录中

