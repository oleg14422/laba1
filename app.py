from flask import Flask, request, render_template, make_response
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    history = request.cookies.get('history')
    if history is None:
        history = ''
    print(type(history))
    if request.method == 'POST':

        text = request.form['textfield']
        try:
            print(text)
            result = eval(text)
            history += str(result) + '\n'
        except:
            error = 'неправильний вираз'
            print('Неправильний вираз')
            return render_template('home.html', error=error)

        response = make_response(render_template('home.html', history=history))
        response.set_cookie('history', history)
        print(history)
        return response

    if request.method == 'GET':
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)