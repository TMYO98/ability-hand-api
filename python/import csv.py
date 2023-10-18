import csv
import os

def write_to_csv(posRead, filename):
    headers = ["current", "voltage", "temperature"]
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(posRead[:3])


posRead1 = [1, 2, 3, 4, 5, 6]
posRead2 = [7, 8, 9, 10, 11, 12]

write_to_csv(posRead1, 'C:/Users/jctam/OneDrive/Escritorio/PSYONIC/ability-hand-api/python/data.csv')
write_to_csv(posRead2, 'C:/Users/jctam/OneDrive/Escritorio/PSYONIC/ability-hand-api/python/data.csv')
