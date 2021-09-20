import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# add python site packages, you can use virtualenvs also
site.addsitedir("C:/Users/user/AppData/Local/Programs/Python/Python39/Lib/site-packages")

# Add the app's directory to the PYTHONPATH 
sys.path.append('C:/Users/user/Desktop/onlinestore') 
sys.path.append('C:/Users/user/Desktop/onlinestore/onlinestore')  

os.environ['DJANGO_SETTINGS_MODULE'] = 'onlinestore.settings' 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlinestore.settings")  
 
application = get_wsgi_application()