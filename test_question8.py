import pytest
import question8 as q
import yaml

yaml_file = 'data/question8.yaml'
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
function_names = [f'question8_{i}' for i in range(1, 5)]

def yaml_data():
    return get_subquestions("data/question8.yaml")  # Side effect

@pytest.mark.parametrize("func_name, index", [(fn, i) for i, fn in enumerate(function_names)])
def test_question8(func_name, index, subquestions, capsys):
    # Use getattr to dynamically get the function from the module q
    question = yaml_data()[index]
    correct_answer = question['Answer']
    answer = getattr(q, func_name)()

    if capsys.disabled():  # run with -s to see output
        print(f"{answer=}")
        print(f"{correct_answer=}")
    
    if isinstance(answer, str):
        answer = answer.lower().strip()
    if isinstance(answer, list):
        answer[0] = answer[0].lower().strip()
        answer[1] = answer[1].lower().strip()
   
    assert correct_answer == answer

