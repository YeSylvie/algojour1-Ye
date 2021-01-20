from flask import Flask, request
import requests
import blockchaine, crud_file

app = Flask(__name)
my_blockchaine = blockchaine.Blockchaine(3)

@app.route('/afficher', methods=['GET'])
def afficher_blockchaine():
    my_blockchaine.afficher()

@app.route('/afficher/block/<i>', methods=['GET'])
def afficher_one_block(i):
    my_blockchaine.afficher_one_block(i)

@app.route('/afficher/block/', methods=['GET'])
def afficher_last_block():
    my_blockchaine.afficher_last_block()

@app.route('/is_blockchaine_valid/', methods=['GET'])
def is_blockchaine_valid():
    my_blockchaine.is_blockchaine_valid()

@app.route('/add_block/<data>/signature/<signature>', methods=['POST'])
def add_block(data, signature):
    my_blockchaine.add_block(data, "Crée par " + signature)

@app.route('/save_all', methods=['POST'])
def save_all():
    file = crud_file.File()
    file.save(my_blockchaine, my_blockchaine.nbr_zero)

@app.route('/delete', methods=['PUT'])
def delete_blockchaine():
    my_blockchaine.delete_all()

@app.route('/delete/block/<i>', methods=['PUT'])
def delete_one_block(i):
    my_blockchaine.delete_one(i)