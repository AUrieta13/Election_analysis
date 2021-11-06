#The data we need to retrieve
#1. the total number of cast votes DONE
#2. a complete list of candidates who received votes DONR
#3. the percentage of votes each candidate won DONE
#4. the total number of votes each candidate won DONE
#5. the winner of the election based on popular votes

#Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Onedrive", "Desktop", "Analysis Projects","Election_analysis", "Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Onedrive", "Desktop", "Analysis Projects","Election_analysis","analysis", "election_analysis.txt")

#1. Intialize VARIBLES : a total vote counter, declare candidate name from reach row, 
# declare the candidate votes dictionary, Winning Candidate and Winning Count Tracker
total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0
#2. Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
        # Read the file object with the reader function.
        file_reader = csv.reader(election_data)
        #Read the header row.
        headers = next(file_reader)
        #Print each row in the CSV File (START FOR LOOP).
        for row in file_reader:
            #Add the total vote counter, get candidate's name from the row (VARIABLES IN LOOP)
            total_votes += 1
            candidate_name = row[2]
            #Check to see if candidate name already exist in candidate option list
            if candidate_name not in candidate_options:
                #Add candidate_name to the candidate_option list if not in 
                 candidate_options.append(candidate_name)
                # Intiate tracking each candidates votes 
                 candidate_votes[candidate_name] = 0
            # Add a vote to the candidate's count
            candidate_votes[candidate_name] += 1
        # END FOR LOOP
# Save the results to our text file.   
with open(file_to_save, "w") as txt_file:
        #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        #Save the final vote count to the text file.
    print(election_results, end="")
    txt_file.write(election_results)

        #Determine percentage of votes of each candidate name by looping through the counts (START NEW FOR LOOP)
        #1. Iterate through the candidate list
        
    for candidate_name in candidate_votes:
            #2. Retrieve vote count of a candidate name using candidate_votes dictionary
        votes = candidate_votes[candidate_name]
            #3.Calculate the percentage of votes for each candidate
        vote_percentage = float(votes)/float(total_votes)*100 
            #4. Print the candidate's name and % of votes won using f string
            # print(f'{candidate_name}: received {vote_percentage:.1%}of the votes.')

        #  To do: print out the winning candidate, vote count and percentage to terminal.
        candidate_results = (
                f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        # Print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        txt_file.write(candidate_results)

        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
            # Determine winning vote count and candidate
            # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                #if true, set winning_count = votes and winning_percentage=vote_percentage
                winning_count=votes
                winning_percentage=vote_percentage
                #Set winning_candidate = candidate's name
                winning_candidate= candidate_name
        # WRITE OUT WINNING CANDIDATE SUMMARY IN FORMAT     
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

#save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
        

# Print the total votes, candidate names, each candidate's total votes
# print(total_votes)
# print(candidate_options)
# print(candidate_votes)