from django import forms


class TemplateForm(forms.Form):
    select year = forms.ChoiceField(choices=(
        "year",
        "2018",
        "2017",
        "2016"
    ))
    body style = forms.ChoiceField(choices=(
        "style",
        "sedan",
        "van",
        "roadster"
    ))
    select make = forms.ChoiceField(choices=(
        "make",
        "toyota",
        "holden",
        "maecedes-benz."
    ))
    car condition = forms.ChoiceField(choices=(
    "condition",
    "condition",
    "condition",
    "condition"
    ))
    select model = forms.ChoiceField(choices=(
    "model",
    "kia - rio",
    "mitsubishi",
    "ford"
    ))
    select price = forms.ChoiceField(choices=(
    "price",
    "$20000.00",
    "$150000.00",
    "$300000.00"
    ))