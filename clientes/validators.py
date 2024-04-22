import re
from validate_docbr import CPF

def cpf_valido(numero_cpf):
        cpf = CPF()
        return cpf.validate(numero_cpf)

def nome_valido(nome):
        return nome.isalph()

def rg_valido(numero_rg):
        return len(numero_rg) ==9

def celular_valido(numero_celular):
        '''verifica se o celular e valido'''
        modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        resposta = re.findall(modelo, numero_celular)
        return resposta