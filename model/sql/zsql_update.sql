UPDATE sneakers
SET
  marca = <dtml-sqlvar marca type="string">,
  nome = <dtml-sqlvar nome type="string">,
  valor = <dtml-sqlvar valor type="float">,
  qtd = <dtml-sqlvar qtd type="int">,
  imagem_path = <dtml-sqlvar imagem_path type="string">
WHERE
  id = <dtml-var card_id>;