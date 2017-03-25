import re

def login(login_txt):
    analise = re.search(r'^[a-z][a-zA-Z]*$',login_txt)
    if(analise):
        return True
    else:
        return False
#--------------------------------------------------------------
def cpf(cpf_txt):
    cpf_valido = []
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
def email(email_txt):
    analise = re.search(r'^[\w]+@[^0-9\W_]+\.[^0-9\W_]+$',email_txt)
    if(analise):
        return True
    else:
        return False
#--------------------------------------------------------------
def senha(senha_txt):
    analise = re.search(r'^\w\w\.\w\w\.\w\w\.\w\w$',senha_txt)
    if(analise):
        senha_separada = separar_senha(senha_txt)
        if(validar_senha(senha_separada)):
            return True
        else:
            return False
    else:
        return False

def separar_senha(senha):
    lista = [[],[],[],[]]
    acm1 = 0
    for i in range(len(senha)):
        if(senha[i] != "."):
            lista[acm1].append(senha[i]);
        else:
            acm1 += 1
    return lista

def validar_senha(senha):
    cont = 0
    for i in range(len(senha)):
        if(checar_numeros(senha[i])or checar_letras(senha[i])):
            cont +=0
        else:
            cont +=1
            
    if(cont == 0):
        return True
    else:
        return False

def checar_numeros(senha):
    primeiro = re.search(r'^[0-9]$',senha[0])
    segundo1 = re.search(r'^[0-9]$',senha[1])
    segundo2 = re.search(r'^[a-zA-Z]$',senha[1])
    if(primeiro):
        if(segundo1):
           if(int(senha[0]) != int(senha[1])):
               return True
           else:
               return False
        elif(segundo2):
           return True
    else:
        return False

def checar_letras(senha):
    primeiro = re.search(r'^[a-zA-Z]$',senha[0])
    segundo1 = re.search(r'^[a-zA-Z]$',senha[1])
    segundo2 = re.search(r'^[0-9]$',senha[1])
    if(primeiro):
        if(segundo1):
            return False
        elif(segundo2):
           return True
    else:
        return False
        
#--------------------------------------------------------------
def nome_app(nome_txt):
    analise = re.search(r'^[A-Za-z]+$',nome_txt)
    if(analise):
        return True
    else:
        return False
#--------------------------------------------------------------
def versao_app(versao_txt):
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
def plataforma(plataforma_txt):
    analise = re.search(r'^\w+$',plataforma_txt)
    if(analise):
        if(plataforma_valida(plataforma_txt)):
            return True
        else:
            return False
    else:
        return False

def plataforma_valida(plataforma):
    analise = plataforma.lower() 
    if(analise == "windows" or analise == "mac"):
        return True
    elif(analise == "linux" or analise == "ios"):
        return True
    elif(analise == "android" or analise == "windowsphone"):
        return True
    else:
        return False
#--------------------------------------------------------------
#def presente(string):
#--------------------------------------------------------------
def separar_input(txt):
    analise = re.split(r'\s',txt)
    return analise

def sistema(string):
    cont = 0
    for i in range(len(string)):
        recebe_info = mandar_informacao(i,string[i])
        if(recebe_info == True):
            cont += 1
        else:
            break
    if(cont == len(string)):
        return True
    
def mandar_informacao(i,string):
    if(i == 0):
        return login(string)
    if(i == 1):
        return cpf(string)
    if(i == 2):
        return email(string)
    if(i == 3):
        return senha(string)
    if(i == 4):
        return nome_app(string)
    if(i == 5):
        return versao_app(string)
    if(i == 6):
        return plataforma(string)
    if(i > 6):
        return presente(string)

txt = str(input("Informe a entrada: "))
string = separar_input(txt)
print(sistema(string))
