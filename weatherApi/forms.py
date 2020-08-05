from django import forms


class Post(forms.Form):
    city = forms.CharField(label="post", max_length=100,
                           widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter city'}))

    period = forms.CharField(label="post", max_length=100,
                           widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Period'}))

