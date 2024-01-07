import pytest
import question10 as q
import yaml
import os

def get_problem_statement(yaml_file):
    # Load the contents of the file into a dictionary
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    return data['Statement']

def get_subquestions(yaml_file):
    # Load the contents of the file into a dictionary
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    return data['Subquestions']

@pytest.fixture
def subquestions():
    subquestions = get_subquestions("data/question10.yaml")
    return subquestions

def yaml_data():
    return get_subquestions("data/question10.yaml")  # Side effect

function_names = [f'question10_{i}' for i in range(1, len(yaml_data()) + 1)]

@pytest.mark.parametrize("func_name, index", [(fn, i) for i, fn in enumerate(function_names)])

def test_question10(func_name, index, subquestions):
    question = yaml_data()[index]
    correct_answer = question['Answer']
    func = getattr(q, func_name)
    answer = func()
    print("==> correct_answer: ", correct_answer)
    print("==> answer: ", answer)
    assert answer == correct_answer

