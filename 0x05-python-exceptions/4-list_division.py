#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print('wrong type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        finally:
            if result:
                div_list.append(result)
            else:
                div_list.append(0)
    return div_list
