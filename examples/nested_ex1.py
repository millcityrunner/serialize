from serialize-mcr import serialize-mcr


class Snack(serialize-mcr):
    schema = [
        # cheese is nice but is optional.
        {'name': 'cheese', 'optional': True},
        # chocolate is a MUST have.
        {'name': 'chocolate'},
        # chips is a must but we have to decide which kind later,
        # so its value can be None, False, "", {}, [].
        {'name': 'chips', 'nullable': True},
    ]


class NestedBucket(serialize-mcr):
    schema = [
        {'name': 'apple'},
        {'name': 'orange'},
        {'name': 'pineapple'},
        {'name': 'snack', 'is_compound': True, 'compound_serialize-mcrr': Snack}
    ]


# test data for NestedBucket
test2 = dict(
    apple="good apple",
    orange="very good orange",
    pineapple="nice pineapple",
    snack=dict(
        chocolate="Ferrero Rocher",
        chips=[]  # yeah its a list of chips!
    ),
)
my_snacks = NestedBucket(test2)
print(my_snacks)
# >>> {"apple": "good apple", "orange": "very good orange", "pineapple": "nice pineapple",
# >>>  "snack": {"chocolate": "Ferrero Rocher", "chips": []}}
