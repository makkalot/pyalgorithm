def merge_action(left_array,right_array):
    """
    The conquer part
    """

    left_index = 0
    right_index = 0
    last_array = []
    
    while left_index !=len(left_array) and right_index != len(right_array):
        if left_array[left_index] < right_array[right_index]:
            last_array.append(left_array[left_index])
            left_index += 1

        else:
            last_array.append(right_array[right_index])
            right_index += 1

    #should check if both are ok
    if left_index !=len(left_array):
        last_array.extend(left_array[left_index:])
    elif right_index != len(right_array):
        last_array.extend(right_array[right_index:])

    return last_array


def merge_sort(main_array):
    """
    The recursive part
    """
    if len(main_array) == 1:
        return main_array
    
    middle = len(main_array)/2
    left = merge_sort(main_array[0:middle])
    right = merge_sort(main_array[middle:len(main_array)])

    return merge_action(left,right)

