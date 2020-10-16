# coding: utf-8

from typing import List
import datetime


def is_empty(field: str) -> bool:
    if field == None:
        return True
    return (field.count(" ") == len(field))

# ----------------


class Endereco:

    def __init__(self,
                 logradouro: str,
                 numero: int,
                 complemento: str,
                 bairro: str,
                 municipio: str,
                 estado: str,
                 cep: str):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.municipio = municipio
        self.estado = estado
        self.cep = cep

    def dados_endereco(self) -> str:
        self.__validar_campos_obrigatorios()

        if (type(self.numero) is int) and (self.numero > 0):
            numero = str(self.numero)
        elif type(self.numero) is str:
            if not is_empty(self.numero):
                numero = self.numero
            else:
                numero = "s/n"
        else:
            numero = "s/n"

        if not is_empty(self.complemento):
            complemento = f" {self.complemento}"
        else:
            complemento = ""

        endereco = f"{self.logradouro}, {numero}{complemento}\n"

        if not is_empty(self.bairro):
            bairro = f"{self.bairro} - "
        else:
            bairro = ""
        endereco += f"{bairro}{self.municipio} - {self.estado}\n"

        if not is_empty(self.cep):
            endereco += f"CEP:{self.cep}"

        return endereco

    def __validar_campos_obrigatorios(self):
        if is_empty(self.logradouro):
            raise Exception("O campo logradouro do endereço é obrigatório")

        if is_empty(self.municipio):
            raise Exception("O campo município do endereço é obrigatório")

        if is_empty(self.estado):
            raise Exception("O campo estado do endereço é obrigatório")


# ----------------

class Venda(object):
    def __init__(self,
                 loja,  # sdds tipagem
                 data_hora: datetime.datetime,
                 ccf: int,
                 coo: int):
        self.loja = loja
        self.__data_hora = data_hora
        self.__ccf = ccf
        self.__coo = coo

    def __get_data_hora(self) -> datetime.datetime:
        return self.__data_hora
    data_hora: datetime.datetime = property(__get_data_hora)

    def __get_ccf(self) -> int:
        return self.__ccf
    ccf: int = property(__get_ccf)

    def __get_coo(self) -> int:
        return self.__coo
    coo: int = property(__get_coo)

    def __validar_campos_obrigatorios(self):
        self.loja.dados_loja()

        if self.ccf <= 0:
            raise Exception("O Contador de Cupom Fiscal (CCF) é obrigatório.")
        if self.coo <= 0:
            raise Exception("O Contador de Cupom Fiscal (COO) é obrigatório.")

    def dados_venda(self) -> str:
        self.__validar_campos_obrigatorios()

        texto_data = self.data_hora.strftime("%d/%m/%Y")
        texto_hora = self.data_hora.strftime("%H:%M:%S")

        return f"{texto_data} {texto_hora}V CCF:{self.ccf} COO:{self.coo}"

    def imprime_cupom(self) -> str:
        return f"{self.loja.dados_loja()}\n------------------------------\n{self.dados_venda()}"


# ----------------


class Loja:

    def __init__(self,
                 nome_loja: str,
                 endereco: Endereco,
                 telefone: str,
                 observacao: str,
                 cnpj: str,
                 inscricao_estadual: str):

        self.nome_loja = nome_loja
        self.endereco = endereco
        self.telefone = telefone
        self.observacao = observacao
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.__vendas: List[Venda] = []

    def __get_vendas(self) -> List[Venda]:
        return self.__vendas

    vendas: List[Venda] = property(__get_vendas)

    def __validar_campos_obrigatorios(self):
        if is_empty(self.nome_loja):
            raise Exception("O campo nome da loja é obrigatório")
        if is_empty(self.cnpj):
            raise Exception("O campo CNPJ da loja é obrigatório")
        if is_empty(self.inscricao_estadual):
            raise Exception("O campo inscrição estadual da loja é obrigatório")

    def dados_loja(self) -> str:
        # Implemente aqui
        self.__validar_campos_obrigatorios()

        loja = f"{self.nome_loja}\n{self.endereco.dados_endereco()}"

        if not is_empty(self.telefone):
            telefone = f"Tel {self.telefone}"
        else:
            telefone = ""

        tem_cep = not is_empty(self.endereco.cep)
        cep_telefone = ""

        if tem_cep and telefone:
            cep_telefone += " "
        cep_telefone += f"{telefone}\n"

        loja += cep_telefone
        if not is_empty(self.observacao):
            loja += self.observacao
        loja += f"\nCNPJ: {self.cnpj}\nIE: {self.inscricao_estadual}"

        return loja

    def adicionar_venda(self, venda: Venda):
        self.__vendas.append(venda)

    def vender(self, data_hora: datetime.datetime, ccf: int, coo: int):
        # Falta fazer a venda kkk
        pass
