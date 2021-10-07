import csv 
def read_price(filename):
    '''Reads 'filename' into a list of tuples'''

    portfolio = {} #Initial empty list
    f = open(filename)
    rows = csv.reader(f)
    
    for row in rows:

        i = 0
            
        try:
            kek = int(row[1])
        except ValueError:
            i = 1

        if i == 0:
            holding = { 'name' : row[0], 
                        'price' : float(row[1]) }
            portfolio.append(holding)

    f.close()
    return portfolio