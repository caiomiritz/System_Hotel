from tkinter import*
from PIL import Image,ImageTk
from clientes import Janela_Clientes

class SistemaGerenciamentoHotel:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento")
        self.root.geometry("1550x800+0+0")

        #-------------IMAGEM DE CIMA-------------------
        img1=Image.open(r"C:\Users\caio.raphaelli\Documents\System_Hotel\imagens\hotel1.png")
        img1=img1.resize((1550,140), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #-------------LOGO DO HOTEL---------------------
        img2=Image.open(r"C:\Users\caio.raphaelli\Documents\System_Hotel\imagens\logohotel.png")
        img2=img2.resize((230,140), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #-------------TITULO PROGRAMA--------------------
        lbl_title=Label(self.root,text="ZANELLA'S HOTEL",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #-------------MAIN FRAME---------------------
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #-------------------MENU--------------------
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #-------------BOTAO FRAME---------------------
        btn_frame=Frame(main_frame,bd=2,bg="black",relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=190)

        clie_btn=Button(btn_frame,text="HÓSPEDES",command=self.detalhes_clientes,width=20,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand2")
        clie_btn.grid(row=0,column=0,pady=1)

        quarto_btn=Button(btn_frame,text="QUARTOS",width=20,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand2")
        quarto_btn.grid(row=1,column=0,pady=1)

        detalhes_btn=Button(btn_frame,text="DETALHES",width=20,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand2")
        detalhes_btn.grid(row=2,column=0,pady=1)

        reportar_btn=Button(btn_frame,text="REPORTAR",width=20,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand2")
        reportar_btn.grid(row=3,column=0,pady=1)

        sair_btn=Button(btn_frame,text="SAIR",width=20,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand2")
        sair_btn.grid(row=4,column=0,pady=1)

        #-----------------IMAGEM CENTRAL---------------
        img3=Image.open(r"C:\Users\caio.raphaelli\Documents\System_Hotel\imagens\slide3.jpg")
        img3=img3.resize((1310,590), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=230,y=0,width=1315,height=600)

        #-----------------IMAGENS BAIXO----------------
        img4=Image.open(r"C:\Users\caio.raphaelli\Documents\System_Hotel\imagens\khana.jpg")
        img4=img4.resize((230,210), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)

        img5=Image.open(r"C:\Users\caio.raphaelli\Documents\System_Hotel\imagens\versao.jpg")
        img5=img5.resize((230,190), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=180)

    def detalhes_clientes(self):
        self.new_window=Toplevel(self.root)
        self.app=Janela_Clientes(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = SistemaGerenciamentoHotel(root)
    root.mainloop()