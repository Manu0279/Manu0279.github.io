import requests
import time 

headers = {
        'Authorization': 'Bearer 4bcc24136d6396d6c7c78b3eb29c1ea2',
    }
# def getResponse(method,planning_id ='',shift_id=''):



#     if planning_id != '':
#         planning_id = '/'+planning_id+'/shifts'
    
#     if shift_id != '':
#         shift_id = '/'+ shift_id +'/reservations'

#     url ='https://shiftheroes.fr/api/v1/plannings'+planning_id+ shift_id

#     if method == "post":
#         response = requests.post(url, headers=headers)
#     elif method == "get":
#         response = requests.get(url, headers=headers)
    
#     return response.json()

# #Get available Shifts
# def availableShifts(shifts):
#     availableShifts = []

#     for shift in shifts:
#         if shift['seats_taken'] < shift['seats']:
#             availableShifts.append(shift)
    
#     return availableShifts

# def schedule_shift(shift) : 

#     return 0

# #response = requests.get('https://shiftheroes.fr/api/v1/plannings/'+ plannings[2]['id'] + '/shifts', headers=headers)
# plannings = getResponse('get')
# shifts = getResponse('get', plannings[0]['id'])

# reservation = getResponse('post',plannings[0]['id'],shifts[1]['id'])

# print(reservation)
# # response = requests.post('https://shiftheroes.fr/api/v1/plannings/'+ planning_id + '/shifts/' + shift_id + '/reservations', headers=headers)
# print("********************Plannings************************************")
# for planning in plannings :
#     print(planning)
# print("********************Planning shifts*****************************")
# for shift in shifts :
#     print(shift)

# print("******************Available Shifts***********************")
# for availableshift in availableShifts(shifts):
#     print(getResponse('post',plannings[2]['id'],availableshift['id']))


# Lister les plannings 
def new_planning():
    liste_init = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
    new_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
    iterations = 0  # Compteur d'itérations

    while liste_init == new_liste:
        iterations += 1
        print(f"Recherche de nouveaux créneaux ... {iterations}")
        new_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
        time.sleep(2)

    print("Nouveau Planning !!")
    id_planning = new_liste[0].get("id") if new_liste else None
    print(f"ID new planning : {id_planning}")
    return id_planning

# Lister les créneaux
def shifts_list(id_planning):
    if id_planning is not None:
        liste_creneaux = requests.get(f'https://shiftheroes.fr/api/v1/plannings/{id_planning}/shifts', headers=headers).json()
        return liste_creneaux
    else:
        print("Aucun planning trouvé.")
        return []

# PRENDRE UNE RÉSERVATION
def reservations(id_planning, ids):
    c = 0 
    for id in ids:
        c += 1
        reservation = requests.post(f'https://shiftheroes.fr/api/v1/plannings/{id_planning}/shifts/{id}/reservations', headers=headers)
        print(f"Réservation {c}/{len(ids)}")
    print("JOB'S DONE !!")

if __name__ == "__main__":
    id_planning = new_planning()
    liste_creneaux = shifts_list(id_planning)
    # Récupérer les IDs des créneaux
    ids = [creneau["id"] for creneau in liste_creneaux]
    print(f"IDs de tous les créneaux : {ids}")
    reservations(id_planning, ids)