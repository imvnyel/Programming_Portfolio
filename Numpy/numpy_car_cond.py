#import codecademylib
import numpy as np

#vehicle_stats = np.genfromtxt('cereal.csv', delimiter=',')
vehicle_stats = np.genfromtxt('vehicle_condition.csv', delimiter=',')
average_vehicle = np.mean(vehicle_stats)

print('Average Score')
print(average_vehicle*20)

vehicle_stats_sorted = np.sort(vehicle_stats)
median_vehicle = np.median(vehicle_stats_sorted)
print('\nMedian Rating:')
print(median_vehicle*20)


# Find out nth Percentiles for range 5-100, set 5
percents = {}
for i in range(5, 100, 5):
  percents[i] = np.percentile(vehicle_stats, i)

for x in percents:
	print(x, ':', percents[x]*20)

 #List of all {percentiles: vehicle} > 60
greater_60 = [{x:percents[x]*20} for x in percents if (percents[x]*20) > 50]
print(greater_60)
#greater_60.sort()
#nth_percentile = greater_60[0].keys()

print('\nLowest Percentile with greater than 60% Rating:')
#print(nth_percentile[0]) 


more_vehicle = np.mean(vehicle_stats > 50)
print('\n{0:0.2f}% of our have more vehicle than ours'.format(more_vehicle * 100))

vehicle_std = np.std(vehicle_stats)

print('\nStandard Deviation')
print(vehicle_std)


#print('''\nWith 96% of the competition having more vehicle/ Per serving,
#	it seems that CrunchieMunchies Cereal tends be the overall healthier cereal. 
#	50% the cereals contain almost twice as many vehicles per Serving. ''')