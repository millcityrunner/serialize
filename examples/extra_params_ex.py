from serialize import Serialize

class OptionalArgs(Serialize):
    # the `optional`, `nullable`, and `default` are optional parameters
    # `optional` -> defaults to False, if True this parameter is not required to be passed into the serializer
    # `nullable` -> defaults to False, if True this parameter can be passed in as a `null` equivalent value
    # `default` -> defaults to None, this parameter only applies if the key is not present in the data,
    #                  cannot apply a default value to a key that is defined to NOT be optional
    schema = [
        {'name': 'player_1', 'type': (str,), 'optional': False, 'nullable': False, 'default': None},
        {'name': 'player_2', 'type': (str,), 'optional': True, 'nullable': False, 'default': 'Player 2'},
    ]


class CannotBeDefaulted(Serialize):
    schema = [
        {'name': 'player_1', 'type': (str,), 'optional': False, 'nullable': False, 'default': 'Player 1'}
    ]


if __name__ == '__main__':
    # here is what will happen if only player_1 is passed in
    test_data = {
        'player_1': 'Alan Turing'
    }

    s1 = OptionalArgs(data=test_data)
    print(s1)
    # >>> s = {"player_1": "Alan Turing", "player_2": "Player 2"}

    # here is what will happen if both values are passed in
    test_data_2 = {
        'player_1': 'Alan Turing',
        'player_2': 'Steve Jobs'
    }

    s2 = OptionalArgs(data=test_data_2)
    print(s2)
    # >>> s = {"player_1": "Alan Turing", "player_2": "Steve Jobs"}

    # here is what will happen if `default` is passed in on a non-optional key
    s3 = CannotBeDefaulted(data=test_data)
    print(s3)
    # >>>   Traceback (most recent call last):
    #           File "/serialize/examples/extra_params_ex.py", line 41, in <module>
    #               s3 = CannotBeDefaulted(data=test_data)
    #           File "/serialize/serialize/__init__.py", line 15, in __init__
    #               self.preproc(data)
    #           File "/serialize/serialize/__init__.py", line 85, in preproc
    #               raise ValueError(_err(6, _name))
    #       ValueError: Property: 'player_1' cannot have a default value when it is required.
