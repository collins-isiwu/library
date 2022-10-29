# library
Library is a web application built with Django that makes API calls to Google Book API in order to retrieve information about the searched book. It uses PostgreSQL to store and retrieve already searched books. Categorizes book and so much more.

### Nature of Project
My intention while programming is to showcase my python OOP and Django prowess. I wanted to make a Django project that is ready for production. Which is why I built the project within DOCKER. The database supporting this web application is POSTgreSQL!


#### User Registration
Django's third-party django-allauth came in handy while working on user registeration and authentication. [Django-allauth docs](https://github.com/pennersr/django-allauth) was clear on how to use it. Django-allauth also provided the necessary views for the login, logout and user registration functionalities [par it's official repository](https://github.com/pennersr/django-allauth). Django-allauth url.py file for the view.py of auth [repository is](https://github.com/pennersr/django-allauth/blob/master/allauth/account/urls.py).

##### Test for User Registration
accounts/tests.py file holds the code for the tests written to check if the signup page is working properly. test_signup_template, test_signup_form and test_signup_view are methods under SignUpPageTests class that tests the User registration process.


#### Requirements
pip freeze > requirements.txt was necessary to create a requirement.txt file within my project directly while putting down all the modules installed for this project.


### Apps
This django project is made up of three apps namely:
1. accounts
2. pages
3. book app
4. ..

#### 1. Accounts App
The accounts app is an app of the django project that handles the logic for login, signup and logout. It contains the CustomUser model of the database.

accounts/form.py contains the UserChangeForm and UserCreationForm for changing and creating the user information. 

##### Test
Head to accounts/test.py The file contains test for CustomUser. I write code to make sure that the custom user model is actually working and is able to create a user, superuser. I also checked for is_superuser(), is_staff() modules while testing the accounts app. In line 8 of the file, I defined a setUp function that retains self.response which helped me to reduce redundancy.
[Django's resolve()](https://docs.djangoproject.com/en/4.0/ref/urlresolvers/#resolve) came in handy to ensure that HomePageView "resolves" a given URL path on line 29 of the file.


#### 2. Pages App
This app is incharge of delivering all my templates to the end-user while simultaneously interacting with the database to create a dynamic page. I used Django's module TemplateView to write my pages/views.py. The views is a class-based views (CBVs). CBVs utilize OOP principles, which allow us to use inheritance, reuse code, and generally write better and cleaner code.

##### Pages App Test
Head to pages/test.py, you will see the tests that I wrote for the pages app. Class "HomepageTests" contains functions testing different parts of the homepage. You can run this test within docker using: $ **docker-compose exec web python manage.py test pages** 
in your terminal.

#### 3. Book App
The Book app contains a Book model that stores all the books searched and saved to this web application. It uses a class based view for handling the logic of each route. It is important to note that the Book Model uses the Universal Unique Identifier [UUID](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.UUIDField) in place of default django ids. This is because it tells a potential hacker exactly how many records we have in your database; it tells them exactly what the id is which can be used in a potential attack; and there can be synchronization issues if you have multiple front-ends.

##### Book App Test
We import TestCase and introduce the setUpTestData156 method to add a sample book to test. Using setUpTestData often dramatically increases the speed of your tests because the initial data is created once rather than each time for each unit test.
The first unit test, test_book_listing, checks that both its string representation and content are correct. Then we use test_book_list_view to confirm that our homepage returns a 200 HTTP status code, contains our body text, and uses the correct books/book_list.html template. Finally, test_book_detail_view tests that our detail page works as expected and that an incorrect page returns a 404. It’s always good both to test that something does exist and that something incorrect doesn’t exist in your tests. The test can be run using *docker-compose exec web python manage.py test book*


