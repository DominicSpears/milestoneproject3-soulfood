# Soul Food!

Welcome to Soul Food, a website for users all over the world to read, 
create and share recipes. Made for my Code Institute Milestone Project 3.

Follow the link to [Soul Food](link needed)

![Image](website multi sizes)

### Contents

1. [Introduction](#intro) 
2. [UX](#ux)
3. [Technologies](#tech) 
4. [Features](#feat)
5. [Testing](#test)
6. [Deployment](#deploy)
7. [Credits](#credit)

___

<a name="intro"></a>
### Introduction

This website is designed to utilise a backend database. By doing so users can read through 
a list of recipes as well as create, edit and delete their own. Each recipe has its own page
to clearly display the information provided, including an ingredients list, method and various
dietary requirements. Also each user has access to their own profile page, a convenient place 
to find all of the recipes that they have created. Alongside this, the site creator is able 
to display and promote a line of cookware, in a way that is organic to the user needs. 
___

<a name="ux"></a>
### UX

### Strategy Plane
#### Potential Users

Visitors
* Experienced with cooking 
* New to cooking
* Not cooking, looking for cookware range
* Site administrator

### Scope Plane
#### Features specific for users

Experienced with cooking
* a wide range of recipes and cuisines
* an easy way to search recipies
* indicators if a meal is vegetarian, vegan, spicy
* calorie count per serving

New to cooking
* ingredients list with clear pairs amounts 
* easy to follow steps
* a picture of each dish
* a clear indication of prep time, cook time and servings

Not cooking, looking for cookware range
* dedicated page for cookware
* clear product images
* links to store/purchase option
* benefits list of specific cookware range

Site administrator
* Able to edit and delete all recipes
* Add, edit and delete cuisines
* Edit and delete users
* Promote the cookware line

### Structure Plane
#### User stories

Experienced with cooking:
1.	As someone with cooking experience, I am looking for a wide range of recipes from a number of varying cuisines. 
2.	As someone with cooking experience, I want a search bar or filter to narrow down the available results and make it easier to find specific recipes.
3.	As someone with cooking experience, I want to know if a meal is suitable for vegetarians, vegans or has any other notable traits.
4.	As someone with cooking experience, I am very conscious about what I eat and want to know how many calories are contained in each serving. 

New to cooking
1.	As someone new to cooking, I want an ingredients list that clearly states each ingredient paired with the amount required.
2.	As someone new to cooking, I want a method that is easy to read and concise, with each step being easy to follow along with. 
3.	As someone new to cooking, I want a picture of each dish to be included with its recipe, so that I can see the completed dish before cooking.
4.	As someone new to cooking, I want to know vital information about each recipe such as prep time, cook time and serving suggestions.

Not cooking, looking for cookware range
1.	As someone researching cookware specifically, I want a page dedicated to only cookware, without any recipes present.
2.	As someone researching cookware specifically, I want clear images of each piece of cookware.
3.	As someone researching cookware specifically, I want there to be links to a store at which I can purchase the desired cookware.
4.	As someone researching cookware specifically, want to know the benefits to the cookware range as a whole e.g. health benefits, materials used.

Site administrator
1. As a site administrator, I want the ability to edit and delete all recipes, even if I didn't write them myself.
2. As a site administrator, I want the ability to add, edit and delete cuisines that users can choose to describe their recipes. 
3. As a site administrator, I want the ability to edit and delete users and complete general site maintenance. 
4. As a site administrator, I want to promote the cookware tha our site is partnered with.   

### Skeleton Plane
#### Wireframes

[Mobile Wireframes](static/images/wireframes/mobile-med.jpg)

[Tablet Wireframes](static/images/wireframes/tablet-med.jpg)

[Desktop Wireframes](static/images/wireframes/desktop-med.jpg)

### Surface Plane

* Background - White/off white e.g. #FFF/#F7F6FA
* Colours/font colours – White/off white e.g. #FFF/#F7F6FA – plain colour to complement the brighter, 
focus colours without overwhelming, #447B8C blue – colour of pans in cookware set, #71B104/ #24580C green
 – colour of some foods, herbs, vegetables
___

<a name="tech"></a>
### Technologies

Technologies used to create the site:

#### Languages
* HTML 
  * The project uses **HTML 5** to create the basic layout and site structure.
* CSS
  * The project uses **CSS 3** to style the html to be aesthetically pleasing and responsive.
* JavaScript
  * The project uses **JavaScript** to provide an interactive experience and functionality.. 
* Python
  * The project uses **Python3** to link the main site and the database. 

#### Database
* [Mongo DB](https://www.mongodb.com/)
  * the project uses **mongo db** as a database provider to store various forms of information.

#### Libraries
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
  * the project uses **flask** as an application framework to aid the creation of complex applications.
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
  * the project uses **jinja v3.0.1** as a templating engine to allow writing code similar to python syntax.
* [PyMongo](https://pypi.org/project/pymongo/)
  * the project uses **pymongo v3.11.4** to connect python code to the mongo database.
* [Materialize](https://flask.palletsprojects.com/en/2.0.x/)
  * the project uses **materialize** as a responsive front-end framework based on material design.
* [Font Awesome](https://fontawesome.com/) 
  * The project uses **Font Awesome Version 5.15.1** to add icons that aid aesthetics or provide social media links.
* [Google Fonts](https://fonts.google.com/)
  * the project uses **google fonts** as a source for its extra fonts.

#### Tools
* [Git](https://git-scm.com/)
  * The project uses **git** as version control.
* [Github](https://github.com/)
  * The project uses **Github** to provide hosting for the development process.
* [Gitpod](https://www.gitpod.io/)
  * The project uses **Gitpod** as a development environment in the browser.
* [Color Dropper](https://chrome.google.com/webstore/detail/color-dropper/cbagleaaaocejmdeichhdkmjebpljckh)
  * The project uses the **color dropper** (a Chrome add on) to help select colors.
* [Balsamiq](https://flask.palletsprojects.com/en/2.0.x/)
  * the project uses **balsamiq** as a wireframing tool to plan the layout of the site.
* [Am I responsive]()
  * the project uses **am i responsive** to create the readme hero image.

#### Hosting 
* [Heroku](https://www.heroku.com/home)
  * the project uses **heroku** as to deploy, manage, and scale the site.
___

<a name="feat"></a>
### Features

#### Register Page
##### Active
* Username and password input
* Register button, adds new user details to the database
* Link to login page

#### Login Page
##### Active
* Username and password input
* Login button, logs existing user into the site, to their profile page
* Link to register page

#### Navbar
##### Active
* Brand logo links to homepage
* Navbar buttons link to individual pages
* Certain nav links only appear when a user or an admin is logged in
* Log out button ends session

#### Footer
##### Active
* Links to social media sites, bring up a new tab

#### Home Page
##### Active
* Link to cookware and recipe page
* If a user/admin is logged in, link to profile page
* If no user/admin is logged in, link to login page

#### Cookware Page
##### Active
* Add cookware button links to add cookware page (admin only)
* For loop reveals all cookware items in the database
* Website button linked to online store for idividual item
* Edit button links to edit cookware page (admin only)
* Delete button removes item from database (admin only)
* Delete modal to confirm removal of an item

#### Add Cookware Page
##### Active
* Inputs for item name, price, image and website link
* Confirmation button add item to the database
* Cancel button returns user to cookware page
* Add modal to confirm addition of an item

#### Edit Cookware Page
##### Active
* Input fields show existing data
* Confirmation button linked to confirmation modal
* Cancel button returns user to cookware page
* Edit modal to confirm update of an item

#### Recipe Page
##### Active
* For loop reveals all recipes in the database
* Search reveals recipes based on the recipe name or cuisines
* Reset button returns all recipes to the page
* Full recipe button linked to view recipe page

#### View Recipe Page
##### Active
* Displays all recipe information from the database
* Dietary requirements (vegetarian, vegan, spicy) displayed with 
color coded icons, grey for no, colored for yes

#### Add Recipe Page (User only)
##### Active
* Input fields for all recipe information
* Cuisine dropdown gets options from the database
* Dietary requirement switches
* Ingredients/method input will recieve a custom number of items
* Plus button adds an input, minus removes an input
* Confirmation button adds a recipe to the database
* Cancel button returns user to recipe page

#### Profile Page
##### Active
* For loop shows all recipes matching the username(user)
* For loop shows all recipes(admin)
* Full recipe button linked to view recipe page
* Edit button linked to edit recipe page
* Delete button linked to confirmation modal
* Delete modal removes recipe from database

#### Edit Recipe Page
##### Active
* Input fields show existing data
* Confirmation button linked to confirmation modal 
* Cancel button returns user to profile page
* Edit modal updates recipe in the database

#### User Page (admin only)
##### Active
* For loop shows all user in the database
* Edit button linked to edit user page
* Delete buttom linked to confirmation modal
* Delete modal removed user from database

#### Edit user Page
##### Active
* Input fields show existing data
* Switch allows users to be made administrators
* Confirmation button linked to confirmation modal
* Cancel button returns user to cookware page
* Edit modal to confirm update of a user

#### Cuisine Page (admin only)
##### Active
* Add cuisine button links to add cuisine page
* For loop reveals all cuisines in the database
* Edit button links to edit cuisine page
* Delete button removes cuisine from database
* Delete modal to confirm removal of an item

#### Add Cuisine Page (admin only)
##### Active
* Input for cuisine name
* Confirmation button linked to modal
* Cancel button returns user to cuisine page
* Modal adds new cuisine to database

#### Edit Cuisine Page (admin only)
##### Active
* Input field shows existing data
* Confirmation button linked to confirmation modal
* Cancel button returns user to cuisine page
* Modal to confirm update of a cuisine
___

<a name="test"></a>
### Testing

For all testing, please follow the link to a dedicated page. [Testing Page](testing.md) 
___

<a name="deploy"></a>
### Deployment

#### To deploy to heroku:
1. Create an app in heroku
2. In the config vars, add IP, Port, db uri and sectret key
3. Create and fill a requirements.txt file using python -m pip freeze
4. Change settings to debug = false in app.py
5. Ensure env.py is included in gitignore file
6. Remove import env from the app.py
7. Code is pushed to github
8. In heroku, set to the github deployment method for automatic updates 
9. To deploy click enable automatic deploys.  

#### To run this project locally:
You will need a github account and to use the chrome browser
1. Install the Github browser extensions for chrome, restart after installation
2. Login to gihub
3. Navigate to the project repository
4. Click on the "Gitpod" button, located in the top right of the page menu
5. This creates a new workspace for local workspace
6. In gitppd, create env.py file with the following contents:
  * os.environ.setdefault("IP", "0.0.0.0")
  * os.environ.setdefault("PORT", "5000")
  * os.environ.setdefault("SECRET_KEY", <>)
  * os.environ.setdefault("MONGO_URI", "mongodb+srv://domSpears:<>@myfirstcluster.7ycsu.mongodb.net/recipe_book?retryWrites=true&w=majority")
  * os.environ.setdefault("MONGO_DBNAME", "recipe_book")

#### To clone this project (work within a local IDE)
1. Select the repository from githib
2. On the project page, click on the "code" dropdown menu icon
3. Copy the clone url by clicking the clipboard icon on the right side
4. Open git bash
5. Change wroking direcory to location where you want directory to be clones
5. Type git clone then paste the copied url
6. Press enter, the local clone is created
___

<a name="credit"></a>
### Credits

#### Code
* Force edit and delete buttons of recipes to the bottom of the div. [w3schools](https://www.w3schools.com/cssref/pr_pos_bottom.asp)

* Writing an if statment used for page authentication. [w3schools](https://www.w3schools.com/python/python_conditions.asp)

* How to make an input field accept a url (for recipe/cookware images). [w3schools](https://www.w3schools.com/tags/att_input_type_url.asp)

* Understanding how to add a customer number of ingredients/method steps. Mentor guidance.

* Create a new page to prevent the page position changing after a search. Mentor guidance.

* Understand the css grid and how to make divs responsive. [materialize](https://materializecss.com/grid.html)

* Learn how to capitalise the username on the profile page. [w3schools](https://www.w3schools.com/cssref/pr_text_text-transform.asp)

* Allow website links to be created in a new tab. [css-tricks](https://css-tricks.com/snippets/html/open-link-in-a-new-window/)

* Helped me understand jinja loops and statments [Codeburst](https://codeburst.io/jinja-2-explained-in-5-minutes-88548486834e) 

* Build a for loop of recipe cards. [Home assistant](https://community.home-assistant.io/t/build-cards-with-for-loop/212311)

#### Media

##### Images
* Recipe images were taken from the BBC food website.
* Cookware images were taken from the Greenpan website, mayflower collection.
* All other images were located via bing images, searched under "free to share and use" licences.

##### Content
* Recipe content (ingredients, method, e.t.c.) was taken from the BBC food website.
* Cookware content (prices, names e.t.c.) was taken from the the Greenpan cookware website.

#### Acknowledgements

* Inspired by [W3Schools.com](https://www.w3schools.com/html/html_intro.asp)
General reference / tutorial assistance.

* Inspired by [Materialize.com](https://materializecss.com/)
General reference / tutorial assistance.

* Inspired by [BBC Food](https://www.bbc.co.uk/food)
General reference, inspiration.

* Inspired by [Code Institute Backend Mini Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/054c3813e82e4195b5a4d8cd8a99ebaa/)
General reference, inspiration.

* Guido Cecilio (mentor) for offering guidance and support.
___