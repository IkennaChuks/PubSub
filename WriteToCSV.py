import csv 
import random
first_name = ['ikenna', 'chinyere', 'blaise', 'andre', 'obum', 'Daniel']
Lastname = ['Mohammed', 'Stephen', 'Hector', 'Ever', 'Hector', 'Andy']


with open('sample2.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(100):
        data = [random.choice(first_name), random.choice(Lastname),str(i)]
        writer.writerow(data)