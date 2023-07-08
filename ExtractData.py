""" 
    IMPORTANT NOTE: 
    ANY CHANGES YOU MIGHT HAVE TO MAKE ARE:
        LINE 10 -> SPECIFY THE DIRECTORY THAT YOU HOLD YOUR GOPHISH'S RESULT FILES (CSV)
        LINE 45/52/60 ->  YOU HAVE TO CHANGE INDEX PARAMETERS INSIDE ARRAYS. LOOK AT YOUR CSV FILE AND DETERMINE WHICH INDEX YOU WANT TO STORE AFTER YOU SPLIT(,) THE EACH LINE.
"""

import os

directory = '.'  # Current directory

file_list = [] # In this list, there will be csv files in the specified directory above

# Iterate over files in the directory
for file_name in os.listdir(directory): 
    # Check if the file is a regular file and not ending with .py or .txt
    if os.path.isfile(os.path.join(directory, file_name)) and not file_name.endswith(".py") and not file_name.endswith(".txt"):
        file_list.append(file_name)

# Variables to keep track of different events
email_sent = 0
email_opened = 0
clicked_link = 0
submit = 0

# We create discreate lists because we want to write them to a file in logical order at the end.
opened = []
clicked = []
submitted = []

# Iterate over each file in the file list
for file in file_list:
    f = open(file, "r")  # Open the file for reading
    for line in f:

        line = line.split(",")  

        if line[1] == "Email Sent":
            email_sent += 1 
            
        if line[1] == "Email Opened":
            email_sent += 1
            email_opened += 1  
            
            opened.append(f"{line[1]}: {line[8]}")  
            
        if line[1] == "Clicked Link":
            email_sent += 1
            email_opened += 1
            clicked_link += 1  
            
            clicked.append(f"{line[1]}: {line[8]}\n")  
            
        if line[1] == "Submitted Data":
            email_sent += 1
            email_opened += 1
            clicked_link += 1
            submit += 1  

            submitted.append(f"{line[1]}: {line[8]}\n")  
            
    f.close()  # Close the file

# Write the event details to the result.txt file
with open("result.txt", "w") as f:
    for line in opened:
        f.write(line + "\n")  # Write opened events to the file
    for line in clicked:
        f.write(line)  # Write clicked events to the file
    for line in submitted:
        f.write(line)  # Write submitted events to the file
        
# Append the summary statistics to the result.txt file
with open("result.txt", "a") as wr:
    wr.write(f"email_sent: {email_sent} \nemail_opened: {email_opened} \nclicked_link: {clicked_link} \nsubmitted_data: {submit}")
