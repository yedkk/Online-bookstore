from django.db import models

# object for users category
#User_Category (category id, category name)
class User_Category(models.Model):
    category_id  = models.IntegerField(primary_key=True)
    category_name:models.CharField(max_length=100,default='',null=False)
# Users Model: for store managers
#User (UserID, staff name, category id, address, phone, email, password)
class User(models.Model):
    user_id =  models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    passwd = models.CharField(max_length=130)
    category_id=models.ForeignKey(User_Category, on_delete = models.CASCADE)

#Customer(customer_id,name,email,password,address,phone,regdate)
class Customer(models.Model):
    customer_id =  models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
    regdate=models.DateField(auto_now=True)

#Permissions (permission id, description)
class Permissions(models.Model):
    permission_id =  models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)
    
#User_permission(user_id,permission_id)
class User_Permission(models.Model):
    user_id =  models.IntegerField(primary_key=True)
    permission_id = models.ForeignKey(Permissions, on_delete = models.CASCADE)


class Publisher(models.Model):
    publisher_id=  models.IntegerField(primary_key=True)
    publisher_name = models.CharField(max_length=255)
class Author(models.Model):
    author_id=  models.IntegerField(primary_key=True)
    author_name = models.CharField(max_length=255)
#Book (ISBN, book_title, author, publisher, language, pub_date, no_pages, quantity, price, keywords, subject)
class Book(models.Model):
    bookID =  models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=100)
    isbn13 = models.CharField(max_length=100)
    author_id = models.ForeignKey(Author, on_delete = models.CASCADE)
    average_rating = models.FloatField()
    language_code= models.CharField(max_length=30)
    num_pages= models.IntegerField()
    ratings_count= models.IntegerField()
    text_reviews_count= models.IntegerField()
    publication_date= models.DateField(auto_now=True)
    publisher_id= models.ForeignKey(Publisher, on_delete = models.CASCADE)
    stocklevel = models.IntegerField()

#Order (order_id, order_date, customer_id, order_status)
class Order(models.Model):
    order_id =  models.IntegerField(primary_key=True)
    order_date = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    order_status = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    quantity =  models.IntegerField()
#Order_details (detail_id, order_id, bookID, quantity, purchase_price, discount)
class Order_Details(models.Model):
    detail_id   =  models.IntegerField(primary_key=True)
    order_id   =  models.ForeignKey(Order, on_delete = models.CASCADE)
    bookID  =  models.ForeignKey(Book, on_delete = models.CASCADE)
    quantity =  models.IntegerField()
    purchase_price =  models.FloatField()
    discount =  models.FloatField()


#Book_movements(log_id,bookID,logdate, quantity)
class Book_movements(models.Model):
    log_id   =  models.IntegerField(primary_key=True)
    bookID   =  models.ForeignKey(Book, on_delete = models.CASCADE)
    logdate  =  models.DateField(auto_now=True)
    quantity =  models.IntegerField()


#Comment (customer_id, bookID, comment_timestamp, rating, comment)

class Comment(models.Model):
    customer   =  models.ForeignKey(Customer, on_delete = models.CASCADE)
    book   =  models.ForeignKey(Book, on_delete = models.CASCADE)
    comment_timestamp  = models.DateTimeField(auto_now_add=True)
    rating =  models.IntegerField()
    comment = models.CharField(max_length=250)
#Usefulness_rating(customer_id, bookID, rater_customer_id, rating, date)

class Usefulness_rating(models.Model):
    customer_id   =  models.ForeignKey(Customer,on_delete = models.CASCADE)
    bookID   =  models.ForeignKey(Book, on_delete = models.CASCADE)
    rater_customer_id  =   models.IntegerField()
    rating =  models.IntegerField()
    ratedate = models.DateTimeField(auto_now_add=True)
#TrustRecord(record_id, customer_id, target_customer_id, status)class Book_movements(models.Model):
class TrustRecord(models.Model):
    record_id   =  models.IntegerField(primary_key=True)
    customer_id   =  models.ForeignKey(Customer, on_delete = models.CASCADE)
    target_customer_id  =  models.IntegerField()
    status =  models.CharField(max_length=20)


#username and password for all users will be stored here. 
class user_credentials(models.Model):
    record_id   =  models.IntegerField(primary_key=True)
    user_id     =  models.IntegerField() #can either be customer id or staff id
    user_type   =  models.IntegerField()  #1 for managers  and 2 for customers
    email = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)