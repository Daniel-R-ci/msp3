# Milestone Project 3 : The ShutterClickers Photo Club

## Table of contents

## Introduction

The ShutterClickers Photo Club is a ficticious photo club. Most of the members are students at the local university and are now looking for a website to post their pictures, both as a way to inspire each other and also promote the site to attract new members, both from the university and the surrounding community.

### Other ideas considered

The photo club was one of two ideas considered before project start. They were written upp in [Initial Ideas](static/readme/README_initial_ideas.md) and discussed with Code Institute Mentor Spencer Barriball. Considering the scope of the project and the timeframe involed, the idea of the probably more complicated quiz app was dropped in favor of the photography page.

## Goals

Provide a place to post photos taken by club members. The members would like the option of choosing wether an album/category would be open to all visitors or only to club members. The club also would like a way to announce excursions or other activities, and these would also be either private (club members only) or public. Only club members should be able to post pictures and create albums, but any registered user should be able to comment on public pictures or events.

## Overview of users and needs

The following hierarchy is displayed from lowest to highest access to the site. This means that Registered Users will also have all functionality granted to Visitor, Member will also have all functionality granted to Registered Users and Visitors.

**Visitors**: Visitors will be able to see all public photo albums and the pictures they contain, as well as see publically posted events. They will also be able to see all approved comments.

**Registered users:** Visitors can register to become a user. Users will be able to give feedback on pictuers and comment on upcoming events. The comments will need to be approved by a webmaster before becoming visible.

**Members:** Members will be able to create albums and post their pictures in them. Members will also be able to post feedback on pictures or comment events and their comments will be published immediately without waiting for webmasters approval.

**Webmasters:** One or a few webmasters will have total access to the site. Webmasters will grant membership status to those users who are paying members of the ShutterClickers Photo Club.

## User stories

The following is a quick overview of the user stories that are being implemented. For a full description of all user stories accpetance criteria and Tasks, see [Full User Stories](static/readme/README_user_stories.md).

