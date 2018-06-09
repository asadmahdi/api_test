https://asad-mahdi-api.herokuapp.com/ is the base url 

Below are examples for all the routes 
/property/get/297 (GET)
/property/get-all (GET)
/property/delete/297 (DELETE)
/property/update-address/297 (PUT)
/owner/update-name/32 (PUT)

The /property endpoints (except for get-all which takes no additional parameter) take a propID at the end.
I used 297 as an example

The /owner/update-name/ endpoint takes an ownerID, they range from 32-62

/property/update-address requires a key 'newAddress' in the request body 

example

{
	"newAddress" : "This is a new address"
}

/owner/update-name requires a key 'newName' in the request body 

{
	"newName" : "This is a new name"
}


Tables + Columns (can be seen in more detail in create_tables.py)

owner table 
	-id 
	-name 

property table 
	-id 
	-geoID
	-situsaddress
	-legalDescription
	-owner