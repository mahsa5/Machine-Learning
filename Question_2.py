#sum of two numbers in a number : 10038 ---> 10011

def base_ten(input_number):
    sum = 0
    number_of_digit = 0
    if number_of_digit == 1:
        return input_number

    else:
        str_input_number = str(input_number)
    tmp = []
    for i in str_input_number:
        sum = str(int(str_input_number[i]) + int(str_input_number[i+1]))
        new_number = int(str_input_number.replace(str_input_number[i:i+2], sum))
        tmp.append(new_number)
    
    return tmp