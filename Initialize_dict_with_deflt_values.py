print("Exercise 4: Initialize dictionary with default values")
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# Expected output
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
a = {}
for i in employees:
    a[i]=defaults
print(a)