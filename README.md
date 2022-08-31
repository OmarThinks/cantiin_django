[![CircleCI](https://circleci.com/gh/OmarThinks/cantiin_django.svg?style=svg)](https://circleci.com/gh/OmarThinks/cantiin_django)
[![CircleCI Build Status](https://circleci.com/gh/OmarThinks/cantiin_django.svg?style=shield "CircleCI Build Status")](https://circleci.com/gh/OmarThinks/cantiin_django) 
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/OmarThinks/CircleCI-hello-world/master/LICENSE) 

# cantiin_django
An ecommerce RESTful API using django and Django REST Framework.

# Website:





<table>
<tr>
<th>Link Type</th>
<th>Link</th>
</tr>

<tr>
<th>Website (On Shared Hosting)</th>
<td>
<a href="https://www.cantiin.com">https://www.cantiin.com</a>
</td>
</tr>




<tr>
<th>Deployment on AWS Elastic Beanstalk</th>
<td>
<a href="http://cantiin-dev.us-east-2.elasticbeanstalk.com/">http://cantiin-dev.us-east-2.elasticbeanstalk.com/</a>
</td>
</tr>



<tr>
<th>Youtube</th>
<td>
<a href="https://www.youtube.com/watch?v=4RjUJZSEsS0">https://www.youtube.com/watch?v=4RjUJZSEsS0</a>
</td>
</tr>

<tr>
<th>RESTful API backend Link</th>
<td>
<a href="https://cantiin.com/api">https://cantiin.com/api</a>
</td>
</tr>




<tr>
<th>Related Projects</th>
<td>
<a href="https://github.com/OmarThinks/Cantiin-React-NextJS">Cantiin React</a><br>
<a href="https://github.com/OmarThinks/Cantiin-React-Native">Cantiin React Native</a>
</td>
</tr>




</table>




















# A) Technologies Used:
1. Django
2. Django REST Framework
3. django_filter
4. CircleCI


# B) How to Run:

```bash
cd _app
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
















# C) Backend:

## C-1) Authentication:

The system uses Django authentication system.  
To use the authentication system you can use this link:
http://127.0.0.1:8000/api/auth/users/  
Here there are djoser endpoints.
This is a the <a href="https://djoser.readthedocs.io/en/latest/base_endpoints.html">documentation</a> of these endpoints.  

<img src="images/auth.gif">

The endpoints of authentication are there.  
Authentication is made by cookie if you want to extend the application using the same origin.  
And it also uses auth header if you want to extend the application 
with different origin.  
Authentication uses JWT.




## C-2) What the app does:

Beyound authentication, the app has three more models.  
- Product (Where the users can handle products)
- Order (Where the user can orders of products)
- Comment (Where the user can handle comments on products)


These are the endpoints of API recources:  
"users": "http://127.0.0.1:8000/api/users/" (This is different from auth endpoints)  
"products": "http://127.0.0.1:8000/api/products/"  
"orders": "http://127.0.0.1:8000/api/orders/"  
"comments": "http://127.0.0.1:8000/api/comments/"

<img src="images/root.gif">








## C-3) Pagination:
All the models have pagination.  
Since it exists in the `settings.py` file.  
The pagination uses pages.  
Each page has 10 records.  


<img src="images/pagination.gif">



## C-4) Validation and Sanitization:
Validation and is used here, it is built in django  and Django REST framework.  
Because we are using Django REST Framework serialization.  
When the user sends a wrong request, the correct response will be returned.



## C-5) Rate Limit:
It means the limit of requests that can be sent bu the users.  
It is very helpful to prevent DoS attacks.  
For users that are 
- logged in: 1000 request/min/IP Adress
- not logged in: 100 request/min/Users


These can be changed by changing `settings.py`.

## C-6) Permissions:
- Not Logged in Users:
	- Create an account (Sign up)
	- Sign in
	- View all data of the API (Users (Username, id, products, and comments), Products, Comments and Orders )
- Logged in Users:
	- Not Logged in users permissions
	- Create a Product, Order or leave a comment on a product
	- Update or delete a product, comment, or order only if it was posted by this certain user.
- Admins (Super users):
	- Logged in users permissions 
	- Update, delete any product, Comment or order posted by any other user.

## C-7) Search:
Search is done using Django Filter:



<img src="images/filter.gif">















## C-8) Custom Authentication Endpoints:



### C-8-1) http://127.0.0.1:8000/api/auth/custom/signup/

This is the signup endpoint.  
The method is POST.  
It expects 2 inputs in the request body: **`username`** and **`password`**.  
When you sign up, you will login also


### C-8-2) http://127.0.0.1:8000/api/auth/custom/login/

This is the login endpoint.  
The method is POST.  
It expects 2 inputs in the request body: **`username`** and **`password`**




### C-8-3) http://127.0.0.1:8000/api/auth/custom/logout/

This is the logout endpoint.  




### C-8-4) http://127.0.0.1:8000/api/auth/custom/user/

This endpoint tells whether the user is authenticated or not.  
- **Authenticated**: 
	- response:
		- Status Code: 200
		- Body: the user information
- **UnAuthenticated**:
	- response:
		- Status Code: 401


































# D) Frontend:


The frontend uses Bootstrap and CSS.  
It it rendered using Jinja templating Engine.


<img src="images/frontend.gif">




## D-A) Authentication:

### D-A-1) Signup:

If the user is not logged in.  
then, on the top of the page, there will be a sign up button.
<img src="images/signup_button.gif">
On clicking this button:


<img src="images/signup_form.gif">

The user will be redirected to the sign up form.



### D-A-2) Logging In:


Just like Sign ing up, there is a log in Button that appears 
when the user is not logged in.
<img src="images/login_button.gif">
<img src="images/logic.gif">


### D-A-3) After Logging In:

After loggin in, the header will change.
<img src="images/changed_header.gif">  
It will have 2 Options:
1. **My Products**: To display a list of user's products
2. **Log Out**: To log out of the system






## D-B) My Products:

### D-B-1) My products List:

If you are loggin in, you will notice that the header 
has a My Products option.  

<img src="images/changed_header.gif">    


When You click on the button, you will be reditected to the 
My Products page.  
This page displays a list of products that you have created, 
There is pagination to see the next products.
<img src="images/my_products_page.gif">       


### D-B-2) Create Product:

On the top of My products page, there is a Craete Product button.  



<img src="images/create_product_button.gif">       



When you Click on that Button, You will be taken to the Create Product Form.

<img src="images/create_product_form.gif">       


There is validation, Be Careful :) :

<img src="images/create_product_form_validation.gif">       
<img src="images/disappointed.gif">       



### D-B-3) Product Details:

On My Products page, You will find a list of Products.  
<img src="images/product_card.gif">       



When you CLick on the View Product Details in the card, 
you will be able to see all the details of the product
<img src="images/product_details_page.gif">       






### D-B-4) Product Delete and Update:


On the product details page, You can Delete the product or edit it 
(If you are the one who posted it).  


<img src="images/delete_and_update.gif">       





But If the product was not Your's, then you can not edit it.
<img src="images/no_delete_or_edit.gif">       

As in this image, the user is logged in, 
but there is no delete or edit buttons.








# E) AWS Elastic Beanstalk Deployment:


http://cantiin-dev.us-east-2.elasticbeanstalk.com/  



Deployed on Elastic Beanstalk.  
And connected to PostgreSQL database using AWS RDS.






















