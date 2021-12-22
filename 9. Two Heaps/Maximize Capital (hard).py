# Given a set of investment projects with their respective profits, we need to find the most profitable projects.
# We are given an initial capital and are allowed to invest only in a fixed number of projects.
# Our goal is to choose projects that give us the maximum profit.
# Write a function that returns the maximum total capital after selecting the most profitable projects.
#
# We can start an investment project only when we have the required capital.
# Once a project is selected, we can assume that its profit has become our capital.
#
# Example 1:
#
# Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2
# Output: 6
# Explanation:
#
# With initial capital of ‘1’, we will start the second project which will give us profit of ‘2’. Once we selected our first project, our total capital will become 3 (profit + initial capital).
# With ‘3’ capital, we will select the third project, which will give us ‘3’ profit.
# After the completion of the two projects, our total capital will be 6 (1+2+3).

from heapq import *


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    minCapitalHeap = []
    maxProfitHeap = []

    # insert all project capitals to a min-heap
    for i in range(0, len(profits)):
        heappush(minCapitalHeap, (capital[i], i))

    print(minCapitalHeap)

    # let's try to find a total of 'numberOfProjects' best projects
    availableCapital = initialCapital
    for _ in range(numberOfProjects):
        # find all projects that can be selected within the available capital and insert them in a max-heap
        # i.e. select capital which could be afforded by availableCapital and push its/their profit(s) to maxProfitHeap which
        print('available capital: ' + str(availableCapital))
        while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
            capital, i = heappop(minCapitalHeap)
            heappush(maxProfitHeap, (-profits[i], i))

        print('before')

        print(minCapitalHeap)
        print(maxProfitHeap)

        # terminate if we are not able to find any project that can be completed within the available capital
        # i.e. nothing could be afforded by current availableCapital
        if not maxProfitHeap:
            break

        # select the project with the maximum profit in this round
        availableCapital += -heappop(maxProfitHeap)[0]
        print('after')
        print(minCapitalHeap)
        print(maxProfitHeap)
        print('\n')
        print('\n')
    return availableCapital


def main():

    # print("Maximum capital: " +
    #     str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))

    # print("Maximum capital: " +
    #       str(find_maximum_capital([0, 3, 3], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 0, 2], [1, 2, 3], 2, 1)))
    # print("Maximum capital: " +
    #     str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
