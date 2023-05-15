<div align="center">
  <table>
  <tr>
    <td><img height="24rem" src="https://raw.githubusercontent.com/victorbrax/filebrax-hub/c65a8072294d7b044a5909e03bcb0e7a7dcf6e3c/docs/br.svg" alt="brazilflag"></td>
    <td>Você fala Português? Por favor, <a href="https://github.com/victorbrax/filebrax-hub/blob/main/docs/LEIAME.md">clique aqui</a>.</td>
  </tr>
</table>
</div>




<div align="center">
  
[![Project](https://img.shields.io/badge/REAL_PROJECT-important.svg)]()
[![Python](https://img.shields.io/badge/Python-informational.svg)]()
[![Jinja2](https://img.shields.io/badge/Jinja2-green.svg)]()
[![Flask](https://img.shields.io/badge/Flask-gray.svg)]()
[![Bootstrap](https://img.shields.io/badge/Bootstrap-red.svg)]()
[![Blueprints](https://img.shields.io/badge/Blueprints-blue.svg)]()
[![Javascript](https://img.shields.io/badge/Javascript-yellow.svg)]()
</div>


<div align="center">
<img width="100%" src="https://raw.githubusercontent.com/victorbrax/tracker-tickets/main/docs/logos/logo-github.png">
</div>
</div>
<p align="center">By <strong>Víctor Gomes</strong></p>

# Greetings! ⚜

The Filebrax Hub (which doesn't share any similarity with my nickname) is a fully functional project for handling file uploads and downloads on a server. It has been developed using Flask as its Micro Framework, with the goal of providing an efficient internal environment. Moreover, thanks to its well-structured architecture using Blueprints, it allows for easy integration of additional backend modules (e. g., [Tracker Tickets](https://github.com/victorbrax/TrackerG), a tracking and management application that I plan to release soon).
</br>
</br>


## Demo 🖼️

Soon, I will make available the main pages of the application in a non-functional way using the GitHub Pages feature for non-experienced programming users.
</br>

<div align="center">
<img height="220vh" src="https://github.com/victorbrax/filebrax-hub/blob/main/docs/gifs/navigation.gif?raw=true">
<img height="220vh" src="https://github.com/victorbrax/filebrax-hub/blob/main/docs/gifs/validacao.gif?raw=true">
</div>
<div align="center">
<img height="220vh" src="https://github.com/victorbrax/filebrax-hub/blob/main/docs/gifs/collapse.gif?raw=true">
<img height="220vh" src="https://github.com/victorbrax/filebrax-hub/blob/main/docs/gifs/404.gif?raw=true">
</div>

## Run Project Locally 🏠

Assumes local installation of [Python](https://python.org/downloads) to run the project locally:

* Clone or fork this repository.
* Create a virtual environment. You can do this by using `python -m venv venv` in the terminal.
* Install the necessary libraries. If you use pip to manage your packages, use `pip install -r requirements.txt`.
* Run `python app.py`
* By default, the application will run on the following address: `127.0.0.1:8000`, with the debug mode enabled.

## Technologies Used 🖥️
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* [Bootstrap](http://getbootstrap.com)
* [Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
* [Jinja2](https://palletsprojects.com/p/jinja/)
* [JavaScript](https://js.org)


## Considerations 📝

* The system doesn't have an authentication module, but I believe that due to the modular architecture of Blueprints, it wouldn't be difficult to implement. If you feel comfortable, you can send me a pull request for the project.
* There is a deliberate project called "_FORCE404_"; you can try accessing it to test if the Flask error handler redirection is working correctly.
* The Uploads environment has validation for "port users" with JavaScript, Jinja2 and Flash Messages.

### Warning ⚠️
If the user tries to upload a project that already exists in the directory, the existing project **will be replaced** by the new one and a message will be displayed.

## License 📜

The code in this project is licensed under the MIT License. See [LICENSE](LICENSE) for details.</br>
Note: My intention is simply to help people who are also studying web development with Python. :)

> Thank you for the prestige. 🐍

















# 🛠️ TrackerG 2.2! 🚧

Atenção, esse projeto está sendo adaptado para publicação!
Desenvolvido em Python, utilizando as bibliotecas Pandas e Tkinter como motores principais.

O objetivo final é gerar um executável e compartilhar entre os membros da organização com o fim de aumentar a produtividade e eliminar a perca de tempo na produção dessa planilha diária e mandatória.

# Estrutura

• *tracker.pyw:* código de origem<br>
• *tracker.ipynb:* código organizado para fuglemans :)

O código usa a biblioteca Pandas como principal motor para aplicar o merge das fórmulas e dropar algumas colunas que não são utilizáveis, parte da estilização também é feita por ela (com excessão do Header, que é feito pela biblioteca do Openpyxl).

As janelas de diálogo são fornecidas via biblioteca TKinter e notificações pela win10toast.

Alguns trechos também usam a biblioteca do sistema operacional para apagar as planilhas antigas e não sobrecarregar pastas com lixo. 
Como as importações de algumas bibliotecas podem exigir alguns segundos de carregamento, o Pynput redireciona para o Desktop quando o programa inicia.

O programa utiliza a extensão *.pyw* para não requisitar console, não é recomendável utilizar o parâmetro ```--noconsole``` do pyinstaller com o programa em *.py* pois ele compromete o desempenho do código.

Também é recomendável usar um ambiente virtual para gerar as distribuições executáveis.

# Modo de uso

O uso do programa é bem simples e intuitivo, ele é composto por três janelas de seleção de arquivos, sendo elas:

1. Arquivo 1 (.xlsx) - Planilha fornecida pela Ninecon
2. Arquivo 2 (.csv) - Planilha extraída do Sistema WHD da Sencinet
3. Caminho de destino - Local onde será salvo a planilha final

## Testes iniciais
~~Você pode usar as source-sheets de apoio que estão no repositório para fazer os testes iniciais.~~ ```confidential file :(``` <br>
Um .gif dele funcionando será adicionado em breve.


Antes da execução do programa, <strong>é necessário renomear a extensão</strong> do <strong>WHD_Tickets.tsv</strong> para <strong>.csv</strong>, esse procedimento será automatizado também na versão 2.3 do Tracker.

Vale ressaltar que a versão dos arquivos é importante, portanto para um Tracker feito da forma correta, é necessário o download do arquivo 1 e 2 no mesmo dia, por exemplo, um *Tracker Ninecon 16082022.xlsx* precisa de um *WHD_Tickets.tsv* extraído no dia 16/08/2022 para ser perfeitamente compatível.

# História
<cite>O primeiro Tracker havia uma interface horripilante e com 3 botões no lugar das janelas de diálogo que abrem diretamente, ele também não formatava a planilha com cores, não apagava arquivos velhos e nem dropava o lixo excessivo, além disso também não salvava as Sheets de backup no arquivo final.</cite>


