import numpy as np
import pandas as pd


class poonsataiiGame:
    def __init__(self):
        self.PATH = "poonsataii.txt"
        self.scores = pd.read_csv(self.PATH, index_col="Round")
    
    def setup(self):
        print("Here is your game history:")
        print(self.scores)

    def getinput(self):
        user_input = input("Press E to enter score, or V to view past scores. ")
        while user_input != "E" and user_input != "V":
            user_input = input("Press E to enter score, or V to view past scores. ")
        if user_input == "V":
            print("Here are your scores:")
            print(self.scores)
            self.getinput()
            return
        if user_input == "E":
            danielleScore = input("How many points did Danielle get that round? ")
            mooseManScore = input("How many points did Moose get that round? ")
            adamScore = input("How many points did Adam get that round? ")
            if danielleScore.isnumeric() and mooseManScore.isnumeric() and adamScore.isnumeric():
                self.scores = self.scores.append({"Moose": int(mooseManScore), "Adam": int(adamScore), "Danielle": int(danielleScore)}, ignore_index=True)
                self.scores.to_csv(self.PATH)
                self.getinput()
                return
            else:
                print("Please enter valid scores")
                self.getinput()
                return
    def run(self):
        self.setup()
        self.getinput()




if __name__ == "__main__":
    pg = poonsataiiGame()
    pg.run()