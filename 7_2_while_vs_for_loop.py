year=int(input("please enter year\n"))
temp_year=year
while year<1450:
    year+=5
    print(year)

print("inside for loop")

year=int(input("please enter year\n"))
for x in range(temp_year,1450,5):
    print(x)
