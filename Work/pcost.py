import csv
import sys
def portfolio_cost(filename):
    'Fun function'

    f = open(filename)
    sum = 0
    rows = csv.reader(f)

    for row in rows:

        i = 0
            
        try:
            kek = int(row[1])
        except ValueError:
            print("Couldn't parse", row)
            i = 1

        if i == 0:
            sum = sum + int(row[1])*float(row[2])

    f.close()
    return sum

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)