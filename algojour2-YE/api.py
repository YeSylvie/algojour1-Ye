import flask
from flask import Flask, request, jsonify
import blockchaine
import crud_file

app = Flask(__name__)
my_blockchaine = blockchaine.Blockchaine(3)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/afficher', methods=['GET'])
def afficher_blockchaine():
    return my_blockchaine.afficher()


@app.route('/afficher/block/<i>', methods=['GET'])
def afficher_one_block(i):
    return my_blockchaine.afficher_one_block(int(i))


@app.route('/afficher/block', methods=['GET'])
def afficher_last_block():
    return my_blockchaine.afficher_last_block()


@app.route('/is_blockchaine_valid', methods=['GET'])
def is_blockchaine_valid():
    return str(my_blockchaine.is_blockchaine_valid())


@app.route('/add_block/<data>/signature/<signature>', methods=['POST'])
def add_block(data, signature):
    my_blockchaine.add_block(data, "Crée par " + signature)
    return flask.Response(status=200)


@app.route('/replace_blockchaine', methods=['POST'])
def replace_blockchaine():
    datas_json = request.get_json()
    taille = datas_json['taille']
    taille = int(taille)
    new_blockchaine = blockchaine.Blockchaine(4)
    new_blockchaine.blockchaines = []
    i = 0
    while i < taille:
        data = datas_json['block'][i]['data']
        signature = datas_json['block'][i]['signature']
        new_blockchaine.add_block(data, "Crée par " + signature)
        i += 1
    my_blockchaine.replace_blockchaine(new_blockchaine)
    return flask.Response(status=200)


@app.route('/save_all', methods=['POST'])
def save_all():
    file = crud_file.File()
    file.save(my_blockchaine, my_blockchaine.nbr_zero)
    return flask.Response(status=200)


@app.route('/delete', methods=['PUT'])
def delete_blockchaine():
    my_blockchaine.delete_all()
    return flask.Response(status=200)


@app.route('/delete/block/<i>', methods=['PUT'])
def delete_one_block(i):
    my_blockchaine.delete_one(int(i))
    return flask.Response(status=200)