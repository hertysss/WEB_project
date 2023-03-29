from flask import Flask, render_template
from flask_login import current_user


app = Flask(__name__)


@app.route('/login')
def login():
    """Возварщает шаблон авторизации"""
    return render_template('auth.html')


@app.route('/reg')
def reg():
    """Возварщает шаблон регистриции"""
    return render_template('reg.html')


@app.route('/logout')
@app.route('/')
def index():
    """Возварщает шаблон главной страницы"""
    return render_template('index.html', current_user=current_user)


def main():
    app.run()


if __name__ == '__main__':
    main()