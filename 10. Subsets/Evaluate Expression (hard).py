# Given an expression containing digits and operations (+, -, *),
# find all possible ways in which the expression can be evaluated by
# grouping the numbers and operators using parentheses.
#
# Example 1:
#
# Input: "1+2*3"
# Output: 7, 9
# Explanation: 1+(2*3) => 7 and (1+2)*3 => 9
# Example 2:
#
# Input: "2*3-4-5"
# Output: 8, -12, 7, -7, -3
# Explanation: 2*(3-(4-5)) => 8, 2*(3-4-5) => -12, 2*3-(4-5) => 7, 2*(3-4)-5 => -7, (2*3)-4-5 => -3

# when to go to if block?
#   - only when input contains only one digit
#   - or contains digits with +/-/*, until scan +/-/* and split two parts, then only one digit side will go to 'if'
# e.g. 1+2 => else -> 1 wont do anything => + => will go to recursive section, then go to if in next loop
#                                               => left: 1 => [1], right: 2 => [2]

# until..  encounter +/-/*, then split the string,
#   if left or right only contains digit, then add to sub-result for further calculation
#   if left or right still contains string, then split again

# then calculate it and add to result again.. jump out from recursive loop.. it may become upper lever left or right

# for example:
# 1 + 2 * 3
# go to else, len=5: index = 0 -> 1 -> do nothing
#                    index = 1 -> + -> left = 1 -> [1]
#                                   -> right = 2 * 3 => len = 3 => index = 0
#                                                                 index = 1, => * => left = [2]
#                                                                                 => right = [3]
#                                                                           => add [6] to result
#... everytime left and right side might contain multiple results, so it needs to calculate one by one.
# every loop starts with an empty result list []

def diff_ways_to_evaluate_expression(input):
    result = []
    # base case: if the input string is a number, parse and add it to output.
    if '+' not in input and '-' not in input and '*' not in input:
        print('add to result: ', int(input))
        result.append(int(input))
        print(result)
    else:
        for i in range(0, len(input)):
            print('index: ', i, ' value: ', input[i])
            char = input[i]
            if not char.isdigit():
                print('- char is not digit')
                # break the equation here into two parts and make recursively calls
                print('left: ', input[0:i])
                leftParts = diff_ways_to_evaluate_expression(input[0:i])
                print('right: ', input[i+1:])
                rightParts = diff_ways_to_evaluate_expression(input[i+1:])
                for part1 in leftParts:
                    print('part 1: ', part1)
                    for part2 in rightParts:
                        print('part 2: ', part2)
                        if char == '+':
                            result.append(part1 + part2)
                        elif char == '-':
                            result.append(part1 - part2)
                        elif char == '*':
                            result.append(part1 * part2)
                        print('- result: ', result)
                        print('\n')

        print('ALL result: ', result)
        print('\n')

    return result

def diff_ways_to_evaluate_expression_2(input):
    return diff_ways_to_evaluate_expression_rec({}, input)


def diff_ways_to_evaluate_expression_rec(map, input):
    if input in map:
        return map[input]
    result = []

    # base case: if the input string is a number, parse and return it.
    if '+' not in input and '-' not in input and '*' not in input:
        result.append(int(input))
    else:
        for i in range(0, len(input)):
            char = input[i]
            if not char.isdigit():
                # break the equation here into two parts and make recursively calls
                leftParts = diff_ways_to_evaluate_expression_rec(
                map, input[0:i])

                rightParts = diff_ways_to_evaluate_expression_rec(
                map, input[i+1:])
                for part1 in leftParts:
                    for part2 in rightParts:
                        if char == '+':
                            result.append(part1 + part2)
                        elif char == '-':
                            result.append(part1 - part2)
                        elif char == '*':
                            result.append(part1 * part2)
            map[input] = result
    return result


def main():


    print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

    # print("Expression evaluations: " +
    #     str(diff_ways_to_evaluate_expression("1")))

    # print("Expression evaluations: " +
    #     str(diff_ways_to_evaluate_expression("2*3-4-5")))

    # print("Expression evaluations: " +
    #     str(diff_ways_to_evaluate_expression_2("1+2*3")))
    #
    # print("Expression evaluations: " +
    #     str(diff_ways_to_evaluate_expression_2("2*3-4-5")))

main()

