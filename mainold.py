from flask import Flask
from flask import url_for, render_template, json

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_hard_password'

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired])
    password = PasswordField('Пароль', validators=[DataRequired])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/')
@app.route('/index')
def index():
    user = "Alex"
    return render_template('index.html', title="Моя главная страница", username=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)

@app.route('/image_sample')
def image():
    return '''<img src ="{}" alt="здесь должна быть картинка, но не нашлась">'''.format(url_for('static', filename='img/92.jpg'))


if __name__ == '__main__':
    app.run()