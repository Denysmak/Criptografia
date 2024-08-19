def limpar_texto(texto):
  lista_retirar = '0123456789 !¨@#$%^&*()_-+=[]{}|\;:",./?'
  letras_acentuadas = {'á':'a', 'â':'a', 'ã':'a', 'à':'a', 'ä':'a', 'é':'e', 'ê':'e', 'ẽ':'e', 'è':'e', 'ë':'e', 'í':'i','î':'i', 'ĩ':'i', 'ì':'i', 'ï':'i',
'ó':'o','ô':'o','õ':'o','ò':'o','ö':'o', 'ú':'u', 'û':'u', 'ũ':'u', 'ù':'u', 'ü':'u'}
  lista_resultado = [i.lower() for i in texto if lista_retirar.find(i) == -1]
  for i in range(len(lista_resultado)):
    for chave, valor in letras_acentuadas.items():
      if lista_resultado[i] == chave:
        lista_resultado[i] = valor
  str_resultado = "".join(lista_resultado)
  return str_resultado


print(limpar_texto('Era uma vez um país encantado, onde tudo parecia sair de um conto de fadas. As florestas eram densas e cheias de vida, com árvores tão altas que pareciam tocar o céu. Os rios corriam cristalinos, serpenteando por entre montanhas majestosas e vales verdes. Os animais viviam em harmonia, e a natureza reinava suprema. No coração deste país, havia um castelo antigo, construído com pedras brilhantes que refletiam a luz do sol de maneira deslumbrante. Dentro do castelo, habitava um rei justo e bondoso, amado por todos os seus súditos. Ele governava com sabedoria e compaixão, sempre preocupado com o bem-estar de seu povo. Um dia, uma ameaça sombria surgiu nas fronteiras do país. Um exército de criaturas malignas, lideradas por um feiticeiro poderoso, começou a invadir e destruir tudo em seu caminho. O rei, sabendo que precisava proteger seu povo, convocou os melhores guerreiros do reino e preparou-se para a batalha. A luta foi feroz e muitas vidas foram perdidas, mas, no final, a coragem e a determinação do rei e de seus aliados prevaleceram. O feiticeiro foi derrotado e suas criaturas foram banidas para sempre. A paz foi restaurada no país encantado, e o rei foi celebrado como um herói. As cicatrizes da batalha começaram a desaparecer, e a vida voltou ao normal. As pessoas continuaram a viver suas vidas em paz, gratas pela bravura de seu rei e pela harmonia que reinava em seu lar. O castelo voltou a brilhar sob a luz do sol, e as florestas, rios e montanhas continuaram a encantar a todos com sua beleza. E assim, o país encantado prosperou, sempre lembrando das lições de coragem e unidade que haviam aprendido.'))