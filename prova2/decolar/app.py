from flask import Flask, json, render_template, request, redirect, jsonify
import sqlite3
import requests

app = Flask(__name__, template_folder='.')

@app.route('/listar', methods=['GET', 'POST'])
def listar ():
	if request.method == 'POST':
		data = request.values.get('data')
		 
		txt = json.dumps({"data":data}) 
		conexaoGol = requests.post(url="http://localhost:8081/servico.php",data=txt)
		txt = conexaoGol.content
		print(txt)
		listaGol = json.loads(txt)
		
		txt = json.dumps({"data":data}) 
		reqLatam = requests.post(url="http://localhost:8082/servico.php",data=txt)
		txt = reqLatam.content
		
		listaLatam = json.loads(txt)

		print(listaLatam)
		return render_template('listar.html',listaGol=listaGol,listaLatam=listaLatam)
	else:
		return render_template('listar.html')

@app.route('/comprar', methods=['GET'])
def comprar ():
	id = request.values.get('id')
	voo = request.values.get('voo')
	return render_template('comprar.html',vooid=id, voonome=voo)

@app.route('/confirmar', methods=['GET', 'POST'])
def confirmar ():
	if request.method == 'POST':
		cpf   = request.values.get('cpf')
		nome   = request.values.get('nome')
		id   = request.values.get('id')
		voo   = request.values.get('voo')
		print(cpf,nome,id,voo)

	
		if voo.find('Gol')>=0:
			urlTxt = "http://localhost:8081/servico_compra.php"
		else:
			urlTxt = "http://localhost:8082/servico_compra.php"
		txt = json.dumps({"id":id,"cpf":cpf,"nome":nome}) 
		resp = requests.post(url=urlTxt,data=txt)
		txt = resp.content
		print(txt)
		resultado = json.loads(txt)
		return render_template('confirmar.html',resultado=resultado)
	return render_template('confirmar.html')

@app.route('/', methods=['GET', 'POST'])
def index():
	return redirect('/listar')


	
app.run(port=5001, use_reloader=True)
