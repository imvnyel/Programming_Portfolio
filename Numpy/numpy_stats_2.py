import numpy as np 
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

survey_size = len(survey_responses)

total_ceballos = sum([1 for i in survey_responses if i == 'Ceballos'])
percentage_ceballos = 100* total_ceballos/survey_size
total_kerrigan = survey_responses.count('Kerrigan')
precentage_kerrigan = 100* total_kerrigan / survey_size

print(percentage_ceballos)
print(precentage_kerrigan)

possible_surveys = np.random.binomial(survey_size, .54, size=10000) / float(survey_size)

ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print(ceballos_loss_surveys)

N = float(7000)
large_survey = np.random.binomial(7000, .54, size=10000) / N
ceballos_loss_new = np.mean(large_survey < 0.5)
print(ceballos_loss_new)

plt.hist(possible_surveys, range=(0,1), bins=20)
plt.hist(ceballos_loss_new, range=(0,1), bins=20, color='yellow')
plt.show()




print(possible_surveys)