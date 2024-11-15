import re
from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
import nltk
from nltk.tokenize import word_tokenize

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456789'
app.config['MYSQL_DB'] = 'plant_data'

mysql = MySQL(app)
nltk.download('punkt')

# Updated the regex pattern to remove extra whitespace
location_pattern = r'^[A-Za-z\s,]+$'

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("Welcome.html")

@app.route("/tips", methods=["GET", "POST"])
def tips():
    if request.method == "POST":
        location = request.form.get("Location")
        climate = request.form.get("Climate")
        plant_name = request.form.get("Plant_Name")

        # Validate the location format
        if not re.match(location_pattern, location):
            error_message = "Invalid location format. Please use letters, spaces, and commas only."
            return render_template("Welcome.html", error_message=error_message)
        
        try:
            # Establish a MySQL connection using the auth plugin
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                'SELECT Plant_Name, Watering_Remainder, Fertilizing_Remainder, Other_Care_Remainder, Tips FROM plant WHERE Location=%s AND Climate=%s AND Plant_Name=%s',
                (location, climate, plant_name))
            plantdet = cursor.fetchall()
            cursor.close()

            if len(plantdet) > 0:
                tokenized_plantdet = []
                for plant in plantdet:
                    fertilizing_remainder = plant['Fertilizing_Remainder']
                    fertilizing_remainder_token = word_tokenize(fertilizing_remainder)
                    plant['Fertilizing_Remainder'] = fertilizing_remainder_token
                    tokenized_plantdet.append(plant)
                return render_template("tips.html", plantdet=tokenized_plantdet)
            else:
                error_message = "No gardening tips found for the specified input."
                return render_template("Welcome.html", error_message=error_message)
        
        except Exception as e:
            error_message = f"Database error: {str(e)}"
            return render_template("Welcome.html", error_message=error_message)
    
    return render_template("Welcome.html")

if __name__ == "__main__":
     app.run(debug=True)
