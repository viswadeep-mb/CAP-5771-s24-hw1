import pytest
import question7 as q
import yaml

yaml_file = 'data/question7.yaml'
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
function_names = [f'question7_{i}' for i in range(1, 3)]

def yaml_data():
    return get_subquestions("data/question7.yaml")  # Side effect

yaml_data()

@pytest.mark.parametrize("func_name, index", [(fn, i) for i, fn in enumerate(function_names)])
def test_question7_ab(func_name, index, subquestions, capsys):
    # Use getattr to dynamically get the function from the module q
    question = yaml_data()[index]
    correct_answer = question['Answer'].lower().strip()
    answer = getattr(q, func_name)().lower().strip()
    assert correct_answer == answer

@pytest.mark.parametrize("func_name, index", [(fn, i) for i, fn in enumerate(function_names)])
def test_question7_c(func_name, index, capsys):
    # Use getattr to dynamically get the function from the module q
    question = yaml_data()[2]
    correct_answer = question['Answer']
    answer = getattr(q, 'question7_3')()
    #if capsys.disabled():
        #print(f"{correct_answer=}, {type(correct_answer)=}")
        #print(f"{answer=}, {type(answer)=}")

    for a, b in zip(correct_answer, answer):
        assert list(a) == list(b)

