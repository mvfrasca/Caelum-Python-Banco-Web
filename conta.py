class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def titular(self):
        return self._titular.capitalize()

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def deposita(self, valor):
        self._saldo -= valor

    def saca(self, valor):
        self._saldo -= valor

    def transfere_para(self, destino, valor):
        self.saca(valor)
        destino.deposita(valor)

    def __str__(self):
        return 'Conta: [numero: {}, titular: {}, saldo: {}, limite: {}]'.format(self._numero, self._titular, self._saldo, self._limite)

