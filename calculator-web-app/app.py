from flask import Flask, render_template, request
import re

app = Flask(__name__)

def safe_eval(expr):
    try:
        # Only allow numbers, operators, and decimal points
        if not re.match(r'^[0-9+\-*/.() ]+$', expr):
            return "Invalid input"
        result = eval(expr)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception:
        return "Error"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        expr = request.form.get('expression', '')
        result = safe_eval(expr)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)