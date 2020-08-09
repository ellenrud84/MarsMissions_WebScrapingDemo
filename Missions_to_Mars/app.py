# import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# instantiate Flask App:
app = Flask(__name__)

# use flask_pymongo to set  up mongo connection:
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# create home route:
@app.route("/")
def home():
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", mars_data=mars_data)

# create scrape route:
@app.route("/scrape")
def scrape():

    # run the scrape funtion
    mars_data=scrape_mars.scrape_info()
    # update the Mongo database using update and upset = true
    mongo.db.collection.update({}, mars_data, upsert= True)
    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)