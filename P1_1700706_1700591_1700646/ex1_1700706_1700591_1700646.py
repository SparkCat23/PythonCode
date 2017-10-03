# Gustavo Zaik - 1700591
# Luka Gabriel - 1700709
# Jhonatan Rafael - 1700646

def contagem(texto):
    con = 0
    dicPalavra = {}
    lTexto = texto.split(' ')
    lPalavras = []
    for x in lTexto:
        if x not in lPalavras:
            lPalavras.append(x)
    lPalavras.sort()
    for x in range(0,len(lPalavras)):
        con = lTexto.count(lPalavras[x])
        dicPalavra[lPalavras[x]] = con
    
    return dicPalavra
