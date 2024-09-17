from source.random_exercises.fizzbuzz import Fizzbuzz


class TestFizzbuzz:

    def setup_method(self, method):
        self.fb = Fizzbuzz()

    def test_should_return_a_string(self):
        assert self.fb.fizzbuzz(1) == "1"

    def test_number3_should_return_Fizz(self):
        assert self.fb.fizzbuzz(3) == "Fizz"

    def test_number5_should_return_Buzz(self):
        assert self.fb.fizzbuzz(5) == "Buzz"

    def test_number9_should_return_Fizz(self):
        assert self.fb.fizzbuzz(9) == "Fizz"

    def test_number10_should_return_Buzz(self):
        assert self.fb.fizzbuzz(10) == "Buzz"

    def test_number15_should_return_FizzBuzz(self):
        assert self.fb.fizzbuzz(15) == "FizzBuzz"
     
