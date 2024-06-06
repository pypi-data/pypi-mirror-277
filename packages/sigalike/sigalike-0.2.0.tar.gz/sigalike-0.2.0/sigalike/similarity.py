import string

import numpy as np

from sigalike.utils import check_content, check_input_type


def _preprocess(s: str) -> str:

    # replace punctuation with whitespace
    s = s.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))

    s = s.lower()
    s = s.strip()

    return s


def shifted_sigmoid_similarity(str1: str, str2: str, shift: int = 4, preprocess: bool = True) -> float:
    """Calculates the shifted sigmoid similarity score between two strings.

    The shifted sigmoid similarity score acts as a fuzzy string matching
    metric. It begins with the ratio of unique tokens from the shorter
    string that are present in the longer string and then subtracts a penalty
    using a shifted sigmoid function (the logistic function) and the difference
    in length between the two token sets.

    Parameters
    ----------
    str1 : str
        The first string to compare.
    str2 : str
        The second string to compare.
    shift : int, default 4
        Amount to shift sigmoid curve.
    preprocess : bool, default True
        Whether or not to run built-in preprocessing.

    Returns
    -------
    float
        Shifted sigmoid similarity score.
    """
    check_input_type(str1, str)
    check_input_type(str2, str)
    check_input_type(shift, int)
    check_input_type(preprocess, bool)
    check_content(str1)
    check_content(str2)

    if preprocess is True:
        str1 = _preprocess(str1)
        str2 = _preprocess(str2)

        # re-check contents
        check_content(str1)
        check_content(str2)

    set_str1 = set(str1.split())
    set_str2 = set(str2.split())
    smaller_set = min(len(set_str1), len(set_str2))
    larger_set = max(len(set_str1), len(set_str2))

    num_matched = len(set_str1.intersection(set_str2))
    match_ratio = num_matched / smaller_set
    num_extra = larger_set - num_matched

    score = match_ratio
    # Penalize if non-perfect match
    if score > 0 and num_extra > 0:
        score -= 1 / (1 + np.exp(-num_extra + shift))

    return max(score, 0)
