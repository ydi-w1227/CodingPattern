# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
#
# Example 1:
#
# Input: N=2
# Output: (()), ()()
# Example 2:
#
# Input: N=3
# Output: ((())), (()()), (())(), ()(()), ()()()

from collections import deque

# if # of '(' == num, also # of ')' == num, then that's one of the final result.
# otherwise,
#   if # of '(' is less than num, then add '('
#   if # of '(' is more than # of ')', then add ')'


class ParenthesesString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount

def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    while queue:
        ps = queue.popleft()
        print('pop left: ' , ps.str, ' ', ps.openCount, ' ', ps.closeCount)
        # if we've reached the maximum number of open and close parentheses, add to the result
        if ps.openCount == num and ps.closeCount == num:
            result.append(ps.str)
            print('balanced parentheses.. ', num)
            print(ps.str)
        else:
            # if we can add an open parentheses, add it
            # i.e. openCount didnt reach num yet
            if ps.openCount < num:
                print('add left (')
                queue.append(ParenthesesString(
                    ps.str + "(", ps.openCount + 1, ps.closeCount))

            # if we can add a close parentheses, add it
            # i.e. open and close are not balanced yet,
            # means that could add close in this case and closeCount wont be larger than openCount..
            if ps.openCount > ps.closeCount:
                print('add right ) ')
                queue.append(ParenthesesString(ps.str + ")",
                    ps.openCount, ps.closeCount + 1))
        print([ele.str for ele in queue])
    return result

def generate_valid_parentheses(num):
  result = []
  parenthesesString = [0 for x in range(2*num)]
  generate_valid_parentheses_rec(num, 0, 0, parenthesesString, 0, result)
  return result


# will do recursive for two conditions...
# if openCount < num will keep add ( first.. until openCount == num
# then from next index will skip adding (, and do adding )
# once index reach to the end of list..
# will jump out to the point where didnt do if openCount > closeCount
# for example, when N = 3
# first time index from 0 - 5 will be ((()))
# i.e. index 0 - 2 only do "if openCount < num", and index 3-5 do both.
# which means when index=2, openCount = 2, closeCount = 0, so that we add one more (
# so index = 3, openCount = 3, closeCount = 0
# now it will go to block "if openCount < num", but not match with condition
# then it will go to block "if openCount > closeCount" and start adding )
# once everything is done, add it to result, then jump back to index 2 to do block "if openCount > closeCount"
# because index = 2 didnt go to second block yet.
# At this moment string is back to 2 2 0 again and go second block to add ) at index 2, which is (, (, ), 0, 0, 0
def generate_valid_parentheses_rec(num, openCount, closeCount, parenthesesString, index, result):

    # if we've reached the maximum number of open and close parentheses, add to the result
    if openCount == num and closeCount == num:
        print('add to result')
        result.append(''.join(parenthesesString))
    else:
        print(index, ' ', openCount, ' ', closeCount)
        print('--- come to add ( ---')
        if openCount < num:  # if we can add an open parentheses, add it
            print('before: ', parenthesesString)
            parenthesesString[index] = '('
            print('after: ', index, ' ', parenthesesString)
            print('\n')
            generate_valid_parentheses_rec(
                num, openCount + 1, closeCount, parenthesesString, index + 1, result)

        print('\n')
        print(index, ' ', openCount, ' ', closeCount)
        print('--- come to add ) ---')
        if openCount > closeCount:  # if we can add a close parentheses, add it
            print('before: ', parenthesesString)
            parenthesesString[index] = ')'
            print('after: ', index, ' ', parenthesesString)
            print('\n')
            generate_valid_parentheses_rec(
                num, openCount, closeCount + 1, parenthesesString, index + 1, result)


def main():
  # print("All combinations of balanced parentheses are: " +
  #       str(generate_valid_parentheses(2)))
  # print("All combinations of balanced parentheses are: " +
  #       str(generate_valid_parentheses(3)))
  #
  # print("All combinations of balanced parentheses are: " +
  #       str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()
