from flask import Flask, render_template, request
import requests
from pymongo import Mongoclient

app = Flask(__name__)

client = Mongoclient("") #put your client srv url in this space
app.db = client.microblog

my_list = []
custom_list = []

@app.route("/", methods=["GET", "POST"])
def main():
    from_amount = None
    to_amount = None
    amount = None

    if request.method == "POST":
        amount = request.form.get("amount")
        from_amount = request.form.get("currency")
        to_amount = request.form.get("currencyto")
        amountpart = request.form.get("amount_2")
        value = request.form.get("Currency_value")

        total_value = float(value) * float(amountpart)
        custom_list.append(total_value)


    if from_amount and amount and to_amount:
        # Convert amount to float
        amount = float(amount)

        # Fetch the conversion rate
        url = f"{from_amount}"    #insert your Api-key here between f and {from_amount}
        response = requests.get(url)
        data = response.json()
        
        # Get conversion rate and calculate result
        conversion_rate = data["conversion_rates"][to_amount]
        result = conversion_rate * amount
        my_list.append(result)

    
    return render_template("main.html", my_list=my_list,custom_list = custom_list)

@app.route("/fancy")

def privacypolicy():

    return render_template("privacypolicy.html")

@app.route("/dongle") 

def termofuse():

    return render_template("termsofuse.html")

@app.route("/aboutus")

def aboutus():

    return render_template("aboutus.html")

@app.route("/feedbackform", methods = ["GET","POST"])

def feedbackform():

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        Rating = request.form.get("rating")
        comments = request.form.get("comments")
        app.db.entries.insert_one({"name": name , "email" : email, "Rating": Rating, "comments" : comments})  # this dictionary will insert the date into mongodb
        



    return render_template("feedbackform.html")