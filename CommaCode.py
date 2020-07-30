a_list = ['apples', 'bananas', 'tofu', 'cats']


def list_to_string(some_list):
    a_string = ', '.join(some_list)
    return a_string


new_string = list_to_string(a_list)

print(new_string)
