"""
Basic demo of using matplotlib.pyplot
"""

from matplotlib import pyplot as pp
from random import randint, uniform

# Useful functions (aka my ignorant model of daily weight change as a function of calories eaten)
MET = 2100  # metabolic constant, average calories burned per day
CAL_MIN = 1500  # minimum number of calories consumed per day
CAL_MAX = 4000  # maximum number of calories consumed per day
EFF_MIN = 0.1  # efficiency: percentage of calories that get converted into body weight
EFF_MAX = 0.4  # efficiency: percentage of calories that get converted into body weight
CA2LB = lambda c: c / 3500  # converts calories into pounds
# estimated weight change as a function of calories eaten and previous day's weight (rounded to nearest tenth of a pound)
LBDD = lambda w, c: w + round(uniform(EFF_MIN, EFF_MAX) * CA2LB(c - MET), 1)

initial_weight = 200  # starting weight (lbs) at beginning of 30 day period

# days 1-30 (x axis)
days = list(range(1, 31))

# calories: list of [number of days] random numbers between 1800 and 4000 calories
calories = [randint(CAL_MIN, CAL_MAX) for i in range(len(days))]

# weights: represents a function of calories eaten on the previous day
weights = [None] * len(days)
for i in range(len(days)):
    weights[i] = 200 if i == 0 else LBDD(weights[i - 1], calories[i])

fig, axis1 = pp.subplots()
axis2 = axis1.twinx()

axis1.plot(days, calories)
axis1.set_xlabel("Days")
axis1.set_ylabel("Calories Eaten")

axis2.plot(days, weights, "r")
axis2.set_ylabel("Weight")

pp.show()
