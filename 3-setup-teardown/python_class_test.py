class TestClass:
    # At the beginning and end of all class tests have completed
    # @classmethod is for they takes uninstantied class object
    #   rather than unique instance of class
    @classmethod
    def setup_class(cls):
        print("\nSetting up class!")
    @classmethod
    def teardown_class(cls):
        print("\nTearing down class!")

    # before - after each unittest
    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1!")
        elif method == self.test2:
            print("\nSetting up test2!")
        else:
            print("\nSetting up unknown test!")
    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test1!")
        elif method == self.test2:
            print("\nTearing down test2!")
        else:
            print("\nTearing down unknown test!")



    def test1(self):
        print("Executing test1!")
        assert True

    def test2(self):
        print("Executing test2!")
        assert True