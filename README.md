

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


