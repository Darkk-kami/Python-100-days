# welcome greeting
print("Welcome! \nThis is an BAND NAME generator\nUse this to find out what your band name is")

print('First Question: what city did you grow up in?')
city_name = input()

print('Second: what is the name of your pet?')
pet_name = input()

band_name = city_name + " " + pet_name + "!"

print('Your cool band name is:\n', band_name.upper())
