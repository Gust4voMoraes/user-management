from flask import Flask
from routes.home import home_route # import the home route from the routes folder
from routes.users import user_route # import the users routes from routes folder

#INITIALIZATION
app = Flask(__name__)

app.register_blueprint(home_route) # register the imported home route varaible
app.register_blueprint(user_route, url_prefix="/users") # register the imported user route variable

#EXECUTION
app.run(debug=True)