from OFS import SimpleItem
from Products.ZSQLMethods.SQL import SQL

from Globals import package_home
import os
global product_path
product_path = os.path.join(package_home(globals())) + '/'

class SneakersM(SimpleItem.SimpleItem):
    "responsavel pelos dados e logica do site"

    meta_type = "Model"
    
    def list_snkrs(self):
        "metodo pra listar todos os tenis"
        return self._zsql_list_snkrs()

    def insert_snkrs(self, marca, nome, valor, qtd, imagem_path):
        "inserir os tenis preenchendo os parametros"
        return self._zsql_insert_snkrs(marca=marca, nome=nome, valor=valor, qtd=qtd, imagem_path=imagem_path)

    _zsql_list_snkrs = SQL(
        id='zsql_list', title='', connection_id='connection',
        arguments='', template=open(
            product_path + 'sql/zsql_list.sql').read()
        )

    _zsql_insert_snkrs = SQL(
        id='zsql_insert', title='', connection_id='connection',
        arguments='marca\nnome\nvalor\nqtd\nimagem_path', template=open(
            product_path + 'sql/zsql_insert.sql').read()
    )