from flask import Flask, request, jsonify

app = Flask(__name__)

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

# Initialisation de la logique de calcul
calc = CalculatorLogic()

@app.route('/')
def home():
    return "Bienvenue dans la calculatrice API! Utilisez /append, /calculate, et /reset pour les opérations."

@app.route('/append', methods=['POST'])
def append():
    data = request.json
    calc.append(data.get('input', ''))
    return jsonify(result=calc.get_result())

@app.route('/calculate', methods=['GET'])
def calculate():
    calc.calculate()
    return jsonify(result=calc.get_result())

@app.route('/reset', methods=['POST'])
def reset():
    calc.reset()
    return jsonify(message="Calculatrice réinitialisée.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
