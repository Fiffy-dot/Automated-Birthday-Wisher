import csv
import datetime as dt
import random
import smtplib

my_email = "testfionamukuhi@gmail.com"
password = "TestCode24/7"
letters = ("letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt")
letter = random.choice(letters)

now = dt.datetime.now()
month_now = now.month
day_now = now.day
date_today = (month_now, day_now)

with open("birthdays.csv") as data_file:
    data = csv.reader(data_file)
    all_data = [row for row in data]
    del all_data[0]  # to remove the first column of titles
    birth_days = []
    for info in all_data:
        birth_date = (int(info[-2]), int(info[-1]))
        birth_days.append(birth_date)
    index = 0
    for tupl in birth_days:
        if tupl == date_today:  # if there's a match send a letter
            index = birth_days.index(tupl)
            name = all_data[index][0]  # get receiver's name
            email = all_data[index][1]  # get receiver's email
            with open(letter) as letter:
                content = letter.read()
                new_letter = content.replace("[NAME]", name)
                connection = smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:HAPPY BIRTHDAY!\n\n{new_letter}")
