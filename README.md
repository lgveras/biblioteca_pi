# Projeto de biblioteca Web - UNIVESP PJI 1 - Grupo 10
Repositório do app de biblioteca de PJI 01 - Grupo 10. Desenvolvido em Django e Vue.js

## 🚀 Passo-a-passo seguido para iniciar os projetos

Para montar a estrutura inicial da aplicação, foram criados um projeto em Django e Vue.js. Para referência, foram utilizadas as seguintes versões:
- Python 3.10.7
- Node 16.15.0
- Django-4.1.7 ([Link da Documentação](https://docs.djangoproject.com/en/4.1/))
- Vue 3 com framework Nuxt ([Vue Docs](https://vuejs.org/guide/introduction.html) - [Nuxt Docs](https://nuxtjs.org/pt/))

Para criar o projeto Djando (No Windows), foram seguidos os seguintes passos:

1. Instalação do Python. Veja como [aqui](https://docs.djangoproject.com/en/4.1/intro/install/#install-python).
2. Atualização do PIP
> $ python -m pip install --upgrade pip
3. É recomendado criar um ambiente virtual (virtual enviroment, ou venv). Assim, o python e dependências serão instalados no diretório local do projeto, evitando conflito com outras versões. O comando abaixo, executado de dentro do diretório "backend" irá criar um ambiente virtual.
> python -m venv bibVenv 
4. Precisamos ativar o venv. Basta executar o script dentro da pasta bibVenv\Scripts
> $ bibVenv\Scripts\activate
5. Instale agora o Django
> $ python -m pip install Django
6 . Veja a versão do Django com o seguinte comando
> $ python -m django --version
4. Depois, o projeto Django deve ser criado
> django-admin startproject backend
7. Execute o projeto Django criado
> $ python manage.py runserver
8. Acesse a aplicação pelo link http://127.0.0.1:8000/

Para criar o projeto Vue.js (No Windows), foram seguidos os seguintes passos:

1. Instale o Node.js deste [link](https://nodejs.org/en/download)
2. Veja a versão do node com o comando
> $ node --version
3. Do diretório biblioteca_pi, execute o comando para criar um projeto Nuxt. Ele já instala o Vue junto
> npx nuxi@latest init frontend
4. Entre no diretório frontend e instale as dependências do projeto com 
> npm install
5. Execute a aplicação em modo de desenvolvimento com o comando
> npm run dev -- -o
6. A aplicação irá abri automaticamente

Esta é só a criação das estruturas do projeto. Ainda falta averiguar como acoplar o Django com o Vue. Até então eu verifiquei duas formas:

- Fazendo o Vue/Nuxt gerar a página dentro do Django e depois importa-la nos arquivos deste último ((Ver aqui)[https://betterprogramming.pub/vue-django-using-vue-files-and-the-vue-cli-d6dd8c9145eb]);
- Usando o Django apenas para backend, sem nada de HTML e se comunicar com ele por meio de chamadas HTTP a partir do Vue. Nesse caso teriamos dois servidores, um pro backend em Django e outro para o frontend em Vue/Nuxt. ((Ver aqui)[https://auth0.com/blog/building-modern-applications-with-django-and-vuejs/]). Essa foi a forma que mais encontrei na Internet.

## ✒️ Autores

* **Eliana Rosa da Cruz Candido** - *Papel no projeto* - [Meu perfil](https://univesp.br)
* **Geovana Ferreira dos Santos** - *Papel no projeto* - [Meu perfil](https://univesp.br)
* **José Eduardo Santos Londe** - *Papel no projeto* - [Meu perfil](https://univesp.br)
* **Ligia Carla da Silva Costa** - *Papel no projeto* - [Meu perfil](https://univesp.br)
* **Ligia Fernanda da Silva Batista** - *Papel no projeto* - [Meu perfil](https://univesp.br)
* **Luiz Gustavo Diniz de Oliveira Veras** - *Desenvolvimento* - [Meu perfil](https://github.com/lgveras)

---
⌨️ com ❤️ por [Luiz Gustavo Véras](https://github.com/lgveras) 😊
