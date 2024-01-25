from flask import Flask, url_for, render_template

#INITIALIZATION
app = Flask(__name__)


#ROUTES
@app.route("/")
def hello():
    title = "User Management"
    users = [
        {"name": "Gustavo", "active_member": True},
        {"name": "Guilherme", "active_member": False},
        {"name": "Maria", "active_member": False},
    ]
    return render_template("index.html", title=title, users=users)#(context variable=variable of the function)


@app.route("/about")
def aboutPage():
    return """
        <h3><b>Gustavo Fernandes de Moraes</b><span>&#128125;</span>: <a href="https://linkedin.com/in/gustavo-fernandes-de-moraes">Linkedin Profile</a></h3>
"""

#EXECUTION
app.run(debug=True)