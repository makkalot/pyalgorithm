import random

def generate_int(start,stop,num_of_elements):
    """
    return a random array of ints
    """

    random_list = []
    for num in xrange(0,num_of_elements):
        tmp = random.randint(start,stop)
        random_list.append(tmp)

    return random_list

if __name__ == "__main__":
    print generate_int(1,100,20)
