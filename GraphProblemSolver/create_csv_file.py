import csv

with open('graph.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', lineterminator = '\n')
    filewriter.writerow(['1', '2', '0.5', 'green'])
    filewriter.writerow(['3', '4', '0.7', 'green'])
    filewriter.writerow(['1', '4', '0.3', 'red'])
    filewriter.writerow(['5', '1', '0.5', 'black'])
    filewriter.writerow(['4', '2', '0.1', 'blue'])
