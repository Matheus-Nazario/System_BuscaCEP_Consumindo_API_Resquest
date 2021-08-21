# -------------------------------------------------------------
# Consumindo mascara utilizando a API
# -------------------------------------------------------------
from acesso_cep import BuscaEndereco

cep = input("Didigite o CEP do seu endereço: ")
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
