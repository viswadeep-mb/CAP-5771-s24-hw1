import pytest
import question2 as q
import yaml

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

accepted_words = ['binary', 'discrete', 'continuous', 'nominal', 'ordinal', 'qualitative', 'quantitative', 'interval', 'ratio']

# Generate function names based on a naming convention
function_names = [f'question2_{i}' for i in range(1, 6)]

# Test that return values are lists
# Test that list elements only contain the words

@pytest.mark.parametrize("func_name", function_names)
def test_question2_list_return(func_name, subquestions):
    # Use getattr to dynamically get the function from the module q
    func = getattr(q, func_name)
    answer = func()
    assert isinstance(answer, list), f"{answer} is not a list"

@pytest.mark.parametrize("func_name", function_names)
def test_question2_word_in_list(func_name, subquestions):
    # Use getattr to dynamically get the function from the module q
    func = getattr(q, func_name)
    answer = func()

    # Check that the answer list only contains accepted words
    for word in answer:
        assert word.lower() in accepted_words, f"{word} not in {accepted_words}"
