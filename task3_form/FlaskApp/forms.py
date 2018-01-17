from wtforms import Form, StringField, validators


class OrderForm(Form):
    person = StringField('Zamawiający:', [
        validators.Length(
            min=3, max=64, message="Długość musi być między %(min)d a %(max)d."
        )
    ])
    food = StringField('Zamówienie:', [
        validators.Required("To pole jest wymagane."),
        validators.Length(
            max=256, message="Długość musi mieć maksymalnie %(max)d."
        )
    ])
