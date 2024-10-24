from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/search", methods=['GET','POST'])
def getIngredients():
    if request.method == 'POST':
        ingredients =request.form['ingredients']
        apiKey = '6001cdeb6c3e4a9a89749d93aad0f20e'
        url = f"https://api.spoonacular.com/recipes/complexSearch"
        params = {
            "apiKey": apiKey,
            "includeIngredients": ingredients,
            "type": "grocery",
            "number": 10,
            "ranking": 1,
            "addRecipeInformation": True
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            recipes = response.json()
            return render_template("recipes.html", recipes=recipes)
        else:
            return ("Error: " + str(response.status_code))


if __name__ == "__main__":
    app.run(debug=True)
