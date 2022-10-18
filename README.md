# library
Library is a web application built with Django that makes API calls to Google Book API in order to retrieve information about the searched book. It uses PostgreSQL to store and retrieve already searched books. Categorizes book and so much more.

### Nature of Project
My intention while programming is to showcase my python OOP and Django prowess. I wanted to make a Django project that is ready for production. Which is why I built the project within DOCKER. The database supporting this web application is POSTgreSQL!

### Apps
This django project is made up of three apps namely:
1. accounts
2. pages
3. bookstore
4. ..

#### 1. Accounts App
The accounts app is an app of the django project that handles the logic for login, signup and logout. It contains the CustomUser model of the database.

accounts/form.py contains the UserChangeForm and UserCreationForm for changing and creating the user information. 

##### Test
Head to accounts/test.py The file contains test for CustomUser. I write code to make sure that the custom user model is actually working and is able to create a user, superuser. I also checked for is_superuser(), is_staff() modules while testing the accounts app. In line 8 of the file, I defined a setUp function that retains self.response which helped me to reduce redundancy.
[Django's resolve()](https://docs.djangoproject.com/en/4.0/ref/urlresolvers/#resolve) came in handy to ensure that HomePageView "resolves" a given URL path on line 29 of the file.


#### 2. Pages App
This app is incharge of delivering all my templates to the end-user while simultaneously interacting with the database to create a dynamic page. I used Django's module TemplateView to write my pages/views.py. The views is a class-based views (CBVs). CBVs utilize OOP principles, which allow us to use inheritance, reuse code, and generally write better and cleaner code.

##### Test
Head to pages/test.py, you will see the tests that I wrote for the pages app. Class "HomepageTests" contains functions testing different parts of the homepage. You can run this test within docker using: $ docker-compose exec web python manage.py test pages 
in your terminal.


#### User Registration
Django's built-in features for user registeration and authentication came in handy here. [Django's docs on auth app](https://docs.djangoproject.com/en/4.0/topics/auth/default/) was clear on how to user Django built-in features. Django also provided the necessary views for the login, logout and user registration functionalities [par it's official repository](https://github.com/django/django/blob/b9cf764be62e77b4777b3a75ec256f6209a57671/django/contrib/auth/views.py). Django's url.py file for the view.py of auth [repository is](https://github.com/django/django/blob/b9cf764be62e77b4777b3a75ec256f6209a57671/django/contrib/auth/urls.py) and well documented [here](https://docs.djangoproject.com/en/4.0/topics/auth/default/#module-django.contrib.auth.views) 

