from django import forms
from authentication.models import Card, EpicLink, List, User

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'description', 'delivery_date', 'priority', 'epic_link', 'list', 'user']

    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Insira o titulo....'}))
    description = forms.CharField(max_length=800, required=True, widget=forms.TextInput(attrs={'class': '.div-input-desc', 'placeholder': 'Insira a descrição....', }))
    delivery_date = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'teste', 'style': "background-color: #FFD6B1"}),
    )
    priority = forms.ChoiceField(
        choices=[('', 'Prioridade')] + list(Card.PRIORITY_CHOICES),
        widget=forms.Select(attrs={'style': "background-color: #ffb1b3; color: #9d2527"}),
        required=True,
    )
    epic_link = forms.ModelChoiceField(
        queryset=EpicLink.objects.all(),
        required=True,
        widget=forms.Select(attrs={'style': "background-color: #ffb1ff; color: #9d257d"}),
        empty_label="Epic Link"
    )
    list = forms.ModelChoiceField(queryset=List.objects.all())
    user = forms.ModelChoiceField(queryset=User.objects.all())

    def clean_epic_link(self):
        epic_link = self.cleaned_data.get('epic_link')
        if epic_link and Card.objects.filter(epic_link=epic_link).exists():
            raise forms.ValidationError("This epic link is already registered.")
        return epic_link
