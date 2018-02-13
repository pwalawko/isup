from flask import Flask, render_template, request, redirect


app = Flask(__name__)

CHARACTERS = ('znak', 'znaki', 'znaków')
orders = []


def plural_form(n):
    if n == 1:
        return 0
    if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        return 1
    return 2


def length_validation(field, req=False, min_le=None, max_le=None):
    field_length = (field and len(field)) or 0
    if field_length == 0:
        if req:
            return "Nie zapomnij o tym polu."
    elif min_le is not None and field_length < min_le:
        return f'Co tak skromnie? Wpisz co najmniej \
            {min_le} {CHARACTERS[plural_form(min_le)]}.'
    elif max_le is not None and field_length > max_le:
        return f'Nie przesadzasz z tą ilością? Wpisz maksymalnie \
            {max_le} {CHARACTERS[plural_form(max_le)]}.'
    else:
        return False


@app.route("/", methods=['GET', 'POST'])
def show_page():
    if request.method == 'POST':
        person = request.form['person']
        food = request.form['food']

        person_val_msg = length_validation(
            person, req=True, min_le=3, max_le=64
        )
        food_val_msg = length_validation(
            food, req=True, max_le=246
        )

        if person_val_msg or food_val_msg:
            person_is_valid = "is-invalid" if person_val_msg else None
            food_is_valid = "is-invalid" if food_val_msg else None
            return render_template(
                'index.html',
                orders=orders,
                person=person,
                food=food,
                person_val_msg=person_val_msg,
                food_val_msg=food_val_msg,
                person_is_valid=person_is_valid,
                food_is_valid=food_is_valid
            )

        orders.append([person, food])
        return redirect("/")

    return render_template(
        'index.html', orders=orders,
    )


if __name__ == "__main__":
    app.run()
