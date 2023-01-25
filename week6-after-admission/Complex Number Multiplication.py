class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        return multiply(num1, num2)
        
        
def multiply(string_num_1, string_num_2):
    real1, imaginary1 = extract_numbers(string_num_1)
    real2, imaginary2 = extract_numbers(string_num_2)
    
    result_real = real1*real2 - imaginary1*imaginary2
    result_complex = real1*imaginary2 + real2*imaginary1
    
    string_form =  turn_to_string((result_real, result_complex))
    return string_form
    
    
def turn_to_string(complex_num):
    string_form =  f"{complex_num[0]}+{complex_num[1]}i"
    return string_form
    

def extract_numbers(string_form):
    match = re.match("(-*\d+)\+(-*\d+)", string_form)
    groups =  match.groups()
    
    real = int(groups[0])
    imaginary = int(groups[1])
    
    return (real, imaginary)

#30min
#3sub