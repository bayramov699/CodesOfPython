"""" FUNCTIONS AND ARGUMNETS"""


rapator = ['Arzu', 'Turqut', 'Rauf', 'Fatime', 'Xaqani', 'Mirelesger', 'Ugur']

def get_members(a, b, c, d, e, f, g):
    members = f'{a}, {b}, {c}, {d}, {e}, {f}, {g}'
    return members

members = get_members(*rapator)

print(members)
