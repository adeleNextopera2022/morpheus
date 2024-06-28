import requests
import json

# Configurazione delle variabili
base_url = 'https://morphpoc.gesti.it/api'
api_token = '291e0063-931b-4e65-a5ec-47bd618c330d'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_token}'
}
print("\nSTART")
# Funzione per ottenere tutte le VM
def get_all_vms():
    response = requests.get(f'{base_url}/servers', headers=headers)
    return response.json()

# Funzione per ottenere VM filtrate per zona e name
def get_filtered_vms_name(zone_id, name):
    response = requests.get(f'{base_url}/servers?zoneId={zone_id}&name={name}', headers=headers)
    return response.json()

# Funzione per ottenere VM filtrate per zona e tag
def get_filtered_vms_tags(zone_id, tag_name):
    response = requests.get(f'{base_url}/servers?zoneId={zone_id}&tags.name={tag_name}', headers=headers)
    return response.json()

# Funzione per ottenere VM filtrate per zona e name
def get_filtered_vms_name(zone_id, name):
    response = requests.get(f'{base_url}/servers?zoneId={zone_id}&name={name}', headers=headers)
    return response.json()

# Verifica con filtri
#print("\nVM filtrate per zona e name:")
#filtered_vms = get_filtered_vms_name(2, 'tn101clientypenull')
#print(json.dumps(filtered_vms, indent=4))
#print("\nEND")

print("\nVM filtrate per zona e tag:")
filtered_vms = get_filtered_vms_tags(2, 'VAR')
print(json.dumps(filtered_vms, indent=4))

# Verifica iniziale senza filtri
print("Tutte le VM:")
all_vms = get_all_vms()
print(json.dumps(all_vms, indent=4))