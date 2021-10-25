from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco



def popular():
    tv.delete(*tv.get_children())
    vquery="SELECT * FROM P_alunos order by N_Matricula"
    linhas=banco.dql(vquery)
    for i in linhas:
        tv.insert("","end",values=i)
        
def deletar():
    try:
        itemSelecionado=tv.selection()[0]
        tv.delete(itemSelecionado)
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser deletado")
    
            
            

def inserir():
    if valunos.get()=="" or vdata.get()=="" or vmatricula.get()=="" or vturma.get()=="":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        return
    try:
        vquery="INSERT INTO P_alunos (N_Matricula, Nome, Data, Turma) VALUES ('"+vmatricula.get()+"','"+valunos.get()+"','"+vdata.get()+"','"+vturma.get()+"')"
        banco.dml(vquery)
    except:
        messagebox.showinfo(title="ERRO", message="Erro ao inserir")
        return
    popular()
    valunos.delete(0,END)
    vdata.delete(0,END)
    vmatricula.delete(0,END)
    vturma.delete(0,END)
    valunos.focus()
    

def pesquisar():
    tv.delete(*tv.get_children())
    vquery="SELECT * FROM P_alunos WHERE (N_Matricula, Nome) VALUES ('"+valunospesquisar.get()+"','"+vmatriculaspesquisar.get()+"')"
    linhas=banco.dql(vquery)
    for i in linhas:
        tv.insert("","end",values=i)



app=Tk()
app.title("Alunos Presentes")
app.geometry("550x350")

quadroGrid=LabelFrame(app,text="Alunos")
quadroGrid.pack(fill="both",expand="yes",padx=10,pady=10)


tv=ttk.Treeview(quadroGrid,columns=('matricula','nome','data','turma'), show='headings')
tv.column('matricula',minwidth=0,width=50)
tv.column('nome',minwidth=0,width=250)
tv.column('data',minwidth=0,width=100)
tv.column('turma',minwidth=0,width=100)
tv.heading('matricula',text='MATRICULA')
tv.heading('nome',text='NOME')
tv.heading('data',text='DATA')
tv.heading('turma',text='Turma')
tv.pack()
popular()

quadroInserir=LabelFrame(app,text="Inserir Novos Alunos")
quadroInserir.pack(fill="both",expand="yes",padx=10,pady=10)

lbmatricula=Label(quadroInserir,text="Matricula")
lbmatricula.pack(side="left")
vmatricula=Entry(quadroInserir)
vmatricula.pack(side="left",padx=10)
lbalunos=Label(quadroInserir,text="Nome")
lbalunos.pack(side="left")
valunos=Entry(quadroInserir)
valunos.pack(side="left",padx=10)
lbdata=Label(quadroInserir,text="Data")
lbdata.pack(side="left")
vdata=Entry(quadroInserir)
vdata.pack(side="left",padx=10)
lbturma=Label(quadroInserir,text="Turma")
lbturma.pack(side='left')
vturma=Entry(quadroInserir)
vturma.pack(side='left',padx=10)
btn_inserir=Button(quadroInserir,text="Inserir",command=inserir)
btn_inserir.pack(side="left",padx=10)

quadroPesquisar=LabelFrame(app,text="Pesquisar Alunos")
quadroPesquisar.pack(fill="both",expand="yes",padx=10,pady=10)


lbalunos=Label(quadroPesquisar,text="NomeAluno")
lbalunos.pack(side="left")
valunospesquisar=Entry(quadroPesquisar)
valunospesquisar.pack(side="left",padx=10)
lbmatriculas=Label(quadroPesquisar,text="Matricula")
lbmatriculas.pack(side="left")
vmatriculaspesquisar=Entry(quadroPesquisar)
vmatriculaspesquisar.pack(side="left",padx=10)
btn_pesquisar=Button(quadroPesquisar,text="Pesquisar",command=pesquisar)
btn_pesquisar.pack(side="left",padx=10)
btn_todos=Button(quadroPesquisar,text="Mostrar Todos",command=popular)
btn_todos.pack(side="left",padx=10)


quadroDeletar=LabelFrame(app,text="Deletar Alunos")
quadroDeletar.pack(fill="both",expand="yes",padx=10,pady=10)

btn_deletar=Button(quadroDeletar,text="Deletar Aluno",command=deletar)
btn_deletar.pack(side="left",padx=10)


app.mainloop()