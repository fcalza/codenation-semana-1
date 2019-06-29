print("dae pessoal")


def soma(op1, op2):
    resultado = op1 + op2
    return resultado


def subtrair(op1 = 0, op2 = 0):
    resultado = op1 - op2
    return resultado


def compara_valor(*args):
    for operador in args:
        if operador == "teste" or  operador == 40:
            print("teste ou 40")
        else:
            print("outracoisa")


def somatorio(*args):
    resultadoSomatoria = 0 
    for operador in args:
        compara_valor(operador)
        resultadoSomatoria += operador
    return resultadoSomatoria


def qual_tipo(*args):
    for tipo in args:
        print(type(tipo))


def boas_vindas(pessoa=None):
    if pessoa.get("sexo") == "fem" and pessoa.get("idade") >= 18:
        print("AAAAAAAAAAAAAAAAAAa")
    elif pessoa.get("nome") == "Dono" or pessoa.get("idade") >= 18:
        print("pode entrar")

    if pessoa.get("nome") == "Bruna" and pessoa.get("idade") == 20 and pessoa.get("rg") == 1:
        print("pessoa pode ficar a noite toda")




#soma
a = 10
b = 3
resultadoSoma = soma(a,b)
print("resultado soma é: ", resultadoSoma)

#subtrair
resultadoSub = subtrair(40, 20)
print("resultado sub é: ", resultadoSub)
# print(f'resultado sub é: {resultadoSub}')
print("resultado sub é: {}".format(resultadoSub))

#somatorio
resultadoSomatorio = somatorio(11, 2, 40, 90)
print("resultado soma é: ", resultadoSomatorio)

#somatorio
resultSomatorio2 = (1, 34, 2)
resultadoSomatorio2 = somatorio(*resultSomatorio2)
print("resultado soma é: ", resultadoSomatorio2)

#tipos
tipo_string = "texto de caracteres"
tipo_int = 222223
tipo_tuple = ("a", "b")
tipo_dict = {"chave": "valor"}
tipo_dict2 = dict(chave="valor")
print(tipo_tuple)
print(tipo_dict)
print(tipo_dict2)
qual_tipo(tipo_dict, tipo_dict2, tipo_int, tipo_tuple, True, None, somatorio)

#pessoa - boas_vindas
pessoa = {
    "nome":"Bruna",
    "idade": 10,
    "sexo": "fem",
}
print(pessoa)
boas_vindas(pessoa)
boas_vindas({"nome":"Dono"})
pessoa2 = {
    "nome":"Bruna",
    "idade": 20,
    "sexo": "fem",
    "rg": True,
}
boas_vindas(pessoa2)




class Cachorro:
    def __init__(self, nome):
        self._nome = nome


    def latir(self):
        if self._nome == "ipa":
            print("au")
        elif self._nome == "bob":
            print("roaf")
        else:
            print("olá")


    def _se_limpar(self):
        print("quem se limpou foi o:", self._nome)


    def rolar(self):
        print(self._nome, "rolou")
        self._se_limpar()
        

    @property
    def nome_cachorro(self):
        return self._nome


    @nome_cachorro.setter
    def set_nome_cachorro(self, nome):
        self._nome = nome


#Classes - invocar classes
ipa = Cachorro("ipa")
ipa.latir()
bob = Cachorro("bob")
bob.latir()
dog = Cachorro("dog")
dog.latir()
dog.rolar()


#**KWARGS
def print_pessoa(**kwargs):
    #kwargs = dict
    for key in kwargs:
        print("chave", key, "| valor:", kwargs[key])


print_pessoa(nome="nomeTeste", idade=22, rg=True)

pessoa2 = {
    "nome":"Bruna",
    "idade": 20,
    "sexo": "fem",
    "rg": True,
}
print_pessoa(**pessoa2)



import unittest

class TestSoma(unittest.TestCase):

    def test_soma_numeros(self):
        somado = soma(1, 2)
        self.assertEquals(3, somado)

    
    def test_subtrair(self):
        subtrai = subtrair(28, 2)
        self.assertEqual(26, subtrai)


unittest.main()


