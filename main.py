
#!/usr/bin/python3

from flask import Flask, render_template
import platform, os, socket, subprocess


app = Flask(__name__)

mensaje=[]


@app.route("/")

def index():
	return render_template('index.html',mensaje=['System Check',''])


@app.route("/<parametro>")

def mostrar(parametro):
	if parametro=="nombre":
		return render_template('index.html', mensaje=['Nombre del equipo', socket.gethostname()])
	elif parametro=="ip":
                return render_template('index.html', mensaje=['IP Local', socket.gethostbyname(socket.gethostname() + ".local")])
	elif parametro=="reiniciar":
                return render_template('index.html', mensaje=['Reiniciar Sistema', subprocess.run("reboot")])
	else:
		return render_template('index.html', mensaje=['Error', 'Parámetro no válido, haz clic en el menú superior'])




if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8080, debug=True)

