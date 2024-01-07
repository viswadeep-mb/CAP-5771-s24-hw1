import utils as u

# In test: lower case, no duplicates
# Handle multiple possible answers

# Use as an example
def question5_1():
    # Use set of dict['bin1'].value
    answer = {
            'bin1': [1,2,3,4,5], 
            'bin2': [6,7,8],
            'bin3': [9]
    }
    return answer

def question5_2():
    answer =  {
        'bin1': [1, 2, 3],
        'bin2': [4, 5, 6],
        'bin3': [7, 8, 9]
    }
    return answer

def question5_3():
    answer = {
        'bin1': [1, 2, 3, 4],
        'bin2': [5, 6, 7],
        'bin3': [8, 9]
    }
    return answer 


# change order. Add a word. 
# Need structural test to pass before answer test pass. 
