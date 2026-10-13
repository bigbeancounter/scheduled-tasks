# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

name_to_replace = "[NAME]"
now = datetime.now()
this_month = now.month
this_day = now.day
this_year = now.year

file = pandas.read_csv("birthdays.csv")

for index, row in file.iterrows():
    if row["month"] == this_month and row["day"] == this_day:
        age = this_year - row["year"]
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
            
        with open(file_path) as letter_file:
            content = letter_file.read()
            updated_content = content.replace(name_to_replace, row["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=row["email"],
                    msg=f"Subject:Happy Birthday from my Python script! You're {age} today! \n\n{updated_content}"
                )
