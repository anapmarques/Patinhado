from django.shortcuts import render
from django.views.generic.base import View
from .models import Pet, Usuario

# Create your views here.

def home(request):
    return render(request, 'PatinhadoWeb/Home.html')

def profile(request):
    return render(request, 'PatinhadoWeb/Profile.html')

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
    template_name = 'PatinhadoWeb/templates/PatinhadoWeb/AddPet.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        especie = request.POST.get('especie')
        raca = request.POST.get('raca')
        idade = request.POST.get('idade')
        descricao = request.POST.get('descricao')
        foto_url = request.POST.get('foto_url')
        doador_id = request.POST.get('doador_id')

        doador = None
        if request.user.is_authenticated and isinstance(request.user, Usuario):
            doador = request.user
        elif doador_id:
            doador = Usuario.objects.filter(pk=doador_id).first()

        if not doador:
            return render(request, self.template_name, {
                'error': 'É necessário informar um usuário doador para cadastrar o animal.',
            })

        try:
            idade = int(idade) if idade else None
        except (TypeError, ValueError):
            idade = None

        pet = self.model(
            nome=nome,
            especie=especie,
            raca=raca,
            idade=idade,
            descricao=descricao,
            foto_url=foto_url,
            doador=doador,
        )
        pet.save()

        return render(request, self.template_name, {'success': True})

class PetAdoptView(View):
    model = Pet
    
    def post(self, request, pk, *args, **kwargs):
        if not request.user.is_authenticated or not isinstance(request.user, Usuario):
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
    template_name = 'PatinhadoWeb/templates/PatinhadoWeb/Profile.html'
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not isinstance(request.user, Usuario):
            return render(request, self.template_name, {'error': 'Usuário não autenticado.'})
        
        usuario = request.user
        pets_doacao = usuario.animais_doacao.all()
        pets_adotados = usuario.pets_adotados.all()

        context = {
            'usuario': usuario,
            'pets_doacao': pets_doacao,
            'pets_adotados': pets_adotados,
        }
        return render(request, self.template_name, context)
