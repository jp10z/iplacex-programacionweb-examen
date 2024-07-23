"""Fichero principal del proyecto flask.
"""

from flask import Flask, render_template, request, session
from credentials import CREDENTIALS

app = Flask(__name__)
app.config["SECRET_KEY"] = "MYSECRETKEY"

@app.route("/", methods=["GET"])
def inicio() -> str:
    """Retorna el render de la página de inicio.

    Returns:
        str: Página renderizada.
    """
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET"])
def ejercicio_1() -> str:
    """Retorna el render de la página del ejercicio 1.

    Returns:
        str: Página renderizada.
    """
    return render_template("ejercicio1.html", formulario=["", "", ""])

@app.route("/ejercicio1", methods=["POST"])
def ejercicio_1_post() -> str:
    """Retorna el render de la página del ejercicio 1.
    Ejecuta las acciones al enviar el formulario.

    Returns:
        str: Página renderizada.
    """
    formulario = ["", "", ""]
    try:
        form = request.form
        nombre = form["nombre"]
        edad = form["edad"]
        cantidad = form["cantidad"]
        formulario = [nombre, edad, cantidad]
        nombre = nombre.strip()
        edad = int(edad)
        cantidad = int(cantidad)
        # variable respuesta
        respuesta = []
        respuesta.append(f"Nombre del cliente: ${nombre}")
        # calcular total sin descuento
        total_sin_descuento = cantidad * 9000
        respuesta.append(f"Total sin descuento: ${total_sin_descuento}")
        # calcular descuento
        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0
        respuesta.append(f"El descuento es: ${descuento}")
        # calcular total
        total = total_sin_descuento - descuento
        respuesta.append(f"El total a pagar es de: ${total}")
    except Exception as ex:
        respuesta = ["Error al procesar el formulario"]
    return render_template("ejercicio1.html", formulario=formulario, respuesta=respuesta)

@app.route("/ejercicio2", methods=["GET"])
def ejercicio_2() -> str:
    """Retorna el render de la página del ejercicio 2.

    Returns:
        str: Página renderizada.
    """
    return render_template("ejercicio2.html")

@app.route("/ejercicio2", methods=["POST"])
def ejercicio2_login() -> str:
    """Realiza login y muestra página del ejercicio 2.

    Returns:
        str: Página renderizada.
    """
    form = request.form
    nombre = form["nombre"].strip()
    contrasenia = form["contrasenia"].strip()
    # validate nombre
    if nombre not in CREDENTIALS:
        return render_template("ejercicio2.html", respuesta="Usuario o contraseña incorrectos")
    # validate password
    if CREDENTIALS[nombre]["password"] != contrasenia:
        return render_template("ejercicio2.html", respuesta="Usuario o contraseña incorrectos")
    # agregar a sesion y retornar
    session["nombre"] = nombre
    grupo = CREDENTIALS[nombre]["group"]
    return render_template("ejercicio2.html", respuesta=f"Bienvenido {grupo} {nombre}")

if __name__ == '__main__':
    app.run(debug=True)