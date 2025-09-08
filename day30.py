def Supper():
    pass

def supper_match():
    day = "Sunday"
    match day:
        case "Sunday":
            return "Chapati and Cabbage"
        case "Monday":
            return "Ugali and Sukuma"
        case "Tuesday":
            return "Githeri and Avocado"
        case "Wednesday":
            return "Rice and Ndengu stew"
        case "Thursday":
            return "Mushed potatoes and stew"
        case "Friday":
            return "Leftover Friday"
        case "Saturday":
            return "Ugali and Sukuma"
        case default:
            return "Enter a valid day"
        
if __name__ =="__main__":
    print(supper_match())

word = "hello"
print(word[0:5:2])


data = [5, "book", [ 34, "hello" ], True]
print(data[2])
print(data[2][1])