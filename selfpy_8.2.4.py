# 8.2.4
#################


def sort_anagrams(list_of_strings):
    """This function does something with list"""
    sorted_list_of_string = list()
    returned_list_of_strings = list()
    elements_bank = list()
    for element in list_of_strings:
        sorted_element = ''.join(sorted(element))
        sorted_list_of_string.append(sorted_element)
    for element in sorted_list_of_string:
        if element not in elements_bank:
            element_list = list()
            for i in range(len(sorted_list_of_string)):
                if sorted_list_of_string[i] == element:
                    element_list.append(list_of_strings[i])
                    elements_bank.append(element)
            returned_list_of_strings.append(element_list)
        else:
            continue
    return returned_list_of_strings
