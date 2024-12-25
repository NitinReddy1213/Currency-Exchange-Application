Welcome to Currency Exchange Application powered by Flask,Exchange-Rate-API,mongoDB

This project is an standalone application which solely focuses on exchanging the currency measure using live exchange rates 
which are accesed through an external API provider named Currency_Rate API exchange (https://www.exchangerate-api.com/)
This project solely involves development using HTML,CSS,PYTHON 3.13.1,FLASK(jinja,render), and database client as mongodb.

├── README.md               # Description of your project
├── app.py                  # Main Python application file
├── dependencies.txt        # List of dependencies for the project
├── static/                 # Directory for CSS and other static files
│   ├── aboutus.css
│   ├── feedbackform.css
│   ├── privacypolicy.css
│   ├── styles.css          # Main CSS file for shared styles
│   ├── termsofuse.css
├── templates/              # Directory for HTML templates
│   ├── aboutus.html
│   ├── feedbackform.html
│   ├── main.html
│   ├── privacypolicy.html
│   ├── termsofuse.html
└── venv/                   # Python virtual environment (add to .gitignore)

This project mainly contains 3 functionalities 
1)The project can exchange currency depending on the live exchange rates available 
2)This project can exchange personally defined currency rates
3)This project can accept feedbacks from customers and store in a mongodb client database.
