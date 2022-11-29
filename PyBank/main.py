import csv #imports necessary module to read and write csv files

total_months = 0 #initializes total months
csvfile = '../python-homework/PyBank/budget_data.csv' #sets path for budget_data.csv
net_pnl = 0 #initializes net profit/losses

with open(csvfile, 'r') as csv_file: #opens the csvfile in read mode
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader) #skips the header
    nums_in_list = [] #initialize a new empty list to store all the numbers in
    months_in_list = [] #initialize a new empty list to store all the months in
    for row in csv_reader: #appends the numbers and months to the lists that were created
        nums_in_list.append(row[1])
        months_in_list.append(row[0])
    for row in nums_in_list: # calculates the sum of the list
        net_pnl += int(row)
    total_months = len(nums_in_list)
    #initializes strings for output
    total_months_str = "Total Months: " + str(total_months)
    net_pnl_str = "Total: " + str(net_pnl)

# initializes vars for the average profit/losses, and indexes for the greatest increase/decrease
average_pnl = 0
greatest_num_index = 0
decrease_num_index = 0

#The greatest increase in profits (date and amount) over the entire period.
greatest_increase = int(nums_in_list[0])
for num in nums_in_list: # searches for greatest increas
    if(int(num) > greatest_increase): #if the current number is greater than the greatest number that we currently have, update greatest_increase
        greatest_increase = int(num)
        greatest_num_index = nums_in_list.index(num)
        

greatest_decrease = int(nums_in_list[0]) #if the current number is less than the greatest lowest number that we currently have, update greatest_decrease
for num in nums_in_list:
    if(int(num) < greatest_decrease):
        greatest_decrease = int(num)
        decrease_num_index = nums_in_list.index(num)      

# creates variables for strings that will be used for writing to the output file
greatest_increase_str = "Greatest Increase: " + months_in_list[greatest_num_index] + " | " + str(greatest_increase)
greatest_decrease_str = "Greatest Decrease: " + months_in_list[decrease_num_index] + " | " + str(greatest_decrease)

#prints the results to the terminal
print("Financial Analysis:")
print(total_months_str)
print(net_pnl_str)
print(greatest_increase_str)
print(greatest_decrease_str)

new_csvfile = '../python-homework/PyBank/output.csv' #initializes a variable for the output csvfile (check terminal or output.csv for results)
with open(new_csvfile, 'w') as csv_output: #opens output.csv in write mode
    writer = csv.writer(csv_output, delimiter=',')
    writer.writerow(["Financial Analysis:"]) #writes data to output.csv
    writer.writerow([total_months_str])
    writer.writerow([net_pnl_str])
    writer.writerow([greatest_increase_str])
    writer.writerow([greatest_decrease_str])