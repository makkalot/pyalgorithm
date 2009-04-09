def shift_text(text,shift_by):
    """
    Shifts a text for example if we have
    abcdefgh and shift_by is 3 than we should
    have defghabc shifted
    """
    print "At the begginning it is : ",text
    for index_shift in range(shift_by):
        tmp = text[index_shift]
        print "The tmp is : ",tmp 
        swap_index = shift_by + index_shift
        text[index_shift]=text[swap_index]
        print "The text is : ",text
        while (swap_index+shift_by) < len(text):
            text[swap_index] = text[swap_index+shift_by]
            swap_index = swap_index+shift_by
            print "The text is : ",text

        text[swap_index]=tmp

    return "".join(text)

if __name__ == "__main__":
    text = "abcdefgh"
    print shift_text(list(text),3)
