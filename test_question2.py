import pytest
import question2 as q
import yaml
#=====
import pytest_utils
try:
    from pytest_utils.pytest_utils.decorators import max_score, visibility
except:
    try:
        from pytest_utils.decorators import max_score, visibility
    except:
        from REFACTORED.pytest_utils.pytest_utils.decorators import max_score, visibility

from gradescope_utils.autograder_utils.decorators import (
    hide_errors,
    leaderboard,
    number,
    partial_credit,
    tags,
    weight,
)
#visibility,  # does not work in gradescope


#=====

yaml_file = 'data/question2.yaml'
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
function_names = [f'question2_{i}' for i in range(1, 6)]

def yaml_data():
    return get_subquestions("data/question2.yaml")  # Side effect

# @visibility does not work
@pytest.mark.parametrize("func_name, index", [(fn, i) for i, fn in enumerate(function_names)])
@max_score(15)
@visibility('hidden')
@hide_errors('Wrong answer!')
def test_question2_list_return(func_name, index, subquestions, capsys):
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

