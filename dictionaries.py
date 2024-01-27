phone_number = {'ram': 1234, 'avi': 8249159831, 'raja': 23723828}
print(phone_number)
phone_number['avi'] = {'home': 8658927325, 'work': 8249159831}
print(phone_number)
print(phone_number['avi']['home'])
name = {0: 'avi', 5: 'disha', 8: 'avishek'}
print(name[5])
del phone_number['avi']
print(phone_number)
# phone_number.clear() #for clear all key value pair
# print(phone_number)
print(phone_number.keys()) 
print(phone_number.values())