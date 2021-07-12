from tkinter import *
from tkinter import ttk


root = Tk()

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)


class App(Funcs):
    def __init__(self) :
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_1()
        self.lista_frame_2()
        root.mainloop()
    
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width= 800, height= 600)
        self.root.minsize(width= 700, height=500)

    def frames_da_tela(self):
        """
        Frames da tela.
        """ 
        self.frame_1 = Frame(self.root, border= 4, background='#dfe3ee',
                             highlightbackground='#759fe6',highlightthickness=2.5)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, border= 4, background='#dfe3ee',
                            highlightbackground="#749fe6", highlightthickness=2.5)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth= 0.96, relheight=0.46)

    def widgets_frame_1(self):
        """
        Botões
        """
        self.bt_limpar = Button(self.frame_1, text= 'Limpar', bd='2', bg='#107db2', fg = 'White',
                                 font=('Verdana', 8, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        #--------------------------------------------------------------------------------------------
        
        self.bt_buscar = Button(self.frame_1, text= 'Buscar', bd='2', bg='#107db2', fg ='White',
                                font=('Verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        #--------------------------------------------------------------------------------------------

        self.bt_novo = Button(self.frame_1, text= 'Novo', bd= '2', bg='#107db2', fg = 'White',
                                font=('Verdana', 8, 'bold'))
        self.bt_novo.place(relx=0.65, rely=0.1, relwidth=0.1, relheight=0.15)
        #--------------------------------------------------------------------------------------------

        self.bt_alterar = Button(self.frame_1, text= 'Alterar',bd= '2', bg='#107db2', fg='White',
                                font=('Verdana', 8, 'bold'))
        self.bt_alterar.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.15)
        #--------------------------------------------------------------------------------------------
 
        self.bt_apagar = Button(self.frame_1, text= 'Apagar', bd= '2', bg='#107db2', fg='White',
                                font=('Verdana', 8, 'bold')  )
        self.bt_apagar.place(relx=0.85, rely=0.1, relwidth=0.1, relheight=0.15)

        """
        Labels e entries
        """ 

        self.lb_codigo = Label(self.frame_1, text = 'Código', bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.05, relwidth=0.07)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.07 )
        #-----------------------------------------------------------------------------
        self.lb_nome = Label(self.frame_1, text= "Nome", bg='#dfe3ee',  fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35, relwidth=0.07)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.9)
        #-----------------------------------------------------------------------------
        self.lb_Telefone = Label(self.frame_1, text= "Telefone", bg='#dfe3ee',  fg='#107db2')
        self.lb_Telefone.place(relx=0.05, rely=0.6, relwidth=0.07)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7,relwidth=0.35)
        #-----------------------------------------------------------------------------
        self.lb_cidade = Label(self.frame_1, text= "Cidade", bg='#dfe3ee',  fg='#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6, relwidth=0.07)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7,relwidth=0.45)
        #-----------------------------------------------------------------------------

    def lista_frame_2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=10)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.96, relheight=0.85)

        #barra de rolagem
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical',)
        self.listaCli.configure(yscroll=self.scroolLista.set, )
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)



App()