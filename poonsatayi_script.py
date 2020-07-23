import numpy as np
import pandas as pd

class poonsataiiGame:
    def __init__(self):
        self.PATH = "poonsataii.txt"
        self.scores = pd.read_csv(self.PATH, index_col="Round")
        self.totals = {'D': 0, 'M': 0, 'A': 0}
        self.deltas = {'D': 0, 'M': 0, 'A': 0}
    
    def initTotals(self):
        d = self.scores['Danielle'].sum()
        m = self.scores['Moose'].sum()
        a = self.scores['Adam'].sum()
        self.totals['D'] = d
        self.totals['M'] = m
        self.totals['A'] = a

    def incTotals(self):
        self.totals['D'] += self.deltas['D']
        self.totals['M'] += self.deltas['M']
        self.totals['A'] += self.deltas['A']

    def setDeltas(self, d, m, a):
        self.deltas['D'] = d
        self.deltas['M'] = m
        self.deltas['A'] = a
    
    def setup(self):
        self.initTotals()
        print("Here is your game history:")
        print(self.scores)

    def getinput(self):
        user_input = input("Press E to enter score, or V to view past scores. ").upper()
        while user_input != "E" and user_input != "V":
            user_input = input("Press E to enter score, or V to view past scores. ")
        if user_input == "V":
            print("Here are your scores so far:")
            print(self.scores)
            print("Here are the current totals:")
            for key in self.totals:
                print(key, self.totals[key])
            self.getinput()
            return
        if user_input == "E":
            danielleScore = input("How many points did Danielle get that round? ")
            mooseManScore = input("How many points did Moose get that round? ")
            adamScore = input("How many points did Adam get that round? ")
            if danielleScore.isnumeric() and mooseManScore.isnumeric() and adamScore.isnumeric():
                mScore = int(mooseManScore)
                aScore = int(adamScore)
                dScore = int(danielleScore)
                self.setDeltas(dScore, mScore, aScore)
                self.incTotals()
                self.scores = self.scores.append({"Moose": mScore, "Adam": aScore, "Danielle": dScore}, ignore_index=True)
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