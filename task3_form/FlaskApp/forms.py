from wtforms import Form, StringField, validators, ValidationError


req_field_msg = "Nie zapominaj o tym polu."


def length(min=-1, max=-1):
    message_max = 'Nie przesadzasz z tą ilością? Wpisz mniej znaków niż %d.' % max
    message_min = 'Co tak skromnie? Wpisz więcej znaków niż %d.' % min

    def _length(form, field):
        le = field.data and len(field.data) or 0
        if le < min:
            raise ValidationError(message_min)
        elif max != -1 and le > max:
            raise ValidationError(message_max)

    return _length


class OrderForm(Form):
    person = StringField('Zamawiający', [
        validators.InputRequired(req_field_msg),
        length(min=3, max=64)
    ])
    food = StringField('Zamówienie', [
        validators.InputRequired(req_field_msg),
        length(max=256)
    ])
