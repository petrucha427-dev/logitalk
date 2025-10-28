from customtkinter import *
from PIL import Image

class AuthWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('700x400')
        self.title('LogiTalk - Вхід')
        self.resizable(False, False)

        # ліва частина
        self.left_frame = CTkFrame(self)
        self.left_frame.pack(side = 'left', fill = 'both')

        img_ctk = CTkImage(light_image=Image.open("bg (2).png"), size=(450, 400))
        self.img_lbl = CTkLabel(self.left_frame, text='Welcome', image= img_ctk, 
                                font=('Helvetica', 60, 'bold'), text_color='white')
        self.img_lbl.pack()

        # права частина
        self.right_frame = CTkFrame(self, fg_color= 'white')
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side = 'right', fill = 'both', expand = 'True')

        self.title_lbl = CTkLabel(self.right_frame, text='LogiTalk',
                                  font=('Helvetica', 30, 'bold'), text_color="#6753cc")
        self.title_lbl.pack(pady = 60)

        self.entry_name = CTkEntry(self.right_frame, placeholder_text= "Введіть ім'я",
                                   placeholder_text_color="#9c94c5",
                                   text_color='#6753cc', fg_color='#eae6ff',
                                   border_color='#eae6ff',
                                   font = ('Helvetica', 20, 'bold'),
                                   corner_radius= 25)
        self.entry_name.pack(fill ='x', padx= 15, pady = 15)
        
        self.login_btn = CTkButton(self.right_frame, text = "Увійти", height= 45,
                                   font = ('Helvetica', 20, 'bold'),
                                   text_color='white', fg_color= '#d06fc0',
                                   hover_color="#834779")
        self.login_btn.pack(fill = 'x', padx= 45, pady = 50)

class MainWindow(CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__()


        self.geometry('800x600')
        self.title('LogiTalk - чат')
        self.minsize(400,400)

win = AuthWindow()
win.mainloop()
