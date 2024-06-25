from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts = [
    {
        "name": "John Doe",
        "age": 30,
        "phone": "123-456-7890",
        "email": "john.doe@example.com",
    },
    {
        "name": "Jane Smith",
        "age": 25,
        "phone": "234-567-8901",
        "email": "jane.smith@example.com",
    },
    {
        "name": "Michael Johnson",
        "age": 40,
        "phone": "345-678-9012",
        "email": "michael.johnson@example.com",
    },
    {
        "name": "Emily Davis",
        "age": 35,
        "phone": "456-789-0123",
        "email": "emily.davis@example.com",
    },
    {
        "name": "William Brown",
        "age": 28,
        "phone": "567-890-1234",
        "email": "william.brown@example.com",
    },
]

@app.route("/")
def main_page():
    return render_template("main.html", contacts=enumerate(contacts))

@app.route("/<int:index>")
def contact_page(index):
    if index >= len(contacts):
        index = len(contacts) - 1
    return render_template("contact.html", contact=contacts[index])

@app.route("/add", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        new_contact = {
            "name": request.form["name"],
            "age": request.form["age"],
            "phone": request.form["phone"],
            "email": request.form["email"],
        }
        contacts.append(new_contact)
        return redirect(url_for("main_page"))
    return render_template("add_contact.html")

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_contact(index):
    if index >= len(contacts):
        return redirect(url_for("main_page"))

    if request.method == "POST":
        contacts[index] = {
            "name": request.form["name"],
            "age": request.form["age"],
            "phone": request.form["phone"],
            "email": request.form["email"],
        }
        return redirect(url_for("contact_page", index=index))
    return render_template("edit_contact.html", contact=contacts[index], index=index)

if __name__ == "__main__":
    app.run(debug=True)