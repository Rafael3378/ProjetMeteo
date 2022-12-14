from flask import Flask, render_template
import backend


app = Flask(__name__) #lignes decorateur


@app.route("/")
def dashboard():
    result = backend.selectreleve()
    return render_template("dashboard.html", resultats = result)

if __name__ == "__main__":
    app.run(debug=True) #affiche si il y a une erreur dans le debogage