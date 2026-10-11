#type_check.py
#This program checks and converts data types.
#Predictions:
#8080 is int
#"8080" is str
#99.5 is float
#"198.51.100.7" is str
#1_000 is int
print(type(8080))
print(type("8080"))
print(type(99.5))
print(type("198.51.100.7"))
print(type(1_000))
port =int("443")
number =str(8080)
value =float("2.5")
print(port, type(port))
print(number, type(number))
print(value, type(value))
