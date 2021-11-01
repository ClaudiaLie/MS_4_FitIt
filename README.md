# Fit It
[Fit It Website](https://fit-it-claudia.herokuapp.com/)

FitIt is the fourth and last project submission for the Full Stack Frameworks Milestone Project by Code Institute. 

The project consists in a gym website, where any user can register or login with their account, subscribe to any subscription plan they prefer, purchase the gym merch, and take track of their purchases.
The application uses Python, Django, JavaScript and CSS as main technologies.

## Table of Contents
- [User Experience](#user-experience)
    * [Strategy Plane](#strategy-plane)
    * [Scope Plane](#scope-plane)
    * [User stories](#user-stories)
    * [Skeleton Plane](#skeleton-plane)
    * [Wireframes](#wireframes)
    * [Design](#design)
        + [Images](#images)
        + [Colors](#colors)
- [Database Schema](#database-schema)
    * [Data Models](#data-models)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)


# User Experience

## Strategy Plane
Fit It is a gym which provides the customer all the products needed to have a better fitness experience, thanks to the store containing many selected items.
The website is clean and aims to reach a vast target audience. Its simple design makes the navigation intuitive and easy, giving the business a higher chance that the customer will feel comfortable and stay on the website to navigate further.

## Scope Plane
The website main goal is to make the Visiting User interested into joining a fitness plan with our experts. The Users have to be able to register easily and manage their account immediately.
The website must be responsive for all devices and easy to navigate for everyone.

### User stories
![User Stories](https://github.com/ClaudiaLie/MS_4_FitIt/blob/main/media/readme_img/user-story.jpg?raw=true)

Registration and User Account settings are satisfied by using Django Allauth, an open source integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

## Skeleton Plane
The website features a Homepage with a main navbar to navigate the main sections of the website: Train for trainings, Prices for subscription plans and Store for the merch. 
- In the Homepage there is immediately a link to the subscription plans, to give to the expert users an efficient navigation.
- The Train page displays all the gym classes available, separated into main sections that can be navigated further if interested, and a calendar with the schedule of the weekly trainings.
- The Prices page contains all the subscription plans briefly described, with a direct link to the product detail in the store page.
- The Store page has its own secondary navigation bar, which regroup in main categories the products available into the store, and extends with a dropdown menu to the more specific items categories.
Each product has its own page with a more detailed description and purchase option.
- The User will be able to Register or Login to the website anytime, thanks to the Account icon always displayed on the page header.

## Wireframes
The wireframes are created with [Wireframe.cc](https://wireframe.cc/)

**Homepage**
![Home Page](https://github.com/ClaudiaLie/MS_4_FitIt/blob/main/media/readme_img/homepage.jpg?raw=true)

**Store Page**
![Store Page](https://github.com/ClaudiaLie/MS_4_FitIt/blob/main/media/readme_img/store.jpg?raw=true)

**Shopping Bag**
![Shopping Bag](https://github.com/ClaudiaLie/MS_4_FitIt/blob/main/media/readme_img/shopping-bag.jpg?raw=true)

**Gym Classes Homepage**
![Gym Classes Homepage](https://github.com/ClaudiaLie/MS_4_FitIt/blob/main/media/readme_img/gym-classes-home.jpg?raw=true)

**Gym Class Page Detail**
![Gym Class Page Detail](https://github.com/ClaudiaLie/MS_4_FitIt/blob/main/media/readme_img/gym-class-page.jpg?raw=true)

**Subscription Page**
![Subscription Page](https://github.com/ClaudiaLie/MS_4_FitIt/blob/main/media/readme_img/subscription-page.jpg?raw=true)


## Design 

### Images
- All the images for the website are copyright free from [Unsplash](https://unsplash.com/)
- The images for the website store items are from Code Institute Boutique Ado Project and from Amazon.uk.

### Colors
I have been researching the psychology of colors to find a color scheme that would be perceieved as interesting, inviting and pleasant for any visitor.
An excellent source to get inspired was [Canva](https://www.canva.com/colors/color-meanings/) but I have decided to keep the color scheme of the main landing page image as follows:

![alt text](https://github.com/ClaudiaLie/MS_4_FitIt/blob/main/media/readme_img/website_palette.jpg?raw=true)

With an extra touch of orange #fb8b3c to symbolize strength, power and energy.

# Database Schema
In the development of Fit It, I have used SQLite3 database as part of Django framework and Heroku PostGres to handle the database for the production version of the website.

I have used [MongoDB](https://www.mongodb.com/) and [MongoDB Atlas](https://www.mongodb.com/atlas/database) to create and export my own fixtures of the products and categories.
[Django’s authentication system](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/) and [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) are also integrated sets of Django and helped manage authentication, registration and account management.
The models below are created with dbdiagram.io:

## Data Models

### Checkout App

**Order Model**

| Field | Field Type | Field Options |
| --- | --- | ---|
| order_number | CharField | max_length=32, null=False, editable=False |
| user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True, blank=False, related_name='orders' |
| full_name | CharField | max_length=50, null=False, blank=False |
| email | EmailField | max_length=254, null=False, blank=False |
| phone_number | CharField | max_length=20, null=True, blank=True |
| country | CountryField | blank_label="Country *", null=False, blank=False |
| postcode | CharField | max_length=20, null=True, blank=True |
| town_or_city | CharField | max_length=40, null=False, blank=False |
| street_address1 | CharField | max_length=50, null=False, blank=False |
| street_address2 | CharField | max_length=50, null=False, blank=False |
| date | DateTimeField | auto_now_add=True |
| delivery_cost | DecimalField | max_digits=6, decimal_places=2 null=False, default=0 |
| order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| original_bag | TextField | null=False, blank=False, default='' |
| stripe_pid | CharField | max_length=254, null=False, blank=False, default='' |

**Order Line Model**

| Field | Field Type | Field Options |
| --- | :--- | ---|
| order | ForeignKey | Order, null=False, blank=False, on_delete=models.CASCADE, related_name="lineitems" |
| product | ForeignKey | Product, null=False, blank=False, on_delete=models.CASCADE |
| product_size | CharField | max_lenght=2, null=True, blank=True, on_delete=models.CASCADE |
| quantity | IntegerField | null=False, blank=False, default=0
| lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |

### Product App

**Category Model**

| Field | Field Type | Field Options |
| --- | --- | --- |
| name | CharField | max_length=254 |
| friendly_name | CharField | max_length=254, null=True, blank=True, |

**Product Model**

| Field | Field Type | Field Options |
| --- | --- | --- |
| category | ForeignKey | 'Category', null=True, blank=True, on_delete=models.SET_NULL |
| sku | CharField | max_length=254, null=True, blank=True |
| name | CharField | max_length=254 |
| description | TextField | 
| has_sizes | BooleanField | default=False, null=False, blank=True |
| price | DecimalField | max_digits=6, deciaml_places=2 |
| image_url | URLField | max_digits=1024, null=True, blank=True |
| image | ImageField | null=True, blank=True |

**Product Review**
| Field | Field Type | Field Options |
| --- | --- | --- |
| product | ForeignKey | Product, related_name='reviews', on_delete=models.CASCADE |
| user | ForeignKey | User, related_name='reviews', on_delete=models.CASCADE |
| content | TextField | blank=True, null=True |
| stars | IntegerField |
| date_added | DateTimeField | auto_now_add=True |



### Profiles App

**User Profile Model**

| Field | Field Type | Field Options |
| --- | :--- | ---|
| user | OneToOneField | User, on_delete=models.CASCADE |
| default_phone_number | CharField | max_length=20, null=True, blank=True |
| default_street_address_1 | CharField | max_length=80, null=True, blank=True |
| default_street_address_2 | CharField | max_length=80, null=True, blank=True |
| default_town_or_city | CharField | max_length=40, null=True, blank=True |
| default_postcode | CharField | max_length=20, null=True, blank=True |
| default_country | CountryField | blank_label="Country", null=True, blank=True |

# Technologies Used

**Core Coding**

- HTML
- CSS
- Python
- JavaScript

**Integrations**

- Django and Django Allauth
- Bootstrap
- Font Awesome
- JQuery
- Google Fonts
- Stripe

**Database Management**

- MongoDB Atlas
- MongoDB Compass

**Version Control, Storage and Hosting**

- GitHub
- GitPod
- Heroku
- AWS

# Testing

A full manual testing file can be found [here.](https://github.com/ClaudiaLie/MS_4_FitIt/blob/main/readme/testing.md)

- For python code validation I have been using [pep8 online](http://pep8online.com/)
- For HTML validation I have used [validatorW3](https://validator.w3.org/)
- For CSS validation I have used [jigsaw.W3](https://jigsaw.w3.org/css-validator/)
- For responsiveness testing I have used Google DevTools

# Deployment
Fit It has been created on Gitpod, with commits pushed directly to the GitHub repository. The project has been deployed to Heroku, which was synchronized to GitHub to update the live site.
The static files are stored in Amazon AWS and the payment infrastructure is managed by Stripe's software and APIs.

## GitHub

To clone the project from GitHub:
- From the Repository page, click the green GitHub button
- From the top of the Repository, Select the Code dropdown menu and select the preferred option: 
  1. Download Zip and run locally. Remember to install any required module and freeze it in requirements.txt and to save all your secret keys in an env.py file.
  2. Open the Repository directly with GitHub Desktop.

## Heroku

After creating a repository in Github and an account on Heroku, create a new app from your Heroku dashboard and follow this steps:

- Enter your 'App name' and choose the appropriate region, then click 'Create app'.
- On the 'Resources' tab, search and add on the Heroku Postgres database.

- To use Postgres, install dj_database_url, and psycopg2 in the project terminal using the following commands;

    `$ pip3 install dj_database_url`

    `$ pip3 install psycopg2-binary`

- Freeze the requirements to ensure Heroku installs all the apps requirements when deployed using the following command;

    `$ pip3 freeze > requirements.txt`

- To migrate to the Postgres, go to settings.py and add the following import;

    `import dj_database_url`

   Then down in the databases setting comment out the default configuration and replace the default database with a call to dj_database_url.parse and give it the database URL from Heroku which can be found under the Heroku app setting config vars.

- Apply all migrations using the following command;

    `$ python3 manage.py migrate`

    After migrations have been applied you will need to re-upload the fixtures to the heroku database using. 

    `$ python3 manage.py loaddata categories`
    `$ python3 manage.py loaddata products`
    
Your database should now be set up on Heroku.

- Create a superuser to log in with using the following command;

    `$ python3 manage.py createsuperuser`

- Go to the Settings tab on Heroku, scroll to the 'Config Vars' section, and click 'Reveal Config Vars'. 

   Enter the variables (key and value) contained in your gitpod environment setting.

- Install gunicorn using the following command;

    `$ pip3 install gunicorn`

    and then:

    `$ pip3 freeze > requirements.txt`


- Create a Procfile and add:

    `web: gunicorn xeption.wsgi:application`

    This tells Heroku to create a web dyno which will run gunicorn and serve the Django app.

   
- Then you need to temporarily disable collectstatic to ensure that Heroku won't collect static files on deployment. This is done by adding the below variable;

    | DISABLE_COLLECTSTATIC  | 1 |

- Add the hostname of Heroku app to allowed hosts in settings.py

- Now you can commit all the changes and push to GitHub;

    `$ git add .`
    `$ git commit -m <'your commit message'>`
    `$ git push`

    If you created your app on the website you will need to initialize your Heroku git remote using the following command;

    `$ heroku git:remote -a xeption`

    Then use the following command to push to Heroku;

    `$ git push heroku master`


# Credits
- Code Institute course material was the main inspiration for this project.
- Slack community has been, as always, an amazing source for bug fixes and to solve any doubt.
- Stack Overflow helped me to solve the cards elements responsiveness.
- The Deployment section of this README.md is inspired by [mion93](https://github.com/mion93/xeption-ms4#readme) repository.
- The product review has been created following [Code With Stein](https://github.com/SteinOveHelset/saulgadgets).