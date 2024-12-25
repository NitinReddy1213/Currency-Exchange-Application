Welcome to Currency Exchange Application powered by Flask,Exchange-Rate-API,mongoDB<br>
<br>
This project is an standalone application which solely focuses on exchanging the currency measure using live exchange rates <br>
which are accesed through an external API provider named Currency_Rate API exchange (https://www.exchangerate-api.com/)<br>
This project solely involves development using HTML,CSS,PYTHON 3.13.1,FLASK(jinja,render), and database client as mongodb.<br>

├── .gitignore              # Specifies files and directories to ignore in Git<br>
├── README.md               # Description of your project<br>
├── app.py                  # Main Python application file<br>
├── dependencies.txt        # List of dependencies for the project<br>
├── static/                 # Directory for CSS and other static files<br>
│   ├── aboutus.css<br>
│   ├── feedbackform.css<br>
│   ├── privacypolicy.css<br>
│   ├── styles.css          # Main CSS file for shared styles<br>
│   ├── termsofuse.css<br>
├── templates/              # Directory for HTML templates<br>
│   ├── aboutus.html<br>
│   ├── feedbackform.html<br>
│   ├── main.html<br>
│   ├── privacypolicy.html<br>
│   ├── termsofuse.html<br>
└── venv/                   # Python virtual environment <br>

<br>

This project mainly contains 3 functionalities 
1)The project can exchange currency depending on the live exchange rates available <br>
2)This project can exchange personally defined currency rates<br>
3)This project can accept feedbacks from customers and store in a mongodb client database.<br>



