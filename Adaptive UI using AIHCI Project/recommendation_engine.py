import pandas as pd

class TrainingRecommender:

    def __init__(self):
        self.data = pd.read_csv("training_data.csv")

    def recommend(self, skill):

        result = self.data[
            self.data["Skill"].str.lower() ==
            skill.lower()
        ]

        if result.empty:
            return ["No recommendations found"]

        recommendations = result.iloc[0]["Recommendations"]

        return recommendations.split(";")
