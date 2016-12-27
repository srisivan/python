
# A program to calculate momentum and velocity of a given object.

print(" ")
print(''' This is a program to calculate a particular object's velocity and  momentum.\n 



As we know, p = mv, where p = momentum, m = mass, v = velocity.\n

We need two things to find a object's momentum. These are:
a.It's mass 
b.It's velocity.\n


Again, as we know, v = d/t , where v = velocity, d = distance, t = time.

We need two things to find a object's velocity.These are: 
a.It's displacement
b.The time taken to displace.

First, to find the object's velocity.\n''')

preference = (input("Do yo need the velocity to be in metres/seconds, or kilmetres/hours?  Enter (m/s) for metres/seconds and (km/h) for kilometres/hours.\n"))

Mass = int(input("Please enter the object's mass, in kilograms.\n"))

if (preference == "km/h") :
    Distance = int(input("Please enter the displacement of the object, in terms of kilometres.\n"))
    Time = int(input("Please enter the time the object took to displace, in terms of hours.\n"))
    
    Velocity_hours = Distance / Time 
     
    print("As you know, velocity = distance/time.")
            
    print("So,according to your submission, v = %s / %s .\n" % (Distance , Time))

    print("The velocity of the given object = %s km/h.\n" % (Velocity_hours))

    print("Now to find the object's momentum.\n")
    
    print("As you know, p = mv. We have accquired the velocity of the given object. The mass you have given is %s. " % ( Mass)) 
    print("We needn't worry about the velocity of the the object, which we have already found. ( Velocity = %s)\n" % (Velocity_hours))

    momentum_hours = Mass * Velocity_hours

    print("The momentum of the given object in terms of km/h, is %s." % (momentum_hours))


elif  (preference == "m/s") :

    Distance_2 = int(input("Please enter the displacement of the object, in terms of metres.\n"))
    Time_2 = int(input("Please enter the time the object took to displace, in terms of seconds.\n"))

    Velocity_seconds = Distance_2 / Time_2 

    print("As you know, velocity = distance/time.")
    print("So, according to your submission, v = %s / %s ." % (Distance_2 , Time_2))

    print("The velocity of the given object = %s m/s.\n" % (Velocity_seconds))

    print("Now to find the object's momentum.\n")
    print("As you know, p = mv. We have accquired the velocity of the given object. The mass you have given is %s." % (Mass))


    print("We needn't worry about the velocity of the the object, which we have already found.( Velocity = %s)\n"  % ( Velocity_seconds)) 
    
    momentum_seconds = Mass * Velocity_seconds

    print("The momentum of the given object, in terms of m/s, is %s." % ( momentum_seconds))


else :
    print("invalid entry")








 
