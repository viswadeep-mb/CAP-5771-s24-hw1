import pytest
import question9 as q
import yaml

valid_strings = ['cosine similarity', 'jaccard', 'euclidean', 'smc']

yaml_file = 'data/question9.yaml'
# Test that the answers to questions are Boolean

# Generate function names based on a naming convention
function_names = [f'question9_{i}' for i in range(1, 6)]

@pytest.mark.parametrize("func_name", function_names)
def test_question9(func_name, capsys):
    # Use getattr to dynamically get the function from the module q
    answer = getattr(q, func_name)()
    assert isinstance(answer, str), f"{answer} is not a str"
    assert answer.lower().strip() in valid_strings, f"{answer} is not in {valid_strings}"
