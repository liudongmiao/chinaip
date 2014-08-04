本项目解析中国的IP，通过合并大段的ip，通过极少的路由完成大范围的中国IP覆盖。

一般来说，使用不到800条路由可以覆盖中国97%的IP，比直接使用4000+条原生少了很多。
即使是要完全覆盖，也可以节省大约1000条路由。
考虑到中国的服务提供商大多使用大范围的IP段，小范围的分给宽带用户，经过实测，使用16。

Mac OS X用户可以直接使用下面命令，下载处理好的文件，放到/etc/ppp下(执行前请先停用VPN)。

    curl -L -O "https://github.com/liudongmiao/chinaip/raw/master/mac/{ip-up,ip-down}"
    chmod +x ip-up ip-down
    sudo cp ip-up ip-down /etc/ppp

Linux用户？本人不用Linux好多年，应该也是有/etc/ppp目录，但是需要调整route的参数。

Windows用户？本人基本没用过Windows。
