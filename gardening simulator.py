class Tree:
    def __init__(self, name, sunOrRain,waterTolerance,windTolerance,snowTolerance):
        self.name=name
        self.sunOrRain=sunOrRain
        self.waterTolerance=waterTolerance
        self.windTolerance=windTolerance
        self.snowTolerance=snowTolerance
    def __str__(self):
        return "prefered weather:% s Rain Tolerance is:% s Wind Tolerance:%s, snow tolerance method:%s" % (self.sunOrRain, self.waterTolerance, self.windTolerance,self.snowTolerance )
    def __repr__(self):
        return "prefered weather:% s Rain Tolerance is:% s Wind Tolerance:%s, snow tolerance method:%s" % (self.sunOrRain, self.waterTolerance, self.windTolerance,self.snowTolerance )

oakTree = Tree("oakTree","Rain","medium" ,"high" ,1 )
almondTree=Tree("almondTree","sun","high" ,"medium" ,2 )
appleTree=Tree("appleTree","Rain","low"  ,"high" ,60 )
array = [oakTree,appleTree,almondTree]

weather = input("whats the weather like?")
for each in array:
    if(each.sunOrRain==weather):
        print(each.name)
        print(each)

RainLevel= input("how much rain is there?")
for each in array:
    if(each.waterTolerance==RainLevel):
        print(each.name)
        print(each)

WindLevel= input("how much wind is there?")

for each in array:
    if(each.windTolerance==WindLevel):
        print(each.name)
        print(each)

SnowLevel= input("how much snow is there?")

for each in array:
    if(each.snowTolerance<=SnowLevel):
        print(each.name + "died")
        print(each)


