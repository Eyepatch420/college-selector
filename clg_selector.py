import csv

def find_top_3_colleges(jee_rank, filename=r"college_branches_cutoff.csv"):
    eligible_options = []

    try:
        # Open the CSV file and read its content
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                college_name = row['College']
                branch = row['Branch']
                cutoff_rank_str = row['Rank']

                # Check if cutoff rank is a valid integer
                if cutoff_rank_str.isdigit():
                    cutoff_rank = int(cutoff_rank_str)
                    
                    # Check if the user's rank is within the cutoff for the college branch
                    if jee_rank <= cutoff_rank:
                        eligible_options.append((college_name, branch, cutoff_rank))
               
                    
        # Sort eligible options by cutoff rank and get the top 3
        eligible_options.sort(key=lambda x: x[2])  # Sort by cutoff rank (ascending)
        top_3_options = eligible_options[:3]  # Take the top 3 options

        return top_3_options

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

# Input JEE rank from user
try:
    jee_rank = int(input("Enter your JEE rank: "))
    results = find_top_3_colleges(jee_rank)

    # Display the top 3 eligible colleges and branches
    if results:
        print("With your JEE rank, here are the top 3 available college and branch options:")
        for college, branch, cutoff_rank in results:
            print(f"{college} - {branch} (Cutoff Rank: {cutoff_rank})")
    else:
        print("No eligible colleges or branches found for your rank.")

except ValueError:
    print("Invalid input: Please enter a valid integer for your JEE rank.")
