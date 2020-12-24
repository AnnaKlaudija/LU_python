n = input("Enter a number: ")

print(n + " + " + 2 * n + " + " + 3 * n + " = ", int(n) + int(2 * n) + int(3 * n))


h = input("Enter the height: ")
r = input("Enter the radius: ")

volume = 3.14 * int(r) * int(r) * int(h)
area = int(2) * 3.14 * int(r) * int(r) + int(h) * int(2) * 3.14 * int(r)

print("Volume: ", round(volume, 2))
print("Area: ", round(area, 2))

secondsentered = int(input("Enter the seconds: "))
minutestotal = secondsentered % 3600
hours = round((secondsentered - minutestotal) / 3600)
secondstotal = minutestotal % 60
minutes = round((minutestotal - secondstotal)/ 60)
seconds = round(minutestotal % 60)


print(str(hours) + " hours " + str(minutes) + " minutes and " + str(seconds) + " seconds")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number

print(str(first_number) + " + " + str(second_number) + " = " + str(addition))
print(str(first_number) + " - " + str(second_number) + " = " + str(subtraction))
print(str(first_number) + " * " + str(second_number) + " = " + str(multiplication))
print(str(first_number) + " / " + str(second_number) + " = " + str(division))

pigs = int(input("Enter the amount of pigs: "))
cows = int(input("Enter the  amount of cows: "))
chicken = int(input("Enter the  amount of chickens: "))

totalllegs = pigs*4 + cows*4 + chicken*2

print("Total amount of legs: " + str(totalllegs))



dalderi = int(input("Enter the number of Dalderi: "))
grasi = int(input("Enter the number of Grasi: "))
santimi = int(input("Enter the number of Santimi: "))

visisantimi = dalderi*37*162 + grasi*162 + santimi

jauniesantimi = visisantimi%100
jauniedalderi = (visisantimi-jauniesantimi)/100

print("Jaunie dālferi: ", round(jauniedalderi))
print("Jaunie santīmi: ", jauniesantimi)