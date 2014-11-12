#!/bin/bash

current_path=$(cd "$(dirname "$0")"; pwd)
install_software='apache2 apache2-mod_wsgi'
install_app='django==1.7 django-grappelli django-pagination django-markdown'
http_wsgi_path='/etc/apache2/conf.d/wsgi.conf'


if which zypper
then 
# 安装必要软件
  for software in $install_software
  do zypper install -y $software
  done
 
  zypper install python-pip

  for app in $install_app
  do pip install $app
  done
# 修改apache wsgi配置中的路径 
  file='/wsgi.py'
  sed -i s~path~$current_path$file~g ./conf/wsgi.conf
  if [ -x $http_wsgi_path ]
  then
    cat ./conf/wsgi.conf >> $http_wsgi_path
    echo "/etc/apache2/conf.d/wsgi.conf changed successful"
  else
    cp ./conf/wsgi.conf /etc/httpd/conf.d/
    echo "/etc/apache2/conf.d/wsgi.conf copied successful"
  fi
# 修改app 中wsgi.py的路径
  sed -i s~AppPath~$current_path~g ./Quentin/wsgi.py
# 启动服务
  systemctl start apache2

else echo 'Please install zypper packages'
fi

