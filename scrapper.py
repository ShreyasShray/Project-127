# importing all the files
from bs4 import BeautifulSoup
import requests
import csv
import time

# URL for the website
Start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Creating headers for the csv
headers = ["name", "distance", "mass", "radius"]

# Using Get Request Method
page = requests.get(Start_url)

# print(page)

soup_object = BeautifulSoup(page.text, "html.parser")

# Waiting for 5 seconds
time.sleep(5)

# Getting the list of tables
start_table = soup_object.find("table")

# Getting all the rows
table_rows = start_table.find_all("tr")
temp_list_1 = []

# Getting all the data in temp_list_1
for tr in table_rows:
    td = tr.find_all("td")
    temp_list_2 = []
    for td_tag in td:
        temp_list_2.append(td_tag.text.rstrip())
    temp_list_1.append(temp_list_2)

# print(temp_list_1)

star_name = []
star_distance = []
star_mass = []
star_radius = []

for i in range(1, len(temp_list_1)):
    if(temp_list_1[i][1] == "?"):
        star_name.append("")
    else:
        star_name.append(temp_list_1[i][1])
    if(temp_list_1[i][3] == "?"):
        star_distance.append("")
    else:
        star_distance.append(temp_list_1[i][3])
    if(temp_list_1[i][5] == "?"):
        star_mass.append("")
    else:
        star_mass.append(temp_list_1[i][5])
    if(temp_list_1[i][6] == "?"):
        star_radius.append("")
    else:
        star_radius.append(temp_list_1[i][6])

# print("star_name :- ", star_name)
# print("star_distance :- ", star_distance)
# print("star_radius :- ", star_radius)
# print("star_mass :- ", star_mass)

star_data = []

# Storing all data in star_data to create csv
for i in range(0, len(temp_list_1)-1):
    temp_star_data = []
    temp_star_data.append(star_name[i])
    temp_star_data.append(star_distance[i])
    temp_star_data.append(star_mass[i])
    temp_star_data.append(star_radius[i])
    star_data.append(temp_star_data)

# print(star_data)

# Creating csv file 
with open("scrapper_2.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)