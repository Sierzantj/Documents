result = 0
number = 67
endbase = 4
for x in range(0,15):
           convdig = ((number % endbase**(x+1)) // endbase**x) * 10**x
           print(convdig)
           result = result + convdig
print("result\n" + str(result))
print(result)