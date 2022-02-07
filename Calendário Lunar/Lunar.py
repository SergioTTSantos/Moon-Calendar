# Importação de módulos
from tkinter import *
import tkinter as ttk 
from datetime import date
from datetime import datetime
import calendar
from PIL import ImageTk, Image
import math, decimal, datetime, sys, getopt

# Variável decimal
dec = decimal.Decimal

# Variável para imagem da lua
img = int(9)

# Dia da semana
def dialit_semana(window, ano_semana, mes_semana, dia_semana, coluna_semana, linha_semana):
    
    coluna = coluna_semana
    linha = linha_semana
    
    ttk.Label(window, text=" (",  font = ("Times New Roman", 10)).grid(column = coluna, row = linha)
    
    ddlit_semana = StringVar()
    ddlit_semana.set("")
    ddlit_semana.set(dia_semana_lit(window, ano_semana, mes_semana, dia_semana))
 
    coluna = coluna_semana + 1
    ttk.Label(window, textvariable = ddlit_semana, font = ("Times New Roman", 10)).grid(column = coluna, row = linha)
    coluna = coluna_semana + 2
    ttk.Label(window, text=") - ",  font = ("Times New Roman", 10)).grid(column = coluna, row = linha)


def dia_semana_lit(window, aa_semana, mm_semana, dd_semana):
    dia_semana = ["Segunda-feira", "Terça-feira ", "Quarta-feira ", 
                  "Quinta-feira ", "Sexta-feira ", "Sábado       ", "Domingo      "]

    data = date(year=aa_semana, month=mm_semana, day=dd_semana)

    indice_da_semana = data.weekday()

    dia_da_semana = dia_semana[indice_da_semana]

    numero_do_dia_da_semana = data.isoweekday()
    
    return dia_da_semana


def fase_lua(window, ano, mes, dia, coluna_lua, linha_lua ):
    coluna = coluna_lua
    linha = linha_lua
      
    diff = datetime.datetime(ano, mes, dia) - datetime.datetime(2001, 1, 1)
    days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
    lunations = dec("0.20439731") + (days * dec("0.03386319269"))

    des = StringVar()
    des.set("")
    des.set(descricao_fase(window, lunations))
    ttk.Label(window, textvariable=des, font = ("Times New Roman", 10)).grid(column = coluna, row = linha)

    coluna = coluna_lua + 2    
    
    
def descricao_fase(window, fase):
    index = (fase * dec(8)) + dec("0.5")
    index = math.floor(index)
       
    #return {0: "Fase Lunar: Lua Nova             ", 1: "Fase Lunar: Lua Crescente       ", 2: "Fase Lunar: Lua Quarto Crescente", 
    #        3: "Fase Lunar: Gibosa               ", 4: "Fase Lunar: Lua Cheia           ", 5: "Fase Lunar: Lua Disseminadora   ", 
    #        6: "Fase Lunar: Lua Quarto Minguante ", 7: "Fase Lunar: Balsâmica           "}[int(index) & 7]
    
    fase_str = {0: "Fase Lunar: Lua Nova             ", 1: "Fase Lunar: Lua Crescente       ", 2: "Fase Lunar: Lua Quarto Crescente", 
                3: "Fase Lunar: Gibosa               ", 4: "Fase Lunar: Lua Cheia           ", 5: "Fase Lunar: Lua Disseminadora   ", 
                6: "Fase Lunar: Lua Quarto Minguante ", 7: "Fase Lunar: Balsâmica           "}[int(index) & 7]  
    
    global img
    img = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}[int(index) & 7] 
    
    return fase_str

# Mostra imagem
def monta_imagem(window, coluna_imagem, linha_imagem):
    coluna = coluna_imagem
    linha = linha_imagem

    ind = img

    if ind == 0:
        caminho = "C:\\Projetos Python\\Projetos\\Calendário Lunar\\Imagens\\A - Lua Nova.gif"
    elif ind == 1:
        caminho = "C:\\Projetos Python\\Projetos\\Calendário Lunar\\Imagens\\B - lua Crescente.gif"
    elif ind == 2:
        caminho = "C:\\Projetos Python\\Projetos\\Calendário Lunar\\Imagens\\C - Lua Quarto Crescente.gif"
    elif ind == 3:
        caminho = "C:\\Projetos Python\\Projetos\\Calendário Lunar\\Imagens\\D - Lua Gibosa.gif"
    elif ind == 4:
        caminho = "C:\\Projetos Python\\Projetos\\Calendário Lunar\\Imagens\\E - Lua Cheia.gif"
    elif ind == 5:
        caminho = "C:\\Projetos Python\\Projetos\\Calendário Lunar\\Imagens\\F - Lua Disseminadora.gif"
    elif ind == 6:
        caminho = "C:\\Projetos Python\\Projetos\\Calendário Lunar\\Imagens\\G - Lua Quarto Minguante.gif"
    elif ind == 7:
        caminho = "C:\\Projetos Python\\Projetos\\Calendário Lunar\\Imagens\\H - Lua Balsamica.gif"
    
    logo = ttk.PhotoImage(file = caminho)
    labelLogo = ttk.Label(window, image=logo)

    labelLogo.grid(row = linha, column = coluna, columnspan=2, rowspan=2, sticky=ttk.W+ttk.E+ttk.N+ttk.S, padx=5, pady=5)

