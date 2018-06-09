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
            prop.append(item.strip())
        owners.add(row[3])
        property_list.append(prop)

    conn = create_connection()
    
    """
    After writing code to read from the file and creating the tables in the db
    Inserted owners into the owner table
    """
    try:
        cur = conn.cursor()
        for owner in owners:
            cur.execute("INSERT INTO owner (name) VALUES (%s);", (owner,))
        cur.close()
        #conn.commit()
        conn.close()
    except Exception as e:
        conn.close()
        print(str(e))

    """
    After inserting data into owner table, 
    get all entries from the owner table, 
    Created a dictionary to map owner names to ids 
    to easily be able to insert the right owner id 
    for each property when inserting properties into the property table
    """
    
    owners_dict = {}
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM owner")
        for row in cur.fetchall():

            #key = name, val = id 
            owners_dict[row[1]] = row[0]

        for prop in property_list:
            
            owner_name = prop[3]
            owner_id = owners_dict.get(owner_name,None)
            cur.execute("INSERT INTO property (id,geoID,legalDescription,situsAddress,ownerID) VALUES \
                (%s,%s,%s,%s,%s);", (prop[0],prop[1],prop[2],prop[4],owner_id))


        cur.close()
        #conn.commit()
        conn.close()
    except Exception as e:
        conn.close()
        print(str(e))
        
    

