# pilot navigation system

speed = int(input("Enter Altitude of plane :"))
if (speed < 3000):
    print("Pilot is ready for Safe landing the plane")
elif (speed > 3000 and speed < 6000):
    print("Pilot is ready to try for landing the plane come down to 3000 and open gear landing!!!")
elif (speed > 6000):
    print("Pilot is not to land the plane and go around!! ")