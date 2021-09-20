from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import Customer
from .models import User_Category
from .models import Publisher
from .models import Book
from .models import Author
from .models import Order
from .models import Comment
from .models import user_credentials
from .models import TrustRecord
import traceback
import hashlib
from django.db import connection
import random
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect
from time import gmtime, strftime


#import sweetify

# Create your views here.
def dashboard(request):
    totalorders = Order.objects.all().count()
    customers = Customer.objects.all().count()
    ordertotal = Order.objects.raw("select order_id, sum(quantity * price) as totals from login_order join login_book on login_book.bookID = login_order.book_id")
    totals = 0
    for torders in ordertotal:
        totals =torders.totals
   
    totalproducts = Order.objects.raw("select order_id,sum(quantity) as totalproducts from login_order")
    totalprods = 0
    for tproducts in totalproducts:
        totalprods = tproducts.totalproducts
    orders = Order.objects.raw("select login_order.*,name, title,price from login_order join login_customer on login_customer.customer_id = login_order.customer_id_id join login_book on login_book.bookID = login_order.book_id limit 10")
    return render(request,'dashboard.html',{"totalorders":totalorders,"totalrevenue":totals,"customers":customers,"totalproducts":totalprods,"orders":orders})
def home(request):
    #cursor = connection.cursor()
    #cursor.execute('''SELECT title,isbn, average_rating,bookID, SUM(`quantity`) AS qnty FROM `login_book` 
    #JOIN `login_order_details` ON login_order_details.`bookID_id` = login_book.`bookID`
    #GROUP BY bookID''')
    #books = cursor.fetchall()
    bks = Book.objects.raw("SELECT title,isbn,price, average_rating,bookID,order_id_id, SUM(quantity) AS qnty FROM login_book  JOIN login_order_details ON login_order_details.bookID_id = login_book.bookID GROUP BY bookID order by qnty desc limit 6")
    listofbooks = []
    for bk in bks:
        listofbooks.append(bk)
    listofbooks.sort(key=lambda x: x.title, reverse=True)
    nobk = len(listofbooks)
    books = []
    for bkd in listofbooks:
        bkd.title = bkd.title[:70]
        books.append(bkd)

    authors = Author.objects.raw("SELECT author_id,author_name,title ,SUM(quantity) AS qnty FROM login_book JOIN login_order_details ON login_order_details.bookID_id = login_book.bookID JOIN login_author ON login_book.author_id_id = login_author.author_id GROUP BY author_id ORDER BY qnty DESC limit 6") 
 
    bnks = list(Book.objects.raw("SELECT title,isbn,price,bookID FROM login_book"))
    recommendation1 = random.sample(bnks, 3)
    recommendation2 = random.sample(bnks, 3)
    #books = Book.objects.select_related()
    return render(request,'index.html',{'books':books, 'authors':authors, 'recommendation1':recommendation1,'recommendation2':recommendation2 })

# The function to process
# user login
def login(request):
    return render(request,'login.html')

def processlogin(request):
    username = request.POST.get("email").lower().strip()
    password = request.POST.get("password").lower().strip()
    user = user_credentials.objects.filter(email=username)
    passwd = ""
    # if the query got a user with that email, start processing
    if user:
        for usr in user:
            pswd= usr.passwd
        if (hashlib.md5(password.encode()).hexdigest() == pswd):
            #Select user details depending on the type of user
            if usr.user_type == 1:
                userd = User.objects.filter(email=username)
                for usd in userd:
                    return HttpResponseRedirect('dashboard',{'user':usd,'status':True})
            else:
                userd = Customer.objects.filter(email=username)
                return HttpResponseRedirect('home')
        else:
            messages.info(request, 'Failed to Login. Check your email or password' )
            return render(request,'login.html',{'status':False})
    else: # this is processed when the user with such email is not found
        messages.info(request, 'Failed to Login. Email Not found')
        return HttpResponseRedirect('login')
def storemanagers(request):
    managers = User.objects.all()
    return render(request,'storemanagers.html',{'managers':managers})

def savemanager(request):
    try:
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email").lower().strip()
        password = request.POST.get("password").lower().strip()
        user = User.objects.create(
                name = name,
                email = email,
                address = address,
                phone = phone,
                passwd =  hashlib.md5(password.encode()).hexdigest(),
                category_id_id = 1
                )
        cstemail = email
        nld = User.objects.filter(email = cstemail)
        newuser = 0
        for nusr in nld:
            newuser = nusr.user_id
        #insert in user credentials
        user_credentials.objects.create(
            user_id = newuser,
            email = email,
            #encrypt the password
            passwd =  hashlib.md5(password.encode()).hexdigest(),
            user_type = 1 
            )
            
        messages.info(request, 'Record Successfully Saved.')
        return HttpResponseRedirect('storemanagers')
    except Exception as e:
        trace_back = traceback.format_exc()
        message = str(e) + " " + str(trace_back)
        messages.info(request, message)
        return HttpResponseRedirect('login')
