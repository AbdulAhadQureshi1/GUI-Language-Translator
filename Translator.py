from googletrans import Translator, LANGUAGES
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('1420x400')
root.title('Translator- By Abdul Ahad')
root.resizable(0,0)
root.config(bg = '#1C2833')

def Translate():
    translator = Translator()
    translated = translator.translate(text=input_text.get(1.0, END), src = src_lang.get(), dest = dest_lang.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)


style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#D4DE33", background= "#566573")

Label(root, text='INPUT', font = 'arial 20 bold',bg='#1C2833',fg ='#D4DE33').place(x=30,y=60)
input_text = Text(root, font='arial', height = 11, wrap = WORD, padx = 5, pady = 5, width = 60,borderwidth='2',bg='#808B96',border=0)
input_text.place(x=30,y=150)


Label(root, text='OUTPUT', font = 'arial 20 bold',bg='#1C2833',fg ='#D4DE33').place(x=780,y=60)
output_text = Text(root, font='arial', height = 11, wrap = WORD, padx = 5, pady= 5, width = 60,borderwidth='2',bg='#808B96',border=0)
output_text.place(x=780,y=150)


language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values = language,width='22',height='10',font = 'Calibri 12')
src_lang.place(x=30, y=100)
src_lang.set('Choose input language')


dest_lang = ttk.Combobox(root, values=language,width='22',height='10',font = 'Calibri 12')
dest_lang.place(x=780,y=100)
dest_lang.set('Choose output language')


Button(root, text="TRANSLATE", font='arial 16 bold',padx=10,pady=10,relief='groove',fg='#1C2833',command = Translate,bg ='#D4DE33',borderwidth=0).place(x=600,y=210)


root.mainloop()