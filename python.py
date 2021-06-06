import random
import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

dice = []
count = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice.append(dice1 + dice2)
    count.append(i)
df = []
fig = ff.create_distplot([dice], ["result"])
fig.show()

