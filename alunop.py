from tkinter import *
import os
import banco


def gravarDados():
    if tb_nmatricula.get() != "":
        vnmatricula=tb_nmatricula.get()
        vnome=tb_nome.get()
        vdata=tb_data.get()
        vturma=tb_turma.get()
        vobs=tb_obs.get("1.0",END)
        vquery="INSERT INTO P_alunos (N_Matricula, Nome, Data, Turma, Obs) VALUES ('"+vnmatricula+"','"+vnome+"','"+vdata+"','"+vturma+"','"+vobs+"')"
        banco.dml(vquery)
        tb_nmatricula.delete(0,END)
        tb_nome.delete(0,END)
        tb_data.delete(0,END)
        tb_turma.delete(0,END)
        tb_obs.delete("1.0",END)
        print("Dados Gravados")
    else:
        print("ERRO")


app=Tk()
app.title("Ata de Presenca")
app.geometry("270x400")
app.configure(background="#1C1C1C")


Label(app,text="N-Matricula",background="#1C1C1C",foreground="#FFFAFA",anchor=W).place(x=32,y=10,width=100,height=30)
tb_nmatricula=Entry(app)
tb_nmatricula.place(x=32,y=30,width=200,height=20)

Label(app,text="Nome",background="#1C1C1C",foreground="#FFFAFA",anchor=W).place(x=32,y=60,width=100,height=30)
tb_nome=Entry(app)
tb_nome.place(x=32,y=80,width=200,height=20)

Label(app,text="Data",background="#1C1C1C",foreground="#FFFAFA",anchor=W).place(x=32,y=110,width=120,height=30)
tb_data=Entry(app)
tb_data.place(x=32,y=130,width=200,height=20)

Label(app,text="Turma",background="#1C1C1C",foreground="#FFFAFA",anchor=W).place(x=32,y=160,width=100,height=30)
tb_turma=Entry(app)
tb_turma.place(x=32,y=180,width=200,height=20)

Label(app,text="OBS",background="#1C1C1C",foreground="#FFFAFA",anchor=W).place(x=32,y=209,width=100,height=20)
tb_obs=Text(app)
tb_obs.place(x=32,y=230,width=200,height=100)


Button(app,text="Marcar Presenca",background="#00008B",foreground="#FFFAFA",command=gravarDados).place(x=80,y=350,width=100,height=20)



app.mainloop()