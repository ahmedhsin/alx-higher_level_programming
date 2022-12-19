#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            val1 = int(my_list_1[i])
            val2 = int(my_list_2[i])
            if val1 % val2 == 0:
                new_list.append(val1 / val2)
            else:
                new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except ValueError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            break
        finally:
            pass
    return new_list
