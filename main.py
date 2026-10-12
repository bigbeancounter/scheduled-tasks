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

folder_path = Path("./letter_templates")
txt_files = list(folder_path.glob("*.txt"))

now = dt.datetime.now()
this_month = now.month
this_day = now.day
this_year = now.year

file = pandas.read_csv("birthdays.csv")

for index, row in file.iterrows():
    if row["month"] == this_month and row["day"] == this_day:
        random_letter = random.choice(txt_files)
        age = this_year - row["year"]

        with open(random_letter, "r") as old_letter:
            content = old_letter.read()
            updated_content = content.replace(name_to_replace, row["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=row["email"],
                    msg=f"Subject:Happy Birthday! You're {age} today! It's just a test! ;-)\n\n{updated_content}"
                )
