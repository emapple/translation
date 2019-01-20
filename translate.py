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
        self.create_widgets()

    def create_widgets(self):
        self.topframe = tk.Frame(self)
        self.topframe.pack(side='top', fill='x')
        self.botframe = tk.Frame(self)
        self.botframe.pack(side='bottom', fill='both')
        self.topframe.configure(bg=self.bgcolor)
        self.botframe.configure(bg=self.bgcolor)

        self.l1 = tk.Label(self.topframe, text='Word to translate:',
                font='Arial 18')
        self.l1.grid(row=0, column=0, ipadx=50)
        self.entry = tk.Entry(self.topframe, font='Courier 18')
        self.entry.grid(row=0, column=1)
        self.entry.configure(bg=self.textcolor1)
        self.l1.configure(bg=self.bgcolor)

        self.b1 = tk.Button(self.topframe, text='Translate!', command=self.translate_word,
                 font='Arial 18')
        self.b1.grid(row=0, column=2, padx=10)
        self.b1.configure(bg=self.bgcolor)

        self.lang_check = {}
        self.make_checkbox(self.botframe, 'es')
        self.make_checkbox(self.botframe, 'it')
        self.make_checkbox(self.botframe, 'fr')
        self.make_checkbox(self.botframe, 'he')
        #for lang in self.lang_check:
        #    self.lang_check[lang][1].pack()
        
        for i, lang in enumerate(self.lang_check):
            self.botframe.rowconfigure(i+1, weight=1)
            self.lang_check[lang][1].configure(bg=self.bgcolor)

    def make_checkbox(self, frame, lang):
        self.lang_check[lang] = [tk.IntVar()]
        self.lang_check[lang][0].set(1)
        self.lang_check[lang].append(tk.Checkbutton(frame, text=lang, font='Arial 14', \
                variable=self.lang_check[lang][0], onvalue=1, offvalue=0, height=5, \
                width=5))

        self.lang_check[lang].append(tk.Text(frame, font='Arial 18', width=60,
            bg=self.textcolor1))
        
        self.lang_check[lang][1].grid(row=len(self.lang_check), column=0)
        self.lang_check[lang][2].grid(row=len(self.lang_check), column=1)
        #self.lang_check[lang][1].pack(side='top')
        #self.lang_check[lang][2].pack(side='right')

    def translate_word(self):
        translations = [self.tr_obj.translate(self.entry.get(), dest=lang)
                if self.lang_check[lang][0].get()
                else -1
                for lang in self.lang_check]
        
        for i, lang in enumerate(self.lang_check):
            if translations[i] != -1:
                if lang is 'he':
                    display_text = translations[i].text[::-1]
                else:
                    display_text = translations[i].text
                self.lang_check[lang][2].replace('1.0', tk.END, display_text)

if __name__ == '__main__':

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
