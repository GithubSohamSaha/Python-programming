def filter_users_by_phone_number_ends_in_5(users):
    print("Users whose phone number ends in 5:")
    for user in users:
        if user['phone'].endswith('5'):
            print(user['name'])

def filter_users_without_email(users):
    print("Users without email address listed:")
    for user in users:
        if 'email' not in user:
            print(user['name'])

def filter_users_by_phone_number_starts_with_9(users):
    print("Users whose phone number starts with 9:")
    for user in users:
        if user['phone'].startswith('9'):
            print(user['name'])

# Given dictionary of users
users = [
    {'name': 'Ram', 'phone': '9434141414', 'email': 'ram@gmail.com'},
    {'name': 'Laksman', 'phone': '8434151515'},
    {'name': 'Bharat', 'phone': '7474161616', 'email': 'bharat@gmail.com'},
    {'name': 'Satrughna', 'phone': '9478171717', 'email': 'satrughna@gmail.com'}
]

# (a) Filter users whose phone number ends in 5
filter_users_by_phone_number_ends_in_5(users)

# (b) Filter users without email address listed
filter_users_without_email(users)

# (c) Filter users whose phone number starts with 9
filter_users_by_phone_number_starts_with_9(users)
