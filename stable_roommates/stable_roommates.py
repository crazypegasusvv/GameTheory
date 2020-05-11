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

    def get_preferences(self):
        return self.preferences

    def add_preferences(self, preferences):
        self.preferences = preferences

    def get_requester(self):
        return self.requester

    def add_request(self, requester):
        self.requester = requester

    def get_proposal(self):
        return self.proposal

    def propose_to(self, person):
        self.proposal = person


def phase_one(people):
    for name in people.keys():
        person = people[name]
        curr_requester = person.get_requester()
        curr_pref = person.get_preferences()
        if not curr_requester:
            print(name, '1st', curr_pref[0].get_name())
            person.propose_to(curr_pref[0])
            people[curr_pref[0].get_name()].add_request(person)
        else:
            print(name, '2nd')

        people[name] = person
    return people


persons = {}
for tenant in tenants:
    persons[tenant] = Person(tenant)

for pref in preferences_list:
    tenant = pref[0]
    tenant_prefer = []
    for each in pref[1:]:
        tenant_prefer.append(persons[each])
    persons[tenant].add_preferences(tenant_prefer)


phase_one(persons)
