from wtforms import Form, StringField, validators, ValidationError


req_field_msg = "To pole jest wymagane."


def length(min=-1, max=-1):
    if min == -1 and max != -1:
        message = 'Pole musi mieć maksymalnie %d znaków.' % max
    elif min != -1 and max == -1:
        message = 'Pole musi mieć co najmniej %d znaków.' % min
    else:
        message = 'Pole musi mieć od %d do %d znaków.' % (min, max)

    def _length(form, field):
        le = field.data and len(field.data) or 0
        if le < min or max != -1 and le > max:
            raise ValidationError(message)

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
