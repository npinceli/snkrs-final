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
        "insere os tenis preenchendo os parametros"
        return self._zsql_insert_snkrs(marca=marca, nome=nome, valor=valor, qtd=qtd, imagem_path=imagem_path)
    
    def search_snkrs(self, card_id):
        "seleciona o item pelo seu id"
        return self._zsql_search_snkrs(card_id=card_id)
    
    def update_snkrs(self, marca, nome, valor, qtd, imagem_path,card_id):
        "atualiza os tenis preenchendo os parametros"
        return self._zsql_update_snkrs(marca=marca, nome=nome, valor=valor, qtd=qtd, imagem_path=imagem_path, card_id=card_id)
    
    def delete_snkrs(self, card_id):
        "deleta o item pelo seu id"
        return self._zsql_delete_snkrs(card_id=card_id)

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

    _zsql_search_snkrs = SQL(
        id='zsql_search', title='', connection_id='connection',
        arguments='card_id', template=open(
            product_path + 'sql/zsql_search.sql').read()
    )
    
    _zsql_update_snkrs = SQL (
        id='zsql_update', title='', connection_id='connection',
        arguments='marca\nnome\nvalor\nqtd\nimagem_path\ncard_id', template=open(
            product_path + 'sql/zsql_update.sql').read()
    )

    _zsql_delete_snkrs = SQL (
        id='zsql_delete', title='', connection_id='connection', 
        arguments='card_id', template=open(
            product_path + 'sql/zsql_delete.sql').read()
    )
    