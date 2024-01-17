from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ZSQLMethods.SQL import SQL
from Products.sneakers.model.sneakersM import SneakersM

class SneakersC(SimpleItem.SimpleItem):
    "responsavel pela interacao entre model e view"

    # css
    insert_css = PageTemplateFile('zpt/css/cadastrar.css', globals())
    update_css = PageTemplateFile('zpt/css/update.css', globals())
    details_css = PageTemplateFile('zpt/css/details.css', globals())

    # html
    list_html = PageTemplateFile('zpt/list.zpt', globals())
    insert_html = PageTemplateFile('zpt/insert.zpt', globals())
    update_html = PageTemplateFile('zpt/update.zpt', globals())
    details_html = PageTemplateFile('zpt/details.zpt', globals())

    meta_type = 'Controller'

    # instanciando a classe da model
    model_ = SneakersM()

    def listarMethod(self):
        "chama o metodo da model"
        return self.model_.list_snkrs()

    def listar(self):
        "chama a instancia da pagina de listar os tenis"
        return self.list_html()

    def inserirForm(self):
        "chama a instancia do form de inserir os tenis"
        return self.insert_html()

    def inserir(self, marca, nome, valor, qtd, imagem_path):
        "chama o metodo e retorna pro index"
        self.model_.insert_snkrs(marca=marca, nome=nome, valor=valor, qtd=qtd, imagem_path=imagem_path)
        self.REQUEST.RESPONSE.redirect('index_html')

    def procurar(self, card_id):
        "chama o metodo da model que procura o tenis pelo id"
        return self.model_.search_snkrs(card_id=card_id)    

    def updateForm(self):
        "chama a instancia do form de atualizar os tenis"
        return self.update_html()
    
    def update(self, marca, nome, valor, qtd, imagem_path, card_id):
        "chama o metodo e retorna pro index"
        self.model_.update_snkrs(marca=marca, nome=nome, valor=valor, qtd=qtd, imagem_path=imagem_path, card_id=card_id)
        self.REQUEST.RESPONSE.redirect('index_html')

    def deletar(self, card_id):
        "chama o metodo e retorna pro index" 
        self.model_.delete_snkrs(card_id=card_id)
        self.REQUEST.RESPONSE.redirect('index_html')

    def details(self):
        "chama a pagina details"
        return self.details_html()