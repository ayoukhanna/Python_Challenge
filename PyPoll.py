import csv

with open('/Users/hanna/Desktop/PyPoll_Resources_election_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    print(csv_file)
    total_votes = 0
    candidates = {}
    for line in csv_reader:
        total_votes = total_votes + 1
        candidate = line[2]
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] = candidates[candidate] + 1




print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
max_votes = 0
winner = ""
for name,votes in candidates.items():
    print(f"{name}: {100*votes/total_votes:.3f}% {votes} ")
    if votes > max_votes:
        max_votes = votes
        winner = name
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")



with open('/Users/hanna/Desktop/PyPoll_Resources_election_data.txt', 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"{name}: {100*votes/total_votes:.3f}% {votes}\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")