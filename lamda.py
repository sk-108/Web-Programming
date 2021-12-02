people = [
    {"Name" : "sourav","house" : "bihar "},
    {"Name" : "nitesh","house" : "jharkhand"},
    {"Name" : "alok ","house" : "up "}
]

# def f(person) :
#     return person["house"]

people.sort(key= lambda person : person["Name"])

print(people)
 