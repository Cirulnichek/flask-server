from flask import Flask,render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template("index.html", title=title)


@app.route('/training/<prof>')
def training(prof):
    prof = ('инженер' in prof or 'строитель' in prof)
    return render_template('trainer.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')