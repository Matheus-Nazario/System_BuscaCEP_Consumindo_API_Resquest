import requests


class BuscaEndereco:
    # iniciando o CEP realizamos a validação
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_Valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    # __STR__ impressão da função
    def __str__(self):
        return self.format_cep()

    # regras da validação cep
    def cep_eh_Valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    # formato do CPD Fatiando
    def format_cep(self):
        num_cep = "{}-{}".format(self.cep[:5], self.cep[5:])
        rua = self.buscar_endereco()["logradouro"]
        bairro = self.buscar_endereco()["bairro"]
        localidade = self.buscar_endereco()["localidade"]
        uf = self.buscar_endereco()["uf"]
        impressao = "CEP: {}\nRua: {}\nBairro: {}\nCidade: {}\nUF: {}".format(
            num_cep, rua, bairro, localidade, uf
        )
        return impressao

    # Acessando a API pelo site via CEP - liberada para todos site brasileiros
    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        return r

    # com a API em mão realizamos a busca do endereço completo
    # em formato de dicionario
    def buscar_endereco(self):
        acesso_API = self.acessa_via_cep()
        dicionario_endereco = acesso_API.json()
        return dicionario_endereco


"""
r = requests.get("https://viacep.com.br/ws/08255100/json/")
print(r.text)
"""
