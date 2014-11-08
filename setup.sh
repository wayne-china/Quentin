#!/bin/bash
if which yum
then 
  install_software='django pip httpd'
  install_app='grappelli pagination markdown2'

  for software in $install_software
  do yum install $software
  done

  for app in $install_app
  do pip install $app
  done

else echo 'Please install Yum packages'
fi

