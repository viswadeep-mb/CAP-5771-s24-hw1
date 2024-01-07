import pytest
import question6 as q
import yaml

yaml_file = 'data/question6.yaml'
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
function_names = [f'question6_{i}' for i in range(1, 4)]

def yaml_data():
    return get_subquestions("data/question6.yaml")  # Side effect

@pytest.mark.parametrize("func_name, index", [(fn, i) for i, fn in enumerate(function_names)])

def test_question6_equal_width(func_name, index, subquestions, capsys):
    # Use getattr to dynamically get the function from the module q
    question = yaml_data()[index]
    correct_answer = question['Answer']
    answer = getattr(q, func_name)()
    if not capsys.disabled():
        #print(f"equal_width: {correct_answer=}")
        #print(f"equal_width: {answer=}")
        print(f"{answer['equal_width'][1]=}")
        print(f"{correct_answer['equal_width'][1]=}")
    assert correct_answer['equal_width'][0].lower() == answer['equal_width'][0].lower()
    assert correct_answer['equal_width'][1] == answer['equal_width'][1]

@pytest.mark.parametrize("func_name, index", [(fn, i) for i, fn in enumerate(function_names)])

def test_question6_equal_frequency(func_name, index, subquestions, capsys):
    # Use getattr to dynamically get the function from the module q
    question = yaml_data()[index]
    correct_answer = question['Answer']
    func = getattr(q, func_name)
    answer = func()
    if not capsys.disabled():
        #print(f"equal_frequency: {correct_answer=}")
        #print(f"equal_frequency: {answer=}")
        print(f"{answer['equal_frequency'][1]=}")
        print(f"{correct_answer['equal_frequency'][1]=}")
    assert correct_answer['equal_frequency'][0].lower() == answer['equal_frequency'][0].lower()
    try:
        assert correct_answer['equal_frequency'][1] == answer['equal_frequency'][1]
    except:
        assert answer['equal_frequency'][1] in correct_answer['equal_frequency'][1] 
