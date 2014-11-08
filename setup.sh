#!/bin/bash

current_path=$(cd "$(dirname "$0")"; pwd)
install_software='django pip httpd'
install_app='grappelli pagination markdown2'
http_wsgi_path='/etc/httpd/conf.d/wsgi.conf'


if which yum
then 
# 安装必要软件
  for software in $install_software
  do sudo yum install $software
  done

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
# 修改app 中wsgi.py的路径
  sed -i s~AppPath~$current_path~g ./Quentin/wsgi.py

else echo 'Please install Yum packages'
fi

