# Given a string, find all of its permutations preserving the character sequence but changing case.
#
# Example 1:
#
# Input: "ad52"
# Output: "ad52", "Ad52", "aD52", "AD52"
#
# Example 2:
#
# Input: "ab7c"
# Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"

def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)

    # process every character of the string one by one
    for i in range(len(str)):
        # only process characters, skip digits
        if str[i].isalpha():
            # we will take all existing permutations and change the letter case appropriately
            # i.e. based on all existing permutations, change at index i,
            # so that all variants (uppercase and lowercase) at current position i will be included
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                # if the current character is in upper case, change it to lower case or vice versa
                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))

    return permutations


def main():
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()
