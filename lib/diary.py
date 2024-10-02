def make_snippet(string):
    split = string.split()
    if len(split) <= 5:
        return string
    return ' '.join(split[:5]) + ' ...'
