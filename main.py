import warnings
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from bmi_calculator import BMICalculator as calc
from diabetes_predictor import DiabetesPredictor as AI, PatientData


app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(24), nullable=False)
    lastname = db.Column(db.String(24), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False, unique=True)

    def __repr__(self):
        return f"Register('{self.firstname}', '{self.lastname}', '{self.email}', '{self.password}')"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template("registration.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        user = Register(firstname=firstname, lastname=lastname, email=email, password=password)
        db.create_all()
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("registration.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        login = Register.query.filter_by(email=email, password=password).first()
        if login is not None:
            return render_template('welcome.html')
    return render_template("registration.html")

# @app.route('/status1', methods=['GET', 'POST'])
# def status():
#     return render_template("status.html")

@app.route('/status', methods=['GET', 'POST'])
def run_prediction():
    if request.method == 'POST':
        # if request.form['status']== 'predict':
        formData = request.form.to_dict()

        bmi = calc.getBMI(float(formData["weight"]), float(formData["height"]))

        model_input = PatientData(
                Age= int(formData["age"]), BMI= bmi,
                BloodPressure= float(formData["bloodpressure"]),
                GlucoseLevel= float(formData["glucose"])
            )

        BMIVerdict = calc.categorize(bmi)
        DiabetesVerdict = AI.classify(model_input)

        return render_template("verdict.html", BMIVerdict=BMIVerdict, DiabetesVerdict=DiabetesVerdict)

    return render_template("status.html")


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app.run(debug=True)