class Category:

    def __init__(self, name: str, comment: str ="") -> None:
        self.name = name
        self.comment = comment


class BMICalculator:

    underweight = Category("Underweight",
        "Higher risks of Malnutrition, Osteoporosis (weak and brittle bones), \
        Hypothermia (abnormally low body temperature), \
        and Decreased Muscle Strength. " )

    normal = Category("Normal weight", "")

    overweight = Category("Overweight",
        'High risk of Heart diseases, Stroke, High Blood Pressure, Osteoarthritis (pain, swelling and reduced motion in joints) \
            Caner and Type 2 Diabetes')

    obesity = Category("Obese",
        'Severe risk of Heart diseases, Stroke, High Blood Pressure, Osteoarthritis (pain, swelling and reduced motion in joints) \
            Caner and Type 2 Diabetes')
    

    @staticmethod
    def getBMI(weight: int, height: int):
        return round(weight/(height**2),1)

    
    @staticmethod
    def categorize(bmi : int):
        if bmi < 18.5:
            return BMICalculator.underweight
        elif bmi == 18.5 or bmi <= 24.9:
            return BMICalculator.normal
        elif bmi == 25.0 or bmi <= 29.9:
            return BMICalculator.overweight
        else: 
            return BMICalculator.obesity
