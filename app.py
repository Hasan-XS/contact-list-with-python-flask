from flask import Flask, render_template, request, redirect, url_for
from extention import *
import config
from model.contact import Contact

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def menu():
    contact = Contact.query.all()
    return render_template("index.html", contact=contact)


@app.route("/add-contact", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        name = request.form.get("name", None)
        last_name = request.form.get("last_name", None)
        phone = request.form.get("phone", None)
        address = request.form.get("address", None)
        code_post = request.form.get("code_post", None)

        contacts = Contact(
            name=name,
            last_name=last_name,
            phone=phone,
            address=address,
            code_post=code_post,
        )

        db.session.add(contacts)
        db.session.commit()
        return redirect(url_for("menu"))
    
    else:
        return render_template("add-contact.html")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
