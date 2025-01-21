def all_thing_is_obj(object: any) -> int :
    if type(object) in [type([]), type(()), type({"",""}), type({})] :
        print(f"{object} : {type(object)}")
    elif type(object) == type("") :
        print(f"{object} is in the kitchen : {type(object)}")
    else :
        print("Type not found")
    return 42