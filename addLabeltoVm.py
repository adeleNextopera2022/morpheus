from typing import Any
import requests, csv, locale, urllib3, json

# Set the locale for the application
locale.setlocale(locale.LC_ALL, '')
# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define vars for API
host = "morphpoc.gesti.it" 
token = "291e0063-931b-4e65-a5ec-47bd618c330d"
headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": "BEARER " + (token)}

# Function to add a label to a Morpheus instance
def addLabelToVm(row: Any):
    # Get the instance details by name
    afunct = getInstancesIdByName(row[0])
    if afunct is None:
        print(f"Instance with name {row[0]} not found.")
        return
    
    instanceid = afunct['id']
    url = f"https://{host}/api/instances/{instanceid}"
    
    # Add a new label
    newLabel = "%s" % row[1]
    labels = afunct.get('labels', [])
    if newLabel not in labels:
        labels.append(newLabel)
    
    # Prepare the payload
    payload = {
        "instance": {
            "labels": labels
        }
    }
    body = json.dumps(payload)
    r = requests.put(url, headers=headers, data=body, verify=False)
    if r.status_code == 200:
        print(f"Successfully updated instance {instanceid}")
    else:
        print(f"Failed to update instance {instanceid}. Status code: {r.status_code}, Response: {r.text}")

# Function to get a server ID by name
def getInstancesIdByName(strName: Any):
    print("Get a id of server by Name")
    url = f"https://{host}/api/instances?name={strName}&vm=true&max=100"
    r = requests.get(url, headers=headers, verify=False)
    data = r.json()
    for a in data.get('instances', []):
        return a
    return None

# Main Method
with open('listvm.csv', newline='') as csvfile:
    # Create a CSV reader with a semicolon delimiter
    csvreader = csv.reader(csvfile, delimiter=';')
    i = 0
    for row in csvreader:
        if i != 0:
            addLabelToVm(row)
        i += 1
