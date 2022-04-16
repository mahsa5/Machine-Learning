#define a string with 0 and 1

def define_string(input_string):

    if '00' or '11' in input_string:
        print("unstable")
    
    for i in len(input_string):
        if i == '?':
            i = '0' or '1'
        
        if input_string[i] != input_string[i+1]:
            print("good string")




        
