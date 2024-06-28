import requests
import json

# Configurazione delle variabili
base_url = 'https://morphpoc.gesti.it/api'
api_token = '291e0063-931b-4e65-a5ec-47bd618c330d'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_token}'
}

print("\nSTART")  # Verifica che il programma inizi

# Funzione per ottenere VM filtrate per zona
def get_filtered_vms(zone_id):
    try:
        response = requests.get(f'{base_url}/servers?zoneId={zone_id}', headers=headers)
        response.raise_for_status()  # Controlla eventuali errori HTTP
        print("API chiamata riuscita")  # Stampa di debug per confermare che la chiamata API ha avuto successo
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore nella chiamata API: {e}")
        return None

# Verifica con filtri
print("\nVM filtrate per zona:")
filtered_vms_response = get_filtered_vms(2)

if filtered_vms_response:
    vms = filtered_vms_response.get('servers', [])

    # Filtra le VM in base al tag 'VAR'
    filtered_vms = [vm for vm in vms if any(tag.get('name') == 'VAR' for tag in vm.get('tags', []))]
    
    if filtered_vms:
        # Stampa le VM filtrate
        print(f"Numero di VM con il tag 'VAR': {len(filtered_vms)}")
        print("VM filtrate con tag 'VAR':")
        print(json.dumps(filtered_vms, indent=4))
    else:
        print("Nessuna VM trovata con il tag 'VAR'.")
else:
    print("Nessuna VM trovata o errore nell'API")

print("\nEND")  # Verifica che il programma termini
