from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from turtle import bgcolor


compiler = Tk()
compiler.title('CodeX - Code at Your Fingers Mr Programmer')
file_path = ''
#Set Screen Resoulution
compiler.geometry("1920x1080")
#Bg Color Of the Tkinter Window
compiler.configure(bg='#222')



def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)


menu_bar = Menu(compiler)

file_option= Menu(menu_bar, tearoff=0)
file_option.add_command(label='Open', command=open_file)
file_option.add_command(label='Save', command=save_as)
file_option.add_command(label='Save As', command=save_as)
file_option.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_option)

run_btn = Menu(menu_bar, tearoff=0)
run_btn.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_btn)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()