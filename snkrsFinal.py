from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ZSQLMethods.SQL import SQL
from Globals import DTMLFile

class Sneakers(SimpleItem.SimpleItem):
    "Objeto"

    main_css = PageTemplateFile('views/css/main.css', globals())
    header_css = PageTemplateFile('views/css/header.css', globals())
    
    _index_html = PageTemplateFile('views/index.zpt', globals())
    header_html = PageTemplateFile('views/header.zpt', globals())

    meta_type = 'Sneakers'

    def __init__(self, id):
        "inicia a instancia"
        self.id = id

    def index_html(self):
        "responsavel pelo index"
        return self._index_html()
    
def manage_addSneakers(self):
    "adicionar o meu produto em uma pasta"
    self._setObject('sneakers_id', Sneakers('sneakers_id'))
