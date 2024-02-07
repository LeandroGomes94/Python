
nome = []
n1 = []
n2 = []
media = []
resultado = []

def calculaMedia(n1, n2):

    media = (n1 + n2 )/ 2
    return media

def verificaStatus(media):

    if media < 5:
        return "Reprovado"
    else:
        return "Aprovado"
        
