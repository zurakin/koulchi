import tkinter as tk
import tkinter.font as tkFont

width = 1000
height = 380

#colors
bgColor = '#F8B195'
textColor = '#6C5B7B'
checkBoxColor = '#F67280'
# checkBoxColor = '#C06C84'
ButtonColor = '#C06C84'




root = tk.Tk()

#Fonts
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

def add_label(name, text, row, column, font=F1, textCOlor=textColor):
    lbl=tk.Label(root,text=text, font=font, bg=bgColor)
    lbl.grid(row=row,column=column)
    labels[name]=lbl

def add_checkbox(name, text, row, column):
    var = tk.IntVar()
    box = tk.Checkbutton(root, text=text, variable=var, font=F2)
    box.configure(bg=checkBoxColor)
    box.grid(row=row, column = column)
    box.select()
    checkboxes[name]=[box, var]

def add_button(name, text, command, row, column):
    b=tk.Button(root,text=text,command=command, height=4, width=20, bg=ButtonColor, font=F2)
    b.grid(row=row,column=column, columnspan=2)
    buttons[name] = b

labels = {}
textWidgets = {}
checkboxes = {}
buttons = {}

add_text(name='searchBar',row=0, column=1, colspan=4, width='40',
    default='What are you looking for?')

add_label('source', 'Source: ', 1, 0)

add_checkbox('avito', 'avito', 1, 1)
add_checkbox('jumia', 'jumia', 1, 2)
add_checkbox('boutika', 'boutika', 1, 3)
add_checkbox('ubuy', 'ubuy', 1,4)

add_label('city', 'City: ', 2, 0)
add_text(name='city',row=2,column=2, colspan=1,width=10, font=F1,default='Maroc',textColor='#6C5B7B')

add_label('price', 'Price Filter: ', 3, 0)
add_label('-', '-', 3, 2)

add_text('min', row=3, column=1, colspan=1, width=10, default='Min')
add_text('max', 3, 3, width=10, default='Max')


def search_show():
    pass
add_button('search_show', 'Search & Show', search_show, 4, 1)

def search_save():
    pass
add_button('search_save', 'Search & Save', search_save, 4, 2)

root.mainloop()
