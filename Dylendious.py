#--------------- FUNÇÕES ESPECIAIS ---------------
import time

def slowprint(texto, atraso=0.02):
  for c in texto:
    print(c,end='',flush=True)
    time.sleep(atraso)

def veryslowprint(texto, atraso=0.5):
  for c in texto:
    print(c,end='',flush=True)
    time.sleep(atraso)

#--------------- ITENS DO TUTORIAL ---------------
chave_chavosa = False

#--------------- INÍCIO DO JOGO ------------------
def inicio():
    print('''
                                Bem-vindo a Dylendious
''')
    slowprint('''
    Você acordou caído em um lugar fechado\n
''')
    resposta_1 = input("   >> ")
    while(resposta_1.upper() != 'LEVANTAR'):
        resposta_1 = input("   >> ")
    else:
        comodo()

def comodo():
        slowprint('''
    É um cômodo é pequeno.
    À sua ESQUERDA há uma escrivaninha velha,
    à DIREITA, uma caixa, e à FRENTE uma porta.\n
''')
        caminho = ['ESQUERDA', 'DIREITA', 'FRENTE']
        decisao_1 = input("   >> ")
        while(decisao_1.upper() not in caminho):
            decisao_1 = input("   >> ")
        else:
            if decisao_1.upper() == caminho[1]:
                caminhoDireita()
            elif decisao_1.upper() == caminho[0]:
                caminhoEsquerda()
            elif decisao_1.upper() == caminho[2]:
                caminhoFrente()

#--------------- CAMINHO DA DIREITA --------------
def caminhoDireita():
        slowprint('''
    Você encontrou uma caixa de madeira simples sem cadeados.
    Do lado de dentro da tampa, você nota um desenho estranho.
    Dentro da caixa está uma pequena chave.\n
''')
        escolha_caixa = ['PEGAR', 'VOLTAR']
        caixa = input("   >> ")
        while(caixa.upper() not in escolha_caixa):
            caixa = input("   >> ")
        else:
            global chave_chavosa
            if caixa.upper() == escolha_caixa[0]:
                chave_chavosa = True
                slowprint('''
   Você pegou uma chave simples\n
''')
                chavosa = input("   >> ")
                while(chavosa.upper() != 'VOLTAR'):
                    chavosa = input("   >> ")
                else:
                    comodo()
            if caixa.upper() == escolha_caixa[1]:
                comodo()
            
#--------------- CAMINHO DA ESQUERDA -------------
def caminhoEsquerda():
    slowprint('''
    Essa escrivaninha parece ter sido muito usada,
    mas não há nada sobre ela além de inscrições talhadas no tampo.
    Talvez alguém tenha feito isso com as próprias unhas.
    Na parte da frente, existe uma gaveta. No meio dela há uma abertura.\n
''')
    escolha_mesa = ['VOLTAR', 'LER', 'ABRIR']
    mesa = input("   >> ")
    while(mesa.upper() not in escolha_mesa):
        mesa = input("   >> ")
    else:
        if mesa.upper() == escolha_mesa[0]:
            comodo()
        elif mesa.upper() == escolha_mesa[1]:
            slowprint('''
    Os arranhões formam números fora de uma sequencia lógica
            14 1 15   3 15 14 6 9 5   14 5 12 5 19\n
''')
            tampo = input("   >> ")
            while(tampo.upper() != 'VOLTAR'):
                tampo = input("   >> ")
            else:
                caminhoEsquerda()
        elif mesa.upper() == escolha_mesa[2]:
            if chave_chavosa == True:
                slowprint('''
    A chave se encaixou muito bem e um baixo ruído
    soa quando a tranca se desfaz.\n
''')
                slowprint('''
    A gaveta está vazia, mas o fundo dela está marcado
    com algo que você espera ser tinta vermelha:
                    18 21 13 15\n
''')
                chavinha = input("   >> ")
                while(chavinha.upper() != 'VOLTAR'):
                    chavinha = input("   >> ")
                else:
                    caminhoEsquerda()
            elif chave_chavosa == False:
                slowprint('''
    Você não pode abrir a gaveta apenas com os dedos\n
''')
            while(mesa.upper() != 'VOLTAR'):
                mesa = input("   >> ")
            else:
                caminhoEsquerda()

#--------------- CAMINHO DA FRENTE ----------------
def caminhoFrente():
    slowprint('''
    A porta não abre. Há uma tranca eletrônica pedindo
    por uma senha de quatro caracteres.\n
''')
    escolha_porta = ['VOLTAR', 'RUMO', 'DERRUBAR']
    porta = input("   >> ")
    while(porta.upper() not in escolha_porta):
        porta = input("   >> ")
    else:
        if porta.upper() == escolha_porta[0]:
            comodo()
        if porta.upper() == escolha_porta[1] or escolha_porta[2]:
            slowprint('''
    A porta se abre com um ranger sinistro, te fazendo perceber que apenas
    uma tranca eletrônica não a salvaria de se abrir com força bruta.

    À sua frente não há nada além de uma floresta densa, você não sabe onde
    está e muito menos se lembra de como chegou aqui.

    Uma sensação estranha se apossa de você, como se o atraísse a olhar
    para trás e, ao mesmo tempo, atiçasse seu instinto de correr para bem longe...\n
''')
            escolha_externa = ['VIRAR', 'OLHAR PARA TRÁS', 'OLHAR PARA TRAS']
            decisao_2 = input("   >> ")
            while(decisao_2.upper() not in escolha_externa):
                decisao_2 = input("   >> ")
            else:
                slowprint('''
    O cômodo estranho em que você acordou não está mais lá. Tudo que resta são
    apenas ruínas que mal sobreviveram a um incêndio. Só então, percebe o cheiro intenso
    de madeira queimada, há fuligem mesmo em suas mãos.

    "O que está acontecendo?"\n
''')
                veryslowprint('''
.
.
.
''')    
                slowprint('''
                            Obrigado por jogar!\n
''')               
                escolha_final = ['S', 'N']
                fim = input("    Deseja jogar outra vez? S/N\n\n     > ")
                while(fim.upper() not in escolha_final):
                    fim = input("    Deseja jogar outra vez? S/N\n\n     > ")
                else:
                    if fim.upper() == escolha_final[0]:
                        inicio()
                    elif fim.upper() == escolha_final[1]:
                        SystemExit
            
if __name__ == "__main__":
    inicio()