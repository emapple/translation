import googletrans
import tkinter as tk
import numpy as np
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.tr_obj = googletrans.Translator()
        self.master = master
        self.bgcolor = '#a9926e'
        self.textcolor1 = '#ecdfc6'
        self.textcolor2 = '#d2c6a1'
        self.pack()
        self.master.configure(bg=self.bgcolor)
        self.lang_list = ['en', 'es', 'it', 'fr', 'he', 'ar']
        self.create_widgets()

    def create_widgets(self):
        self.topframe = tk.Frame(self)
        self.topframe.pack(side='top', fill='x')
        self.botframe = tk.Frame(self)
        self.botframe.pack(side='bottom', fill='both')
        self.topframe.configure(bg=self.bgcolor)
        self.botframe.configure(bg=self.bgcolor)
        self.master.bind('<Return>', self.translate_word)
        
        self.src = tk.StringVar(self.master) #source language
        self.src.set(self.lang_list[0])
        self.srcmenu = tk.OptionMenu(self.topframe, self.src, *self.lang_list)
        self.srcmenu.configure(bg=self.textcolor2, activebackground=self.textcolor1,
                font='Arial 18')
        self.srcmenu['menu'].configure(bg=self.textcolor1, font='Arial 18')
        self.srcmenu.grid(row=0, column=0, ipadx=50, padx=20)
        self.l1 = tk.Label(self.topframe, text='word to translate:',
                font='Arial 18')
        self.l1.grid(row=0, column=1)#, ipadx=50)
        self.entry = tk.Entry(self.topframe, font='Courier 18')
        self.entry.grid(row=0, column=2)
        self.entry.configure(bg=self.textcolor1)
        self.l1.configure(bg=self.bgcolor)

        self.b1 = tk.Button(self.topframe, text='Translate!', command=self.translate_word,
                 font='Arial 18')
        self.b1.grid(row=0, column=3, padx=10)
        self.b1.configure(bg=self.bgcolor)

        self.lang_menu = []
        for lang in self.lang_list[1:4]:
            self.make_menu(self.botframe, lang)
        #self.make_checkbox(self.botframe, 'it')
        #self.make_checkbox(self.botframe, 'fr')
        #self.make_checkbox(self.botframe, 'he')
        #for lang in self.lang_check:
        #    self.lang_check[lang][1].pack()
        
        self.b2 = tk.Button(self.topframe, text='Add language', command=lambda: self.make_menu(self.botframe, 'en'),
                font='Arial 18')
        self.b2.grid(row=0, column=4, padx=30)
        self.b2.configure(bg=self.bgcolor)

    def make_menu(self, frame, lang):
        self.lang_menu.append([tk.StringVar()])
        self.lang_menu[-1][0].set(lang)
        self.lang_menu[-1].append(tk.OptionMenu(frame, self.lang_menu[-1][0], 
            *self.lang_list))
        self.lang_menu[-1][1].configure(font='Arial 14', bg=self.textcolor2,
            activebackground=self.textcolor1)
        self.lang_menu[-1][1]['menu'].configure(bg=self.textcolor1, font='Arial 14')

        self.lang_menu[-1].append(tk.Text(frame, font='Arial 18', width=60,
            bg=self.textcolor1))
        
        self.lang_menu[-1][1].grid(row=len(self.lang_menu), column=0)
        self.lang_menu[-1][2].grid(row=len(self.lang_menu), column=1)
        #self.lang_check[lang][1].pack(side='top')
        #self.lang_check[lang][2].pack(side='right')
        self.botframe.rowconfigure(len(self.lang_menu), weight=1)
        self.lang_menu[-1][1].configure(bg=self.bgcolor)

    def translate_word(self, event=None):
        translations = [self.tr_obj.translate(self.entry.get(), dest=self.lang_menu[i][0].get(), 
            src=self.src.get())
                if self.lang_menu[i][0].get()
                else -1
                for i in range(len(self.lang_menu))]
        
        for i in range(len(self.lang_menu)):
            if translations[i] != -1:
                if translations[i].dest in ['he', 'ar']:
                    display_text = translations[i].text[::-1]
                else:
                    display_text = translations[i].text
                self.lang_menu[i][2].replace('1.0', tk.END, display_text)

if __name__ == '__main__':

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

