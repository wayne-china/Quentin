"""
WSGI config for gallery project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

#import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery.settings")
#
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
#


import os
import sys
path = '/home/rollingwayne/gallery'
if path not in sys.path:
    sys.path.append(path)
#os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.append(current_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

