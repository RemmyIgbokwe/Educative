def check_sum(num_list):
    for first_num in range(len(num_list)):
        for second_num in range(first_num, len(num_list)):
            if num_list[first_num] + num_list[second_num] == 0:
                return True
    return False


