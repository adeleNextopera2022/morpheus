import requests
import json
 
# Configurazione delle variabili
base_url = 'https://morphpoc.gesti.it/api'
api_token = '291e0063-931b-4e65-a5ec-47bd618c330d'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_token}'
}
 
# Funzione per ottenere tutte le VM scoperte
def get_discovered_vms():
    response = requests.get(f'{base_url}/zones/discover/instances', headers=headers)
    return response.json()
 
# Funzione per convertire una VM scoperta in una gestita
def convert_vm_to_managed(vm_id, group_id, tenant_id, username, password, instance_type, os_type, plan_id, tags):
    payload = {
        'groupId': group_id,
        'tenantId': tenant_id,
        'adminUsername': username,
        'adminPassword': password,
        'installAgent': False,  # No agent install
        'instanceType': instance_type,
        'osType': os_type,
        'planId': plan_id,
        'tags': tags
    }
    response = requests.post(f'{base_url}/zones/instances/{vm_id}/convert', headers=headers, data=json.dumps(payload))
    return response.json()
 
# Ottieni tutte le VM scoperte
discovered_vms = get_discovered_vms()
 
# Filtra le VM sulla rete denominata gst101
gst101_vms = [vm for vm in discovered_vms['instances'] if vm['network']['name'] == 'gst101']
 
# ID del gruppo gst-101
gst101_group_id = 'ID_DEL_GRUPPO_GST-101'
# ID del tenant
tenant_id = 'ID_DEL_TENANT'
# Credenziali amministrative
admin_username = 'admin_username'
admin_password = 'admin_password'
# Tipo di istanza
instance_type = 'instance_type_id'
# Tipo di sistema operativo
os_type = 'os_type_id'
# ID del piano
plan_id = 'plan_id'
# Tag (eventuale)
tags = [{'name': 'example_tag', 'value': 'example_value'}]
 
# Converti e assegna le VM al gruppo gst-101
for vm in gst101_vms:
    vm_id = vm['id']
    result = convert_vm_to_managed(vm_id, gst101_group_id, tenant_id, admin_username, admin_password, instance_type, os_type, plan_id, tags)
    print(f'VM {vm["name"]} converted: {result}')
 
print('Conversione completata.')