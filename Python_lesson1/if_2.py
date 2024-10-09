a = "I am a Data Scientist"
if "Data" in a:
 print("It is present")
else:
 print(False)   

first = 25
second = 34
third = 45
if first >= second and first >= third:
 print(first)
elif second >= first and second >= third:
 print(second)
elif third >= first and third >= second:
 print(third)
else:
 print("All of the values are equal")