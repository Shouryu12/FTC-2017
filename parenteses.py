def validar_remocao(pilha,lista):
    if pilha == '{' and lista == '}':
        return True
    elif pilha == '(' and lista == ')':
        return True
    elif pilha == '[' and lista == ']':
        return True
    return False

def remover_espacos(lista):
    i = 0
    while(i < len(lista)):
        if(lista[i] == " "):
            lista = lista.replace(lista[i],"")
        i += 1
    return lista

def analisar(lista):
    pilha = []
    cont = 0
    for i in range(len(lista)):
        if(lista[i] == '{' or lista[i] == '(' or lista[i] == '['):
            pilha.append(lista[i])
            cont += 1
        elif(lista[i] == '}' or lista[i] == ')' or lista[i] == ']'):
            elemento = pilha.pop()
            if(validar_remocao(elemento,lista[i]) != True):
                return False
        else:
            return False
    if len(lista) == 2*cont:
        return True
    return False

try:
    txt = str(input())
    n_txt = remover_espacos(txt)
    if(analisar(n_txt) == True):
        print("True")
    else:
        print("False")
except:
    print("False")