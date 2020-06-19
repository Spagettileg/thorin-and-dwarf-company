# Thorin & Dwarf Company | Test Analysis & Report 

Access main [READEME](https://github.com/Spagettileg/thorin-and-dwarf-company/blob/master/README.md) file

View [Thorin & Dwarf Company](https://thorin-and-dwarf-company.herokuapp.com/) as a deployed project in Heroku

## Table of Contents
1. [Introduction](#introduction) 
2. [Systems Based Testing](#systems-based-testing)
3. [Manual Testing](#manual-testing)
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
##### Registration Testing

##### Navigation Testing

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
Javascript |https://jshint.com/                |main.js                  |Pass     |No errors found
Javascript |https://jshint.com/                |clean-blog.js            |Pass     |Some instances of $ being undefined due to using jQuery. No errors found
Javascript |https://jshint.com/                |contact_me.js            |Pass     |Some instances of $ being undefined due to using jQuery. No errors found
Javascript |https://jshint.com/                |jqBootstrapValidation.js |Pass     |Some instances of $ being undefined due to using jQuery. No errors found
Python3    |http://pep8online.com              |run.py                   |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com              |test_app.py              |Pass     |All convention errors corrected = ok

### Responsiveness & Rendering
Chrome DevTools together with a selection of mobile, table and desktop devices were relied upon through the entire software development cycle. A key objective was to test both the rendering and responsiveness of the software application against multiple screen resolutions and web browser platforms. Any bugs identified were debugged in real time with special observations noted in a [testing matrix control document](https://github.com/Spagettileg/thorin-and-dwarf-company/blob/master/tests/user-testing-thorin_vfinal.zip).

The Thorin & Dwarf Company application has been tested by students from the Slack community, together with friends and family members. Feedback on what worked well and what did not was recorded and suitable corrections to the code were keyed.

In the final analysis, this application can be passed as fully responsive across all devices that participated in testing.

## Browser Compatability

The following browsers were used in testing the Thorin & Dwarf Company application. Internet Explorer was out of scope for testing due to obsolete capability

platform | version
---------|--------
Chrome   |71.0.3578.98
Edge     |42.17134.1.0
Firefox  |65.0.1
Safari   |12.1.4
Opera    |58.0.3135.65
