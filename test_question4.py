import pytest
import question4 as q
import yaml

yaml_file = 'data/question4.yaml'
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
function_names = [f'question4_{i}' for i in range(1, 4)]

def yaml_data():
    return get_subquestions("data/question4.yaml")  # Side effect

@pytest.mark.parametrize("func_name, index", [(fn, i) for i, fn in enumerate(function_names)])

def test_question4_list_return(func_name, index, subquestions, capsys):
    # Use getattr to dynamically get the function from the module q
    question = yaml_data()[index]
    correct_answer = question['Answer']
    func = getattr(q, func_name)
    answer = func()
    answer = [w.lower().strip() for w in answer]
    # Everything lower case
    correct_answer = [w.lower() for w in correct_answer]
    if capsys.disabled():
        print("answer: ", answer)
        print("correct_answer: ", correct_answer)
    assert correct_answer[0] == answer[0] and correct_answer[1] == answer[1]

