#removing the local maximu

def list_n_array(input_list):
    
    if len(input_list) == 1:
        return input_list

    
    list_ = input_list[1:-1]
    operation = 0
    result =[]
    
    for i in list_:
        if list_[i+1] > list_[i] and list_[i+1] > list_[i+2]:
            list_[i+2] = list_[i+1]
            result.append(i+2)
            operation += 1   

    return operation, result


