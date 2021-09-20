
CREATE TABLE login_author (
	author_id	INT(10) NOT NULL,
	author_name	VARCHAR(255) NOT NULL,
	PRIMARY KEY(author_id)
);
CREATE TABLE  login_customer (
	customer_id	INT(10)  NOT NULL,
	NAME	VARCHAR(100) NOT NULL,
	address	VARCHAR(255) NOT NULL,
	phone	VARCHAR(100) NOT NULL,
	email	VARCHAR(100) NOT NULL,
	passwd	VARCHAR(100) NOT NULL,
	regdate	DATE NOT NULL,
	PRIMARY KEY(customer_id)
);
CREATE TABLE  login_order (
	order_id	INT(10)  NOT NULL,
	order_date	VARCHAR(100) NOT NULL,
	order_status	VARCHAR(100) NOT NULL,
	customer_id_id	INT(10)  NOT NULL,
	PRIMARY KEY(order_id),
	FOREIGN KEY(customer_id_id) REFERENCES login_customer(customer_id) 
);
CREATE TABLE  login_permissions (
	permission_id	INT(10)  NOT NULL,
	description	VARCHAR(100) NOT NULL,
	PRIMARY KEY(permission_id)
);
CREATE TABLE  login_publisher (
	publisher_id	INT(10)  NOT NULL,
	publisher_name	VARCHAR(255) NOT NULL,
	PRIMARY KEY(publisher_id)
);
CREATE TABLE  login_user_category (
	category_id	INT(10)  NOT NULL,
	PRIMARY KEY(category_id)
);
CREATE TABLE  login_user_permission (
	user_id	INT(10)  NOT NULL,
	permission_id_id	INT(10)  NOT NULL,
	PRIMARY KEY(user_id),
	FOREIGN KEY(permission_id_id) REFERENCES login_permissions(permission_id) 
);
CREATE TABLE  login_user (
	user_id	INT(10)  NOT NULL,
	NAME	VARCHAR(100) NOT NULL,
	address	VARCHAR(255) NOT NULL,
	phone	VARCHAR(100) NOT NULL,
	email	VARCHAR(100) NOT NULL,
	passwd	VARCHAR(130) NOT NULL,
	category_id_id	INT(10)  NOT NULL,
	PRIMARY KEY(user_id),
	FOREIGN KEY(category_id_id) REFERENCES login_user_category(category_id) 
);
CREATE TABLE  login_usefulness_rating (
	id	INT(10)  NOT NULL,
	rater_customer_id	INT(10)  NOT NULL,
	rating	INT(10)  NOT NULL,
	ratedate	DATETIME NOT NULL,
	bookID_id	INT(10)  NOT NULL,
	customer_id_id	INT(10)  NOT NULL,
	PRIMARY KEY(id AUTOINCREMENT),
	FOREIGN KEY(bookID_id) REFERENCES login_book(bookID) ,
	FOREIGN KEY(customer_id_id) REFERENCES login_customer(customer_id) 
);
CREATE TABLE  login_trustrecord (
	record_id	INT(10)  NOT NULL,
	target_customer_id	INT(10)  NOT NULL,
	STATUS	VARCHAR(20) NOT NULL,
	customer_id_id	INT(10)  NOT NULL,
	PRIMARY KEY(record_id),
	FOREIGN KEY(customer_id_id) REFERENCES login_customer(customer_id) 
);
CREATE TABLE  login_order_details (
	detail_id	INT(10)  NOT NULL,
	quantity	INT(10)  NOT NULL,
	purchase_price	REAL NOT NULL,
	discount	REAL NOT NULL,
	bookID_id	INT(10)  NOT NULL,
	order_id_id	INT(10)  NOT NULL,
	PRIMARY KEY(detail_id),
	FOREIGN KEY(order_id_id) REFERENCES login_order(order_id) ,
	FOREIGN KEY(bookID_id) REFERENCES login_book(bookID) 
);
CREATE TABLE  login_comment (
	id	INT(10)  NOT NULL,
	comment_timestamp	DATETIME NOT NULL,
	rating	INT(10)  NOT NULL,
	COMMENT	VARCHAR(250) NOT NULL,
	bookID_id	INT(10)  NOT NULL,
	customer_id_id	INT(10)  NOT NULL UNIQUE,
	FOREIGN KEY(customer_id_id) REFERENCES login_customer(customer_id) ,
	PRIMARY KEY(id AUTOINCREMENT),
	FOREIGN KEY(bookID_id) REFERENCES login_book(bookID) 
);
CREATE TABLE  login_book_movements (
	log_id	INT(10)  NOT NULL,
	logdate	DATE NOT NULL,
	quantity	INT(10)  NOT NULL,
	bookID_id	INT(10)  NOT NULL,
	FOREIGN KEY(bookID_id) REFERENCES login_book(bookID) ,
	PRIMARY KEY(log_id)
);
CREATE TABLE  login_book (
	bookID	INT(10)  NOT NULL,
	title	VARCHAR(255) NOT NULL,
	isbn	VARCHAR(100) NOT NULL,
	isbn13	VARCHAR(100) NOT NULL,
	average_rating	REAL NOT NULL,
	language_code	VARCHAR(30) NOT NULL,
	num_pages	INT(10)  NOT NULL,
	ratings_count	INT(10)  NOT NULL,
	text_reviews_count	INT(10)  NOT NULL,
	publication_date	DATE NOT NULL,
	stocklevel	INT(10)  NOT NULL,
	author_id_id	INT(10)  NOT NULL,
	publisher_id_id	INT(10)  NOT NULL,
	FOREIGN KEY(author_id_id) REFERENCES login_author(author_id) ,
	FOREIGN KEY(publisher_id_id) REFERENCES login_publisher(publisher_id) ,
	PRIMARY KEY(bookID)
);
CREATE INDEX  login_order_customer_id_id_7bd4d617 ON login_order (
	customer_id_id
);
CREATE INDEX  login_user_permission_permission_id_id_b85c01b5 ON login_user_permission (
	permission_id_id
);
CREATE INDEX  login_user_category_id_id_262de62d ON login_user (
	category_id_id
);
CREATE INDEX  login_usefulness_rating_bookID_id_8f4df8c0 ON login_usefulness_rating (
	bookID_id
);
CREATE INDEX  login_usefulness_rating_customer_id_id_c06570eb ON login_usefulness_rating (
	customer_id_id
);
CREATE INDEX  login_trustrecord_customer_id_id_409a06bd ON login_trustrecord (
	customer_id_id
);
CREATE INDEX  login_order_details_bookID_id_14816b5d ON login_order_details (
	bookID_id
);
CREATE INDEX  login_order_details_order_id_id_92fa2588 ON login_order_details (
	order_id_id
);
CREATE INDEX  login_comment_bookID_id_ebbf1b68 ON login_comment (
	bookID_id
);
CREATE INDEX  login_book_movements_bookID_id_e2a762ea ON login_book_movements (
	bookID_id
);
CREATE INDEX  login_book_author_id_id_e0182437 ON login_book (
	author_id_id
);
CREATE INDEX  login_book_publisher_id_id_0138556f ON login_book (
	publisher_id_id
);
COMMIT;
