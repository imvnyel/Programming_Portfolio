# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(damages=damages):
  damage_update = []
  conversion = {'M': 1000000,'B': 1000000000}
  for info in damages:
    if info == 'Damages not recorded':
      damage_update.append(info)
    for k in conversion:
      if k in info:
        new_info = float(info.strip(k)) * conversion[k]
        damage_update.append(new_info)
  return damage_update

ud = update_damages()

# write your construct hurricane dictionary function here:
def hurricane_dict(names=names, months=months, years=years, max_sustained_winds=max_sustained_winds, areas_affected=areas_affected, damages=ud, deaths=deaths):
  hurricane = {}
  for i in range(len(names)):
    hurricane_info = { 
      'Name': names[i],
      'Month': months[i],
      'Year': years[i],
      'Max Sustained Wind': max_sustained_winds[i],
      'Areas Affected': areas_affected[i],
      'Damages': damages[i],
      'Deaths': deaths[i]
     }
    hurricane[names[i]] = hurricane_info
  return hurricane
hurricane_index = hurricane_dict()
 
# write your construct hurricane by year dictionary function here:
def hurricane_by_year(hurricane_index):
  hurricane_by_year = {}
  for i in hurricane_index:
    current_year = hurricane_index[i]['Year']
    current_cane = hurricane_index[i]
    if current_year not in hurricane_by_year:
      hurricane_by_year[current_year] = [current_cane]
    else:
      hurricane_by_year.get(current_year).append(current_cane)
  return hurricane_by_year 


by_year = hurricane_by_year(hurricane_index)


# write your count affected areas function here:
def count_affected(hurricane_index):
  areas_affected = {}
  for i in hurricane_index:
    for area in hurricane_index[i]['Areas Affected']:
      if area not in areas_affected:
        areas_affected[area] = 1
      else:
        areas_affected[area] += 1
  return areas_affected

#prints total count of all hurricane affected areas
area_affected = count_affected(hurricane_index)



# write your find most affected area function here:
def most_hit(area_affected):
  highest = 0
  to_show = []
  for counts in area_affected:
    if area_affected.get(counts) > highest:
      highest = area_affected.get(counts)
      to_show = [counts, highest]
  return to_show
hits = most_hit(area_affected)

def most_often_hit(hits=hits):
  #prints most affected area
  print('The most hit area is {0} : {1} times'.format(hits[0], hits[1]))




# write your greatest number of deaths function here:
def most_deaths(hurricane_index):
  highest = 0
  for i in hurricane_index:
    deaths = hurricane_index[i]['Deaths']
    #print(hurricane_index[i]['Name'])
    if deaths > highest:
      highest = deaths
      to_show = [hurricane_index[i]['Name'], highest]
  return to_show
dead = most_deaths(hurricane_index)

def deadliest_cane(dead=dead):
  print('The deadliest Hurricane of all time was Hurricane {0}: {1} dead'.format(dead[0], dead[1]))
  



# write your catgeorize by mortality function here:
def mortality_rating(hurricane_index):
  mortality_scale = {0: 0,
                    1: 100,
                    2: 500,
                    3: 1000,
                    4: 10000}
  mortality_dict = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for item in hurricane_index:
    mortality = hurricane_index[item]['Deaths']
    hurricane_info = hurricane_index[item]
    for i in mortality_scale:
      #print(mortality_scale[i])
      try:
        if mortality_scale[i] <= mortality and mortality <= mortality_scale[i+1]:
          #print('---->', i+1)
          mortality_dict[i+1].append(hurricane_info)
      except:
        #print(mortality)
        if mortality > 10000:
          #print('KeyError')
          mortality_dict[5].append(hurricane_info)
          #print('appended')
  return mortality_dict, mortality_scale

md, ms= mortality_rating(hurricane_index)
def mortality_print(md=md,ms=ms):
  for i in md:
    if i != 5:
      print('\nFewer than {} deaths'.format(ms[i], ':'))
    else:
      print('\nMore than {} deaths'.format(ms[4], ':'))
    for item in md[i]:
      print(item.get('Name').center(25)+': ', item.get('Deaths'))



# write your greatest damage function here:
def greatest_damage(hurricane_index):
  max_cost = 0
  most_damage = []
  for item in hurricane_index:
    cost = hurricane_index[item]['Damages']
    current_hurricane = hurricane_index[item]['Name']
    if cost != 'Damages not recorded' and float(cost) > max_cost:
      max_cost = cost
      most_damage = [current_hurricane, max_cost]
  return most_damage
gd = greatest_damage(hurricane_index)  

def most_damage_print(gd=gd):
  string_rep =''
  convert_list = {'B': 1000000000, 'M': 1000000}
  for num in convert_list:
    count_zero = gd[1] / convert_list[num]
    if count_zero > 0:
      string_rep = str(count_zero)+num
      #print(string_rep)
      print('the Hurricane that caused the most damage is {0}, causing ${1} in damages'.format(gd[0], string_rep))
      return
    else:
      string_rep = str(count_zero)+num
    print(string_rep)
    print('the Hurricane that caused the most damage is {0}, causing ${1} in damages'.format(gd[0], string_rep))
      





# write your catgeorize by damage function here:
def cat_by_damage(hurricane_index=hurricane_index):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  store_ratings = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for cst in hurricane_index:
    costs = hurricane_index[cst]['Damages']
    if costs == 'Damages not recorded':
      store_ratings[0].append(hurricane_index[cst])
    else:
      for scale in damage_scale:
        try:
          if costs >= damage_scale[scale] and costs < damage_scale[scale+1]:
            store_ratings[scale+1].append(hurricane_index[cst])
        except:
            if costs > damage_scale[4]:
              store_ratings[5].append(hurricane_index[cst])
  return store_ratings, damage_scale
store_ratings, ds = cat_by_damage() 
  
def damages_by_cat(store_ratings=store_ratings, ds=ds):
  for i in store_ratings:
    if i != 5:
      print('Cat', i,': \n(Caused less than ${0}(USD) damage)'.format(ds[i]))
    else:
      print('Cat', i,': \n(Caused More than ${0}(USD) damage)'.format(ds[4]))
    for x in store_ratings[i]:
      print(x.get('Name').center(20), x.get('Damages'))
  #print(store_ratings[0])

#initialization


selection = {1:'Show damages information',
            2: 'Show mortality information',
            3: 'Show deadliest Hurricane',
            4: 'Show expensive Hurricane'} 

for s in selection:
  print(s, selection[s])

   
damages_by_cat()   
mortality_print()

print('\n--------------------------Records----------------------\n'.center(25))
most_damage_print()
print('----->Most Hit')
most_often_hit()
print('----->Deadliest')
deadliest_cane()