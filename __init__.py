import snkrsFinal

def initialize(context): 
    """Inicializa e mostra na lista de produtos"""
    context.registerClass(
        snkrsFinal.Sneakers,
        constructors = ( 
            # Chamado quando alguem adiciona o produto     
            snkrsFinal.manage_addSneakers,                                             
        )
    )