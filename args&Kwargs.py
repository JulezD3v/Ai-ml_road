# ...existing code...
count = 0  # global counter

def outUpdate(name, *args):
    global count
    count += 1
    print(type(args))
    for arg in args:
        print(arg)

outUpdate("Julie", 25, True, "Julie Kim")

def outputData(**kwargs):
    global count
    count += 1
    print(type(kwargs))
    print(kwargs["name"])
    print(kwargs["num"])
    print(kwargs["reg"])


outputData(name="John Smith", num=5, b=True, reg="pa106/g/19700/23")

ans = input("Write your name all in  caps: ")

# you can read the global without 'global'
print("Total calls counted:", count)
# ...existing code...