def data_sel():
    aa_val = int(aa_entrada.get())
    dd_val = int(dia_busca.get())
    mm_val = meses_busca.index(mes_busca.get()) + 1
    
    if not dd_val or not mm_val or not aa_val:
        print('erro')
    elif aa_val < 1900 or aa_val > 2100:
        print('erro')
    else:
        # Dia da semana escolhido
        dialit_semana(window, aa_val, mm_val, dd_val, 4, 10)

        # Fase da lua escolhida
        fase_lua(window, aa_val, mm_val, dd_val, 7, 10)
        
        # Imagem da lua
        monta_imagem(window, 9, 10)
        
        return


# Montando a janela 
window = ttk.Tk() 
window.title('Calendário Lunar') 
window.geometry('850x350') 
 
# Data atual (dd/mm/aaaa - Dia da semana)
# dd/mm/aaaa
data_atual = date.today()
data_atu = data_atual.strftime('%d/%m/%Y')

ttk.Label(window, text = "",font = ("Times New Roman", 10)).grid(column = 1,row = 1) 
ttk.Label(window, text = "",font = ("Times New Roman", 10)).grid(column = 1,row = 2)
ttk.Label(window, text = "Data Atual:",font = ("Times New Roman", 10,'bold'), justify = "right").grid(column = 2,row = 2) 
ddmmaaaa=StringVar()
ddmmaaaa.set("")
ddmmaaaa.set(data_atu)
ttk.Label(textvariable=ddmmaaaa, font = ("Times New Roman", 10), justify = "left").grid(column = 3,row = 2)

# Dia da semana
dialit_semana(window, data_atual.year, data_atual.month, data_atual.day, 4, 2)

# Fase da lua atual
fase_lua(window, data_atual.year, data_atual.month, data_atual.day, 7, 2)

# Imagem da lua atual
monta_imagem(window, 9, 2)


# Montando escolha de data
ttk.Label(window, text = "               ",font = ("Times New Roman", 10)).grid(column = 1,row = 3)
ttk.Label(window, text = "               ",font = ("Times New Roman", 10)).grid(column = 1,row = 4)
ttk.Label(window, text = "               ",font = ("Times New Roman", 10)).grid(column = 1,row = 5)
ttk.Label(window, text = "Escolha data para pesquisa:",font = ("Times New Roman", 10,'bold')).grid(column = 2,row = 6) 
ttk.Label(window, text = "               ",font = ("Times New Roman", 10)).grid(column = 1,row = 7)

# Dia
ttk.Label(window, text = "Dia",font = ("Times New Roman", 10)).grid(column = 1,row = 8) 

dia_busca = StringVar(window)
dias_busca = ('1','2','3','4','5','6','7','8','9', '10', '11','12','13','14','15','16','17','18','19', '20', 
      '21','22','23','24','25','26','27','28','29', '30', '31')

dd_busca = OptionMenu(window, dia_busca, *dias_busca)
dd_busca.grid(column = 2,row = 8)

# Mes
ttk.Label(window, text = "Mês",font = ("Times New Roman", 10)).grid(column = 3,row = 8)

mes_busca = StringVar(window)
meses_busca = ('Janeiro','Fevereiro','Março','Abril','maio','Junho','Julho','Agosto', 
      'Setembro','Outubro','Novembro','Dezembro')

mm_busca = OptionMenu(window, mes_busca, *meses_busca)
mm_busca.grid(column = 4,row = 8)

# Ano
ttk.Label(window, text = "Ano",font = ("Times New Roman", 10)).grid(column = 5,row = 8)

aa_entrada = Entry(window)
aa_entrada.grid(column = 6,row = 8)

# Montando botão
ttk.Label(window, text = "               ",font = ("Times New Roman", 10)).grid(column = 1,row = 9)
btn_pesq = Button(window,text="Pesquisar", command = data_sel)#,command=nomes
btn_pesq.grid(column = 3,row = 10)

# Mostrando a janela 
window.mainloop()