# stable roommate problem

tenants = ['Alie', 'Berry', 'Cherry', 'Dimple', 'Evelyn', 'Fiona']
preferences_list = [['Alie', 'Cherry', 'Dimple', 'Berry', 'Fiona', 'Evelyn'],
                    ['Berry', 'Fiona', 'Evelyn', 'Dimple', 'Alie', 'Cherry'],
                    ['Cherry', 'Berry', 'Dimple', 'Evelyn', 'Alie', 'Fiona'],
                    ['Dimple', 'Evelyn', 'Berry', 'Cherry', 'Fiona', 'Alie'],
                    ['Evelyn', 'Cherry', 'Alie', 'Berry', 'Dimple', 'Fiona'],
                    ['Fiona', 'Evelyn', 'Alie', 'Cherry', 'Dimple', 'Berry']]


class Person(object):
    def __init__(self, name):
        self.name = name
        self.preferences = None
        self.requester = None
        self.proposal = None

    def get_name(self):
        return self.name

    def get_preferences(self):
        return self.preferences

    def get_next_preference(self):
        if len(self.preferences) == 0:
            return None
        return self.preferences[0]

    def compare(self, first, second):
        return self.preferences.index(first) < self.preferences.index(second)

    def add_preferences(self, preferences):
        self.preferences = preferences

    def remove_preference(self, name):
        if name in self.preferences:
            self.preferences.remove(name)

    def get_requester(self):
        return self.requester

    def add_request(self, requester):
        self.requester = requester

    def get_proposal(self):
        return self.proposal

    def propose_to(self, person):
        self.proposal = person


def justify_req(people, person, requester):
    if people[person].get_requester() is None:
        print(person + ' has no previous requests ')
        people[requester].propose_to(person)
        people[person].add_request(requester)
    else:
        prev_requester = people[person].get_requester()
        print(person + ' has request from ' + prev_requester)
        if people[person].compare(requester, prev_requester):
            print('\t' + person + ' prefers ' + requester + ' to ' + prev_requester)
            people[requester].propose_to(person)
            people[person].add_request(requester)
            people[prev_requester].propose_to(None)
            people[prev_requester].remove_preference(person)
            next_pref = people[prev_requester].get_next_preference()
            if next_pref is not None:
                people = justify_req(people, next_pref, prev_requester)
        else:
            print('\t' + person + ' prefers ' + prev_requester + ' to ' + requester)
            people[requester].remove_preference(person)
            people[requester].propose_to(None)
            next_pref = people[requester].get_next_preference()
            if next_pref is not None:
                people = justify_req(people, next_pref, requester)
    return people


def phase_one(people):
    for name in people.keys():
        first = people[name].get_next_preference()
        people = justify_req(people, first, name)
    return people


def phase_two(people):
    print('Reduced lists:')
    for ech in people:
        print(ech, ' : ', people[ech].get_preferences())
    cycle_exists = True
    match_exists = True
    while cycle_exists:
        starter = None
        for mate in people.keys():
            mate_prefs = people[mate].get_preferences()
            if len(mate_prefs) > 1 and starter is None:
                starter = mate
            elif len(mate_prefs) == 0:
                match_exists = False
                break
        if starter is None:
            cycle_exists = False
        else:
            p_set = [starter]
            follower = people[starter].get_preferences()[1]
            q_set = [follower]
            next_mate = people[follower].get_preferences()[-1]
            while next_mate not in p_set:
                p_set.append(next_mate)
                q_set.append(people[next_mate].get_preferences()[1])
                next_mate = people[q_set[-1]].get_preferences()[-1]
            p_set.append(next_mate)
            for pos in range(len(q_set)):
                people[q_set[pos]].remove_preference(p_set[pos + 1])
                people[p_set[pos + 1]].remove_preference(q_set[pos])
    if not match_exists:
        print('\nNo stable matching possible in this case!')
    else:
        num_pairs = len(people.keys())/2
        print('\nStable Roommates:')
        for ech in people:
            num_pairs -= 1
            print(ech, ' --- ', people[ech].get_preferences()[0])
            if num_pairs == 0:
                break


persons = {}
for tenant in tenants:
    persons[tenant] = Person(tenant)

for pref in preferences_list:
    tenant = pref[0]
    tenant_prefer = []
    for each in pref[1:]:
        tenant_prefer.append(each)
    persons[tenant].add_preferences(tenant_prefer)

persons = phase_one(persons)
print('\n')

for persn in persons.keys():
    if persons[persn].get_proposal() is not None:
        prefs = persons[persn].get_preferences()
        last_index = prefs.index(persons[persn].get_requester()) + 1
        for rej in prefs[last_index:]:
            persons[persn].remove_preference(rej)
            persons[rej].remove_preference(persn)
    else:
        print('No stable matching possible in this case!')
        break

phase_two(persons)
