from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pwinput

janela = Tk()
janela.geometry("300x200")
janela.title("Par ou Impar")
janela.configure()

label1 = Label(janela, text="JOGADOR 1")
label1.place(x=10, y=10)

cx1 = Entry(janela,show="*", width=3)
cx1.place(x=40, y=40)

label2 = Label(janela, text="JOGADOR 2")
label2.place(x=10, y=80)
cx2 = Entry(janela,  show='*', width=3)
cx2.place(x=40, y=110)

combo = ttk.Combobox(state="readonly", values=["Par", "Impar"], width=5)
combo.place(x=80, y=40)
combo2 = ttk.Combobox(state="readonly", values=["Par", "Impar"], width=5)
combo2.place(x=80, y=110)

Resultado1 = Label(text="Resultado")
Resultado1.place(x=190, y=10)

Resultado2 = Label(text="")
Resultado2.place(x=190, y=60)

Resultado3 = Label(text="")
Resultado3.place(x=150, y=100)



def parimpar():
  resul1 = int(cx1.get())
  resul2 = int(cx2.get())
  total = int(resul1 + resul2)


  Resultado1.configure(text=total)

  if total%2==0:
      Resultado2.configure(text="PAR")
  else:Resultado2.configure(text="IMPAR")

  if combo.get() == "Par":
      if total%2==0:

         Resultado3.configure(text="JOGADOR 1 GANHOU")
      else:
          Resultado3.configure(text="JOGADOR 2 GANHOU")

  if combo2.get() == "Par":
          if total%2==0:
              Resultado3.configure(text="JOGADOR 2 GANHOU")
          else:
              Resultado3.configure(text="JOGADOR 1 GANHOU")

  if combo.get() == "Par":
      if combo2.get() == "Par":
          Resultado3.configure(text="0")
          Resultado2.configure(text="0")
          Resultado1.configure(text="0")
          messagebox.showinfo("Par ou Impar", "Par e Par tente novamente")

  if combo.get() == "Impar":
      if combo2.get() == "Impar":
          Resultado3.configure(text="")
          Resultado2.configure(text="")
          Resultado1.configure(text="")
          messagebox.showinfo("Par ou Impar", "impar e impar tente novamente")


      

botao = Button(janela, text="Confirma", command=parimpar)
botao.place(x=120, y=160)



mainloop()