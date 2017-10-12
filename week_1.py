def combine_str(string_no1, string_no2):
    """ Combines two strings and returns one output"""
    sl = []
    for i in range(len(string_no1+string_no2)):
        if i <= (len(string_no1)-1):
            sl.append(string_no1[i])
        if i <= (len(string_no2)-1):
            sl.append(string_no2[i])
    return print("".join(sl))
combine_str("1234","567ccxcxjlkjlkj8")

