# Currency Exchange Application

## Overview
Currency Exchange Application is a Flask-based web application that allows users to convert currencies, view exchange rates, and access additional financial resources like terms of use and privacy policies.

## Features
- Convert currencies with real-time exchange rates
- User-friendly interface
- Feedback form for user inquiries
- Informational pages (About Us, Privacy Policy, Terms of Use)

## Project Structure
```
nitinreddy1213-currency-exchange-application/
├── README.md
├── app.py
├── dependencies.txt
├── static/
│   ├── aboutus.css
│   ├── feedbackform.css
│   ├── privacypolicy.css
│   ├── styles.css
│   └── termsofuse.css
└── templates/
    ├── aboutus.html
    ├── feedbackform.html
    ├── main.html
    ├── privacypolicy.html
    └── termsofuse.html
```

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nitinreddy1213/currency-exchange-application.git
   cd currency-exchange-application
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r dependencies.txt
   ```

4. **Run the Application**
   ```bash
   flask run
   ```

5. **Access the App**
   - Open your browser and go to `http://127.0.0.1:5000`

## Usage
- Convert currencies quickly with an intuitive interface.
- Submit feedback using the feedback form.
- Access important pages such as About Us, Privacy Policy, and Terms of Use.

## Technologies Used
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS

## Contributing
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.


