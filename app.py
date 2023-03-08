from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/")

db = client.test_database

collection = db.test_collection

@app.route("/")
def index():
    # Fetch a single document from the test_collection
    collection.insert_one({'name':'TD5'})
    data = collection.find_one()
    
    # Return the fetched data as a string
    return str(data)

# Start the Flask application if this file is being executed as the main script
if __name__ == "__main__":
    # Start the Flask application, listening on all available interfaces
    app.run(host="0.0.0.0")