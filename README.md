# DjangoCom
Curso Django test para apresentacao do Prof August

Primeiro instalar o Pip sendo o Ambiente Virtual Python
  python get-pip.py
  sudo easy_install pip
  sudo pip install virtualenv
Mais informacoes no https://pip.pypa.io/en/stable/installing/

Criando o Ambiente Virtual
  virtualenv <nome do projeto>

Ativando o Ambiente Virutal
  source bin/activate
Comando no Windows
  .\Scripts\activate

Verificando os pacotes instalados
  pip freeze

Comando para instalar o Django no diretorio do seu projeto
  pip install Django

Comandos básicos para o Django

  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver <ip:port>
  python manage.py collectstatic
  
 !! Aviso !!
 Se for tentar acessar o /admin o superuser cadastrado é: 
 Admin padrão:
  django
 Senha:
  admin123
  
