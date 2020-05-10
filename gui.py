import tkinter as tk
import tkinter.font as tkFont

width = 1280
height = 720

#colors
bgColor = '#F8B195'
textColor = '#6C5B7B'
checkBoxColor = '#F67280'
# checkBoxColor = '#C06C84'
ButtonColor = '#C06C84'




root = tk.Tk()
F1 = tkFont.Font(family="Arial Black", size=20)
F2 = tkFont.Font(family="Baskerville", size=15)
root.configure(bg = bgColor)
root.title('Koulchi')
root.geometry(f'{width}x{height}')

def add_text(name,row, column, width=None, font=F1,  default=None, colspan = 1, textColor=textColor):
    global textWidgets
    if width!=None:
        tw=tk.Text(root,height=1,width=width, font=font)
    else:
        tw=tk.Text(root,height=1, font=font)
    textWidgets[name] = default
    tw.grid(row=row,column=column, columnspan = colspan)
    if default!=None:
        tw.insert(tk.END,default)
        tw.configure(fg=textColor)

textWidgets = {}

add_text(name='searchBar',row=0, column=1, colspan=4, width='40',
    default='What are you looking for?')


srcLabel=tk.Label(root,text="Source: ", font=F1, bg=bgColor)
srcLabel.grid(row=1,column=0)

avitoCheck = tk.IntVar()
avito = tk.Checkbutton(root, text="Avito", variable=avitoCheck, font=F2)
avito.configure(bg=checkBoxColor)
avito.grid(row=1, column = 1)
avito.select()

jumiaCheck = tk.IntVar()
jumia = tk.Checkbutton(root, text="Jumia", variable=jumiaCheck, font=F2)
jumia.configure(bg=checkBoxColor)
jumia.grid(row=1, column = 2)
jumia.select()

boutikaCheck = tk.IntVar()
boutika = tk.Checkbutton(root, text="Boutika", variable=boutikaCheck, font=F2)
boutika.configure(bg=checkBoxColor)
boutika.grid(row=1, column = 3)
boutika.select()

ubuyCheck = tk.IntVar()
ubuy = tk.Checkbutton(root, text="Ubuy", variable=ubuyCheck, font=F2)
ubuy.configure(bg=checkBoxColor)
ubuy.grid(row=1, column = 4)
ubuy.select()

city=tk.Text(root,height=1,width=20, font=F1)
city.grid(row=2,column=2, columnspan=2)
city.insert(tk.END,'Maroc')
city.configure(fg='#6C5B7B')

priceLabel=tk.Label(root,text="Price Filter: ", font=F1, bg=bgColor)
priceLabel.grid(row=3,column=0)



root.mainloop()
