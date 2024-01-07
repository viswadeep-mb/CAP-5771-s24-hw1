import pytest
import question5 as q
import yaml

yaml_file = 'data/question5.yaml'
# Test that the answers to questions are Boolean

def get_subquestions(yaml_file):
    # Load the contents of the file into a dictionary
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    return data['Subquestions']

@pytest.fixture
def subquestions():
    return get_subquestions(yaml_file)

# Generate function names based on a naming convention
function_names = [f'question5_{i}' for i in range(1, 4)]

def yaml_data():
    return get_subquestions("data/question5.yaml")  # Side effect

@pytest.mark.parametrize("func_name, index", [(fn, i) for i, fn in enumerate(function_names)])

def test_question5_list_return(func_name, index, subquestions, capsys):
    # Use getattr to dynamically get the function from the module q
    question = yaml_data()[index]
    correct_answer = question['Answer']
    func = getattr(q, func_name)
    answer = func()

    answer = {key.lower(): value for key, value in answer.items()}
    correct_answer = {key.lower(): value for key, value in correct_answer.items()}

    # Everything lower case
    #if capsys.disabled():
        #print("answer: ", answer)
        #print("correct_answer: ", correct_answer)
    assert correct_answer['bin1'] == answer['bin1']

