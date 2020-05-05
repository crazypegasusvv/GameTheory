# Gale-Shapley algorithm
persons_count = 0


class Person(object):
    def __init__(self, name, prefs):
        self.name = name
        self.prefs = prefs

    def get_name(self):
        return self.name

    def get_prefs(self):
        return self.prefs


class Man(Person):
    def __init__(self, name, prefs):
        global persons_count
        persons_count += 1
        self.id = persons_count
        self.engaged_to = None
        self.pending = prefs
        super().__init__(name, prefs)

    def propose(self, acceptor):
        self.pending.remove(acceptor)

    def get_pending(self):
        return self.pending

    def get_name(self):
        return self.name


class Woman(Person):
    def __init__(self, name, prefs):
        self.engaged_to = None
        super().__init__(name, prefs)

    def engage_to(self, proposer):
        self.engaged_to = proposer

    def get_engaged(self):
        return self.engaged_to


def get_proposer(single_men):
    for man in single_men:
        remaining = man.get_pending()
        if len(remaining) > 0:
            single_men.remove(man)
            single_men.append(man)
            return single_men, man, remaining[0]
    return None


def get_woman(woman_name):
    for acceptor in women:
        if woman_name == acceptor.get_name():
            return acceptor


def get_man(man_name):
    for proposer in men:
        if man_name == proposer.get_name():
            return proposer


def stable_marriage(proposers, acceptors):
    single_men = proposers[:]
    single_women = acceptors[:]
    possibility = get_proposer(single_men)
    while possibility:
        single_men = possibility[0]
        proposer = possibility[1]
        acceptor = get_woman(possibility[2])
        proposer.propose(acceptor.get_name())
        if acceptor in single_women:
            acceptor.engage_to(proposer)
            single_men.remove(proposer)
            single_women.remove(acceptor)
        else:
            ex_engaged = acceptor.get_engaged()
            woman_prefs = acceptor.get_prefs()
            if woman_prefs.index(ex_engaged.get_name()) > woman_prefs.index(proposer.get_name()):
                single_men.append(ex_engaged)
                single_men.remove(proposer)
                acceptor.engage_to(proposer)
        possibility = get_proposer(single_men)


ifp = open('input.txt')
ofp = open('output.txt','w')
tests = int(ifp.readline())

for test in range(tests):
    num = int(ifp.readline())
    men = []
    women = []

    for i in range(num):
        text = ifp.readline().split()
        men.append(Man(text[0], text[1:]))

    for i in range(num):
        text = ifp.readline().split()
        women.append(Woman(text[0], text[1:]))

    stable_marriage(men, women)

    ofp.write('stable marriages for Case#'+ str(test + 1) + '\n')
    for woman in women:
        ofp.write(woman.get_name() + '\t' + woman.get_engaged().get_name() + '\n')
    ofp.write('-----------------------------\n')
