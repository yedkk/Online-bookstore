"""onlinestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('dashboard',views.dashboard, name="dashboard"),
    path('login',views.login,name='login'),
    path('storemanagers',views.storemanagers, name='storemanagers'),
    path('savemanager',views.savemanager, name='savemanager'),
    path('customers',views.customers, name='customer'),
    path('books',views.books, name='books'),
    path('orders',views.orders, name='orders'),
    path('publishers',views.publishers, name='publishers'),
    path('authors',views.authors, name='authors'),
    path('processlogin',views.processlogin, name='processlogin'),
    path('savenewcustomer',views.savenewcustomer, name='savenewcustomer'),
    path('addbooks',views.addstock, name='addbooks'),
    path('save_added_stock',views.save_added_stock, name='save_added_stock'),
    path('openbook',views.openbook, name='openbook'),
    path('saveorder',views.saveorder, name='saveorder'),
    path('savebook',views.savebook, name='savebook'),
    path('savetrustedrating',views.savetrustedrating, name='savetrustedrating'),
    path('savecomment',views.savecomment, name='savecomment'),
    path('degreesearch',views.degreesearch, name='degreesearch'),
    path('viewcustomers',views.viewcustomers, name='viewcustomers'),
    path('viewcustomer',views.viewcustomer, name='viewcustomer'),
    path('recommendations',views.recommendations, name='recommendations'),
    path('getrecommendations',views.getrecommendations, name='getrecommendations'),
    path('processpurchaselogin',views.processpurchaselogin, name='processpurchaselogin'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
