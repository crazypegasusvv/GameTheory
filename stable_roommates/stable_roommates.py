# stable roommate problem
# To-Do : algorithm phase 1 and phase 2

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

    def get_next_preference(self):
        if len(self.preferences) == 0:
            return None
        return self.preferences[0]

    def compare(self, first, second):
        return self.preferences.index(first) < self.preferences.index(second)

    def add_preferences(self, preferences):
        self.preferences = preferences

    def remove_preference(self, name):
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
        print('---> ' + person + ' has no previous requests <---')
        people[requester].propose_to(person)
        people[person].add_request(requester)
    else:
        prev_requester = people[person].get_requester()
        print('---> ' + person + ' has request from ' + prev_requester + ' <---')
        if people[person].compare(requester, prev_requester):
            print('.... ' + person + ' prefers ' + requester + ' to ' + prev_requester + ' ....')
            people[requester].propose_to(person)
            people[person].add_request(requester)
            people[prev_requester].propose_to(None)
            people[prev_requester].remove_preference(person)
            next_pref = people[prev_requester].get_next_preference()
            if next_pref is not None:
                people = justify_req(people, next_pref, prev_requester)
        else:
            print('.... ' + person + ' prefers ' + prev_requester + ' to ' + requester + ' ....')
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


persons = {}
for tenant in tenants:
    persons[tenant] = Person(tenant)

for pref in preferences_list:
    tenant = pref[0]
    tenant_prefer = []
    for each in pref[1:]:
        tenant_prefer.append(each)
    persons[tenant].add_preferences(tenant_prefer)

phase_one_people = phase_one(persons)

for pers in phase_one_people.keys():
    perst = phase_one_people[pers]
    if perst.get_proposal() is not None:
        print(perst.get_name(), perst.get_proposal(), perst.get_requester())
    else:
        print('No stable matching possible in this case!')
        break
