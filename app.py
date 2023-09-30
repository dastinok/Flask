from flask import Flask
from flask import render_template, request



app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def get_index():  # put application's code here
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def get_login():
    if request.method == 'POST':
        name = request.form.get('name'),
        email = request.form.get('email')
        return f"Вы авторизовались {name}"
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
