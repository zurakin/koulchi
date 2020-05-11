import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import avito, jumia
import webbrowser, os, time
from datetime import datetime

width = 1000
height = 300

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

def get_file_name(item):
    name = item.replace(' ', '_')+' '
    now = datetime.now()
    name += now.strftime('%H.%M %d.%h.%y')
    name += '.html'
    return name

def search():
    item = textWidgets['searchBar'].get('1.0',tk.END).strip()
    textWidgets['searchBar'].delete('1.0', tk.END)
    textWidgets['searchBar'].insert(tk.END, 'What are you looking for?')
    city = textWidgets['city'].get('1.0', tk.END).strip()
    try:
        min = int(textWidgets['min'].get('1.0', tk.END).strip())
    except:
        min = 0
    try:
        max = int(textWidgets['max'].get('1.0', tk.END).strip())
    except:
        max = 1000000
    avito_check = checkboxes['avito'][1].get()
    jumia_check = checkboxes['jumia'][1].get()
    boutika_check = checkboxes['boutika'][1].get()
    ubuy_check = checkboxes['ubuy'][1].get()
    result = []
    if avito_check:
        url = avito.get_url(item, city)
        shL = avito.scrape(url, min, max)
        result.extend(shL)
    if jumia_check:
        url = jumia.get_url(item, min, max)
        shL = jumia.scrape(url)
        result.extend(shL)
    return item, result


def search_show(event=None):
    item, result=search()
    df = pd.DataFrame(result)
    df['link'] = df['link'].apply(lambda x: f'<a href="{x}" target="_blank">link here</a>')
    if not os.path.exists('temp'):
        os.mkdir('temp')
    df.to_html('temp\\'+get_file_name(item), escape=False, render_links=True)
    webbrowser.open('temp\\'+get_file_name(item))
    time.sleep(1)
    os.remove('temp\\'+get_file_name(item))


def search_save(event=None):
    item, result=search()
    df = pd.DataFrame(result)
    if not os.path.exists('searches'):
        os.mkdir('searches')
    df.to_html('searches\\'+get_file_name(item))

def add_text(name,row, column, width=None, font=F1,  default=None, colspan = 1, textColor=textColor):
    global textWidgets
    if width!=None:
        tw=tk.Text(root,height=1,width=width, font=font)
    else:
        tw=tk.Text(root,height=1, font=font)
    textWidgets[name] = tw
    tw.bind('<Return>', search_show)
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

def sb_clicked(event):
    if textWidgets['searchBar'].get('1.0',tk.END).strip()=='What are you looking for?':
        textWidgets['searchBar'].delete('1.0', tk.END)
add_text(name='searchBar',row=0, column=1, colspan=4, width='40',
    default='What are you looking for?')
textWidgets['searchBar'].bind("<Button-1>",sb_clicked)

add_label('source', 'Source: ', 1, 0)

add_checkbox('avito', 'avito', 1, 1)
add_checkbox('jumia', 'jumia', 1, 2)
add_checkbox('boutika', 'boutika', 1, 3)
add_checkbox('ubuy', 'ubuy', 1,4)

add_label('city', 'City: ', 2, 0)
add_text(name='city',row=2,column=2, colspan=1,width=10, font=F1,default='Maroc',textColor='#6C5B7B')

add_label('price', 'Price Filter: ', 3, 0)
add_label('-', '-', 3, 2)

def min_clicked(event):
    if textWidgets['min'].get('1.0',tk.END).strip()=='Min':
        textWidgets['min'].delete('1.0', tk.END)
add_text('min', row=3, column=1, colspan=1, width=10, default='Min')
textWidgets['min'].bind("<Button-1>",min_clicked)

def max_clicked(event):
    if textWidgets['max'].get('1.0',tk.END).strip()=='Max':
        textWidgets['max'].delete('1.0', tk.END)
add_text('max', 3, 3, width=10, default='Max')
textWidgets['max'].bind("<Button-1>",max_clicked)


add_button('search_show', 'Search & Show', search_show, 4, 1)

add_button('search_save', 'Search & Save', search_save, 4, 2)

root.mainloop()
