from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators

app = Flask(__name__)

# Model
class InputForm(Form):
    a = FloatField(validators=[validators.InputRequired()])
    b = FloatField(validators=[validators.InputRequired()])
    p = FloatField(validators=[validators.InputRequired()])
    q = FloatField(validators=[validators.InputRequired()])
	
# View
@app.route('/hw2', methods=['GET', 'POST'])
def index():
    s = None
    t = None
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate() and \
        request.form['btn'] == 'add':
        s = form.a.data + form.b.data
    elif request.method == 'POST' and form.validate() and \
        request.form['btn'] == 'multiply':
        t = form.p.data * form.q.data
    else:
        s = None
        t = None

    return render_template("view.html", form=form, s=s)
    return render_template("view.html", form=form, t=t)

if __name__ == '__main__':
    app.run(debug=True)
