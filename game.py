from tkinter import *
from random import randint

#variaveis
pontos = 100
vitoriageral = 0
vitorias = list()
vezes = list()


#função/jogo
def botao_comando(num):
    global pontos, vitorias, vezes, vitoriageral
    computador = randint(1, 3)
    texto_vitoria = 'Parabéns, você acertou!'
    texto_derrota = f'Eu pensei no {computador} e não no {num}!'
    if num == computador:
        pontos += 50
        vezes.append(1)
        vitorias.append(1)
        resultado2['text'] = len(vezes)
        if len(vezes) == 3:
            if len(vitorias) >= 2:
                vitoriageral += 1
                placar_vitorias['text'] = vitoriageral
                vezes.clear()
                vitorias.clear()
            else:
                vezes.clear()
                vitorias.clear()
        resultado1['text'] = texto_vitoria
        pontos_geral['text'] = pontos
    elif num != computador:
        vezes.append(1)
        pontos -= 5
        resultado2['text'] = len(vezes)
        if len(vezes) == 3:
            if len(vitorias) >= 2:
                vitoriageral += 1
                placar_vitorias['text'] = vitoriageral
                vezes.clear()
                vitorias.clear()
            else:
                vezes.clear()
                vitorias.clear()
        resultado1['text'] = texto_derrota
        pontos_geral['text'] = pontos


#criação da janela
master = Tk()
master.title("Jogo da adivinhação versão 1.1")
master.iconbitmap(default="icone.ico")
master.geometry("704x404+305+143")
master.wm_resizable(width=False, height=False)


#importação da imagem de fundo
jogo_imagem = PhotoImage(file="jogo 2.png")

#Label
labelJogo = Label(master, image=jogo_imagem)
labelJogo.place(x=0, y=0)


#função para mapeamento da aréa
def clique_mouse(retorno):
    print(f'X: {retorno.x} | Y:{retorno.y} Geo: {master.geometry()}')


#Imagens nos botões
im_botao1 = PhotoImage(file="botão1.png")
im_botao2 = PhotoImage(file="botão2.png")
im_botao3 = PhotoImage(file="botão3.png")

#Botões
botao1 = Button(master, image=im_botao1, relief='flat', command=lambda: botao_comando(1))
botao2 = Button(master, image=im_botao2, relief='flat', command=lambda: botao_comando(2))
botao3 = Button(master, image=im_botao3, relief='flat', command=lambda: botao_comando(3))

#Localização dos botões
botao1.place(width=50, height=50, x=260, y=96)
botao2.place(width=50, height=50, x=329, y=96)
botao3.place(width=50, height=50, x=399, y=96)

#Informações que aparecem na tela
placar_vitorias = Label(master, text='0', relief='flat', fg='#ffffff', bg='#240a41')
placar_vitorias.place(width=25, height=25, x=85, y=112)

pontos_geral = Label(master, text='100', relief='flat', fg='#ffffff', bg='#240a41')
pontos_geral.place(width=25, height=25, x=594, y=112)

resultado1 = Label(master, text=">>><<<", relief='flat', fg='#ffffff', bg='#240a41')
resultado1.grid(row=1, column=0, padx=(280), pady=(173))

resultado2 = Label(master, text='0', relief='flat', fg='#ffffff', bg='#240a41')
resultado2 .place(width=20, height=20, x=518, y=175)

#eventos - mapear area do pc
#master.bind("<Button-1>", clique_mouse)

master.mainloop()

