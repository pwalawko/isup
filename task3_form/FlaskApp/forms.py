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


def length(min_le=None, max_le=None):

    def _length(form, field):
        le = (field.data and len(field.data)) or 0
        if min_le is not None and le < min_le:
            raise ValidationError(
                f'Co tak skromnie? Wpisz więcej niż \
                {min_le} {CHARACTERS[plural_form(min_le)]}.'
            )
        elif max_le is not None and le > max_le:
            raise ValidationError(
                f'Nie przesadzasz z tą ilością? Wpisz mniej niż \
                {max_le} {CHARACTERS[plural_form(max_le)]}.'
            )

    return _length


class OrderForm(Form):
    person = StringField('Zamawiający', [
        validators.InputRequired(req_field_msg),
        length(min_le=3, max_le=64)
    ])
    food = StringField('Zamówienie', [
        validators.InputRequired(req_field_msg),
        length(max_le=256)
    ])