def authors(request):
    authors = Author.objects.all()
    return render(request,'authors.html',{'authors':authors})
def publishers(request):
    publishers = Publisher.objects.all()
    return render(request,'publishers.html',{'publishers':publishers})
def orders(request):
    orders  = Order.objects.raw("select login_order.*,name, title,price from login_order join login_customer on login_customer.customer_id = login_order.customer_id_id join login_book on login_book.bookID = login_order.book_id")
    return render(request,'orders.html',{'orders':orders})
def books(request):
    books = Book.objects.select_related()
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    return render(request,'books.html',{'books':books,'authors':authors,'publishers':publishers})
def customers(request):
    customers = Customer.objects.all()
    return render(request,'customers.html',{'customers':customers})
def addstock(request):
    id = request.GET.get('id')
    book = Book.objects.get(pk = id )
    return render(request,'addstock.html',{'book':book})
def save_added_stock(request):
    bkid =  request.POST.get("bookid")
    quantity  = request.POST.get("quantity")
    book = Book.objects.get(pk = bkid )
    book.stocklevel = book.stocklevel + int(quantity)
    book.save()
    return HttpResponseRedirect('books')

def openbook(request):
    bkid =  request.GET.get("bookid")
    book = Book.objects.get(pk = bkid )
    author   = book.author_id
    comments  = Comment.objects.raw("SELECT login_comment.*,name from login_comment join login_customer on login_comment.customer_id = login_customer.customer_id where book_id ="+bkid) 

    return render(request,'book.html',{'book':book, "author":author,"comments":comments,'customers':customers})

def savecomment(request):
    bkid =  request.POST.get("bookid")
    customerid =  request.POST.get("customerid")
    rate =  request.POST.get("rating")
    comment =  request.POST.get("comment")
    Comment.objects.create(
        comment_timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime()),
        rating = rate,
        comment = comment,
        book_id = bkid,
        customer_id  = 2
    )

    
    book = Book.objects.get(pk = bkid )
    author   = book.author_id
    comments  = Comment.objects.raw("SELECT login_comment.*,name from login_comment join login_customer on login_comment.customer_id = login_customer.customer_id") 

    return render(request,'book.html',{'book':book, "author":author,"comments":comments,'customers':customers})


def saveorder(request):
    bkid =  request.POST.get("bookid")
    quantity =  request.POST.get("quantity")
    return render(request,'loginpurchase.html',{'bookid':bkid,'quantity':quantity})


def savebook(request):
    book = Book.objects.create(
            title            =  request.POST.get("title"),
            isbn             =  request.POST.get("isbn"),
            isbn13            =  request.POST.get("isbn3"),
            language_code    =  request.POST.get("language_code"),
            num_pages        =  request.POST.get("num_pages"),
            publication_date =  request.POST.get("publication_date"),
            stocklevel       =  request.POST.get("stocklevel"),
            author_id_id     =  request.POST.get("author_id"),
            publisher_id_id  =  request.POST.get("publisher_id"),
            average_rating = 0,
            ratings_count =0,
            text_reviews_count = 0
    )
    
    return HttpResponseRedirect('books')


def viewcustomers(request):
    customers = Customer.objects.raw("select login_customer.*, count(login_trustrecord.status) as totalcount from login_customer left join login_trustrecord on login_trustrecord.target_customer_id = login_customer.customer_id group by login_customer.customer_id")
    return render(request,'viewcustomers.html',{"customers":customers})
def degreesearch(request):
    books = Book.objects.raw("SELECT login_book.*, login_author.author_name , login_publisher.publisher_name FROM login_book join login_author on login_book.author_id_id = login_author.author_id join login_publisher on login_book.publisher_id_id = login_publisher.publisher_id")
    return render(request,"degreesearch.html",{"books":books})
def recommendations(request):
    return render(request,"loginrecommend.html")
