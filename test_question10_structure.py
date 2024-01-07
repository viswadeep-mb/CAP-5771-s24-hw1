import pytest
import question10 as q
import yaml

yaml_file = 'data/question10.yaml'

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
function_names = [f'question10_{i}' for i in range(1, 11)]

@pytest.mark.parametrize("func_name", function_names)
def test_question10_bool_return(func_name, subquestions):
    # Use getattr to dynamically get the function from the module q
    func = getattr(q, func_name)
    answer = func()
    assert type(answer) == bool, f"{answer} is not a bool"
