from flask import Flask, render_template, request, redirect, url_for
from conta import Conta
import csv

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World com Flask'

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/lista')
def lista():

    arquivo = open('contas.txt', 'r')
    leitor = csv.reader(arquivo)

    contas = []
    for linha in leitor:
        conta = Conta(linha[0], linha[1], linha[2], linha[3])
        contas.append(conta)
    arquivo.close()

    return render_template('lista.html', contas=contas)

@app.route('/cria_conta', methods=['POST'])
def cria_conta():

    dados = request.form.to_dict(flat=True)
    numero = dados['numero']
    titular = dados['titular']
    saldo = float(dados['saldo'])
    limite = float(dados['limite'])

    conta = Conta(numero, titular, saldo, limite)

    arquivo = open('contas.txt', 'a')
    arquivo.write(f'{conta.numero},{conta.titular},{conta.saldo},{conta.limite}\n')
    arquivo.close()

    #return lista()
    return redirect(url_for('lista'))
    
if __name__ == '__main__':
    app.run()