from wtforms import Form, StringField, validators, ValidationError


CHARACTERS = ('znak', 'znaki', 'znaków')
req_field_msg = "Nie zapominaj o tym polu."


def plural_form(n):
    if n == 1:
        plural = 0
    else:
        if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            plural = 1
        else:
            plural = 2

    return plural


def length(min=-1, max=-1):
    max_char_written = CHARACTERS[plural_form(max)]
    min_char_written = CHARACTERS[plural_form(min)]
    message_max = f'Nie przesadzasz z tą ilością? \
        Wpisz mniej niż {max} {max_char_written}.'
    message_min = f'Co tak skromnie? \
        Wpisz więcej niż {min} {min_char_written}.'

    def _length(form, field):
        le = (field.data and len(field.data)) or 0
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
