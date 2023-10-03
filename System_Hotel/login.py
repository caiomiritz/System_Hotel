from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Janela_Login:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\caio.raphaelli\Documents\System_Hotel\imagens\taj.jpg")

        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame=Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1=Image.open(r"C:\Users\caio.raphaelli\Documents\System_Hotel\imagens\288592.png")
        img1=img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str=Label(frame, text="Login", font=("malgun gothic semilight", 20, "bold"), fg="white", bg="black")
        get_str.place(x=130, y=110)


        #-----------LABEL DO LOGIN---------------

        usuario=lbl=Label(frame, text="Usuário", font=("malgun gothic semilight", 20, "bold"), fg="white", bg="black")
        usuario.place(x=120, y=170)

        self.txtuser=Entry(frame, font=("malgun gothic semilight", 15, "bold"))
        self.txtuser.place(x=40, y=210, width=270)

        senha=lbl=Label(frame, text="Senha", font=("malgun gothic semilight", 20, "bold"), fg="white", bg="black")
        senha.place(x=130, y=250)

        self.txtsenha=Entry(frame, font=("malgun gothic semilight", 15, "bold"))
        self.txtsenha.place(x=40, y=290, width=270)

        #--------------Icones do login-----------------

        img2=Image.open(r"C:\Users\caio.raphaelli\Documents\System_Hotel\imagens\LoginIconAppl.png")
        img2=img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=700, y=348, width=25, height=25)

        img3=Image.open(r"C:\Users\caio.raphaelli\Documents\System_Hotel\imagens\lock-512.png")
        img3=img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=710, y=428, width=25, height=25)

        
        #------------Botao Login----
        
        loginbnt=Button(frame, command=self.login, text="Logar", font=("malgun gothic semilight", 12, "bold"), bd=3, relief=RIDGE, 
                        fg="white", bg="red",activeforeground="white", activebackground="red")
        loginbnt.place(x=110, y=335, width=120, height=35)

        #------------Botao register----

        registerbnt=Button(frame, text="Novo Usuário", font=("malgun gothic semilight", 12, "bold"), borderwidth=0, 
                        fg="white", bg="black",activeforeground="white", activebackground="black")
        registerbnt.place(x=20, y=400, width=130)

        #----------forget buton------

        forgetbnt=Button(frame, text="Esqueci a Senha", font=("malgun gothic semilight", 12, "bold"), borderwidth=0, 
                        fg="white", bg="black",activeforeground="white", activebackground="black")
        forgetbnt.place(x=190, y=400, width=130)
        

    def login(self):
        
        if self.txtuser.get()=="" or self.txtsenha.get()=="":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")
        elif self.txtuser.get()=="caio" and self.txtsenha.get()=="123":
            messagebox.showinfo("Sucesso", "Login validado !")
        else:
            messagebox.showerror("Invalido", "Senha ou Usuário inválidos")

            
    


        
            



if __name__ == "__main__":
    root=Tk()
    app=Janela_Login(root)
    root.mainloop()