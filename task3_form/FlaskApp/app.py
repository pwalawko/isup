import os
import sqlite3
from flask import Flask, g, render_template, request, redirect


app = Flask(__name__)
app.config.from_object(__name__)

CHARACTERS = ('znak', 'znaki', 'znaków')


app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'zarelko.db'),
    SECRET_KEY='development key'
))


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


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
    db = get_db()
    cur = db.execute('select person, food from orders')
    entries = cur.fetchall()

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
                entries=entries,
                person=person,
                food=food,
                person_val_msg=person_val_msg,
                food_val_msg=food_val_msg,
                person_is_valid=person_is_valid,
                food_is_valid=food_is_valid
            )

        db = get_db()
        db.execute(
            'insert into orders (person, food) values (?, ?)',
            [person, food]
        )
        db.commit()

        return redirect("/")

    return render_template(
        'index.html', entries=entries,
    )


if __name__ == "__main__":
    app.run()
