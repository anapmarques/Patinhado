from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.views.generic.base import View
from .forms import UsuarioCreationForm, PetModelForm
from .models import Pet

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    pets = Pet.objects.filter(adotado=False)[:10]
    return render(request, 'PatinhadoWeb/Home.html', {'pets': pets})

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
    return render(request, 'PatinhadoWeb/pet/AddPet.html')

class PetListView(View):
    def get(self, request):
        from django.core.paginator import Paginator
        pets_list = Pet.objects.all()
        paginator = Paginator(pets_list, 50)
        page_number = request.GET.get('page')
        pets = paginator.get_page(page_number)
        contexto = {'pets': pets}
        return render(request, 'PatinhadoWeb/pet/PetList.html', contexto)

class PetDetailView(View):
    def get(self, request, pk):
        pet = get_object_or_404(Pet, pk=pk)
        contexto = {'pet': pet}
        return render(request, 'PatinhadoWeb/pet/PetDetail.html', contexto)

class PetCreateView(View):
    model = Pet
    template_name = 'PatinhadoWeb/pet/AddPet.html'
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        context = {'form': PetModelForm()}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        formulario = PetModelForm(request.POST, request.FILES)
        if formulario.is_valid():
            pet = formulario.save(commit=False)
            pet.doador = request.user
            print(pet.doador)
            pet.save()
            return redirect('profile')
        else:
            context = {'form': formulario}
            return render(request, self.template_name, context)

class PetUpdateView(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('login')
        pet = get_object_or_404(Pet, pk=pk, doador=request.user)
        formulario = PetModelForm(instance=pet)
        contexto = {'form': formulario, 'pet': pet}
        return render(request, 'PatinhadoWeb/pet/PetEdit.html', contexto)
 
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('login')
        pet = get_object_or_404(Pet, pk=pk, doador=request.user)
        formulario = PetModelForm(request.POST, request.FILES, instance=pet)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalhepet', pk=pk)
        else:
            contexto = {'form': formulario, 'pet': pet}
            return render(request, 'PatinhadoWeb/pet/PetEdit.html', contexto)

class PetDeleteView(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('login')
        pet = get_object_or_404(Pet, pk=pk, doador=request.user)
        contexto = {'pet': pet}
        return render(request, 'PatinhadoWeb/pet/PetDelete.html', contexto)
 
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('login')
        pet = get_object_or_404(Pet, pk=pk, doador=request.user)
        pet.delete()
        return redirect('listapets')

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
