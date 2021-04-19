import numpy as np

rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11])


rain_mean = np.mean(rainfall)
rain_median = np.median(rainfall)
first_quarter = np.percentile(rainfall, 25)
third_quarter = np.percentile(rainfall, 75)
interquartile_range = third_quarter - first_quarter
rain_std = np.std(rainfall)

output = [
  {'Mean': rain_mean},
  {'Median': rain_median},
  {'25%': first_quarter},
  {'75%': third_quarter},
  {'Interquartile': interquartile_range},
  {'Std Dev': rain_std}]

for i in range(len(output)):
  for x in output[i]:
    print(x, output[i].get(x))
  