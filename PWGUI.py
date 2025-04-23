import tkinter as tk
import PWGen

def generate():
    pass
#variable, die den rahmen für das gibt wie root = wird von Funktion tk belegt 

root = tk.Tk()
# öffnet Fenster und mainloop hältfenster offen alles andere findet zwischen den beiden aufrufen statt
# Defaultgrösse festlegen
# titel angeben
root.title('Passwortgenerator')
root.geometry('400x400')
root.resizable(False, False)  
                #def resizable(width: None = None,height: None = None) -> tuple[bool, bool]
                #Instruct the window manager whether this width can be resized
                # in WIDTH or HEIGHT. Both values are boolean values.
                # false sperrt in beide Richtungen
                # root.minsize() würde minimalgrösse festlegen
# Label für Eingabe Anzahl Zeichen
lblNum = tk.Label(master=root, text='Anzahl Zeichen', font=('Arial Black',10), bg='RED')

# Eingabefeld Anzahl Zeichen
inNum = tk.Entry(root)
# Label für Eingabe Ausschlusszeichen
lblNoChar = tk.Label(master=root, text='Ausschlusszeichen', font=('Arial Black',10), bg='RED')
# Eingabefeld Ausschlusszeichen
inNoChar = tk.Entry(root)
# Ausgabe des Passworts (Label (Schriftzug auf Oberfläche))
lblPasswort = tk.Label(master=root, text='Passwort', font=('Arial Black',10), bg='YELLOW')
# Button zum Generieren
btnGen  = tk.Button(master=root, text='Generiere_PW', font=('Arial Black',10), command = generate)
# Button zum Kopieren in Zwischenablage
btnGenCopy  = tk.Button(master=root, text='Kopiere_in_Zwischenablage', font=('Arial Black',10))
# Layout Widgets
# pack()-Methode zeigt Label auf Bildschirmfenster an
lblNum.pack(pady=10) 
inNum.pack()  
#pady macht Abstand v einer Zeile nach oben und unten von 10 auf y achse
lblNoChar.pack(pady=10) 
inNoChar.pack() 

root.mainloop()