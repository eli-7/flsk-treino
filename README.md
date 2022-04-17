# flsk-treino
Treino Flask e set de ambiente virtual
--------------------------------------------------------------------------------
Vídeos assistidos: 
https://youtu.be/WWVEymSt1iI - Como Criar API com Python - Crie a Sua Própria
API no Python
https://www.youtube.com/watch?v=Z1RJmh_OqeA - Learn Flask for Python - Full
Tutorial
-----------------------------------------------------------------------------

PASSOS:

1.1. No GITHUB, criei um repositório (flsk-treino)
1.2. No windows explorer, cliquei com o botão direito do mouse e selecionar o
     Git Bash Here
1.2.1. Digite: git init
1.2.2. Digite: git clone <url copiada>
1.3. Criei um ambiente virtual (dentro do diretório clonado)
     Digite: python -m venv ./<nome-virtual>
1.4 Ativei o ambiente virtual (dentro do diretório clonado)
    Digite: .\<nome-virtual>\Scripts\activate
    Obs1.: Scripts tem que ser em letra maiúscula
    Obs2.: Se conseguiu ativar, aparecerar na linha do prompt do lado esquerdo
           entre parênteses o nome do ambiente virtual
1.5. Enqto ativado o ambiente virtual, instalar as bibliotecas do python neces-
    sárias para o desenvolvimento nesse ambiente
    Digite: pip install Flask
    Digite: pip install pandas
    Digite: pip install requests

--------------------
IDE utilizada: ATOM
Lembrando que tive que ir no \File\Settings\+ Install dar um search em Packages
e procurar:
1) atom-python-run
2) atom-python-virtualenv
Para 1) rodar o Python dentro do Atom para não ter que abrir um terminal (cmd)
e rodar de lá. Assim, consigo rodar dentro do Atom (Opção Packages\Scripts)
2) Antes de rodar, escolher em Packages\Virtualenv o ambiente virtual
Obs.: Para consultar pacotes instalados dar browse: file:///C:/Users/lilic/.atom/packages/
--------------------
