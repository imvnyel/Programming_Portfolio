import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head())

platform_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()

print(platform_views)

#add a column that checks for a timestamp
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

#groupby click source and is_click
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

#create pivot for easier analysis
clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()

#create a column that shows percent of user per source that clicked
clicks_pivot['percent_clicked'] = clicks_pivot[True] /( clicks_pivot[True] + clicks_pivot[False])

print(clicks_pivot)

#count num of users per group
exp_count = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()

exp_count_pivot = exp_count.pivot(columns='is_click', index='experimental_group', values='user_id')

#calculate percentage of clicks per test group
exp_count_pivot['percent_click'] = exp_count_pivot[True] / (exp_count_pivot[True] + exp_count_pivot[False])

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_by_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
b_clicks_by_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
#print(exp_pivot)

a_clicks_by_day_pivot = a_clicks_by_day.pivot(columns='is_click',index='day',values='user_id').reset_index()
b_clicks_by_day_pivot = b_clicks_by_day.pivot(columns='is_click',index='day',values='user_id').reset_index()

a_clicks_by_day_pivot['percent_clicks'] = a_clicks_by_day_pivot[True] / (a_clicks_by_day_pivot[True] + a_clicks_by_day_pivot[False])

b_clicks_by_day_pivot['percent_clicks'] = b_clicks_by_day_pivot[True] / (b_clicks_by_day_pivot[True] + b_clicks_by_day_pivot[False])

a_percent = a_clicks_by_day_pivot.percent_clicks.mean()
b_percent = b_clicks_by_day_pivot.percent_clicks.mean()

print('A: {0:.2f}% ::: B: {1:.2f}%'.format(a_percent, b_percent))
print(b_clicks_by_day_pivot)
