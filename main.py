from flask import Flask,render_template, url_for
import json

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template("index.html", title=title)


@app.route('/training/<prof>')
def training(prof):
    prof = ('инженер' in prof or 'строитель' in prof)
    return render_template('trainer.html', prof=prof)


@app.route('/list_prof/<list_prof>')
def jobs(list_prof):
    param = dict()
    with open("jobs.json", "rt", encoding="utf8") as f:
        param['jobs'] = json.loads(f.read())
    if list_prof == 'ul':
        param['list_type'] = "ul"
    elif list_prof == 'ol':
        param['list_type'] = "ol"
    else:
        return render_template('wrong_param.html')
    return render_template('jobs.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')