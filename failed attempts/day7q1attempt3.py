input = open('day7/input7.txt').read().split('\n')
input = [[col for col in row.split(' ')] for row in input]

class tree(object):
    def __init__(self):
        self.data = []
        self.branch = []

    def addBranch(self, amount):
        for i in range(0, amount):
            self.branch.append(tree())
    
    def branchValue(self, list):
        for i in range(len(list)):
            self.data.append(list[i])

home = tree()
home.addBranch(3)
home.branchValue([1,2,3])
home.branch[0].addBranch(1)
home.branch[0].branch[0].branchValue([2])
print(home.branch[0].data)
print(home.data)