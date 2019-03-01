#! /bin/sh
# chkconfig: 345 85 15
# 上面一行注释:哪些Linux级别需要启动manage_dxmanager(3,4,5)；启动序号(85)；关闭序号(15)。
# 指定项目目录
PROJECT_DIR="/home/dxm/dxmanager"
# 指定脚本目录在哪里
SCRIPTS_DIR="/home/dxm/script"
# 描述
DESC="dxmanager"
# 名称
NAME="dxm"
# 脚本名称
SCRIPT_FILENAME="manager_dxm.sh"
# 脚本目录名称
SCRIPTNAME=`pwd`/$SCRIPT_FILENAME
# PID
PID="uwsgi.pid"
# 启动函数
d_start(){
# 进入到项目目录
cd $SCRIPTS_DIR
# 判断这个PID是否存在
if [  -f $PID ];then
echo -e "\n\033[34m$NAME项目启动中........\033[0m"
# 如果不存在执行
uwsgi --ini uwsgi.ini
killall nginx
/etc/init.d/nginx start
# 自动收集静态文件
cd $PROJECT_DIR && python manage.py collectstatic --noinput
echo -e "\n\033[32m$NAME 项目启动完成........\033[0m"
exit 0
fi
echo -e "\n\033[33m$NAME 项目已启动请勿重复启动\033[0m"
}
# 关闭函数
# 关闭项目
d_stop(){
# 进入脚本目录
cd $SCRIPTS_DIR
# 判断这个pid文件是否存在
if [  -f "uwsgi.pid" ];then
# 这个项目已经关闭了
echo -e "\n\033[33m$NAME 项目已经关闭了请先启动\033[0m"
fi
echo -e "\n\033[34m$NAME 项目关闭中........\033[0m"
echo -e "\nStop $DESC: $NAME"
# 如果没有关闭
uwsgi --stop uwsgi.pid
# 是否停掉Nginx根据实际需要来操作~~！因为Nginx有对静态文件缓存［注意］
killall nginx
/etc/init.d/nginx start
echo -e "\n\033[32m$NAME 项目关闭完成........\033[0m"
}

d_restart(){
d_stop
sleep 1
d_start
}

case "$1" in
start)
echo -e "\nstarting $DESC: $NAME"
d_start
;;
stop)
echo -e "\nStop $DESC: $NAME"
d_stop
;;
restart)
echo -e "\nRestart $DESC: $NAME"
d_restart
;;
*)
echo "Usage: $SCRIPTNAME {start|stop|restart}" >&2
exit 3
;;
esac
