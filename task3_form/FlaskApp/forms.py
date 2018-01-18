from wtforms import Form, StringField, validators, ValidationError


req_field_msg = "To pole jest wymagane."


def length(min=0, max=0):
    message = 'Pole musi mieć od %d do %d znaków.' % (min, max)

    def _length(form, field):
        l = field.data and len(field.data) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)

    return _length


class OrderForm(Form):
    person = StringField('Zamawiający', [
        validators.InputRequired(req_field_msg),
        length(min=3, max=50)
    ])
    food = StringField('Zamówienie', [
        validators.InputRequired(req_field_msg),
        length(max=50)
    ])
