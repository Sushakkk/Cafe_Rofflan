from django import forms
import re

class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
            ],
        )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
            ],
        )

    def clean_phone(self):
        data = self.cleaned_data['phone']

        # if not data.isdigit():
        #     raise forms.ValidationError("Номер телефона не соответствует формату")
        pattern = re.compile(r'^\+7 \(\d{3}\)-\d{3}-\d{4}$')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера. Формат: +7 (000)-000-0000")

        return data