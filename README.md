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
Head to accounts/test.py The file contains test for CustomUser. I write code to make sure that the custom user model is actually working and is able to create a user, superuser. I also checked for is_superuser(), is_staff() modules while testing the accounts app. In line 6 of the file, I defined a setUp function that retains self.response which helped me to reduce redundancy.


#### 2. Pages App
This app is incharge of delivering all my templates to the end-user while simultaneously interacting with the database to create a dynamic page. I used Django's module TemplateView to write my pages/views.py. The views is a class-based views (CBVs). CBVs utilize OOP principles, which allow us to use inheritance, reuse code, and generally write better and cleaner code.

##### Test
Head to pages/test.py, you will see the tests that I wrote for the pages app. Class "HomepageTests" contains functions testing different parts of the homepage. You can run this test within docker using: $ docker-compose exec web python manage.py test pages 

in your terminal.
