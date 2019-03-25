from random import randint

# input data set
TRAIN_INPUT_X = list()
# output data set
TRAIN_OUTPUT_Y = list()

TRAIN_DATA_SET_LIMIT = 10
for i in range(6):
    c = randint(0, TRAIN_DATA_SET_LIMIT)
    x = randint(0, TRAIN_DATA_SET_LIMIT)
    # Linear equation
    # y = mx + c
    m = 2
    y = (m * x) + c
    TRAIN_INPUT_X.append([c, x])
    TRAIN_OUTPUT_Y.append(y)

print("Train input")
print(TRAIN_INPUT_X)
print("Train output")
print(TRAIN_OUTPUT_Y)

# machine learning algorithm
from sklearn.linear_model import LinearRegression

algorithm = LinearRegression(n_jobs=-1)
# training stage
algorithm.fit(X=TRAIN_INPUT_X, y=TRAIN_OUTPUT_Y)

TEST_DATA_SET = [[10, 2]]
# predict output form train model
output = algorithm.predict(X=TEST_DATA_SET)
# this is the factor/logic for processing each input data set with respect to output data set
# it is same as the equation which we use to create the data set
coefficients = algorithm.coef_

print("coefficients - logic -> ")
print(coefficients)

print("Actual input")
print(TEST_DATA_SET)
print("Actual output")
print(output)
