#### Using pycharm IDE 
Install pycharm
Open the project

Install scikit learn

`
pip install scikit-learn
`

Run the script - 
    linear_equation_example.py
    
##Machine Learning
####Input data set - 

`
TRAIN_INPUT_X, TRAIN_OUTPUT_Y
`

####Training stage - 
sklearn.linear_model - LinearRegression

`
algorithm.fit(X=TRAIN_INPUT_X, y=TRAIN_OUTPUT_Y)
`

####Validation stage - not doing in this example

####Testing stage - 
Testing data - 
TEST_DATA_SET = [[10, 2]]
output prediction

`
output = algorithm.predict(X=TEST_DATA_SET)
`

####Example

`
Train input
[[7, 5], [4, 9], [6, 3], [7, 0], [2, 5], [3, 8]]
Train output
[17, 22, 12, 7, 12, 19]

Relation between input and out as below-

[7, 5] ->
2*5+7 = 17

coefficients - logic -> 
[1. 2.]

Actual input
[[10, 2]]
Actual output
[14.]

Output should be like below-

2*2+10 = 14
`

