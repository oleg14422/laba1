from flask import Flask, request, render_template, make_response, redirect, url_for
from form import MyForm
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def home():
    history = request.cookies.get('history')
    if history is None:
        history = ''
    print(type(history))
    form = MyForm()
    if form.validate_on_submit():
        print('FORM IS VALID')

        text = str(form.text.data)
        try:
            print(text)
            result = eval(text)
            history += str(result) + '\n'
        except:
            error = 'неправильний вираз'
            return render_template('home.html', error=error, form=MyForm(formdata=None))

        response = make_response(render_template('home.html', history=history, form=MyForm(formdata=None)))
        response.set_cookie('history', history)
        print(history)
        return response

    print(3)
    print(history)
    return render_template('home.html', history=history, form=MyForm(formdata=None))

if __name__ == '__main__':
    app.run(debug=True)