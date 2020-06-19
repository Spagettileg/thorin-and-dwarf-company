# Thorin & Dwarf Company | Test Analysis & Report 

Access main [READEME](https://github.com/Spagettileg/thorin-and-dwarf-company/blob/master/README.md) file

View [Thorin & Dwarf Company](https://thorin-and-dwarf-company.herokuapp.com/) as a deployed project in Heroku

## Table of Contents
1. [Introduction](#introduction) 
2. [Systems Based Testing](#systems-based-testing)
3. [Manual Testing](#manual-testing)
    * [Contact Testing](#contact-testing)    
    * [Registration Testing](#registration-testing)
    * [Navigation Testing](#navigation-testing)
4. [Code Validation](#code-validation)
    * [Responsiveness and Rendering](#responsiveness-and-rendering)
    * [Browser Compatability](#browser-compatability)
    

## Testing
### Introduction
A combination of system based and manual testing processes was applied to this project to ensure the UXD was upheld. To make sure the data was correctly loaded, images would be successfully rendered and dynamic links would accurately support the user to navigate through this application.

The software has been thoroughly tested in many ways. JavaScript and its associated functions have all undergone extensive manual testing. JS hint was used to help validate the Javascript code.

Werkzeug library import has helped identity logic errors when trying to get Flask application, Python & JSON database to all correctly interact. 

Manual testing has been based upon a walkthrough of key process steps the User will experience.    

All possible user actions were mimicked to put the tester in the shoes of the user. 

### Systems Based Testing 

- Flask Application testing for connection to web-browser:
 
```
import os
from flask import Flask
app = Flask(__name__)
@app.route('/')  # Route decorator & default test
def hello():
    return 'Hello World'
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

```
- Outcome in Bash Ubuntu (Flask testing):

```
ubuntu:~environment $ python3 run.py
    *Serving Flask app "app" (lazyloading)
    *Envioronment: production
     WARNING: This is a development server. Do not use it in a production deployment.
     Use a production WSGI server instead.
    *Debug mode: on
    *Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
    *Restarting with stat
    *Debugger is active
    *Debugger PIN: xxx-xxx-xxx

```
- Outcome in web browser (Flask testing passed):

```
Hello World

```

### Manual Testing
##### Contact Testing

###### •	Name (contact.html)
1.	Key url address in web browser
2.	Click on **Contact** in navbar
3.	Click in **Name** field (placeholder text helps the user with data entry)
4.	Key in full name
5.	If empty fields exist when clicking **Send**, then user will get error message with request to complete missing data
6.	Once data entered, user to move to next data input request

###### •	Email Address (contact.html)
1.	Click in **Email Address** field (placeholder text helps the user with data entry)
2.	Key in email address
3.	If empty fields exist when clicking **Send**, then user will get error message with request to complete missing data
4.	Once data entered, user to move to next data input request

###### •	Phone Number (contact.html)
1.	Click in **Phone Number** field (placeholder text helps the user with data entry)
2.	Key in a password
3.	If empty fields exist when clicking **Send**, then user will get error message with request to complete missing data
4.	Once data entered, user to move to next data input request

###### •	Message (contact.html)
1.	Click in **Message** field (placeholder text helps the user with data entry)
2.	Re-Key the password
3.	If empty fields exist when clicking **Send**, then user will get error message with request to complete missing data
4.	Once data entered, user to click **Send** button
5.	User will see a confirmation message that message has been reeived

##### Registration Testing

###### •	First Name (register.html)
1.	Key url address in web browser
2.	Click on **Register** in navbar
3.	Click in **First Name** field (placeholder text helps the user with data entry)
4.	Key in first name
5.	If empty fields exist when clicking **Register**, then user will get error message with request to complete missing data
6.	Once data entered, user to move to next data input request

###### •	Surname (register.html)
1.	Click in **Surname** field (placeholder text helps the user with data entry)
2.	Key in surname
3.	If empty fields exist when clicking **Register**, then user will get error message with request to complete missing data
4.	Once data entered, user to move to next data input request

###### •	Email Address (register.html)
1.	Click in **Email Address** field (placeholder text helps the user with data entry)
2.	Key in email address
3.	If empty fields exist when clicking **Register**, then user will get error message with request to complete missing data
4.	Once data entered, user to move to next data input request

###### •	Password (register.html)
1.	Click in **Password** field (placeholder text helps the user with data entry)
2.	Key in a password
3.	If empty fields exist when clicking **Register**, then user will get error message with request to complete missing data
4.	Once data entered, user to move to next data input request

###### •	Repeat Your Password (register.html)
1.	Click in **Repeat Your Password** field (placeholder text helps the user with data entry)
2.	Re-Key the password
3.	If empty fields exist when clicking **Register**, then user will get error message with request to complete missing data
4.	Once data entered, user to click **Register** button

##### Navigation Testing
###### •	Navbar tests

1. Hover cursor on **navbar brand logo** and cursor changes to pointer and text colour change from white to grey 
2. **Navbar brand logo**, when clicked will return the user to the home page
3. Hover cursor on **Home** and cursor changes to pointer and text colour change from white to grey
4. Click **Home** for User to then navigate to `index.html` page
5. Hover cursor on **About** and cursor changes to pointer and text colour change from white to grey
4. Click **About** for User to then navigate to `about.html` page
5. Hover cursor on **Contact Us** and cursor changes to pointer and text colour change from white to grey
6. Click **Contact Us** for User to then navigate to `contact.html` page
7. Hover cursor on **Register** and cursor changes to pointer and text colour change from white to grey
8. Click **Register** for User to then navigate to **register modal** view

 
###### •	Homepage Post tests
1. Hover cursor on **more posts** button and cursor pointer appears with button colour change from Oil Blue to Deep Oil Blue 
2. Click **more posts** button and user will navigate to [The Hobbit Quotes Database](http://lotrproject.com/quotes/book/TheHobbit) to view more post material
3. Hover cursor on a **Post** and cursor pointer appears with text colour change from Coal Black to Oil Blue
4. Click **Post** text and user will navigate to wiki page to view more character post material
5. Hover cursor on a **Post Author** and cursor pointer appears with text colour change from Coal Black to Oil Blue
6. Click **Post Author** text and user will navigate to source of quote web page

###### •	About tests
1. Hover cursor on **Character Name** and cursor pointer appears with button colour change from Coal Black to Oil Blue 
2. Click **Character Name** and user navigates to single character write up

###### •	Member tests
1. Hover cursor on **Return** button and cursor pointer appears with button colour change from Oil Blue to Deep Oil Blue 
2. Click **Return** button and user navigates to `about.html` page

###### •	Social media links tests
1. Hover cursor on **Social Media Icon** and cursor pointer appears with button colour change from Coal Black to Oil Blue 
2. Click **Social Media Icon** and user will navigate to either **twitter**, **facebook** or **instagram**, depending on selected icon


### Code Validation

Code       | Url Link                          | Filename                | Outcome | Comments
-----------|-----------------------------------|-------------------------|---------|---------
HTML5      |https://validator.w3.org           |base.html                |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |index.html               |Pass     |Jinja templating language used = ok        
HTML5      |https://validator.w3.org           |about.html               |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |login.html               |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |contact.html             |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |member.html              |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |register.html            |Pass     |Jinja templating language used = ok
CSS3       |https://jigsaw.w3.org/css-validator|style.css                |Pass     |W3C CSS Validator results - CSS level 3 + SVG = ok
Javascript |https://jshint.com/                |base.html                |Pass     |Some instances of $ being undefined due to using jQuery. No errors found    
Javascript |https://jshint.com/                |main.js                  |Pass     |Some instances of $ being undefined due to using jQuery. No errors found 
Javascript |https://jshint.com/                |clean-blog.js            |Pass     |No errors found
Javascript |https://jshint.com/                |contact_me.js            |Pass     |Some instances of $ being undefined due to using jQuery. No errors found
Javascript |https://jshint.com/                |jqBootstrapValidation.js |Pass     |Some instances of $ being undefined due to using jQuery. No errors found
Python3    |http://pep8online.com              |run.py                   |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com              |test_app.py              |Pass     |All convention errors corrected = ok

#### Responsiveness & Rendering
Chrome DevTools together with a selection of mobile, table and desktop devices were relied upon through the entire software development cycle. A key objective was to test both the rendering and responsiveness of the software application against multiple screen resolutions and web browser platforms. Any bugs identified were debugged in real time with special observations noted in a [testing matrix control document](https://github.com/Spagettileg/thorin-and-dwarf-company/blob/master/tests/user-testing-thorin_vfinal.zip).

The Thorin & Dwarf Company application has been tested by students from the Slack community, together with friends and family members. Feedback on what worked well and what did not was recorded and suitable corrections to the code were keyed.

In the final analysis, this application can be passed as fully responsive across all devices that participated in testing.

#### Browser Compatability

The following browsers were used in testing the Thorin & Dwarf Company application. Internet Explorer was out of scope for testing due to obsolete capability

platform | version
---------|--------
Chrome   |71.0.3578.98
Edge     |42.17134.1.0
Firefox  |65.0.1
Safari   |12.1.4
Opera    |58.0.3135.65

#### Test Observations
The following media queries were added to improve the project responsiveness on all tested devices.

Media Query                 | Device  | Class           | Comments
----------------------------|---------|-----------------|-------------
TBC                         | TBC     | `tbc`           | `tbc`
