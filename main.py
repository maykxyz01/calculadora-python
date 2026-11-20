from tkinter import *
from tkinter import ttk

import re 

def porcentagem():
    global expressao
    m = re.search(r"[\d.,]+$", expressao)
    if m:
        num = float(m.group().replace(",", ".")) / 100
        expressao = expressao[:m.start()] + str(num).replace(".", ",")
        app_label.config(text=expressao)

def inverter_sinal():
    global expressao
    m = re.search(r"[\d.,]+$", expressao)
    if m:
        expressao = expressao[:m.start()] + "(-" + m.group() + ")"
        app_label.config(text=expressao)

# cores

cor1 = "#1e1f1e" #preta
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul
cor4 = "#D3D3D3" #cinza
cor5 = "#FFAB40" #laranja


janela = Tk()
janela.title("Calculadora")
janela.geometry("260x318")
janela.config(bg=cor1)

#criando frames

frame_tela = Frame(janela, width=260, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=260, height=268)
frame_corpo.grid(row=1, column=0)

#criando label

app_label = Label(frame_tela, width=19, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Arial", 14, "bold"), bg=cor3, fg=cor4)
app_label.place(x=0, y=0)

expressao = ""

def entrar_valor(valor):
    global expressao
    expressao += str(valor)
    app_label.config(text=expressao)

def limpar():
    global expressao
    expressao = ""
    app_label.config(text="")

def apagar():
    global expressao
    expressao = expressao[:-1]
    app_label.config(text=expressao)

def calcular():
    global expressao
    try:
        conta = expressao.replace("÷", "/").replace("×", "*").replace(",", ".")
        resultado = str(eval(conta))
        expressao = resultado
        app_label.config(text=resultado)
    except Exception:
        expressao = ""
        app_label.config(text="Erro")

#criando botoes

col_w = 260 // 4
row_h = 268 // 5

estilo = dict(
    font=("Arial", 14, "bold"),
    relief=FLAT,
    bd=0,
    fg="white",
    activeforeground="white",
)

b_1 = Button(frame_corpo, text="⌫", command=apagar, bg=cor4, activebackground=cor4, **estilo)
b_1.place(x=0 * col_w, y=0, width=col_w, height=row_h)

b_2 = Button(frame_corpo, text="C", command=limpar, bg=cor4, activebackground=cor4, **estilo)
b_2.place(x=1 * col_w, y=0, width=col_w, height=row_h)

b_3 = Button(frame_corpo, text="%", command=porcentagem, bg=cor4, activebackground=cor4, **estilo)
b_3.place(x=2 * col_w, y=0, width=col_w, height=row_h)

b_4 = Button(frame_corpo, text="÷", command=lambda: entrar_valor("÷"), bg=cor5, activebackground=cor5, **estilo)
b_4.place(x=3 * col_w, y=0, width=col_w, height=row_h)

b_5 = Button(frame_corpo, text="7", command=lambda: entrar_valor("7"), bg=cor4, activebackground=cor4, **estilo)
b_5.place(x=0 * col_w, y=1 * row_h, width=col_w, height=row_h)

b_6 = Button(frame_corpo, text="8", command=lambda: entrar_valor("8"), bg=cor4, activebackground=cor4, **estilo)
b_6.place(x=1 * col_w, y=1 * row_h, width=col_w, height=row_h)

b_7 = Button(frame_corpo, text="9", command=lambda: entrar_valor("9"), bg=cor4, activebackground=cor4, **estilo)
b_7.place(x=2 * col_w, y=1 * row_h, width=col_w, height=row_h)

b_8 = Button(frame_corpo, text="×", command=lambda: entrar_valor("×"), bg=cor5, activebackground=cor5, **estilo)
b_8.place(x=3 * col_w, y=1 * row_h, width=col_w, height=row_h)

b_9 = Button(frame_corpo, text="4", command=lambda: entrar_valor("4"), bg=cor4, activebackground=cor4, **estilo)
b_9.place(x=0 * col_w, y=2 * row_h, width=col_w, height=row_h)

b_10 = Button(frame_corpo, text="5", command=lambda: entrar_valor("5"), bg=cor4, activebackground=cor4, **estilo)
b_10.place(x=1 * col_w, y=2 * row_h, width=col_w, height=row_h)

b_11 = Button(frame_corpo, text="6", command=lambda: entrar_valor("6"), bg=cor4, activebackground=cor4, **estilo)
b_11.place(x=2 * col_w, y=2 * row_h, width=col_w, height=row_h)

b_12 = Button(frame_corpo, text="-", command=lambda: entrar_valor("-"), bg=cor5, activebackground=cor5, **estilo)
b_12.place(x=3 * col_w, y=2 * row_h, width=col_w, height=row_h)

b_13 = Button(frame_corpo, text="1", command=lambda: entrar_valor("1"), bg=cor4, activebackground=cor4, **estilo)
b_13.place(x=0 * col_w, y=3 * row_h, width=col_w, height=row_h)

b_14 = Button(frame_corpo, text="2", command=lambda: entrar_valor("2"), bg=cor4, activebackground=cor4, **estilo)
b_14.place(x=1 * col_w, y=3 * row_h, width=col_w, height=row_h)

b_15 = Button(frame_corpo, text="3", command=lambda: entrar_valor("3"), bg=cor4, activebackground=cor4, **estilo)
b_15.place(x=2 * col_w, y=3 * row_h, width=col_w, height=row_h)

b_16 = Button(frame_corpo, text="+", command=lambda: entrar_valor("+"), bg=cor5, activebackground=cor5, **estilo)
b_16.place(x=3 * col_w, y=3 * row_h, width=col_w, height=row_h)

b_17 = Button(frame_corpo, text="+/-", command=inverter_sinal, bg=cor4, activebackground=cor4, **estilo)
b_17.place(x=0 * col_w, y=4 * row_h, width=col_w, height=row_h)

b_18 = Button(frame_corpo, text="0", command=lambda: entrar_valor("0"), bg=cor4, activebackground=cor4, **estilo)
b_18.place(x=1 * col_w, y=4 * row_h, width=col_w, height=row_h)

b_19 = Button(frame_corpo, text=",", command=lambda: entrar_valor(","), bg=cor4, activebackground=cor4, **estilo)
b_19.place(x=2 * col_w, y=4 * row_h, width=col_w, height=row_h)

b_20 = Button(frame_corpo, text="=", command=calcular, bg=cor5, activebackground=cor5, **estilo)
b_20.place(x=3 * col_w, y=4 * row_h, width=col_w, height=row_h)

janela.mainloop()