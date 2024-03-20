import json

people_string = '''
{
    "people":[
    {
        "name": "Ayush Kasliwal",
        "phone":"9764564185",
        "emails":["akasliwal1611@gmail.com", "kasliwalayush123@gmail.com"],
        "has_license": false
    },
    {
        "name": "AK",
        "phone": "9156525532",
        "emails": "ayushkasliwal2001@gmail.com",
        "has_license": true
    }0
    ]    
}
'''
 
data = json.loads(people_string)

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=4, sort_keys=True)

print(new_string)
