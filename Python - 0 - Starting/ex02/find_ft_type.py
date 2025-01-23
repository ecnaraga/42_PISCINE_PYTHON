def all_thing_is_obj(object: any) -> int:
    if type(object) is type([]):
        print(f"List : {type(object)}")
    elif type(object) is type(()):
        print(f"Tuple : {type(object)}")
    elif type(object) is type({"", ""}):
        print(f"Set : {type(object)}")
    elif type(object) is type({}):
        print(f"Dict : {type(object)}")
    elif type(object) is type(""):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42
