
type = input("insert type of conversion\n")
val = input("insert source value\n")

match type:
    case "F <-> C":
        if val[-1] == 'F':
            val=val[0:len(val)-1]
            print("the tempreture in Celsious is " + str(((float(val)-32)*5/9))+"\n" )
        elif val[-1] == 'C':
            val = val[0:len(val) - 1]
            print("the tempreture in Fahrenhiet is " + str((float(val)* 9 / 5)+32)+"\n")
        else:
            print("you inserted something incompatable\n")
    case  "MPH <-> KPH":
        if val[-3:] == "MPH":
            val = val[0:len(val) - 3]
            print("the speed in KPH is " + str(float(val)/0.621371192) + "\n")
        elif val[-3:] == 'KPH':
            val = val[0:len(val) - 3]
            print("the speed in MPH is " + str(float(val)*0.621371192) + "\n")
        else:
            print("you inserted something incompatable\n")
    case "kg <-> stone <-> lbs":
        if val[-2:] == "kg":
            val = val[0:len(val) - 2]
            print("the weight in lb is " + str(float(val) * 2.2 ) + " the weight in stone is " + str(float(val)* 0.1575 ) +"\n")
        elif val[-5:] == 'stone':
            val = val[0:len(val) - 5]
            print("the weight in lb is " + str(float(val) * 14 ) + " the weight in kg is " + str(float(val)* 6.35029 ) +"\n")
        elif val[-3:] == 'lbs':
            val = val[0:len(val) - 3]
            print("the weight in stone is " + str(float(val) / 14 ) + " the weight in kg is " + str(float(val)*0.45359237  ) +"\n")
        else:
            print("you inserted something incompatable\n")