from flask import Flask, render_template

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
    return render_template("contact.html", contact=contacts[index])

if __name__ == "__main__":
    app.run(debug=True)