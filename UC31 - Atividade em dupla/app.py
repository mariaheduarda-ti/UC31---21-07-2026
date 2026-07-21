from flask import Flask, render_template, session, redirect
from datetime import datetime

app = Flask(__name__)

app.secret_key = "123"

@app.route('/')
def inicio():

    if 'brasil' not in session:
        session['brasil'] = 0

    if 'argentina' not in session:
        session['argentina'] = 0

    if 'franca' not in session:
        session['franca'] = 0

    if 'espanha' not in session:
        session['espanha'] = 0

    placar = {
        'Brasil': session['brasil'],
        'Argentina': session['argentina'],
        'França': session['franca'],
        'Espanha': session['espanha']
    }

    lider = max(placar, key=placar.get)

    total = (
        session['brasil']
        + session['argentina']
        + session['franca']
        + session['espanha']
    )

    data = datetime.now().strftime("%d/%m/%Y")

    return render_template(
        'index.html',
        brasil=session['brasil'],
        argentina=session['argentina'],
        franca=session['franca'],
        espanha=session['espanha'],
        lider=lider,
        total=total,
        data=data
    )


@app.route('/ponto/<time>')
def ponto(time):

    if time in session:
        session[time] += 1

    return redirect('/')


@app.route('/zerar')
def zerar():

    session['brasil'] = 0
    session['argentina'] = 0
    session['franca'] = 0
    session['espanha'] = 0

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)