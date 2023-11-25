# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: November 24th, 2023
# Description: This program contains a function words_in_both that takes two strings as input 
# and returns a set of words that are common to both strings, in a case-insensitive manner. 
# The words in the returned set are all lower-case.

def words_in_both(string1, string2):
    """
    Returns a set of words that are common to both input strings.

    The function splits each string into words, converts them to lower case, and then
    finds the intersection of these sets of words. The result is case-insensitive.

    :param string1: The first input string.
    :param string2: The second input string.
    :return: A set of words (in lower case) that are common to both strings.
    """
    # Splitting the strings into words and converting to lower case
    words1 = set(string1.lower().split())
    words2 = set(string2.lower().split())

    # Finding the intersection of the two sets
    common_words = words1.intersection(words2)

    return common_words


