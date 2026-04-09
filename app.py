from flask import Flask, render_template, request
import random

app = Flask(__name__)

def calcular_pi(n):
    dentro = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            dentro += 1
    return 4 * dentro / n

@app.route('/', methods=['GET', 'POST'])
def index():
    pi = None
    if request.method == 'POST':
        n = int(request.form['iteraciones'])
        pi = calcular_pi(n)
    return render_template('index.html', pi=pi)

if __name__ == '__main__':
    app.run(debug=True)
