def outputData(name, *args):      
    print( type(args) )      
    for arg in args:              
        print(arg)


outputData("John Smith", 5, True, "Jess")

def outputData(**kwargs):      
    print( type(kwargs) )      
    print( kwargs[ "name" ] )      
    print( kwargs[ "num" ] )
    
outputData(name = "John Smith", num = 5, b = True)