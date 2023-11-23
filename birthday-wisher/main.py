##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the
# person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# ---------------------------- MY SOLUTION ------------------------------- #

import os
import pandas
import smtplib
from datetime import datetime
from random import choice

my_email = "creativesuvam@gmail.com"
g_password = "yvlv bkxv bvqy ikqj"
PLACEHOLDER = "[NAME]"

# now = dt.datetime.now()
today_day = float(datetime.now().day)
today_month = float(datetime.now().month)

df = pandas.read_csv("birthdays.csv")
data = df[(df.day == today_day) & (df.month == today_month)]

# Pick a random .txt file
random_txt_file = choice(os.listdir("letter_templates"))
# print("Random .txt file:", random_txt_file)

# Define the full path to the randomly selected .txt file
file_path = os.path.join("letter_templates", random_txt_file)

with open(file_path) as file:
    message = file.read()
    for index, row in data.iterrows():
        name = row["name"]
        new_message = message.replace(PLACEHOLDER, name)
# print(new_message)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=g_password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Happy Birthday!\n\n{new_message}")
