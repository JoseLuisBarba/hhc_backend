def bin_packing_heuristic(caregivers, vehicles):
    vehicles_packing = []
    caregivers_assigned = []  

    for vehicle in vehicles:
        max_capacity = vehicle['capacity']
        current_capacity = 0
        caregivers_selected = []
        max_skill = 0

        for caregiver in caregivers:

            if caregiver not in caregivers_assigned:

                if current_capacity < max_capacity:
                    caregivers_selected.append(caregiver)
                    caregivers_assigned.append(caregiver)
                    current_capacity += 1
                    max_skill += caregiver['skill']

        vehicles_packing.append({
            "id": vehicle["id"],
            "reg_num": vehicle["reg_num"],
            "MAX_Q": max_skill,
            "MIN_Q": 0,
            "VD": vehicle["average_speed"],
            "FLETE": vehicle["freight_km"],
            "CC": 0.35,
            "EM": 2.7,
            "caregivers": caregivers_selected
        })

    return vehicles_packing


# caregivers = [
#     {
#         "dni": "70659591",
#         "skill": 50,
#         "schedule_id": 0,
#         "email": "barba@example.com",
#         "name": "Jose",
#         "lastname": "Barba",
#         "is_active": True,
#         "phone": "973697758",
#         "birthdate": "2001-11-19",
#         "createdAt": "2024-02-06T20:37:38"
#     },
#     {
#         "dni": "70659592",
#         "skill": 40,
#         "schedule_id": 0,
#         "email": "sam@example.com",
#         "name": "Sam",
#         "lastname": "Llo",
#         "is_active": True,
#         "phone": "973697758",
#         "birthdate": "2001-11-19",
#         "createdAt": "2024-02-06T20:37:38"
#     },
#     {
#         "dni": "70659593",
#         "skill": 45,
#         "schedule_id": 0,
#         "email": "jane@example.com",
#         "name": "Jane",
#         "lastname": "Doe",
#         "is_active": True,
#         "phone": "973697758",
#         "birthdate": "2001-11-19",
#         "createdAt": "2024-02-06T20:37:38"
#     },
#     {
#         "dni": "70659594",
#         "skill": 55,
#         "schedule_id": 0,
#         "email": "john@example.com",
#         "name": "John",
#         "lastname": "Doe",
#         "is_active": True,
#         "phone": "973697758",
#         "birthdate": "2001-11-19",
#         "createdAt": "2024-02-06T20:37:38"
#     },
#     {
#         "dni": "70659595",
#         "skill": 60,
#         "schedule_id": 0,
#         "email": "alice@example.com",
#         "name": "Alice",
#         "lastname": "Smith",
#         "is_active": True,
#         "phone": "973697758",
#         "birthdate": "2001-11-19",
#         "createdAt": "2024-02-06T20:37:38"
#     },
# ]


# import random

# vehicles = []

# for i in range(10):
#     capacity = random.randint(2, 5)
#     vehicle = {
#         "id": i + 1,
#         "reg_num": f"vehicle_{i + 1}",
#         "capacity": capacity,
#         "average_speed": 40,
#         "freight_km": 15,
#         "is_active": True,
#         "createdAt": "2024-02-06T20:45:51.829Z"
#     }
#     vehicles.append(vehicle)



# result = bin_packing_heuristic(caregivers, vehicles)

# for i in result:
#     print(f"Vehículo: {i}")