cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
averege_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars avaiable."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", averege_passengers_per_car, "in each car."
print ("Hey %s there" % "trung") # Co the k dung dau ()

'''
Cau hoi: 
1. Bien space_in_a_car = 4.0, neuthay bang 4 thi sao?
=> carpool_capacity = cars_driven * space_in_a_car = 30 * 4 = 120 thay vi 120.0
2. Chu y: 4.0 la kieu so dau phay dong (floating point number)
3. Hieu y nghia tung dong lenh tren
4. Chac chan rang ban hieu phep "=" la phep gan gia tri cho bien
5. Chu y khong co dau cach trong ten bien
6. Cach viet in gia tri cua bien thong qua % nhu tren.
Cau truc nay trong C:
print("Hey %s there", %"trung")
'''