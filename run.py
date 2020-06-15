import os # We're using os module to get the 'enviroment' variable > helps connect to Cloud9
import json
from flask import Flask, render_template, request, flash # Importing our Flask Class. Render_Template supports writing of HTML code in python file.

app = Flask(__name__) # Flask convention (__name__) is our variable is called 'app'. Creating an instance & storing in a variable called 'app'
app.secret_key = 'some secret' 

@app.route("/") # Route decorator is a way of wrapping functions. Tells Flask what URL should trigger the function

# Note: Currently, the ("/") route decorator is binded to the index() function 
# Note: whenever the root is called, then the function is called too 

def index(): # Function called 'index'
    return render_template("index.html") # Text has been replaced by the new render_template function and points towards index.html file.
    
@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)
    
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name: # Matching url object to member name. 
                member = obj
                
    return render_template("member.html", member=member) # Return to render the detail captured via member.html file
    
@app.route("/contact", methods=["GET", "POST"]) # The GET & POST arguments are set in a array. 
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form["name"])) # For Flash messaging - link to contact.html page
    return render_template("contact.html", page_title="Contact")
    
@app.route("/register")
def register():
    return render_template("register.html", page_title="Register")
    
if __name__ == "__main__":             # __main__ is the name of a default module in python
    app.run(host=os.environ.get("IP"), # An internal environment variable that Cloud9 has set
    port=int(os.environ.get("PORT")),  # PORT is casted as an integer. The integer is needed 
    debug=False)                       # 'True' allows us to debug code easier. Avoid using true for formal deployment to GitHub Pages
    
    