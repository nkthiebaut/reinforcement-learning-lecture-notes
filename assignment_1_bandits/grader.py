import os
import numpy as np

class IncorrectAnswerException(Exception):
    pass

def test(got, expected, feedback=None):
    if got == expected:
        return

    expect_string = f'got: <{got}>, but expected: <{expected}>'

    if feedback is None:
        feedback = expect_string
    else:
        feedback = f'{feedback}\n   {expect_string}'

    raise IncorrectAnswerException(feedback)

def record(file_name, answer):
    os.makedirs('responses', exist_ok=True)
    np.save(f'responses/{file_name}', answer)
