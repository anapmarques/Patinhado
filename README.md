# Patinhado

Plataforma web para adoção de pets, desenvolvida em Django.

## Funcionalidades

### Para Usuários

- **Cadastro e Autenticação**: Sistema completo de registro de usuarios com login e logout
- **Gerenciamento de Perfil**: Edicao e exclusao de perfil do usuario com foto, telefone e endereco
- **Listagem de Pets**: Visualizacao de animais disponiveis para adoção na pagina inicial
- **Detalhes de Pet**: Visualizacao completa das informacoes de cada animal

### Para Doadores

- **Cadastro de Pet**: Adicionar novos animais para doacao com foto, nome, especie, raca, idade e descricao
- **Edicao de Pet**: Atualizar informacoes dos animais cadastrados
- **Exclusao de Pet**: Remover animais do sistema
- **Gerenciamento de Pedidos**: Aprovar ou rejeitar pedidos de adoção recebidos

### Para Adotantes

- **Solicitacao de Adoção**: Enviar pedido de adoção para um animal
- **Edicao de Pedido**: Modificar mensagem do pedido (enquanto pendente)
- **Cancelamento de Pedido**: Cancelar pedido pendente
- **Acompanhamento**: Ver status dos pedidos enviados

### Recursos Adicionais

- **Painel do Usuario**: Visualizacao centralizada de pets doados, pets adotados e pedidos
- **Validacoes de Negocio**: Garante queanimais adotados tenham adotante definido
- **Paginação**: Lista de pets com paginacao para melhor desempenho
- **Upload de Imagens**: Suporte a upload de fotos de pets e usuarios

## Workflow

O sistema de adoção funciona em três etapas:

1. **Doação**: Um usuário cadastra um pet para adoção
2. **Solicitação**: Outro usuário Interested envía um pedido de adoção
3. **Aprovação**: O doador aprova ou rejeita o pedido

### Páginas Principais

| Página | Descrição |
|--------|-----------|
| **Home** (`/`) | Lista pets disponíveis para adoção com paginação |
| **Lista de Pets** (`/pets/`) | Visualização completa de todos os pets |
| **Detalhes do Pet** (`/pets/<id>/`) | Informações completas do animal com opción de adoção |
| **Adotar Pet** (`/pets/<id>/adotar/`) | Formulário para solicitar adoção |
| **Painel do Usuário** (`/profile/`) | Central do usuário: pets doados, adotados e pedidos |
| **Cadastrar Pet** (`/pets/add/`) | Formulário para adicionar novo pet |
| **Editar Pet** (`/pets/<id>/editar/`) | Atualizar dados do pet |
| **Editar Perfil** (`/profile/editar/`) | Atualizar dados pessoais |
| **Meus Pedidos** (`/profile/`) | Lista de pedidos enviados/recebidos |
| **Sobre** (`/aboutus/`) | Informações sobre o projeto |
| **Contato** (`/contact/`) | Formulário de contato |

## Tecnologias Utilizadas

- **Backend**: Django 6.0.3
- **Banco de Dados**: SQLite (desenvolvimento)
- **Imagens**: Pillow 12.2.0
- **Autenticacao**: Django Auth com argon2-cffi
- **Frontend**: HTML5, CSS3
- **Containerizacao**: Docker e Docker Compose (imagem Alpine leve)

## Como Usar

### Pré-requisitos

- Python 3.10+
- Docker Desktop (opcional)

### Instalação Local (sem Docker)

1. Clone o repositorio:
   ```bash
   git clone <url-do-repositorio>
   cd Patinhado
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env`
   - Ajuste as configurações necessárias

5. Execute as migrações:
   ```bash
   cd Patinhado
   python manage.py migrate
   ```

6. Crie um superusuário (opcional):
   ```bash
   python manage.py createsuperuser
   ```

7. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

8. Acesse no navegador:
   - http://127.0.0.1:8000

### Instalação com Docker

1. Execute o container:
   ```bash
   docker run -d -p 8000:8000 --name patinhado doctortangerina/patinhado:latest
   ```

2. Acesse no navegador:
   - http://localhost:8000

Ou com Docker Compose:
```bash
docker-compose up -d
```

Nota: O arquivo `docker-compose.yml` está configurado para utilizar a imagem `doctortangerina/patinhado:latest` do Docker Hub. Para utilizar a tag latest explicitamente, use `doctortangerina/patinhado:latest`.

### Estrutura do Projeto

```
Patinhado/
├── Patinhado/          # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── PatinhadoWeb/      # Aplicação principal
    ├── models.py     # Modelos de banco de dados
    ├── views.py     # Lógicas de visualização
    ├── forms.py     # Formulários
    ├── urls.py      # Rotas da aplicação
    ├── templates/   # Templates HTML
    └── static/     # Arquivos estáticos (CSS, JS, imagens)
```

## Desenvolvedores

- **Ana Luiza**
- **Arthur Sardella**

## Licença

MIT License

---

## Disclaimer

Este trabalho foi desenvolvido com auxílio de inteligência artificial.

- **Modelo de IA**: Big Pickle (opencode/big-pickle)
- **Ferramenta**: OpenCode
- **Frontend/Backend**: Desenvolvidos com assistência de IA
- **Logo**: Gerado pelo ChatGPT 5.3