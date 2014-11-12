#!/bin/bash

current_path=$(cd "$(dirname "$0")"; pwd)
install_software='httpd mod_wsgi'
install_app='django==1.7 django-grappelli django-pagination django-markdown2'
http_wsgi_path='/etc/httpd/conf.d/wsgi.conf'


if which yum
then 
# 安装必要软件
  sudo yum update
  for software in $install_software
  do sudo yum install -y $software
  done
 
  easy_install pip

  for app in $install_app
  do sudo pip install $app
  done
# 修改apache wsgi配置中的路径 
  file='/wsgi.py'
  sed -i s~path~$current_path$file~g ./conf/wsgi.conf
  if [ -x $http_wsgi_path ]
  then
    sudo cat ./conf/wsgi.conf >> $http_wsgi_path
  else
    sudo cp ./conf/wsgi.conf /etc/httpd/conf.d/
  fi
# 修改app 中wsgi.py的路径
  sed -i s~AppPath~$current_path~g ./Quentin/wsgi.py
# 启动服务
  service httpd start

else echo 'Please install Yum packages'
fi

