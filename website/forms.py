from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile,Reservation

class MakeReservation(forms.ModelForm):
    name = forms.CharField(label="Nome Completo:",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label="Telefone",max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    alergies = forms.CharField(label="Quais minhas Alergias?",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    obs = forms.CharField(label="Observações:",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Reservation
        fields = ('name','phone_number','gluten','lactose','vegan','vegetarian','kids_menu','alergies','obs')
        labels = {
            'gluten':'É intolerante ao Glúten:',
            'lactose':'É intolerante à Lactose:',
            'vegan':'É Vegano',
            'vegetarian':'É Vegetariano',
            'kids_menu':'Cardápio Infantil (Até 12 anos)-Meia Entrada',
        }
        widgets = {
            'gluten':forms.CheckboxInput( attrs={'class':'form-check-input'}),
            'lactose':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'vegan':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'vegetarian':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'kids_menu':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(label="Nome", max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Sobrenome", max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="",  widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password',)


class SignUpForm(UserCreationForm):
    #email =  forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e-mail Adicional'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sobrenome'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'e-mail de usuário'
        self.fields['username'].widget.attrs['style'] = 'text-transform:lowercase;'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''
        #self.fields['username'].help_text = '<span class="form-text text-muted"><small>Obrigatório</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = ''
        #self.fields['password1'].help_text = ''
        self.fields['password1'].help_text = '<small><ul class="form-text text-muted small"><li>Sua senha não pode ser muito parecida com o resto das suas informações pessoais.</li><li>Sua senha precisa conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser uma senha comumente utilizada.</li><li>Sua senha não pode ser inteiramente numérica.</li></ul></small>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Senha'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Informe a mesma senha informada anteriormente, para verificação.</small></span>'

class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=100,label="Telefone", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'54-99999-9999'}),required=True)
    link = forms.ChoiceField(label="Seu vínculo com a escola:",
                            initial='',widget=forms.Select(attrs={'class':'form-select'}),
                             choices=((1, "Aluno"),
                                        (2, "Parente de Aluno"),
                                        (3, "Professor"),
                                        (4, "Coordenação"),
                                        (5, "Outro")),
                                required=True)
    link_school =forms.CharField(max_length=100,label="Aluno com quem tem associação:", widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)

    class Meta:
        model = UserProfile
        fields = ('phone_number','link','link_school')

