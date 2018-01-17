from flask import Flask, render_template, request, redirect
from forms import OrderForm


app = Flask(__name__)

orders = []


@app.route("/", methods=['GET', 'POST'])
def show_page():
    form = OrderForm(request.form)
    if request.method == 'POST' and form.validate():
        person = form.person.data
        food = form.food.data
        orders.append([person, food])
        return redirect("/")
    return render_template('index.html', orders=orders)


if __name__ == "__main__":
    app.run()
