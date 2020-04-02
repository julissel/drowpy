import stack


def is_braces_sequence_correct(seq: str) -> bool:
    """
    Check correctness of braces sequence in statement
    >>> is_braces_sequence_correct("()(())")
    True
    >>> is_braces_sequence_correct("()[()]")
    True
    >>> is_braces_sequence_correct(")")
    False
    >>> is_braces_sequence_correct("[(])")
    False
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()