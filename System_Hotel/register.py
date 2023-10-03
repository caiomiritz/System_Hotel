from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox



class Register:

    def __init__(self, root):
        
        self.root=root
        self.root.title("Novo Usuário")
        self.root.geometry("900x780+300+0")

        #----------------Variaveis----------------------
        self.var_name=StringVar()
        self.var_telefone=StringVar()
        self.var_mail=StringVar()
        self.var_usuario=StringVar()
        self.var_senha=StringVar()
        self.var_confsenha=StringVar()
        self.var_tiposegur=StringVar()
        self.var_palavrasegur=StringVar()
        
        #-----------------------BG Image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\caio.raphaelli\Documents\System_Hotel\imagens\6191107.jpg")
        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        #-----------Frame principal

        frame=Frame(self.root, bg="black")
        frame.place(x=200, y=40, width=500, height=700)

        register_lbl=Label(frame, text="REGISTRE-SE AQUI", font=("malgun gothic semilight", 30, "bold"), fg="gold", bg="black")
        register_lbl.place(x=80, y=20)

        #=====================LABEL AND ENTRY================================

        #------Nome
        fname=Label(frame, text="Nome:", font=("malgun gothic semilight", 20, "bold"), bg="black", fg="white")
        fname.place(x=50, y=100)

        fname_entry=ttk.Entry(frame, textvariable=self.var_name, font=("malgun gothic semilight", 20, "bold"))
        fname_entry.place(x=200, y=100, width=250)

        #----E-mail
        fmail=Label(frame, text="E-mail:", font=("malgun gothic semilight", 20, "bold"), bg="black", fg="white")
        fmail.place(x=50, y=160)

        fmail_entry=ttk.Entry(frame, textvariable=self.var_mail, font=("malgun gothic semilight", 20, "bold"))
        fmail_entry.place(x=200, y=160, width=250)

        #-----Telefone
        ffone=Label(frame, text="Telefone:", font=("malgun gothic semilight", 20, "bold"), bg="black", fg="white")
        ffone.place(x=50, y=220)

        ffone_entry=ttk.Entry(frame, textvariable=self.var_telefone, font=("malgun gothic semilight", 20, "bold"))
        ffone_entry.place(x=200, y=220, width=250)

        #----Usuario
        fuser=Label(frame, text="Usuário:", font=("malgun gothic semilight", 20, "bold"), bg="black", fg="white")
        fuser.place(x=50, y=280)

        fuser_entry=ttk.Entry(frame, textvariable=self.var_usuario, font=("malgun gothic semilight", 20, "bold"))
        fuser_entry.place(x=200, y=280, width=250)

        #-----Senhas
        fsenha=Label(frame, text="Senha:", font=("malgun gothic semilight", 20, "bold"), bg="black", fg="white")
        fsenha.place(x=50, y=340)

        fsenha_entry=ttk.Entry(frame, textvariable=self.var_senha, font=("malgun gothic semilight", 20, "bold"))
        fsenha_entry.place(x=200, y=340, width=250)

        fc_senha=Label(frame, text="Confirmar:", font=("malgun gothic semilight", 20, "bold"), bg="black", fg="white")
        fc_senha.place(x=50, y=400)

        fc_senha_entry=ttk.Entry(frame, textvariable=self.var_confsenha, font=("malgun gothic semilight", 20, "bold"))
        fc_senha_entry.place(x=200, y=400, width=250)

        #------Tipo Segurança
        fsegur=Label(frame, text="Segurança:", font=("malgun gothic semilight", 20, "bold"), bg="black", fg="white")
        fsegur.place(x=50, y=455)

        self.combo_segur_P=ttk.Combobox(frame, textvariable=self.var_tiposegur, font=("malgun gothic semilight", 15, "bold"), state="readonly")
        self.combo_segur_P["values"]=("Selecionar", "Local de Nascimento", "Apelido", "Nome do seu pet", "Comida favorita", "Cor favorita")
        self.combo_segur_P.place(x=200, y=465, width=250)
        self.combo_segur_P.current(0)

        fc_segur=Label(frame, text="Palavra:", font=("malgun gothic semilight", 20, "bold"), bg="black", fg="white")
        fc_segur.place(x=50, y=520)

        fc_segur_entry=ttk.Entry(frame, textvariable=self.var_palavrasegur, font=("malgun gothic semilight", 20, "bold"))
        fc_segur_entry.place(x=200, y=520, width=250)

        #------------------------CheckButton---
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame, variable=self.var_check, text="Eu aceito com os Termos & Condições", font=("malgun gothic semilight", 10, "bold"), 
                             relief=RIDGE, bd=0, onvalue=1, offvalue=0)
        checkbtn.place(x=130, y=580)

        #----------Botoes

        registerbnt=Button(frame, text="Registrar", font=("malgun gothic semilight", 15, "bold"), bd=3, 
                        fg="white", bg="red",activeforeground="white", activebackground="red", relief=RIDGE, command=self.register_data)
        registerbnt.place(x=40, y=620, width=120)

        loginbnt=Button(frame, text="Login", font=("malgun gothic semilight", 15, "bold"), bd=3, 
                        fg="white", bg="blue",activeforeground="white", activebackground="blue", relief=RIDGE)
        loginbnt.place(x=340, y=620, width=120)

    
    #-----------------------Declaração Função---------------------

    def register_data(self):
        if self.var_name.get()=="" or self.var_mail.get()=="" or self.var_tiposegur.get()=="Selecionar" or self.var_telefone.get()=="" or self.var_palavrasegur.get()=="":
            messagebox.showerror("Erro", "Todos os campos precisam ser preenchidos")
        elif self.var_senha.get()!=self.var_confsenha.get():
            messagebox.showerror("Erro", "Senhas diferentes")
        elif self.var_check.get()==0:
            messagebox.showerror("Erro", "Por favor aceite os Termos & Condições")
        else:
            messagebox.showinfo("Sucesso", "Conta criada")








if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()


