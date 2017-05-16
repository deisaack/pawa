from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.core.urlresolvers import reverse
from . models import Application
from mzito.authentication.models import Profile
from django import forms
from django.conf import settings


class PowerApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            "transformer",
            "distance",
            "payment_method",
            'receipt_no',
            'amount'
        ]

# class PowerApplicationForm(forms.ModelForm):
#     class Meta:
#         model = Application
#         fields = [
#             "transformer",
#             "distance",
#             "payment_method",
#             'receipt_no'
#         ]

# class PowerApplicationForm(forms.ModelForm):
#     model = Application
#
#     def __init__(self, *args, **kwargs):
#         model = Application
#         super(Application, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         user = settings.AUTH_USER_MODEL.objects.get(pk=id)
#
#         self.helper.layout = Layout(
#             Field('transformer', label="Your Nearest Transformer", autofocus="", required=True),
#             Field('distance', placeholder="Enter Full Name"),
#             Field('payment_method', placeholder="Enter Password"),
#             Field('receipt_no', placeholder="Re-enter Password"),
#             Submit('sign_up', 'Sign up', css_class="btn-warning"),
#             )


# class PowerApplicationForm(forms.ModelForm):
#     user = forms.CharField(widget=forms.HiddenInput())
#     transformer = forms.CharField(
#         widget=forms.CharField(attrs={'class': 'form-control'}),
#         label="Your Nearest Transformer",
#         required=True)
#     distance = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         label="Approximate distance from Transformer",
#         required=True)
#
#     payment_method = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         label="Convenient payment method",
#         required=True)
#     receipt_no = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         label="Confirm new password",
#         required=True)
#
#     class Meta:
#         model = Application
#         fields = ['user', 'transformer', 'distance', 'payment_method']
#
#     def clean(self):
#         super(PowerApplicationForm, self).clean()
#         transformer = self.cleaned_data.get('transformer')
#         distance = self.cleaned_data.get('distance')
#         payment_method = self.cleaned_data.get('payment_method')
#         user = settings.AUTH_USER_MODEL.objects.get(pk=id)
#
#         return self.cleaned_data