import pytest
import question7 as q
import yaml

yaml_file = 'data/question7.yaml'
# Test that the answers to questions are Boolean

accepted_answers = ['increase/decrease', 'the same', 'non-increasing', 'non-decreasing', 'no change']

# Generate function names based on a naming convention
function_names = [f'question7_{i}' for i in range(1, 3)]

# Test that return values are lists
# Test that list elements only contain the words

@pytest.mark.parametrize("func_name", function_names)

def test_question7_ab(func_name, capsys):
    # Use getattr to dynamically get the function from the module q
    answer = getattr(q, func_name)()
    assert answer in accepted_answers, f"{answer} is not in {accepted_answers}"

def test_question7_c_answer_list_of_tuples(capsys):
    #answer = [(0., 4.), (4., 5.), (5., 8.), (8., 'infinity')]
    answer= getattr(q, 'question7_3')()
    if capsys.disabled():
        print("answer: ", answer)
    # Answer is a list of tuples
    assert isinstance(answer, list), f"answer is not a list"
    assert len(answer) == 4, f"The answer should have length 4"
    for answ in answer:
        assert isinstance(answ, tuple) or isinstance(answ, list), "The answer is not a list or a tuple"
        for i in [0, 1]:
            assert isinstance(answ[i], float) or isinstance(answ[i], str), f"{answ[i]} should be a list or a str"
            if isinstance(answ[i], str):
                assert answ[i].lower().strip() == 'infinity', f"{answ[i]} should be the string 'infinity'"
