from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Pet


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class PetModelForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'nome',
            'especie',
            'raca',
            'idade',
            'descricao',
            'foto_url',
        ]
 
    nome = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nome do pet',
        })
    )
 
    especie = forms.ChoiceField(
        label='Espécie',
        choices=Pet.Especie.choices,
        widget=forms.Select()
    )
 
    raca = forms.CharField(
        label='Raça',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex: Labrador, Siamês...',
        })
    )
 
    idade = forms.IntegerField(
        label='Idade (em anos)',
        required=False,
        min_value=0,
        help_text='Idade em anos',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Ex: 3',
        })
    )
 
    descricao = forms.CharField(
        label='Descrição',
        required=False,
        help_text='Conte um pouco sobre o pet',
        widget=forms.Textarea(attrs={
            'placeholder': 'Descreva o temperamento, histórico, necessidades especiais...',
            'rows': 4,
        })
    )
 
    foto_url = forms.URLField(
        label='URL da Foto',
        required=False,
        help_text='Insira o link de uma foto do pet',
        widget=forms.URLInput(attrs={
            'placeholder': 'https://exemplo.com/foto.jpg',
        })
    )