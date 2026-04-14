from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import View
from .forms import UsuarioCreationForm, PetModelForm
from .models import Pet, Usuario

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'PatinhadoWeb/Home.html')

def login(request):
    return render(request, 'PatinhadoWeb/auth/Login.html')

def registro(request):
    if request.method == 'POST':
        formulario = UsuarioCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('profile')
        contexto = {'form': formulario}
    else:
        formulario = UsuarioCreationForm()
        contexto = {'form': formulario}
    return render(request, 'PatinhadoWeb/auth/Register.html', contexto)

def profile(request):
    return render(request, 'PatinhadoWeb/Profile.html')

def addpet(request):
    return render(request, 'PatinhadoWeb\pet\AddPet.html')

class PetListView(View):
    model = Pet
    template_name = 'PatinhadoWeb/templates/PatinhadoWeb/PetList.html'
    context_object_name = 'pets'
    
    def get(self, request, *args, **kwargs):
        pets = self.model.objects.filter(adotado=False).order_by('data_chegada')
        context = {self.context_object_name: pets}
        return render(request, self.template_name, context)

class PetDetailView(View):
    model = Pet
    template_name = 'PatinhadoWeb/templates/PatinhadoWeb/Pet.html'
    context_object_name = 'pet'
    
    def get(self, request, pk, *args, **kwargs):
        pet = self.model.objects.get(pk=pk)
        context = {self.context_object_name: pet}
        return render(request, self.template_name, context)

class PetAddView(View):
    model = Pet
    template_name = 'PatinhadoWeb/pet/AddPet.html'
    
    def get(self, request, *args, **kwargs):
        context = {'form': PetModelForm()}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        formulario = PetModelForm(request.POST)
        if formulario.is_valid():
            pet = formulario.save(commit=False)
            pet.doador = request.user
            print(pet.doador)
            pet.save()
            return redirect('profile')
        else:
            context = {'form': formulario}
            return render(request, 'PatinhadoWeb/addPet.html', context)

class PetAdoptView(View):
    model = Pet
    
    def post(self, request, pk, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'PatinhadoWeb/templates/PatinhadoWeb/Pet.html', {
                'error': 'Usuário não autenticado.',
                'pet': self.model.objects.get(pk=pk),
            })
        
        pet = self.model.objects.get(pk=pk)
        pet.marcar_adotado(request.user)

        return render(request, 'PatinhadoWeb/templates/PatinhadoWeb/Pet.html', {
            'pet': pet,
            'success': 'Pet adotado com sucesso!',
        })

class ProfileView(View):
    template_name = 'PatinhadoWeb/Profile.html'
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        
        usuario = request.user
        pets_doacao = usuario.animais_doacao.all()
        pets_adotados = usuario.pets_adotados.all()

        context = {
            'usuario': usuario,
            'pets_doacao': pets_doacao,
            'pets_adotados': pets_adotados,
        }
        return render(request, self.template_name, context)
