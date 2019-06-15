import os # We're using os module to get the 'enviroment' variable > helps connect to Cloud9
from flask import Flask, render_template # Importing our Flask Class. Render_Template supports writing of HTML code in python file.

app = Flask(__name__) # Flask convention (__name__) is our variable is called 'app'. Creating an instance & storing in a variable called 'app'

@app.route("/") # Route decorator is a way of wrapping functions. Tells Flask what URL should trigger the function

# Note: Currently, the ("/") route decorator is binded to the index() function 
# Note: whenever the root is called, then the function is called too 

def index(): # Function called 'index'
    return render_template("index.html") # Text has been replaced by the new render_template function and points towards index.html file.
    
@app.route("/about")
def about():
    return render_template("about.html", page_title="About")
    
@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")
    
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")
    
if __name__ == "__main__":             # __main__ is the name of a default module in python
    app.run(host=os.environ.get("IP"), # An internal environment variable that Cloud9 has set
    port=int(os.environ.get("PORT")),  # PORT is casted as an integer. The integer is needed 
    debug=False)                       # 'True' allows us to debug code easier. Avoid using true for formal deployment to GitHub Pages
    
    