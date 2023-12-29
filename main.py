from flask import Flask,render_template

app = Flask('Project1', template_folder="templates", static_folder="static")


data = {"name": "Gleb Ignatenko",
        "age": "14",
        "city": "Kyiv"}


@app.route('/mem')
def mem():
    return render_template("mem.html")

@app.route('/podil')
def podil():
    return render_template("podil.html")

@app.route('/')
def index():
    return render_template("index.html", **data)


if __name__ == "__main__":
    app.run(debug=True)

