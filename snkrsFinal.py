from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ZSQLMethods.SQL import SQL
from Globals import DTMLFile

class Sneakers(SimpleItem.SimpleItem):
    "configuracao necessaria para inciar o produto"

    # css
    main_css = PageTemplateFile('views/css/main.css', globals())
    header_css = PageTemplateFile('views/css/header.css', globals())
    
    # html
    _index_html = PageTemplateFile('views/index.zpt', globals())
    header_html = PageTemplateFile('views/header.zpt', globals())

    # nome do produto na lista
    meta_type = 'Sneakers'

    def __init__(self, id, connection):
        "inicia a instancia"
        self.id = id
        self.connection = connection

    def get_database_connection(self):
        "responsavel pela conexao"
        return self.connection

    def index_html(self):
        "responsavel pelo index"
        return self._index_html()
    
def manage_addSneakers(self, id, connection, RESPONSE):
    "adicionar o meu produto em uma pasta"
    conn = getattr(self, connection)
    self._setObject(id, Sneakers(id, conn))
    RESPONSE.redirect('index_html')

#  formulario para pedir o ID do produto e a conexao com o banco
manage_addSneakersForm = DTMLFile('views/add_SneakersForm', globals())