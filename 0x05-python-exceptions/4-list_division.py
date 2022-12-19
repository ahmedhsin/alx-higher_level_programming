#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if int(my_list_1[i]) % int(my_list_2[i]) == 0:
                new_list.append(int(my_list_1[i]) / int(my_list_2[i]))
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
