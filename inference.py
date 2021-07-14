import pickle
from flask import Flask
from flask import request
import os

app = Flask(__name__)
model = pickle.load(open("churn_model.pkl", "rb"))

@app.route("/")
def hello():
    return "<p>hello</p>"

@app.route("/predict_churn", methods=["GET"])
def get_prediction():
    global model
    is_male = request.args.get("is_male")
    num_inters = request.args.get("num_inters")
    late_on_payment = request.args.get("late_on_payment")
    age = request.args.get("age")
    years_in_contract = request.args.get("years_in_contract")
    request_data = [[is_male, num_inters, late_on_payment, age, years_in_contract]]
    print(request_data)    
    return str(model.predict(request_data)[0])


# Running from pycharm the code instead of terminal
if __name__ == "__main__":
    print(model)

    port = os.environ.get('PORT')
    if port:
        app.run(host="0.0.0.0", port=int(port))
    else:
        app.run()

