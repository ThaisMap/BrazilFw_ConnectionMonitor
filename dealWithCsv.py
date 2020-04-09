import csv

with open('ips.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row)
