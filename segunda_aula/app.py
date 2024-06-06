from flask import Flask, request, json

programa = Flask (__name__, template_folder=".")

@programa.route('/valida', methods=['POST','GET'])
def valida():
    txt = request.get_data()
    obj = json.loads(txt)
    documento = obj['documento']
    obj={"status":True}
    if len(documento) != 11:
        obj={"status":False}
    if not documento.isdigit():
        obj={"status":False}
    txt = json.dumps(obj)
    return txt

programa.run(port=5002, use_reloader=True)