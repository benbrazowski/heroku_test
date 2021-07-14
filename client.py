import pandas as pd
import numpy as np
import requests
from github import Github

REPO_NAME = "HerokuTest"

# server_url = "http://localhost:5000/predict_churn"
server_url = "https://vert-monsieur-76492.herokuapp.com/predict_churn"
github = Github()

repository = github.get_user().get_repo(REPO_NAME)

data = pd.read_csv("x_test.csv")
preds = np.loadtxt("preds.csv")

for index, row in data.iterrows():
    responsive = requests.get(server_url,
                              params={"is_male": int(row["is_male"]),
                                      "num_inters": int(row["num_inters"]),
                                      "late_on_payment": int(row["late_on_payment"]),
                                      "age": int(row["age"]),
                                      "years_in_contract": row["years_in_contract"]})

    # Checks if the response is ok
    if str(int(preds[index])) == responsive.text:
        print(f"Good Prediction on row : {index}")
    else:
        print(f"Issues with prediction in row: {index}")

    # exit the code after 5 iterations.
    if index == 4:
        break
