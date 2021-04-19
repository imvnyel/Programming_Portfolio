import codecademylib
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')
average_calories = np.mean(calorie_stats)

print('Competitors Average Calories/Serving:')
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
median_calories = np.median(calorie_stats_sorted)
print('\nCompetitors Median Calories/Serving:')
print(median_calories)


# Find out nth Percentiles for range 5-100, set 5
percents = {}
for i in range(5, 100, 5):
  percents[i] = np.percentile(calorie_stats, i)

# List of all {percentiles: calories} > 60
greater_60 = [{x:percents[x]} for x in percents if percents[x] > 60]
greater_60.sort()
nth_percentile = greater_60[0].keys()

print('\nLowest Percentile with greater than 60 Calories:')
print(nth_percentile[0])


more_calories = np.mean(calorie_stats > 60)
print('\n{0:0.2f}% of our Competitors have more calories than ours'.format(more_calories * 100))

calorie_std = np.std(calorie_stats)

print('\nStandard Deviation')
print(calorie_std)


print('''\nWith 96% of the competition having more Calories/ Per serving,
	it seems that CrunchieMunchies Cereal tends be the overall healthier cereal. 
	50% the competitors cereals contain almost twice as many Calories per Serving. ''')