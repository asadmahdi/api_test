import csv



with open('dataFile.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    columns = next(readCSV)
    property_list = []
    for row in readCSV:
        prop = []
        for item in row:
            print(item.strip(), end = ', ')
            prop.append(item.strip())
        print()
        property_list.append(prop)
    for item in columns:
        item = item.strip()

    for prop in property_list:
        print(prop)
        pass
    
    print(columns)

print(done)