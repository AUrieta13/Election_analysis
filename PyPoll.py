#The data we need to retrieve
#1. the total number of cast votes
#2. a complete list of candidates who received votes
#3. the percentage of votes each candidate won
#4. the total number of votes each candidate won
#5. the winner of the eclection based on popular votes

#Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Onedrive", "Desktop", "Analysis Projects","Election_analysis", "Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Onedrive", "Desktop", "Analysis Projects","Election_analysis","analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
        # Read the file object with the reader function.
        file_reader = csv.reader(election_data)
        #Print the header row.
        headers = next(file_reader)
        print(headers)




#     # Print the file object.
#      print(election_data)

# # Create a filename variable to a direct or indirect path to the file.


# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     txt_file.write('Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson')
