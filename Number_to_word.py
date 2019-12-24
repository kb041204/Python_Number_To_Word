#input and check number within range
def input_number (min, max):
    incorrect = 1

    #print("Please enter an integer from " + str(min) + " to " + str(max) + ".")
    print("Please enter an integer from (-10^66 + 1) to (10^66 - 1).")
    while (incorrect):
        try:
            number = int(input())
            incorrect = 0
        except ValueError: #Wrong data type
                print("\Wrong data type. Please try again.")
                incorrect = 1
                
        if (incorrect == 0 and (number > max or number < min)): #out of range
            #print("\nNumber not between" + str(min) + " and " + str(max) + ". Please try again.")
            print("\nNumber not between (-10^66 + 1) and (10^66 + 1). Please try again.")
            incorrect = 1 
    return number


#single digit
def single_digit (number):
    single_place_list = ["","one","two","three","four","five","six","seven","eight","nine"]
    return single_place_list[number]


#double digit
def double_digit (multiple_of_ten, number):
    string = ""
    ten_special = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    normal_shit = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if (number <= 19 and number >= 10): #10~19
        string = ten_special[number-10]
    else:
        if (multiple_of_ten): #multiple of 10 (omit single digit)
            string = normal_shit[int(number / 10)]
        else:
            string = normal_shit[int(number / 10)] + " " + single_digit(number % 10)
    return string


#hundred
def hundred (number):
    string = ""
    if (number == 0): #zero
        string = "zero"
    elif (int(number / 100) != 0): #Bigger than 99
        string = single_digit(int(number/100)) + " hundred"
        
        if (number % 10 == 0): #multiple of 10
            if (number % 100 != 0):
                string = string + " " + double_digit(1, number % 100)
        else:
            string = string + " " + double_digit(0, number % 100)
            
    elif (int(number / 10) == 0): #Less than 10
        string = single_digit(number)

    else: #10~99
        if (number % 10 == 0): #multiple of 10
            string = string + double_digit(1, number % 100)
        else:
            string = string + double_digit(0, number % 100)
            
    return string


#separater
def separater (number):
    string = ""

    if (number < 0):
        string = "negative "
        number = number * -1
    
    first_group_divisor = 0
    
    large_number =  ["vigintillion", "novemdecillion", "octodecillion", "septendecillion", "sexdecillion",
                     "quindecillion", "quattuordecillion", "tredecillion", "duodecillion", "undecillion",
                     "decillion", "nonillion", "octillion", "septillion", "sextillion", "quintillion",
                     "quadrillion", "trillion", "billion", "million", "thousand", ""]
                    #10^63, 10^60, ... , 10^6, 10^3

    number_of_loop = int( (len(str(number))-1) / 3)

    if (number_of_loop != 0): #larger than 999
        first_group_divisor = pow(10,  (int((len(str(number))-1)/ 3)* 3) ) #first 1~3 number
        string = string + hundred ( int(number / first_group_divisor)) + " " + large_number[(number_of_loop+1)*-1] + " "
        number = number - int(number / first_group_divisor) * first_group_divisor #only 3n number left, n > 1
        
        for i in reversed(range(0, number_of_loop)): #remaining 3-digit pairs
            first_three_number = int((number / pow(10,i*3))) #first three digits

            if(first_three_number != 0): #all three digits are 0
                string = string + hundred ( first_three_number ) + " " + large_number[(i+1)*-1] + " "
                
            number = number - first_three_number * pow(10, 3*i) #remaining digits

            #print(string)
    else:
        string = string + hundred (number)

    return string
        

#main body
def main():
    minimum = (pow(10,66)-1) * -1   #inclusive
    maximum = pow(10,66)-1          #inclusive
    
    input_no = input_number(minimum, maximum)
    print(separater(input_no) + "\n")

    
main()
