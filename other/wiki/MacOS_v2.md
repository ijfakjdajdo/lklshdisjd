## v2版脚本已不再维护

## 脚本可以干什么

总有人不明白本脚本到底在干什么，那就大概说明一下吧：

1. git_pull.sh 这是最重要的脚本，用来在每小时自动更新lxk0301大佬的js脚本，不要再问为什么不切换gitee了，github比gitee更新；自动更新我的shell脚本；检测js脚本是否有增加，如果有，自动在你的定时任务中也增加（AutoAddCron=true时）；检测是否有短期任务过期，如果有，就自动在你的定时任务中删除（AutoDelCron=true时）；按照你设置的参数去设置。
2. rm_log.sh 这个用来删除旧日志。
3. first_run.sh 这个是物理机用来一键克隆的脚本，只需要在第一次运行，或者是重新部署时运行。
4. jd.sh.sample 这个是样例，当有新的任务时，自动把它复制一份，这个文件自动识别和它同名的js文件并运行js脚本。
5. git_pull_function.sh是git_pull.sh背后的脚本，你不用管它。
6. 所有以`.sample`结尾的文件，均不需要你编辑。

## 部署环境

1. 在[Node.js官网](https://nodejs.org/zh-cn/download)下载并安装Node.js长期支持版（已包括npm）；

2. 安装git、wget、curl、perl，可能某个软件已经集成在系统中。

    *注：如果上述软件不在这几个路径中：`/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin`，那么请在`/usr/local/bin`目录下创建软连接。*

## 克隆脚本

请不要完全照抄下面的命令，请替换为自己的用户名。

cd至你想存放脚本的路径之后运行一键安装脚本，假如为`/Users/用户名/jd`，那么：

**以下全文均以此路径`/Users/用户名/jd`进行举例，请自行修改为你自己的路径！**

**以下全文均以此路径`/Users/用户名/jd`进行举例，请自行修改为你自己的路径！**

**以下全文均以此路径`/Users/用户名/jd`进行举例，请自行修改为你自己的路径！**

```shell
cd /Users/用户名/jd
wget --no-check-certificate https://raw.githubusercontent.com/EvineDeng/jd-base/main/first_run.sh

# wget如果出错，要么你科学上网github，要么你手动下载好first_run.sh，放在这个目录下，没有问题再运行下面的命令
bash first_run.sh
```

*注：物理机如需多账号并发，需要创建多个文件夹，然后分别进入每个文件夹后运行上述命令，然后在每个创建的文件夹下都按下面说明配置一下，并且在制定定时任务时，你配置了多少个文件夹，那么同一条定时任务就要重复几次（因为.sh脚本路径不一样）。*

脚本会自动在`/Users/用户名/jd`下克隆下脚本并创建日志文件夹，分别如下：

- `log`: 记录所有日志的文件夹，其中跑js脚本的日志会建立对应名称的子文件夹，并且js脚本日志会以`年-月-日-时-分-秒`的格式命名。

- `scripts`: 从 [lxk0301/jd_scripts](https://github.com/LXK9301/jd_scripts) 克隆的js脚本。

- `shell`: 从 [EvineDeng/jd-base](https://github.com/EvineDeng/jd-base) 克隆的shell脚本。

## 修改信息

进入`/Users/用户名/jd`目录，复制`git_pull.sh.sample`为`git_pull.sh`；然后编辑`git_pull.sh`。

**注意：**

- *请不要直接修改`git_pull.sh.sample`！而只修改`git_pull.sh`。*

- [参数清单](参数清单)，**如何修改请仔细阅读`git_pull.sh`中的注释。**

## 初始化

**在首次编辑好`git_pull.sh`这个文件后，请务必手动运行一次`git_pull.sh`，不仅是为检查错误，也是为了运行一次`npm install`用以安装js指定的依赖。**

**在其他任何时候，只要你编辑过`git_pull.sh`，又想马上看到效果，请必须手动运行一次`git_pull.sh`！**

1. 完成所有信息修改以后，先检查一下git_pull.sh能否正常运行。

    ```shell
    cd /Users/用户名/jd/shell
    chmod +x *.sh       
    bash git_pull.sh
    ```

    **注：首次运行的日志很重要，如果过程中有任何错误，请参考错误提示来解决问题。主要包括两类问题：一是无法访问github，请想办法改善网络；二是`git_pull.sh`会运行`npm install`，用来安装js指定的依赖，如果你网络不好，日志中会有提示，请注意阅读。**

    **针对首次运行`git_pull.sh`**，出现类似以下字样才表示`npm install`运行成功：
    ```
    audited 205 packages in 3.784s

    11 packages are looking for funding
    run `npm fund` for details

    found 0 vulnerabilities
    ```
    
    如果`npm install`失败，请尝试手动运行，可按如下操作，如果失败，可运行多次：

    ```shell
    cd /Users/用户名/jd/scripts
    npm install || npm install --registry=https://registry.npm.taobao.org
    ```

2. 看看js脚本的信息替换是否正常。

    ```shell
    cd /Users/用户名/jd/scripts
    git diff    # 请使用上下左右键、Page Down、Page Up进行浏览，按q退出
    ```

3. 然后你可以手动运行一次任何一个以`jd_`开头并以`.sh`结尾的脚本（有些脚本会运行很长时间，sh本身不输入任何内容在屏幕上，而把日志全部记录在日志文件中）。

    ```shell
    cd /Users/用户名/myjd/jd/shell
    bash jd_unsubscribe.sh
    ```

    去`/Users/用户名/jd/log/jd_unsubscribe`文件夹下查看日志，查看结果是否正常，如不正常，请从头检查。

4. 如何想在终端中看到输出，那么可如下操作：

    ```shell
    cd /Users/用户名/jd/scripts
    node jd_unsubscribe.js
    ```

## 定时任务

1. 进入`/Users/用户名/jd/shell`目录，复制`crontab.list.sample`为`crontab.list`到`/Users/用户名/jd`目录下，然后编辑`crontab.list`。

2. 编辑定时任务并自己根据你的需要调整，也可以使用其他可视化工具编辑。**请注意将`crontab.list`这个文件中的`/root`目录替换为自己的目录。**

    ```shell
    nano crontab.list
    ```

3. 添加定时任务。

    **请注意：以下命令会完整覆盖你当前用户的crontab清单，请务必先检查当前用户是否存在其他定时任务！！！**

    **请注意：以下命令会完整覆盖你当前用户的crontab清单，请务必先检查当前用户是否存在其他定时任务！！！**

    **请注意：以下命令会完整覆盖你当前用户的crontab清单，请务必先检查当前用户是否存在其他定时任务！！！**

    > **你可以先使用`crontab -l`命令检查当前用户的定时任务清单，如果有，请将这部分任务放在下面这个`crontab.list`文件最上方，然后再运行下面的命令，这样你原来的定时任务也就保留了。**
    
    > **如果以后你还要增加其他定时任务，也请加在这个文件最上方以后，再运行下面命令。如果不添加在这个文件中，那么脚本会在自动增删定时任务时以crontab.list中的清单覆盖掉你通过其他方式添加的定时任务。**

    ```shell
    crontab crontab.list
    ```

    **如果你害怕你其他的任务被脚本覆盖，那么请将git_pull.sh中的`AutoAddCron`和`AutoDelCron`都设置为`false`！！！这样脚本就不会自动增删任务了！！！**

    **如果你害怕你其他的任务被脚本覆盖，那么请将git_pull.sh中的`AutoAddCron`和`AutoDelCron`都设置为`false`！！！这样脚本就不会自动增删任务了！！！**

    **如果你害怕你其他的任务被脚本覆盖，那么请将git_pull.sh中的`AutoAddCron`和`AutoDelCron`都设置为`false`！！！这样脚本就不会自动增删任务了！！！**

**说明：**

- `crontab.list`这个文件必须存放在`/Users/用户名/jd`（和 shell scripts log 三个文件夹在同一级）下。

- 第一条定时任务`/Users/用户名/jd/shell/git_pull.sh`会自动更新js脚本和shell脚本，并完成Cookie、互助码等信息修改，这个任务本身的日志会存在`/Users/用户名/jd/log/git_pull.log`中。更新过程不会覆盖掉你已经修改好的`git_pull.sh`文件。

- 第二条定时任务`/Users/用户名/jd/shell/rm_log.sh`用来自动删除旧的js脚本日志，如果你未按下一节`自动删除旧日志`中操作的话，这条定时任务不会生效。

- 当`git_pull.sh`中的`AutoAddCron`设置为`false`时（不自动增加新的定时任务），如何手动添加新增js脚本的定时任务：

    1. 检查有没有新增脚本：
        ```shell
        cd /Users/用户名/jd  # 先cd至你存放脚本的目录
        cat log/js-add.list
        ```
    2. 如果上一条命令不为空说明有新的定时任务待添加，把内容记下来，比如有个新增的任务叫为`jd_test`，那么就运行以下命令:
        ```shell
        cp shell/jd.sh.sample shell/jd_test.sh
        ```
     3. 再次提醒不要忘记赋予可执行权限：
        ```shell
        chmod +x shell/jd_test.sh
        ```
    4. 编辑crontab.list，并添加进crontab
        ```shell
        nano crontab.list
        crontab crontab.list
        ```

- 如果想使用自动增加定时任务的功能（`git_pull.sh`中`AutoAddCron`设置为`true`），而又不想手动改crontab，那么你的机子必须是北京时间，使用`date`命令可以查看系统时间。

## 自动删除旧日志

单个日志虽然小，但如果长期运行的话，日志也会占用大量空间，如需要自动删除，请按以下流程操作：

1. 复制一份rm_log.sh，并赋予可执行权限：

    ```shell
    cd /Users/用户名/jd/shell
    cp rm_log.sh.sample rm_log.sh
    chmod +x rm_log.sh
    ```

2. 该脚本在运行时默认删除`7天`以前的日志，如果需要设置为其他天数，请修改脚本中的`HowManyDays`。

3. 按`定时任务`部分的说明修改定时任务。

## 补充说明

- 其实`shell`目录下所有以`jd_`开头以`.sh`结尾的文件内容全都一样，全都是从`jd.sh.sample`复制来的，它们是依靠它们自身的文件名来找到所对应的`scripts`目录下的js文件并且执行的。所以，有新的任务时，只要你把`jd.sh.sample`复制一份和新增的`.js`脚本名称一样，赋予可执行权限，再增加定时任务就可以了。

- 如果想要重新调整定时任务运行时间，请不要直接使用`crontab -e`命令修改，而是编辑`/Users/用户名/jd/crontab.list`这个文件，然后使用`crontab /Users/用户名/jd/crontab.list`命令覆盖。这样的好处脚本会自动依靠这个文件来增加新的定时任务和删除失效的定时任务。

- 如果shell脚本有更新，需要你手动复制一份`git_pull.sh.sample`，并重新修改必须的信息，然后命名为`git_pull.sh`，流程如下：
    ```shell
    cd /Users/用户名/jd/shell
    cp git_pull.sh.sample git_pull_2.sh

    # 然后修改git_pull_2.sh，你也可以可视化编辑
    nano git_pull_2.sh
    
    # 修改好后，替换旧的git_pull.sh
    mv git_pull_2.sh git_pull.sh

    # 不要忘记赋予修改后的.sh脚本可执行权限
    chmod +x git_pull.sh
    ```

- 如有帮助到你，请点亮 star 。
