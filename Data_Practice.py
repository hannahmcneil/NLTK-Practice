import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data_file = 'sim-expanded_questionnaire.csv'
questionnaire = pd.read_csv(data_file, sep='\t')
column_names = questionnaire.columns.values
sorted_by_age = questionnaire.sort_values(['age'], ascending=True)
sorted_by_engagement = questionnaire.sort_values(['age'], ascending=True)
# sorted_by_age['age']: first column being the participant number and the second being the age, sorted in ascending order
# sorted_by_age: returns same thing as questionnaire, only the rows are sorted in ascending order of age
# Some interesing things to examine: Length or complexity of response, level of engagement, level of difficulty, time
sorted_by_age['engagement'].plot(kind='hist') # just an example, can also do bar graphs
plt.show()