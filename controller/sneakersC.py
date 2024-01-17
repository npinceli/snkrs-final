from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ZSQLMethods.SQL import SQL
from Products.sneakers.model.sneakersM import SneakersM

class SneakersC(SimpleItem.SimpleItem):
    "responsavel pela interacao entre model e view"

    # css
    insert_css = PageTemplateFile('zpt/css/cadastrar.css', globals())
    update_css = PageTemplateFile('zpt/css/update.css', globals())

    # html
    list_html = PageTemplateFile('zpt/list.zpt', globals())
    insert_html = PageTemplateFile('zpt/insert.zpt', globals())
    update_html = PageTemplateFile('zpt/update.zpt', globals())

    meta_type = 'Testando'

    model_ = SneakersM()

    def listarMethod(self):
        "chama o metodo"
        return self.model_.list_snkrs()

    def listar(self):
        "chama a lista"
        return self.list_html()

    def inserirForm(self):
        "mostra o form de insert"
        return self.insert_html()

    def inserir(self, marca, nome, valor, qtd, imagem_path):
        "chama o metodo e retorna pro index"
        self.model_.insert_snkrs(marca=marca, nome=nome, valor=valor, qtd=qtd, imagem_path=imagem_path)
        self.REQUEST.RESPONSE.redirect('index_html')

    def procurar(self, card_id):
        "chama o metodo"
        return self.model_.search_snkrs(card_id=card_id)    

    def updateForm(self):
        "mostra o form de update"
        return self.update_html()
    
    def update(self, marca, nome, valor, qtd, imagem_path, card_id):
        "chama o metodo e retorna pro index"
        self.model_.update_snkrs(marca=marca, nome=nome, valor=valor, qtd=qtd, imagem_path=imagem_path, card_id=card_id)
        self.REQUEST.RESPONSE.redirect('index_html')

    def deletar(self, card_id):
        "chama o metodo e retorna pro index" 
        self.model_.delete_snkrs(card_id=card_id)
        self.REQUEST.RESPONSE.redirect('index_html')