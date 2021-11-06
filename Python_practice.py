from typing import KeysView


counties = ['Arapahoe', 'Denver', 'Jefferson'] 

if 'Arapahoe' in counties and 'El Paso' not in counties:
    print('Only Arapahoe is in the list of counties')
else:
    print('Arapahoe is in the list of counties and El Paso is not in the list of counties')

for county in counties:
    print(county)

numbers= [0,1,2,3,4]
for num in range(5):
    print(num)

for county in range(len(counties)):
    print(counties[county])

counties_tuple = ('Arapahoe', 'Denver', 'Jefferson')
for tuple in range(len(counties_tuple)):
    print(counties_tuple[tuple])

counties_dict = {'Arapahoe': 422829, 'Denver':463353, 'Jefferson': 432438}
for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

counties_dict = {'Arapahoe': 422829, 'Denver':463353, 'Jefferson': 432438}
for county in counties_dict:
    print(counties_dict[county])


counties_dict = {'Arapahoe': 422829, 'Denver':463353, 'Jefferson': 432438}
for county in counties_dict:
    print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key,value)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

print(f"I received {percentage_votes}% of the total votes.")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total number votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
candidate_votes = int(input('How many votes did the candidate get in the election'))
message_to_canadidate= (
    f"You received {candidate_votes:,} votes in the election. "
     f"The total number of votes were {total_votes:,}. "
     f"The percentage of votes you received were {percentage_votes:.2f}%.")

print(message_to_canadidate)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

for county, voters in voting_data:
    print(f"{county} country had {voters} registered voters")