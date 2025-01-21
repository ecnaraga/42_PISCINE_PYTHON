def NULL_not_found(object: any) -> int:
    if not object :
        if type(object) == type(None) :
            print(f"Nothing: {object} {type(object)}")
        elif type(object) == type(0) :
            print(f"Zero: {object} {type(object)}")
        elif type(object) == type(" ") :
            print(f"Empty: {type(object)}")
        elif type(object) == type(False) :
            print(f"Fake: {object} {type(object)}")
        return 0
    elif type(object) == type(0.0) and str(object) == str(float('NaN')):
        print(f"Cheese: nan {type(object)}")
        return 0
    else :
        print("Type not Found")
        return 1