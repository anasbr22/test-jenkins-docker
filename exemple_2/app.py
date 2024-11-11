import tkinter as tk

# logique de calcul
class CalculatorLogic:
    def __init__(self):
        self.result = ""

    def reset(self):
        self.result = ""

    def calculate(self):
        try:
            self.result = str(eval(self.result))
        except Exception:
            self.result = "Erreur"

    def append(self, text):
        self.result += text

    def get_result(self):
        return self.result


# Classe qui gère l'interface graphique
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice")
        self.root.geometry("400x600")

        # Initialisation de la logique de calcul
        self.logic = CalculatorLogic()
        self.result_var = tk.StringVar()

        # Création de l'affichage du résultat
        self.result_display = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="sunken", justify="right")
        self.result_display.grid(row=0, column=0, columnspan=4)

        # Définition des boutons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0, 2), ('Exit', 5, 2, 2)
        ]

        # Création dynamique des boutons
        for button in buttons:
            if len(button) == 3:
                text, row, col = button
                self.create_button(text, row, col)
            elif len(button) == 4:
                text, row, col, colspan = button
                self.create_button(text, row, col, colspan)

    def create_button(self, text, row, col, colspan=1):
        button = tk.Button(self.root, text=text, font=("Arial", 18), width=6, height=2, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, columnspan=colspan)

    def on_button_click(self, text):
        if text == "C":
            self.logic.reset()
        elif text == "=":
            self.logic.calculate()
        elif text == "Exit":
            self.root.quit()
        else:
            self.logic.append(text)

        # Met à jour l'affichage du résultat
        self.result_var.set(self.logic.get_result())

def run_calculator():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_calculator()
