import json
with open('config/programas.json', 'r', encoding='utf-8') as file_json:
    dados = json.load(file_json)

listaProgramas = dados["programas"]
programas_para_abrir = []  
 
listaFrames = dados["tituloFrames"]
listaTitulos = []
for item in listaFrames:
    textoLabel = item["frame"]
    listaTitulos.append(textoLabel)
    
