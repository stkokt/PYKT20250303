import tkinter as tk
import PWGen

def generate():
    lblPassword.configure(text=PWGen.pwgenSimple(int(inNum.get()), inNoChar.get()))

def copyClipboard():
     lblPassword.clipboard_clear()
     lblPassword.clipboard_append(lblPassword.cget('text'))

root=tk.Tk()
root.title('Passwortgenerator')
root.geometry('400x400')
root.resizable(False,False)

# Create Widgets
lblNum = tk.Label(root, bg='RED', text='Anzahl Zeichen:', font=('Arial Black', 10))
inNum = tk.Entry(root)
lblNoChar = tk.Label(root, bg='RED', text='aber ohne:', font=('Arial Black', 10))
inNoChar = tk.Entry(root)
lblPassword=tk.Label(root, bg='RED', text="Passwort",font=('Helvetica', 25))
btnGen = tk.Button(root, text="Generieren", command=generate)
btnGenCopy=tk.Button(root, text="Copy to Clipboard", command=copyClipboard)


# Layout Widgets
# Pack()- Methode

# lblNum.pack()
# inNum.pack()
# lblNoChar.pack()
# inNoChar.pack()
# btnGen.pack()
# lblPassword.pack()
# btnGenCopy.pack()

# Grid- Methode

# lblNum.grid(row=0, column=0, padx=10, pady=10, sticky='e')
# inNum.grid(row=0, column=1, padx=10, pady=10)
# lblNoChar.grid(row=1, column=0, padx=10, pady=10, sticky='e')
# inNoChar.grid(row=1, column=1, padx=10, pady=10)
# btnGen.grid(row=2, column=1, columnspan=2, pady=10)
# lblPassword.grid(row=3, column=1, columnspan=2, pady=10)
# btnGenCopy.grid(row=4, column=1, columnspan=2, pady=10)

lblNum.place(relx=0.15, rely=0.3)
inNum.place(relx=0.45, rely=0.3)


root.mainloop()