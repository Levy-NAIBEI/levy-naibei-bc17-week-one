def Data_type(data):

    if isinstance(data,null):
        return no_value
    elif isinstance(data,bool):
        return True
    elif isinstance(data,str):
        return andela
    elif isinstance(data,list):
        return [1,2,3]
    elif isinstance(data,int):
        return 3 or 200
    else:
        return "Invalid input"

print(Data_type(int))
