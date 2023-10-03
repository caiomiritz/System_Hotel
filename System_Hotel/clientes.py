from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk

class Janela_Clientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Hóspedes")
        self.root.geometry("1296x570+230+220")

        #-------------TITULO PROGRAMA--------------------
        lbl_title=Label(self.root,text="ADICIONAR DETALHES",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1296,height=50)

        #-------------LOGO DO HOTEL---------------------
        img2=Image.open(r"C:\Users\caio.raphaelli\Documents\System_Hotel\imagens\logohotel.png")
        img2=img2.resize((100,40), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=4,width=100,height=40)

        #--------------LABEL FRAME-----------------------
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Detalhes do Hóspede", font=("arial",15,"bold"),padx=2)
        labelframeleft.place(x=5, y=50, width=380, height=515)

        #-------------LABELS E ENTRADAS---------------------
        
        # Referencia Cliente
        ref_cli=Label(labelframeleft, text="Referência: ", font=("arial",12,"bold"), padx=2, pady=6)
        ref_cli.grid(row=0, column=0, sticky=W)
        txt_ref_cli=ttk.Entry(labelframeleft, width=24, font=("arial",13,"bold"))
        txt_ref_cli.grid(row=0, column=1)

        # Nome do Cliente
        nome_cli=Label(labelframeleft, text="Nome: ", font=("arial",12,"bold"), padx=2, pady=6)
        nome_cli.grid(row=1, column=0, sticky=W)
        txt_nome_cli=ttk.Entry(labelframeleft, width=24, font=("arial",13,"bold"))
        txt_nome_cli.grid(row=1, column=1)

        # Nome da Mãe
        nomeM_cli=Label(labelframeleft, text="Nome da Mãe: ", font=("arial",12,"bold"), padx=2, pady=6)
        nomeM_cli.grid(row=2, column=0, sticky=W)
        txt_nomeM_cli=ttk.Entry(labelframeleft, width=24, font=("arial",13,"bold"))
        txt_nomeM_cli.grid(row=2, column=1)

        # Genero 
        gen_cli=Label(labelframeleft, text="Gênero: ", font=("arial",12,"bold"), padx=2, pady=6)
        gen_cli.grid(row=3, column=0, sticky=W)
        gen_box=ttk.Combobox(labelframeleft, font=("arial",12,"bold"), width=22, state="readonly")
        gen_box["value"]=("Masculino", "Feminino", "Outros")
        gen_box.current(0)
        gen_box.grid(row=3, column=1)
        
        # CEP
        cep_cli=Label(labelframeleft, text="CEP: ", font=("arial",12,"bold"), padx=2, pady=6)
        cep_cli.grid(row=4, column=0, sticky=W)
        txt_cep_cli=ttk.Entry(labelframeleft, width=24, font=("arial",13,"bold"))
        txt_cep_cli.grid(row=4, column=1)

         # Celular
        tel_cli=Label(labelframeleft, text="Número Telefone: ", font=("arial",12,"bold"), padx=2, pady=6)
        tel_cli.grid(row=5, column=0, sticky=W)
        txt_tel_cli=ttk.Entry(labelframeleft, width=24, font=("arial",13,"bold"))
        txt_tel_cli.grid(row=5, column=1)

         # Email
        email_cli=Label(labelframeleft, text="E-mail: ", font=("arial",12,"bold"), padx=2, pady=6)
        email_cli.grid(row=6, column=0, sticky=W)
        txt_email_cli=ttk.Entry(labelframeleft, width=24, font=("arial",13,"bold"))
        txt_email_cli.grid(row=6, column=1)

         # Nacionalidade
        nacio_cli=Label(labelframeleft, text="Nacionalidade: ", font=("arial",12,"bold"), padx=2, pady=6)
        nacio_cli.grid(row=7, column=0, sticky=W)
        nacio_box=ttk.Combobox(labelframeleft, font=("arial",12,"bold"), width=22, state="readonly")
        nacio_box["value"]=("Brasileiro", "Uruguaio", "Argentino", "Estado-Unidense", "Paraguaio", "Outros")
        nacio_box.current(0)
        nacio_box.grid(row=7, column=1)

         # Tipo ID
        tipo_id_cli=Label(labelframeleft, text="ID Tipo: ", font=("arial",12,"bold"), padx=2, pady=6)
        tipo_id_cli.grid(row=8, column=0, sticky=W)
        tipo_box=ttk.Combobox(labelframeleft, font=("arial",12,"bold"), width=22, state="readonly")
        tipo_box["value"]=("CPF", "RG", "Passaporte", "Outros")
        tipo_box.current(0)
        tipo_box.grid(row=8, column=1)

         # Numero ID
        num_id_cli=Label(labelframeleft, text="Numero ID: ", font=("arial",12,"bold"), padx=2, pady=6)
        num_id_cli.grid(row=9, column=0, sticky=W)
        txt_numID_cli=ttk.Entry(labelframeleft, width=24, font=("arial",13,"bold"))
        txt_numID_cli.grid(row=9, column=1)

         # Endereço
        ender_cli=Label(labelframeleft, text="Endereço: ", font=("arial",12,"bold"), padx=2, pady=6)
        ender_cli.grid(row=10, column=0, sticky=W)
        txt_ender_cli=ttk.Entry(labelframeleft, width=24, font=("arial",13,"bold"))
        txt_ender_cli.grid(row=10, column=1)

        #----------------------BOTOES--------------------------
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=420, width=371, height=37)

        btn_add=Button(btn_frame, text="Adicionar", font=("arial",12,"bold"), bg="green", fg="black", width=8)
        btn_add.grid(row=0, column=0, padx=1)

        btn_att=Button(btn_frame, text="Atualizar", font=("arial",12,"bold"), bg="yellow", fg="black", width=8)
        btn_att.grid(row=0, column=1, padx=1)

        btn_del=Button(btn_frame, text="Deletar", font=("arial",12,"bold"), bg="red", fg="black", width=8)
        btn_del.grid(row=0, column=2, padx=1)

        btn_reset=Button(btn_frame, text="Resetar", font=("arial",12,"bold"), bg="white", fg="black", width=8)
        btn_reset.grid(row=0, column=3, padx=1)

        #--------------------------TABLE FRAME----------------------
        table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="Sistema de Busca e Visualização", font=("arial",15,"bold"),padx=2)
        table_frame.place(x=435, y=50, width=858, height=515)

        procurarPor=Label(table_frame, text="Procurar por: ", font=("arial",12,"bold"), bg="red", fg="white")
        procurarPor.grid(row=0, column=0, sticky=W, padx=2)
        
        procura_box=ttk.Combobox(table_frame, font=("arial",12,"bold"), width=22, state="readonly")
        procura_box["value"]=("Nome", "CPF", "RG", "Referência")
        procura_box.current(0)
        procura_box.grid(row=0, column=1, padx=2)
    
        txt_procura=ttk.Entry(table_frame, width=24, font=("arial",13,"bold"))
        txt_procura.grid(row=0, column=2, padx=2)

        btn_procurar=Button(table_frame, text="Procurar", font=("arial",12,"bold"), bg="white", fg="black", width=8)
        btn_procurar.grid(row=0, column=3, padx=2)

        btn_all=Button(table_frame, text="Mostrar Tudo", font=("arial",12,"bold"), bg="white", fg="black", width=10)
        btn_all.grid(row=0, column=4, padx=2)

        #--------------------DATA FRAME------------------------------
        data_table=Frame(table_frame, bd=2, relief=RIDGE)
        data_table.place(x=0, y=50, width=849, height=350)

        scroll_x=ttk.Scrollbar(data_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(data_table, orient=VERTICAL)

        self.Hosp_Table_Detalhes=ttk.Treeview(data_table, columns=("Referência", "Nome", "Nome da Mãe", "Gênero", 
                                                                   "CEP", "Telefone", "E-mail", "Nacionalidade", "Tipo ID", "ID", "Endereço"), 
                                                                   xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Hosp_Table_Detalhes.xview)
        scroll_y.config(command=self.Hosp_Table_Detalhes.yview)

        self.Hosp_Table_Detalhes.heading("Referência", text="Referência")
        self.Hosp_Table_Detalhes.heading("Nome", text="Nome")
        self.Hosp_Table_Detalhes.heading("Nome da Mãe", text="Nome da Mãe")
        self.Hosp_Table_Detalhes.heading("Gênero", text="Gênero")
        self.Hosp_Table_Detalhes.heading("CEP", text="CEP")
        self.Hosp_Table_Detalhes.heading("Telefone", text="Telefone")
        self.Hosp_Table_Detalhes.heading("E-mail", text="E-mail")
        self.Hosp_Table_Detalhes.heading("Nacionalidade", text="Nacionalidade")
        self.Hosp_Table_Detalhes.heading("Tipo ID", text="Tipo ID")
        self.Hosp_Table_Detalhes.heading("ID", text="ID")
        self.Hosp_Table_Detalhes.heading("Endereço", text="Endereço")

        self.Hosp_Table_Detalhes["show"]="headings"

        self.Hosp_Table_Detalhes.column("Referência", width=100)
        self.Hosp_Table_Detalhes.column("Nome", width=100)
        self.Hosp_Table_Detalhes.column("Nome da Mãe", width=100)
        self.Hosp_Table_Detalhes.column("Gênero", width=100)
        self.Hosp_Table_Detalhes.column("CEP", width=100)
        self.Hosp_Table_Detalhes.column("Telefone", width=100)
        self.Hosp_Table_Detalhes.column("E-mail", width=100)
        self.Hosp_Table_Detalhes.column("Nacionalidade", width=100)
        self.Hosp_Table_Detalhes.column("Tipo ID", width=100)
        self.Hosp_Table_Detalhes.column("ID", width=100)
        self.Hosp_Table_Detalhes.column("Endereço", width=100)

        self.Hosp_Table_Detalhes.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    root = Tk()
    obj = Janela_Clientes(root)
    root.mainloop()