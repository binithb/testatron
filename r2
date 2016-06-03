import math

MAX_RANGE = 10
# [1L, 3L, 9L, 27L, 81L, 243L, 729L, 2187L, 6561L, 19683L]

available_weights_list = [long(math.pow(3, n)) for n in range(0, MAX_RANGE)]
print available_weights_list


def check_balance(left_side_weight, weights_list):
    # print "left weight " + str(left_side_weight) + " verifying " + str(weights_list)
    print "\t\t" + str(weights_list)
    right_side_weight = 0
    for index, c in enumerate(weights_list):
        if c is 'L':
            left_side_weight += available_weights_list[index]
        elif c is 'R':
            right_side_weight += available_weights_list[index]
        elif c is '-':
            pass
        else:
            raise AssertionError("invalid position")
    # print left_side_weight == right_side_weight
    return left_side_weight == right_side_weight


def strip_trailing_hyphens(weights_list):
    for index, c in enumerate(weights_list[::-1]):
        if c is 'L' or c is 'R':
            return weights_list[:len(weights_list) - index]

def find_series(left_side_weight):
    if not _find_series(left_side_weight,'-', 'R') and not _find_series(left_side_weight,'R', '-'):
        raise AssertionError("failed to find series for " + str(left_side_weight))

def _find_series(left_side_weight, template_char, replace_char):
    awl = available_weights_list
    starting_weights_list = [template_char for _ in range(0, MAX_RANGE)]
    found_series = False
    loop_count = 0
    attempted_weight_list = starting_weights_list
    for index_1 in range(0, len(awl)):
        print "l1" * 80

        for index_2 in range(0, len(awl)):
            print "\tl2 :" + str(index_2)

            previous_char = None
            # for index_3 in range(0, len(awl)):
            for index_3 in range(index_2, len(awl)):
                loop_count += 1

                if check_balance(left_side_weight, attempted_weight_list):
                    print "series " + str(strip_trailing_hyphens(attempted_weight_list))
                    found_series = True
                    break

                if previous_char:
                    attempted_weight_list[index_3 - 1] = previous_char
                    previous_char = None

                if index_3 >= index_1:
                    previous_char  = attempted_weight_list[index_3]
                    attempted_weight_list[index_3] = replace_char
                    # print "\t\tl3 : " + str(loop_count)

            if found_series:
                break
            else:
                attempted_weight_list[index_2] = replace_char
                if 0 < index_2 and index_2 > index_1:
                    attempted_weight_list[index_2 - 1] = template_char

            attempted_weight_list[index_3 ] = template_char

        for i in range(0, index_1 + 1):
            attempted_weight_list[i] = replace_char
        for i in range(index_1 + 2, len(awl)):
            attempted_weight_list[i] = template_char

        if found_series:
            break

    print "loop count " + str(loop_count)

    if not found_series:
        return False
    else:
        return True


# check_balance(2, ['L', 'R'])
# check_balance(8, ['L', '-', 'R'])
# find_series(1)
# find_series(4)
# find_series(12)
# 1 Rs
# find_series(3)
# find_series(9)
# find_series(27)
# find_series(81)
# find_series(243)
# find_series(729)
# find_series(2187)
# find_series(6561)
# find_series(19683)



# find_series(4)
# find_series(12)
find_series(39)
# find_series(100)
