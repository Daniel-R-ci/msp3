# Milestone Project 3 : The ShutterClickers Photo Club

## Full user stories including critera and tasks

### Webmaster - Administration

As a ***webmaster***, I would ***need to have full access to the site*** in order to:  
- ***approve comments made by registered users***
- ***move users to Members group after becoming members of the photo club***
- ***grant superuser rights to new webmasters***
- ***in worst case suspend someones account***

**Criteria**

- An admin page will total rights


**Tasks**

- Implement an functional and visibly pleasing Django Admin interface where all necessary inforamtion is presented in a clear and easy way


### Member - Album and photo handling

As a ***member of the photo club***, I would like to **create albums and post my pictures to them** in order to ***show them to others***. 

**Criteria**

- Be able to create new albums, private or public
- Be able to upload pictures to one of my albums, including optional information about the picture (see discussions below)
- Be able to edit or delete albums if needed
- Be able to edit photos (or information relating to them) or delete them altoghether

**Task**

- Include full CRUD functionality for members to handle their albums and pictures
- Implement showing albums and photos on the website
- Make sure private albums are not shown to visitors or users

**Priority:**

### Member - Create events

As a ***member***, I would like to ***post information about upcoming events***, in order to ***meet other members and engage more in the hobby***.

**Criteria**

- Be able to post information about upcoming events
- Be able to edit information about upcoming events, if they change

**Task**

- Implement a way for adding and editing events
- Implement showing of events on the website
- Make sure private events are not shown to visitors or users

***Note:*** Members should not be able to delete events. If an event is canceled, the event should be changed with the information that it has been canceled. If needed, webmaster can be contacted to delete all information about the event. 


### Members & Users - Give feedback on photographs

As a ***member or registered user***, I would like to ***give feedback or words of praise on pictures***, in order to ***give the photographer both confidence and a way to hone their skills***.

Criteria

- Be able to post comments on pictures (users would need to have their comments approved by webmaster)
- Be able to read approved comments

Tasks

- Implement CRUD functionality for comments made by users and members
- Make sure users comments are not displayed unless approved by webmaster
- Display approved comments in relation to related picture

### Members & Users - Comment on upcoming events

As a ***member or registered user***, I would like to ***comment on upcoming events***, in order to ***ask for more information, announce my intention to attend etc***.

**Criteria**

- Be able to post comments on events (users would need to have their comments approved by webmaster)
- Be able to read approved comments

**Tasks**

- Implement CRUD functionality for comments made by users and members
- Make sure users comments are not displayed unless approved by webmaster
- Display approved comments in relation to related event


### User registration

As a ***visitor to the site***, I would like to ***register to become a user***, in order to ***interact more with the club and possibly become a member***.

**Criteria**

- Be able to register as a new user

**Task**

- Implement a sign up form that registers a new user


