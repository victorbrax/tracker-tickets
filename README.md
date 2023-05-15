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
[![Pandas](https://img.shields.io/badge/Pandas-green.svg)]()
[![Openpyxl](https://img.shields.io/badge/Openpyxl-gray.svg)]()
</div>


<div align="center">
<img width="100%" src="https://raw.githubusercontent.com/victorbrax/tracker-tickets/main/docs/logos/logo-github.png">
</div>
</div>
<p align="center">By <strong>Víctor Gomes</strong></p>

# Greetings! ⚜


_**Tracker Tickets**_ is one of **my early spreadsheet automation projects**, which is why I have a lot of affection for it. [PandaGAMI]() was born from it.

_**TT**_ is a script that compares two spreadsheets, highlights important rows, formats the header, and saves the file. It may seem like a simple task, but it's a real project that **saved me many hours** of using the VLOOKUP function in Excel during a period of my life in my previous job, where I had to assemble this spreadsheet **from downloaded files every day**.
</br>
</br>

## Demo 🖼️

<div align="center">
<img height="400vh" src="https://raw.githubusercontent.com/victorbrax/tracker-tickets/main/docs/images/example.png">
</div>

## Run Project Locally 🏠

Assumes local installation of [Python](https://python.org/downloads) to run the project locally:

* Clone or fork this repository.
* Create a virtual environment. You can do this by using `python -m venv venv` in the terminal.
* Install the necessary libraries. If you use pip to manage your packages, use `pip install -r requirements.txt`.
* Run `python app.py`
* Check the file `Tracker Tickets.xlsx` appearing at the project's root path.

## Technologies Used 🖥️
* [Pandas](https://pandas.pydata.org/)
* [Openpyxl](https://openpyxl.readthedocs.io/en/stable/)
* [Jinja2](https://palletsprojects.com/p/jinja/)

## Considerations 📝
> The first Tracker had a rather rudimentary interface made with Tkinter. Additionally, it didn't format the spreadsheets with colors and didn't delete old columns. Subsequently, the decision was made to remove the visual interface, simplifying the execution process by eliminating the dialog boxes for file selection. This was done to enhance the understanding and usability of the Tracker.

* Obviously, the spreadsheets in the sheetfiles folder are very basic examples since the actual files are private and **cannot be published**.
* You can adapt it for larger datasets, specify the columns you want to exclude, and add more merges.
* You can easily change the colors by modifying the `hexadecimal codes` in the styling calls.

## License 📜

The code in this project is licensed under the MIT License. See [LICENSE](LICENSE) for details.</br>

> Thank you for the prestige. 🐍
