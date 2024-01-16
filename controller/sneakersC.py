from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ZSQLMethods.SQL import SQL
from Products.sneakers.model.sneakersM import SneakersM

class SneakersC(SimpleItem.SimpleItem):
    "responsavel pela interacao entre model e view"

    # css
    insert_css = PageTemplateFile('zpt/css/cadastrar.css', globals())

    # html
    list_html = PageTemplateFile('zpt/list.zpt', globals())
    insert_html = PageTemplateFile('zpt/insert.zpt', globals())

    meta_type = 'Testando'

    model_ = SneakersM()

    def listarMethod(self):
        "chama o metodo"
        return self.model_.list_snkrs()

    def listar(self):
        "chama a lista"
        return self.list_html()

    def inserirForm(self):
        "mostrar o form de insert"
        return self.insert_html()

    def inserir(self, marca, nome, valor, qtd, imagem_path):
        "chama o metodo e retorna pro index"
        self.model_.insert_snkrs(marca=marca, nome=nome, valor=valor, qtd=qtd, imagem_path=imagem_path)
        self.REQUEST.RESPONSE.redirect('index_html')
