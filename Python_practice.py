print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
# This code was comment out because variable holding the list 
# was created on line 2 of the code
# code will run normal it doesn't required the code on line 9
# it does run normal even with that code not comment out
# counties = ["Arapahoe","Denver","Jefferson"]

# line of code shows how to use membership operators in and not in
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


# this line of code is combining membership operators 
# and logical operators into one code 20-23 lines 
# are using "and" logical operators "in" membership operators 
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# line 27-30 are using logical operator "or" membership operator "in"
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

# line 33-37 are using logical operator "or" 
# membership operator "in" also "not in"
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# practicing for loop also know as count-controlled loop
# it will continue to loop throught the counties 
# until it has no more items to loop over
for county in counties:
    print(county)
# creating a new variable that holds a list
numbers = [0, 1, 2, 3, 4]
# starting the for loop to print all numbers in our list
for num in numbers:
    print(num)
# for loop using range function to print all the numbers in list
for num in range(5):
    print(num)
# The variable i is used to indicate the index, or the values 0, 1, and 2, in the length of the counties list. The letter i is often used for simplicity, but any variable can be used.
# Inside the range() function, we get the length of the list of counties, which is the integer 3.
# Then, we iterate through the list, where the variable i is equal to 0 for the first index. The 0 is passed into the print(counties[i]) statement, where i = 0, and "Arapahoe" is printed.
# This process is continued until all three items, or counties, in the list are printed to the screen.

#this code is using also a for loop but instead of hard coding the index
#we use the len method to retrieve the lenght of indexes and retrieve all 
#the counties
for i in range(len(counties)):
    print(counties[i])
# exercise using tuple first step create the tuple
counties_tuples = ("Arapahoe","Denver","Jefferson") 
# set up the for loop to iterate through tupple
for i in range(len(counties_tuples)):
    print(counties_tuples[i])
# exercise using tuple another way to print the tupple
for county in counties_tuples:
    
    print(county)
# setting up a dictionary variable to loop over in later code
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# this code will loop over the dictionary and print the keys
for county in counties_dict:
    print(county)
# this code will loop over the dictornay 
# and print the keys using keys()method
# When using the keys() method, 
# it doesn't matter what variable name we use in the for loop. 
# The keys() method will print each key in order.
for county in counties_dict.keys():
    print(county)
# this code will print the values of the dic
# using the values methods
for voters in counties_dict.values():
    print(voters)
# this loop prints the values of dict by calling the key []
for county in counties_dict:
    print(counties_dict[county])
# this loop prints the values of dict using the "get" method
for county in counties_dict:
    print(counties_dict.get(county))
# This loop prints the keys and values of dict using items
for county, voters in counties_dict.items():
    print(county, voters)
# creating new variable that holds our list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
# for loop will print the list of dict and their values
# brake down: it will loop through the votinng_data variable
# find the keys in county_dict and match it in the voting_data dict
# and print them both
for county_dict in voting_data:
    print(county_dict)
# using range method to print the dictionary list 
for i in range(len(voting_data)):

      print(voting_data[i])
# loop prints the keys or counties in the voting_data dict list
# this uses the range method
for i in range(len(voting_data)):

      print (voting_data[i]['county'])
# nested loop prints the list of dict and values using value method 
# first loop used to retrieve each dictionary
# second loop used to retrieve values 
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# this code will allow us to print only the numbers of register voters
for county_dict in voting_data:

     print(county_dict['registered_voters'])
# this code will allow us to print only the counties 
for county_dict in voting_data:
    print(county_dict['county'])
# printing dictionary not using F-string method note: the counties_dict
# doesnt need to be created again since we created earlier we can 
# just call it in the print function code runs fine either method
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
# printing method using f-strings same result as code line 128-130
# but is more intuitive and clear
for county, voters in counties_dict.items():
    print(f"{ county } county has { voters } registered voters.")
# code lines 136-137 create and input variable this allow users to input 
# information that code will later use for printing the "int" is saying integer
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
# using F-string to produce multiple strings we created a variable that 
# holds all of our f-strings later using print we call on the variable
# and not each individual string
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)
