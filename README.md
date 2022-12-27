# library
Library is a web application built with Django that makes API calls to Google Book API via JQUERY in order to retrieve information about the searched book. It uses PostgreSQL to store and retrieve already searched books. Categorizes book and so much more.

### Nature of Project
My intention while programming is to showcase my python OOP and Django prowess. I wanted to make a Django project that is ready for production. Which is why I built the project within DOCKER. The database supporting this web application is POSTgreSQL!

### Distinctiveness and Complexity
My final project is distinctive and complex because I went beyond the course curriculum to learn and implement a Django application that is ready for production by learning how to use POSTgreSQL in Django, Docker, base directory templates and static files, advanced django settings in settings.py file, file/image uploads in Django to list but a few. I also implemented Django third-party packages like django-debug-toolbar, allauth, crispy_forms, crispy_bootstrap5 and django-isbn-field. This project also contains four different apps including: pages app, catalogue app, book app and accounts app. I implemented permission on this project, which restricted certain users from adding Library Books. This project is also complex and unique because it utilizes UUID as the primary key of Catalogue Model and Book Model found in Catalogue.models and Book.models respectively. UUID is excellent in achieving good security against hackers.


### Google Books API
I implemented Google Books API using JQUERY. It allows users to search for any book they have in mind. The list of books bearing that name will be displayed. Users can click on such books to be taken to the official google book page where they can read up the book and get more information on it. 


#### User Registration
Django's third-party django-allauth came in handy while working on user registeration and authentication. [Django-allauth docs](https://github.com/pennersr/django-allauth) was clear on how to use it. Django-allauth also provided the necessary views for the login, logout and user registration functionalities [par it's official repository](https://github.com/pennersr/django-allauth). Django-allauth url.py file for the view.py of auth [repository is](https://github.com/pennersr/django-allauth/blob/master/allauth/account/urls.py).

##### Test for User Registration
accounts/tests.py file holds the code for the tests written to check if the signup page is working properly. test_signup_template, test_signup_form and test_signup_view are methods under SignUpPageTests class that tests the User registration process.


#### Requirements
pip freeze > requirements.txt was necessary to create a requirement.txt file within my project directly while putting down all the modules installed in this project.


### Apps
This django project is made up of three apps namely:
1. accounts
2. pages
3. book app
4. catalogue app

#### 1. Accounts App
The accounts app is an app in this django project that handles the logic for login, signup and logout. It contains the CustomUser model of the database.

accounts/form.py contains the UserChangeForm and UserCreationForm for changing and creating the user information. 

##### Test
Head to accounts/test.py The file contains test for CustomUser. I wrote code to make sure that the custom user model is actually working and is able to create a user, superuser. I also checked for is_superuser(), is_staff() modules while testing the accounts app. In line 8 of the file, I defined a setUp function that retains self.response which helped me to reduce redundancy.
[Django's resolve()](https://docs.djangoproject.com/en/4.0/ref/urlresolvers/#resolve) came in handy to ensure that HomePageView "resolves" a given URL path on line 29 of the file.


#### 2. Pages App
This app is incharge of delivering all my templates to the end-user while simultaneously interacting with the database to create a dynamic page. I used Django's module TemplateView to write my pages/views.py. The views is a class-based views (CBVs). CBVs utilize OOP principles, which allow us to use inheritance, reuse code,  implement DRY, and generally write better and cleaner code.

##### Pages App Test
Head to pages/test.py, you will see the tests that I wrote for the pages app. Class "HomepageTests" contains functions testing different parts of the homepage. You can run this test within docker using: $ **docker-compose exec web python manage.py test pages** 
in your terminal.

#### 3. Book App
The Book app contains a Book model that stores all the books searched and saved to this web application. It allows users to save their private ebooks on this application while making it available ONLY to them through filtered queries. Users can also edit books and delete such books whenever they want.
I learnt how to upload FILES/IMAGES while working on this app.
It uses a class based view for handling the logic of each route. It is important to note that the Book Model uses the Universal Unique Identifier [UUID](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.UUIDField) in place of default django ids as the primary key of Book model. This is because, Django's default pk tells a potential hacker exactly how many records we have in the database; it tells them exactly what the id is which can be used in a potential attack; and there can be synchronization issues if you have multiple front-ends.

##### Book App Test
I imported TestCase and introduced the setUpTestData156 method to add a sample book to test. Using setUpTestData often dramatically increases the speed of your tests because the initial data is created once rather than each time for each unit test.
The first unit test, test_book_listing, checks that both its string representation and content are correct. Then we use test_book_list_view to confirm that our homepage returns a 200 HTTP status code, contains our body text, and uses the correct books/book_list.html template. Finally, test_book_detail_view tests that our detail page works as expected and that an incorrect page returns a 404. It’s always good both to test that something does exist and that something incorrect doesn’t exist in your tests. The test can be run using *docker-compose exec web python manage.py test book*


#### 3. Catalogue App
The Catalogue allows users with permission to add LIBRARY BOOKS to this project. The library is open for all to see and use but can only be added and edited from the frontend by selected users through Django permissions.
This app functions like a digital library as it allows users to borrow books and return them before the DUE DATE. 
While working on this app, I learnt how to use Django permission to allow certain permissions to certain users. Reviews was also implemented in this app which allowed users to comment on a particular book.


#### Templates
The templates of this project can be found in the BASE DIRECTORY. This is to ensure that Django is able to find templates faster than app level templates. Thereby, improving the overall speed of the application.


#### Static Files
Static Files are also found in the BASE DIRECTORY to improve speed.


#### Media Files
Media Files are those files uploaded by the user while static files includes JavaScript, CSS and images uploaded by the developer during development. Media files can be found in the BASE DIRECTORY. It includes images and documents uploaded by the USER.


#### DOCKER
Docker is a tool designed to make it easier for developers to develop, ship, and run applications by using containers. Containers allow devs to package an application with all of its requirements and configurations, such as libraries and other dependencies and deploy it as a single package. Using docker makes your app platform-independent and running a docker container on Linux, macOS, Windows or ARM-based platforms is not so different (for the majority of use cases at least) and I think that is the most out of it for most of the dev enthusiasts.
The docker files present in this project includes docker-compose-prod.yml, docker-compose.yml, Dockerfile, and .dockerignore. Docker-compose-prod.yml is ran during production while docker.compose.yml is ran during development. These two files contains set of instructions to docker on how to run the application. Dockerfile contains instructions on the python version to be used in this project, set environment variable, set the work directory, install dependencies and copy project while .dockerignore tells Docker to ignore certain files.



#### Environment Varibles
Envirnoment varibles was also set for this project especially for Django's SECRET KEY. This is to ensure that the secret key of this web application is not open for users to see in GITHUB or any other source code sharing services. Django's SECRET KEY as Django said must be kept secret!


### How to Run.
1. To run this application, you will need to install Docker on your local machine.
2. Open a virtual environment and install django using  python -m pip install django~=4.0.0
3. Run  python manage.py runserver
4. Run deactivate to deactivate virtual environment.
5. Run docker-compose up -d --build (this installs all the necessary dependencies for this application to run).
6. You are ready to run this application!
7. For every django command that you have to run be sure to pre-fix docker-compose exec web before the command! For instance, you want to run python manage.py runserver to start django. Do it like this: "docker-compose exec web python manage.py runserver" or "docker-compose exec web python manage.py makemigrations" to create migrations, and so on and so forth.
8. Run docker-compose down to stop Docker
9. Run docker-compose up -d to start up docker without reinstalling dependencies and requirements all over again!


