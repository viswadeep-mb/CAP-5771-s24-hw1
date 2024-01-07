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

accepted_words = ['binary', 'discrete', 'continuous', 'nominal', 'ordinal', 'qualitative', 'quantitative', 'interval', 'ratio']

# Generate function names based on a naming convention
function_names = [f'question5_{i}' for i in range(1, 4)]

# Test that return values are lists
# Test that list elements only contain the words

@pytest.mark.parametrize("func_name", function_names)
def test_question5_list_return(func_name, subquestions):
    # Use getattr to dynamically get the function from the module q
    func = getattr(q, func_name)
    answer = func()
    print("answer: ", answer)
    assert isinstance(answer, dict), f"{answer} is not a dict"
    assert len(answer.keys()) == 3, f"{answer} has the wrong length"
    assert set(answer.keys()) == set(['bin1', 'bin2', 'bin3']), "The keys are incorrect"

