import PWGen
import tkinter as tk

def generate():
    lblPasswort.configure(text = PWGen.pwgenPro(int(inNumCap.get()), int(inNumLow.get()), int(inNumDigits.get()), int(inNumSpecs.get()), inNoChar.get()))

def copyClipboard():
    lblPasswort.clipboard_clear()
    lblPasswort.clipboard_append(lblPasswort.cget('text'))

root = tk.Tk()
root.title('Passwortgenerator')
root.geometry('400x800')
root.resizable(False, False)

# Create Widgets

# Label für Eingabe Anzahl Großbuchstaben
lblNumCap = tk.Label(master=root, text='Anzahl Zeichen', font=('Arial Black', 10),bg='RED')
# Eingabefeld Anzahl Großbuchstaben
inNumCap = tk.Entry(root)
# Label für Eingabe Anzahl Kleinbuchstaben
lblNumLow = tk.Label(master=root, text='Anzahl Zeichen', font=('Arial Black', 10),bg='RED')
# Eingabefeld Anzahl Kleinbuchstaben
inNumLow = tk.Entry(root)
# Label für Eingabe Anzahl Zahlen
lblNumDigits = tk.Label(master=root, text='Anzahl Zeichen', font=('Arial Black', 10),bg='RED')
# Eingabefeld Anzahl Zahlen
inNumDigits = tk.Entry(root)
# Label für Eingabe Anzahl Sonderzeichen
lblNumSpecs = tk.Label(master=root, text='Anzahl Zeichen', font=('Arial Black', 10),bg='RED')
# Eingabefeld Anzahl Sonderzeichen
inNumSpecs = tk.Entry(root)
# Label für Eingabe Ausschlusszeichen
lblNoChar = tk.Label(master=root, text='Auschlusszeichen', font=('Arial Black', 10),bg='RED')
# Eingabefeld Ausschlusszeichen
inNoChar = tk.Entry(root)
# Ausgabe des Passworts (Label)
lblPasswort = tk.Label(master=root, text='Passwort', font=('Arial Black', 20),bg='RED')
# Button zum Generieren
btnGen = tk.Button(master=root, text='Generiere', font=('Arial Black', 10), command = generate)
# Button zum Kopieren in die Zwischenablage
btnGenCopy = tk.Button(master=root, text='Kopiere in Zwischenablage', font=('Arial Black', 10), command = copyClipboard)

# Layout Widgets
# pack()- Methode

# lblNum.pack(pady=10)
# inNum.pack()
# lblNoChar.pack(pady=10)
# inNoChar.pack()
# lblPasswort.pack(pady=10)
# btnGen.pack()
# btnGenCopy.pack(pady=10)

# grid()- Methode

# lblNum.grid(row=0, column=0, padx=10, pady=10, sticky='w')
# inNum.grid(row=0, column=1, padx=10, pady=10, sticky='w')
# lblNoChar.grid(row=1, column=0, padx=10, pady=10, sticky='w')
# inNoChar.grid(row=1, column=1, padx=10, pady=10, sticky='w')
# btnGen.grid(row=2, column=0, padx=10, pady=10, sticky='w')
# lblPasswort.grid(row=3, column=0, padx=10, pady=10, sticky='w', columnspan=2)
# btnGenCopy.grid(row=4, column=0, padx=10, pady=10, sticky='w')

# place() - Methode

lblNumCap.place(x=30, y=30)
inNumCap.place(x=200, y=30, width=150)
lblNoChar.place(x=30, y=80)
inNoChar.place(x=200, y=80, width=150)
lblPasswort.place(x=30, y=150, width=340, height=100)
btnGen.place(x=30, y=280, width=100, height=50)
btnGenCopy.place(x=150, y=280, width=220, height=50)

root.mainloop()

