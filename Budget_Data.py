import csv

with open('/Users/hanna/Desktop/PyBank_Resources_budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    print(csv_file)
    total = 0
    total_change = 0
    total_amount = 0
    greatest_increase = 0
    greatest_month = ""
    greatest_decrease = 999999999
    worst_month = ""
    for line in csv_reader:
        #print(line)
        total = total + 1
        total_amount= total_amount + int(line[1])
        if total > 1:
            change = int(line[1])-previous
            total_change = total_change + change
            if change > greatest_increase:
                greatest_increase = change
                greatest_month = line[0]
            if change < greatest_decrease:
                greatest_decrease = change
                worst_month = line[0]
        previous = int(line[1])
average_change = total_change/(total-1)
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits:{greatest_month}, {greatest_increase}")
print(f"Greatest Decrease in Profits: {worst_month}, {greatest_decrease}")
with open('/Users/hanna/Desktop/PyBank_Resources_budget_data.txt', 'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Months: {total}\n")
    txt_file.write(f"Average Change: ${average_change}\n")
    txt_file.write(f"Greatest Increase in Profits:{greatest_month}, {greatest_increase}\n")
    txt_file.write(f"Greatest Decrease in Profits: {worst_month}, {greatest_decrease}\n")