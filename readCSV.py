import csv
from create_tables import create_connection


with open('dataFile.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    columns = next(readCSV)
    property_list = []
    owners = set()
    #Just going to assume that there would not be different owners with the 
    #same name for the sake of this project
    for row in readCSV:
        prop = []
        for item in row:
            #print(item.strip(), end = ', ')
            prop.append(item.strip())
        owners.add(row[3])
        #print()
        property_list.append(prop)

    conn = create_connection()
    #cur.execute("INSERT INTO country (name,summary,lat,lon,flag_img) VALUES (%s,%s)", (countries[i].name, countries[i].summary, countries[i].lat.countries[i].lon, countries[i].flag_img ))

    """
    try:
        cur = conn.cursor()
        for owner in owners:
            cur.execute("INSERT INTO owner (name) VALUES (%s);", (owner,))
        cur.close()
        conn.commit()
        conn.close()
    except Exception as e:
        conn.close()
        print(str(e))
    """
    owners_dict = {}
    print(len(property_list))


    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM owner")
        for row in cur.fetchall():

            #print(row)
            owners_dict[row[1]] = row[0]

        for prop in property_list:
            
            owner_name = prop[3]
            #print(owner_name)
            print(prop)
            owner_id = owners_dict.get(owner_name,None)
            print(owner_name + ' : ' + str(owner_id))
            cur.execute("INSERT INTO property (id,geoID,legalDescription,situsAddress,ownerID) VALUES \
                (%s,%s,%s,%s,%s);", (prop[0],prop[1],prop[2],prop[4],owner_id))


        cur.close()
        conn.commit()
        conn.close()
    except Exception as e:
        print(str(e))
        conn.close()
        

    
    #print(columns)

