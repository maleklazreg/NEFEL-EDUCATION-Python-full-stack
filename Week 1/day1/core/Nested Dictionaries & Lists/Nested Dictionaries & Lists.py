#update values
x = [[5,2,3],[10,8,9]]
students = {
    {'first_name': 'michael','last_name':'jordan'},
    {'first_name': 'john','last_name':'rosales'}
}
sports = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x':10,'y':20}]

x[1][0] = 15
sports["basketball"][1] = "briant"

sports["football"][0] = "andres"

z[0]["y"] = 30

def itrtdictionary(x):
    for i in range(len(x)):
        print(f"{"first_name"} - {x[i]["first_name"]} - {"last_name"} - {x[i]["last_name"]}")
itrtdictionary(students)

def itrsdictionary2(a,b):
    for i in range(len(a)):
        print(b[i][a])

itrsdictionary2("first_name", students)
print("*"*20)
itrsdictionary2("last_name", students)
print("*"*20)

def info(kamous):
    for key1 in kamous:
        print(f"{len(kamous[key1])} {key1}")
        for key2 in kamous[key1]:
            print(key2)

info(sports)

