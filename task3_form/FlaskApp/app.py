from flask import Flask, render_template, request, redirect


app = Flask(__name__)

orders = []


@app.route("/", methods=['GET', 'POST'])
def show_page():
    if request.method == 'POST':
        person = request.form['person']
        food = request.form['food']
        orders.append([person, food])
        return redirect("/")
    return render_template('index.html', orders=orders)


if __name__ == "__main__":
    app.run()
