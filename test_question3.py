import pytest
import question3 as q
import yaml

yaml_file = 'data/question3.yaml'
# Test that the answers to questions are Boolean

def get_subquestions(yaml_file):
    # Load the contents of the file into a dictionary
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    return data['Subquestions']

@pytest.fixture
def subquestions():
    return get_subquestions(yaml_file)

#accepted_words = ['binary', 'discrete', 'continuous', 'nominal', 'ordinal', 'qualitative', 'quantitative', 'interval', 'ratio']

# Generate function names based on a naming convention
function_names = [f'question3_{i}' for i in range(1, 6)]

def yaml_data():
    return get_subquestions("data/question3.yaml")  # Side effect

@pytest.mark.parametrize("func_name, index", [(fn, i) for i, fn in enumerate(function_names)])

def test_question3_list_return(func_name, index, subquestions, capsys):
    # Use getattr to dynamically get the function from the module q
    question = yaml_data()[index]
    correct_answer = question['Answer']
    func = getattr(q, func_name)
    answer = func()
    # Everything lower case
    correct_answer = [w.lower() for w in correct_answer]
    answer = [w.lower() for w in answer]
    with capsys.disabled():
        print(f"{correct_answer=}")
        print(f"{answer=}")
    assert set(answer) == set(correct_answer)

