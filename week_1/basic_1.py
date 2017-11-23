def combine_str(string_no1, string_no2):
    """ Combines two strings and returns one output"""
    str_list = []
    
    for i in range(len(string_no1 + string_no2)):

        if i <= (len(string_no1)-1):
            str_list.append(string_no1[i])

        if i <= (len(string_no2)-1):
            str_list.append(string_no2[i])

    return ("".join(str_list)) # makes the list(str_list) a string 
