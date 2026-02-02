
def reverse_word(word):
    # my_list = word.split(" ")
    # my_list_reverse = my_list[::-1]
    my_reverse_words = " ".join(word.split(" ")[::-1])
    return my_reverse_words



print(reverse_word("Now that Font Awesome 7 has been released we are marking version 6 as Long"))