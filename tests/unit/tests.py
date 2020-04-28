if __name__ == '__main__':
    import os
    from tests.unit import TestSuite

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    ts = TestSuite()
