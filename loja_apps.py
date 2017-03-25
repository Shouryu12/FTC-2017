import re

def login():
    login_txt = str(input("Usuario: "))
    analise = re.search(r'^[a-z][a-zA-Z]*$',login_txt)
    if(analise):
        return True
    else:
        return False
#--------------------------------------------------------------
def cpf():
    cpf_valido = []
    cpf_txt = str(input("CPF: "))
    analise = re.search(r'^\d\d\d\.\d\d\d\.\d\d\d\-\d\d$',cpf_txt)
    if(analise):
        cpf_valido = formar_lista1(cpf_txt)
        cpf_valido += [ver_primeiro_digito(cpf_valido)]
        cpf_valido += [ver_segundo_digito(cpf_valido)]
        if(pegar_finais(cpf_txt) == pegar_finais(cpf_valido)):
            return True
        else:
            return False
    else:
        return False

def formar_lista1(cpf):
    acm1 = 0
    acm2 = 0
    limite = 9
    lista = []
    while(acm1 < limite):
        if(cpf[acm2] != "."):
            lista += [cpf[acm2]]
            acm1 +=1
        acm2 +=1
    return lista

def ver_primeiro_digito(lista):
    acm1 = 0
    acm2 = len(lista)+1
    soma = 0
    while(acm1 < len(lista)):
        soma += int(lista[acm1])*acm2
        acm1 +=1
        acm2 -=1
    resto = soma%11
    if(resto <= 2):
        return str(0)
    else:
        return str(11 - resto)

def ver_segundo_digito(lista):
    acm1 = 0
    acm2 = len(lista)+ 1
    soma = 0
    while(acm1 < 10):
        soma += (int(lista[acm1]) * acm2)
        acm1 +=1
        acm2 -=1
    resto = soma%11
    if(resto <= 2):
        return str(0)
    else:
        return str(11 - resto)

def pegar_finais(cpf):
    acm1 = 0
    acm2 = len(cpf)-2
    limite = 2
    lista = []
    while(acm1 < limite):
        lista += [cpf[acm2]]
        acm1 +=1
        acm2 +=1
    return lista
#--------------------------------------------------------------
def email():
    email_txt = str(input("E-mail: "))
    analise = re.search(r'^[\w]+@[^0-9\W_]+\.[^0-9\W_]+$',email_txt)
    if(analise):
        return True
    else:
        return False
#--------------------------------------------------------------
#def senha():
#--------------------------------------------------------------
def nome_app():
    nome_txt = str(input("Nome do app: "))
    analise = re.search(r'^[A-Za-z]$',nome_txt)
    if(analise):
        return True
    else:
        return False
#--------------------------------------------------------------
def versao_app():
    versao_txt = str(input("Versao do app: "))
    analise = re.search(r'^[0-9]+.[0-9]+$',versao_txt)
    if(analise):
        if(analisar_versao(versao_txt)):
            return True
        else:
            return False
    else:
        return False

def analisar_versao(versao):
    lista = separar_versao(versao)
    if(int(lista[0]) >= int(lista[1])):
        return True
    else:
        return False
        
def separar_versao(versao):
    acm1 = 0
    acm2 = 0
    lista = ["",""]
    while(acm1 < len(versao)):
        if(versao[acm1] != "."):
            lista[acm2] += str(versao[acm1])
        else:
            acm2+=1
        acm1+=1
    return lista
#--------------------------------------------------------------
def plataforma():
    plataforma_txt = str(input("Plataforma: "))
    analise = re.search(r'^\w+$',plataforma_txt)
    if(analise):
        if(plataforma_valida(plataforma_txt)):
            return True
        else:
            return False
    else:
        return False

def plataforma_valida(plataforma):
    teste = plataforma.lower() 
    if(teste == "windows" or teste == "mac"):
        return True
    elif(teste == "linux" or teste == "ios"):
        return True
    elif(teste == "android" or teste == "windowsphone"):
        return True
    else:
        return False
#--------------------------------------------------------------
#def presente():
#--------------------------------------------------------------
    
#print(login())
#print(cpf())
#print(email())
#print(senha())
#print(nome_app())
#print(versao_app())
#print(plataforma())
