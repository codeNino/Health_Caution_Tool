import joblib
import numpy as np
import warnings

warnings.filterwarnings('ignore')

class PatientData:

    def __init__(self, Age: int, BMI: float, BloodPressure: float, GlucoseLevel : float, Pregnancy: int = 0):
        self.age = Age
        self.bmi = BMI
        self.bp = BloodPressure
        self.glucose = GlucoseLevel
        self.pregnancy = Pregnancy 
        


class Prediction:

    def __init__(self, confidence: float, prediction: int):
        if prediction == 0:
            self.category = "Non-Diabetic"
            self.comment = f"Your Health data suggests you are {self.category} with a \
             {100 - int(round(confidence[0]*100,0))}% confidence of being otherwise."
        else:
            self.category = "Diabetic"
            self.comment = f"Your Health data suggests you are {self.category} with a \
             {round(confidence[1]*100,1)}% confidence."




class DiabetesPredictor:

    model = joblib.load("diabetesModel.pkl")

    @staticmethod
    def classify(data: PatientData):  

        user_input =   np.array([data.pregnancy, data.glucose, data.bp, data.bmi, data.age])

        prediction = DiabetesPredictor.model.predict(user_input.reshape(1,-1))[0]
        confidence = DiabetesPredictor.model.predict_proba(user_input.reshape(1,-1))[0]

           
        return Prediction(confidence, prediction)
        