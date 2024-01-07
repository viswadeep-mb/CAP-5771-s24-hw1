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

# Test that return values are lists
# Test that list elements only contain the words

@pytest.mark.parametrize("func_name", function_names)

def test_question6(func_name, subquestions, capsys):
    # Use getattr to dynamically get the function from the module q
    func = getattr(q, func_name)
    answer = func()
    keys = [k.lower().strip() for k in answer.keys()]
    values = list(answer.values())
    values0 = [v[0].lower().strip() for v in values]
    values1 = [v[1] for v in values]
    
    for v in values0:
        assert(v in ['no change', 'change']), f"{v} is not among the specified choices"

    for v in values1:
        assert(isinstance(v, int)), f"{v} is not an int"

    #if capsys.disabled():
        #print(f"{values0=}")
        #print(f"{values1=}")

    assert isinstance(answer, dict), f"{answer} must be a dict"
    assert len(keys) == 2, "{answer} must be a dictionary with two keys"
    assert set(keys) == set(['equal_frequency', 'equal_width']), "The keys are not among the specified choices"

