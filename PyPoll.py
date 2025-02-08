# Add dependencies
import csv  # Allows reading and writing CSV files (comma-separated values)
import os   # Provides functions to interact with the operating system (e.g., file paths)

# Define file paths for loading and saving data
file_to_load = os.path.join("Resources", "election_results.csv")  # Path to input CSV file
file_to_save = os.path.join("analysis", "election_analysis.txt")  # Path to output text file

# Initialize a variable to count the total number of votes
total_votes = 0  

# Create a list to store unique candidate names
candidate_options = []  

# Create a dictionary to store the number of votes each candidate receives
candidate_votes = {}  

# Variables to track the winning candidate and their vote count/percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open and read the election results file
with open(file_to_load) as election_data:  
    # Read the file as a CSV using the csv.reader() function
    file_reader = csv.reader(election_data)

    # Read and store the header row (column names) to skip it
    headers = next(file_reader)

    # Iterate through each row in the CSV file (skipping headers)
    for row in file_reader:
        # Increment the total vote count
        total_votes += 1  

        # Extract the candidate's name from the row (column index 2)
        candidate_name = row[2]  

        # If the candidate is encountered for the first time:
        if candidate_name not in candidate_options:
            # Add the candidate to the list of options
            candidate_options.append(candidate_name)

            # Initialize their vote count in the dictionary
            candidate_votes[candidate_name] = 0  

        # Increment the candidate's vote count
        candidate_votes[candidate_name] += 1  

# Open the output text file to save election results
with open(file_to_save, "w") as txt_file:

    # Create a formatted string for the election summary
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    # Print election summary to the terminal
    print(election_results, end="")  

    # Save election summary to the text file
    txt_file.write(election_results)  

    # Iterate through the dictionary of candidate votes
    for candidate_name in candidate_votes:
        # Retrieve the total votes for the candidate
        votes = candidate_votes[candidate_name]  

        # Calculate the percentage of total votes received
        vote_percentage = float(votes) / float(total_votes) * 100  

        # Format the candidate's results for display
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print the candidate's results to the terminal
        print(candidate_results)

        # Save the candidate's results to the output file
        txt_file.write(candidate_results)

        # Check if this candidate has the highest vote count so far
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # Update winning candidate details
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Create a formatted summary of the winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # Print the winning candidate summary to the terminal
    print(winning_candidate_summary)  

    # Save the winning candidate summary to the text file
    txt_file.write(winning_candidate_summary)  