Github Projects has been used throughout the project to keep track of these user stories and their progress. All criteria and tasks are also available in the Github Project. The progress on the board at the time of project submission shows their actual status.  
The Github Project is available at [https://github.com/users/Daniel-R-ci/projects/7](https://github.com/users/Daniel-R-ci/projects/7)

### Webmaster - Administration

As a ***webmaster***, I would ***need to have full access to the site*** in order to:  
- ***approve comments made by registered users***
- ***move users to Members group after becoming members of the photo club***
- ***grant superuser rights to new webmasters***
- ***in worst case suspend someones account***

### Member - Album and photo handling

As a ***member of the photo club***, I would like to **create albums and post my pictures to them** in order to ***show them to others***. 

### Member - Create events

As a ***member***, I would like to ***post information about upcoming events***, in order to ***meet other members and engage more in the hobby***.

***Note:*** Members should not be able to delete events. If an event is canceled, the event should be changed with the information that it has been canceled. If needed, webmaster can be contacted to delete all information about the event. 

### Members & Users - Give feedback on photographs

As a ***member or registered user***, I would like to ***give feedback or words of praise on pictures***, in order to ***give the photographer both confidence and a way to hone their skills***.

### Members & Users - Comment on upcoming events

As a ***member or registered user***, I would like to ***comment on upcoming events***, in order to ***ask for more information, announce my intention to attend etc***.

### User registration

As a ***visitor to the site***, I would like to ***register to become a user***, in order to ***activate more with the club and possibly become a member***.

## Club information

As a ***visitor or registered member***, I would like to have a way to ***get more information about the ShutterClickers Photo Club and if need be contact them with questions*** in order to ***learn more about the club and possibly decide to be a member***.

## Discussion of user stories

### Member - Post pictures

What kind of information will be needed for categories and pictures? In a category with a good name and a good description there may not be a need to give information about any specific picture, but in other albums there might be a need for it. From this follows than any information about a specific picture should be optional and not required. The information that can be posted will be a short description about the picture, and another field for technical information that the photographer may want to share (ISO, shutter speed and similar things).

## Basic design of website and page requirements

The website will be built with Python / Django framework. Custom Java Script will be used to enhance user experience when needed. Bootstrap will be used to make the website responsive to different screen sizes and access both css and functionality.

The following pages/views will be accomondated:

- **Index**, the introductionary page to the website
- **Albums**, browse photos by albums
- **Photos**, bigger rendering of picture together with comment section
- **Events**, read about upcoming events and comment on them
- **Login** / **logout** / **signup**, will be handled with Django auth apps
- **Admin**, will be handled with Django Admin interface
- **About/contact**, for information about the Shutterclickers Photo Club, including contact form

## MVP Priority
(MVP- Minimal Viable Product)

The prefered index page/view is relatively complex and uses several functions to give an overwiev of what is happening on the site. It will present what is going on without having to browse around the entire site to get updated. Due to time restraints, this page will only be implemented if there is time remaining at the end of the project. Therefore, a MVP version will be constructed first to create a pleasing and welcoming entrance but without the desired functionality since focus should be on getting the core functions working in their respective pages/views before launch. Wireframes for both versions are presented in next chapter.

Getting the photo album part of the web page also has a higher priority than getting the events section up an running

Another feature that will be implemented if time permits is album and photo functionality (CRUD management) via the public website (though controlled by login). To get a MVP website up and running as soon as possible, these functions will initially be handled through Djangos Admin interface, where club members will have Group Permission to perform some of these functions in the Admin interface. They will not however have the same access as the Superuser(s) / Webmasters.

The priorities therefore works out into this:
1. Setting up admin interface
2. Creating MVP Index page
3. Implementing albums and photos (public)
4. Implementing comments on photos
5. Implementing events and comments (public)
6. Implement about/contact page §
7. Creating fully featured index page
9. Implementing CRUD functionality for photos and events in default views (not relying on admin interface)
9. Differentiating between public and private albums
10. Differentiating between public and private events

§ About info could be implemented either as static html or with dynamic information stored in database. Actual implementation will depend on time available

### MVP Priority in Github Projects

To track progress an additional column, "MVP Read" has been added to Github Project. When a user story/task fullfills the criteria for MVP launch it will be moved to this column (unless of course it also meets all criterias at the same time, in wich case it will be moved to "Done"). When all user stories are either marked as MVP Ready or Done, tasks will be moved from "MVP Ready" to "In progress" based on the priority outlined above.

### Additional tasks in Github Project

An additional item called ***Webmasters reminder*** has been created as a way for the developer to keep track of remaining tasks that doesn't specifically match a user story. This will be checked when nearing project completion, and viewed regularly as a reminder of what needs to be done. Additional tasks can be added during the project.

At project start, the list includes
- Manual test on several devices and screen sizes
- SEO and Lightroom Reports
- HTML Validation
- CSS Validation
- Python Validation

Added during the project
- Make sure active class works on all elements in navbar in base.html

## Wireframes

[Balsamic](https://balsamiq.com/) was used to construct the wireframe used during development

### Index page/view

The mvp index page that will be constructed first  
![mvp index](static/readme/MVP%20Index%20page.png)

The prefered index page with different functions that will enhance user experience but only implemented if there is time before project submission  
![Prefered index page](static/readme/Preferred%20index%20page.png)

## Colors and fonts

Black was choosen as the main background color, since black or possibly white was considered to be the colors least likely to clash with published photos. On off-white or very light gray color would be prefered for texts. Headline would breferebly stand out a little with some color between light and dark but something that doesn't stick out too much. The idea is to let the photos bring life and colors to the website, and the webpage background and other text should not detract from that.

With these critera [Coolors.co](https://coolors.co/) was used to come up with a pleasing palette.

![Colors palette](static/readme/palette.png)  
From left to right  
- black: #000000; Background
- bone:  #ece2d0; Headlines
- isabelline: #f6f0ed; Text
- giants-orange: #fe5d26ff; Links


Fonts were selected from Google Fonts. The category ***Feelng - Artistic*** was searched for headlines, and the choise fell on **Chango**. The main font ***Kumbh Sans*** was found in **Feeling - Calm**.

## Entity Relationship DiagramD

The following ERD model outlines the different entities and their relations to each other. The Entity ***Users(Django)*** represents the User model already provided by Django, and only shows the ID field for relation purposes. The foreign keys in the model matches the primary keys of related entities, but will in development be using DJango Foreign Key without actually specifiing the stored type.

Fields where datatype is followed by **?** indicates a non-required field.
Some fields are marked with on or several *:
- ' * Fields marked as Date should be implemented as DateTime fields, something not available in the program used for ERD
- ' ** Photos wont be uploaded to the database, Cloudinary will be used, and is in the model shown as Serial type instead
- ' *** Fields use to show wether albums or events are public will have the default setting to true

![ERD Model](static/readme/ERD_v1.2.png)
ERD created with [drawSQL](https://drawsql.app/)

## Database implementation

## Programming structure

## Deployment

Github has been used throughout the project to keep track up work and commits. The Github repository from the project is available at [github.com/Daniel-R-ci/msp3](https://github.com/Daniel-R-ci/msp3)

As soon as Django was installed and set up the project was Deployed to Heroku to provide hosting for the running of the page. A new Herokuapp named ***dr-ci-msp3*** was created an connected to the Github Repository. New Deployments to Django has been made after every new major function as been implemented and tested in the local development environment. The deployed version is available at [dr-ci-msp3-14a6a7c6c0fe.herokuapp.com/](https://dr-ci-msp3-14a6a7c6c0fe.herokuapp.com/)

The branch that is deployed on Heroku is the ***main*** branch. During setup phase the config var DISABLE_COLLECTSTATIC was set to 1. This was later changed after implementation of Whitenoise and the collection of static files was activated.

### Difference in deployed version and development version

The code for the development and deployed versions are the same, with the following exception.

- The .venv folder used for the virtual environment is excluded in the project's .gitignore file, since these files are only relevant for the devlopment environment
- The development version contains a env.py file, excluded in .gitignore. This file contains information not to be revealed to the public. The values set in this file is in the deployed version set in Heroku's config variables. The env.py file / config variables contains the following information:
    - DATABASE_URL: the connection string for the database used
    - DJANGO_SECRET_KEY: The SECRET_KEY originally stored in settings.py after project creation
    - DEBUG_STATUS: This value is always set to "True" in the development version and an empty string in the deployed version at Heroku (they are converted to boolean values True respectively False with the bool() method). This eliminates the need to change the status back and forth between deployment, and ensures the deployed version never accidentally gives away sensitiv error information.

## Testing

### Automated testing

### Manual testing

### Other validation

### List of notable bugs and errors caught during testing

- Low contrast may be reported between headline color and background, ok for Large Text and Icons according to WebAim
- Dotted line around Bootstrap Navbar when using Developers tools in Chrome

## Finished website

### User cases completed

### User cases began but not completed

### User cases remaing

### Future development

### Error handling

## Credits

- [Balsamic](https://balsamiq.com/) was used to construct the wireframe used during development
- [Bootstrap](https://getbootstrap.com/), for responsiveness and many other things a (but not limited to) form objects, buttons etc
- [Coolors.co](!https://coolors.co), for picking color palette
- [drawSQL](https://drawsql.app/) was used for drawing the ERD Model
- Spencer Barriball, Code Institute mentor

### Code dependencies code found online

- Login, logout and signup pages and forms have been largely re-used from Code Institute ***I think therefore I blog*** walkthrough project.
- The technic to use zip(x,y) to transfer multiple relating classes to Django Template found at [https://stackoverflow.com/questions/67961063/django-template-using-forloop-counter-as-an-index-to-a-list](https://stackoverflow.com/questions/67961063/django-template-using-forloop-counter-as-an-index-to-a-list)
- Thurough description on how CSS Object fit works found at [https://www.digitalocean.com/community/tutorials/css-cropping-images-object-fit](https://www.digitalocean.com/community/tutorials/css-cropping-images-object-fit)


