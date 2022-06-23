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

def convert_damages(damages):
  conversion = {"M": 1000000,
              "B": 1000000000}
  updated_damages = []

  for damage in damages:
    if damage == 'Damages not recorded':
      updated_damages.append(damage)
    if damage[-1] == "M":
      updated_damages.append(float(damage.strip("M")) * conversion["M"])
    if damage[-1] == "B":
      updated_damages.append(float(damage.strip("B")) * conversion["B"])
  return updated_damages

updated_damages = convert_damages(damages)
print(updated_damages)


# write your construct hurricane dictionary function here:

def make_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):

  hurricanes = {}

  for num in range(len(names)):
    hurricanes[names[num]] = {"Name" : names[num], "Month" : months[num], "Year" : years[num], "Max Sustained Wind" : max_sustained_winds[num], "Areas Affected" : areas_affected[num], "Damage" : updated_damages[num], "Death" : deaths[num]}
  return hurricanes

hurricanes = make_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes)


# write your construct hurricane by year dictionary function here:

def hurricane_year(dict):
  hurricane_by_year ={}
  for element in dict:
    current_year = dict[element]['Year']
    current_cane = dict[element]
    if current_year in hurricane_by_year:
      hurricane_by_year[current_year].append(current_cane)
    else:
      hurricane_by_year[current_year] = [current_cane]
  return hurricane_by_year

hurricane_by_year = hurricane_year(hurricanes)
print(hurricane_by_year[1932])


# write your count affected areas function here:

def affected_area_count(data):
    areas_affected_count = {}
    for hurricane in data.values():
        area_list = hurricane["Areas Affected"]
        for area in area_list:
            if area not in areas_affected_count:
                areas_affected_count[area] = 1
            else:
                areas_affected_count[area] += 1
    return areas_affected_count


count_of_affected_areas = affected_area_count(hurricanes)
print(count_of_affected_areas)


# write your find most affected area function here:

def most_affected(data):
  count = 0
  area = ''
  for key, value in data.items():
    if value > count:
      count = value
      area = key
  return area + " " + str(count)

max_affected = most_affected(count_of_affected_areas)
print(max_affected)


# write your greatest number of deaths function here:

def deadliest_hurricane(data):
  count = 0
  name = ''
  year = 0
  for cane in data.values():
    if cane["Death"] > count:
      count = cane["Death"]
      name = cane["Name"]
      year = cane["Year"]
  return str(year) + " " + name + ": " + str(count) + " deaths"

deadliest_cane = deadliest_hurricane(hurricanes)
print(deadliest_cane)


# write your catgeorize by mortality function here:

def mortality(data):

    mortality_rates = {0:[], 1:[], 2:[], 3:[], 4:[]}

    for cane in data:

        rate = 0
        deaths = data[cane]['Death']

        if deaths < 100:
            rate = 0
        elif deaths >= 100 and deaths < 500:
            rate = 1
        elif deaths >= 500 and deaths < 1000:
            rate = 2
        elif deaths >= 1000 and deaths < 10000:
            rate = 3
        else:
            rate = 4

        if rate not in mortality_rates:
            mortality_rates[rate] = data[cane]
        else:
            mortality_rates[rate].append(data[cane])

    return mortality_rates

mortality_rates = mortality(hurricanes)
print(mortality_rates)



# write your greatest damage function here:

def most_damage(data):
  max_damage = 0
  name = ''
  year = 0
  for cane in data.values():
    damage = cane["Damage"]
    if isinstance(damage, float) is True:
      if damage > max_damage:
        max_damage = cane["Damage"]
        name = cane["Name"]
        year = cane["Year"]
  return str(year) + " " + name + ": $" + str(max_damage)

max_damage = most_damage(hurricanes)
print(max_damage)



# write your catgeorize by damage function here:

def damage_caused(data):

    damage_scale = {0: [], 1: [], 2: [], 3: [], 4: []}

    for cane in data:

        rate = 0
        damage = hurricanes[cane]['Damage']

        if damage == 'Damages not recorded':
            continue
        elif damage < 100000000:
            rate = 0
        elif damage >= 100000000 and damage < 1000000000:
            rate = 1
        elif damage >= 1000000000 and damage < 10000000000:
            rate = 2
        elif damage >= 10000000000 and damage < 50000000000:
            rate = 3
        else:
            rate = 4

        if rate not in damage_scale:
            damage_scale[rate] = data[cane]
        else:
            damage_scale[rate].append(data[cane])

    return damage_scale

damage_scale_dict = damage_caused(hurricanes)
print(damage_scale_dict)