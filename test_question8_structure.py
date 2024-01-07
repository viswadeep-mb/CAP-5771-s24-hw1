import pytest
import question8 as q
import yaml

valid_strings = ['x1', 'x2', 'x3', 'y1', 'y2', 'y3']

yaml_file = 'data/question8.yaml'
# Test that the answers to questions are Boolean

# Generate function names based on a naming convention
function_names = [f'question8_{i}' for i in range(1, 5)]

@pytest.mark.parametrize("func_name", function_names)
def test_question8(func_name, capsys):
    # Use getattr to dynamically get the function from the module q
    answer = getattr(q, func_name)()
    assert isinstance(answer, list) or isinstance(answer, str), f"answer is neither a list or a string"
    if isinstance(answer, list):
        # list of two strings
        assert len(answer) == 2, f"{answer} must be a list of length 2"
        assert answer[0] in valid_strings, f"{answer[0]} is not in {valid_strings}"
        assert answer[1] in valid_strings, f"{answer[1]} is not in {valid_strings}"

    if isinstance(answer, str):
        assert answer == "equally similar", f"{answer} is the incorrect string"
