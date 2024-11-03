# app.py

from flask import Flask, render_template, request
from operation import add, subtract, multiply, divide, power, sqrt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form.get('num1', 0))
    num2 = float(request.form.get('num2', 0))
    operation = request.form.get('operation')
    result = None

    # Use the appropriate function based on the operation
    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    elif operation == 'power':
        result = power(num1, num2)
    elif operation == 'sqrt':
        result = sqrt(num1)

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=False)