def getrecommendations(request):
    email = request.POST.get("email")
    try:
        customer = Customer.objects.get(email=email)
        if customer:
            #get list of customer who bought similar books
            customerswhobought = Order.objects.raw("select order_id, customer_id_id from login_order where login_order.book_id in (SELECT bookID from login_book join login_order on login_book.bookID = login_order.book_id  where login_order.customer_id_id ="+ str(customer.customer_id )+")"  )
            #now get other books bought by same customers
            #customerids = list(customerswhobought)
            customerids = []
            
            for ids in customerswhobought:
                idk = str(ids.customer_id_id)
                customerids.append(idk)
                

            myids = ', '.join(customerids)
            #books = Book.objects.raw("select login_book.* from login_order  join login_book on login_book.bookID = login_order.book_id where customer_id_id in (" + str(myids)  +")")
            books = Book.objects.raw("SELECT login_book.*, login_author.author_name , login_publisher.publisher_name FROM  login_order  join login_book on login_book.bookID = login_order.book_id  join login_author on login_book.author_id_id = login_author.author_id join login_publisher on login_book.publisher_id_id = login_publisher.publisher_id where customer_id_id in (" + str(myids) +")")
            #return HttpResponse("FOUND " + str(len(books)))
            return render(request,"recommendedbooks.html",{"books":books})
        else:
            messages.info(request, 'Failed 1 to Login. Email Not found')
            return render(request,"loginrecommend.html")
    except Exception as e:
        trace_back = traceback.format_exc()
        message = str(e) + " " + str(trace_back)
        messages.info(request, "Failed 2 to Login. Email Not found " + message)
        return render(request,"loginrecommend.html")

    return render(request,)
def viewcustomer(request):
    idpk = request.GET.get("id")
    customer = Customer.objects.get(pk=idpk)
    comments = Comment.objects.raw("SELECT login_comment.*,name,title from login_comment join login_customer on login_comment.customer_id = login_customer.customer_id join login_book on login_book.bookID = login_comment.book_id where login_comment.customer_id ="+idpk) 
    return render(request,'viewcustomer.html',{"customer":customer,"comments":comments})

def savetrustedrating(request):
    customer_id =  request.POST.get("customerid")
    rating =  request.POST.get("rating")
    username = request.POST.get("email").lower().strip()
    customer = Customer.objects.get(email=username)
    
    if customer:
        TrustRecord.objects.create(
            target_customer_id =customer_id,
            status = rating,
            customer_id_id = customer.customer_id
        )
        return HttpResponseRedirect('viewcustomers')
    else:
        return HttpResponseRedirect('viewcustomers')



def processpurchaselogin(request):
    bookid=  request.POST.get("bookid")
    quantity =  request.POST.get("quantity")
    username = request.POST.get("email").lower().strip()
    password = request.POST.get("password").lower().strip()
    user = user_credentials.objects.get(email=username)

    # if the query got a user with that email, start processing
    if user:
        pswd = user.passwd
        if (hashlib.md5(password.encode()).hexdigest() == pswd):
            userd = Customer.objects.get(email=username)
            #create the order
            order = Order.objects.create(
            order_date = datetime.date.today(),
            order_status = 'Pending',
            customer_id_id = userd.customer_id,
            book_id = bookid,
            quantity =  quantity
            )
            order.save()
            messages.info(request, 'Order Successfully Created' )
            return HttpResponseRedirect('home')
        else:
            messages.info(request, 'Failed to Login. Check your email or password' )
            return render(request,'loginpurchase.html',{'bookid':bookid,'quantity':quantity})
    else: # this is processed when the user with such email is not found
        messages.info(request, 'Failed to Login. Email Not found')
        return render(request,'loginpurchase.html',{'bookid':bookid,'quantity':quantity})








def savenewcustomer(request):
    try:
        name = request.POST.get("name")
        email = request.POST.get("email").lower().strip()
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        password = request.POST.get("password").lower().strip()
        #save the customer
        customer = Customer.objects.create(
            name = name,
            email = email,
            address = address,
            phone = phone,
            passwd =  hashlib.md5(password.encode()).hexdigest(),
            regdate = datetime.date.today()
            )
        cstemail = email
        
        #customer.save()
        nld = Customer.objects.filter(email = cstemail)
        newuser = 0
        for nusr in nld:
            newuser = nusr.customer_id
        #insert in user credentials
            user_credentials.objects.create(
                user_id = newuser,
                email = email,
                passwd =  hashlib.md5(password.encode()).hexdigest(),
                user_type = 2 
                )
        
        messages.info(request, 'Record Successfully Saved. Now you can Login to your account')
        return HttpResponseRedirect('login')
    except Exception as e:
        trace_back = traceback.format_exc()
        message = str(e) + " " + str(trace_back)
        messages.info(request, "Error while trying to save data")
        return HttpResponseRedirect('login')