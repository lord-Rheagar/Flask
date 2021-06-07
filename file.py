from flask import Flask

app = Flask(__name__)

lst = []

@app.route("/")
@app.route("/home")

def home_page():
    return "<h1>Welcome</h1> <b> Goto /add/nameofnewstring to add new string</b> </br>  <b> Goto /list to see string</b>"

@app.route("/add/<string:text>")

def add_text(text):
    lst.append(text)
    return f"<b>Added, {text} to the list!</b>"

@app.route("/list")

def get_list():
    concat_string = "".join(lst)
    return f"<b>Concatenated String is : {concat_string}</b>"

@app.route("/exit")
def exit():
    return "<h1>Thank You</h1>"


if __name__ == "__main__":
    app.run()