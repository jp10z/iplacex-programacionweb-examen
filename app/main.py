"""Fichero principal del proyecto flask.
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def inicio() -> str:
    """Retorna el render de la página de inicio.

    Returns:
        str: Página renderizada.
    """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)