class Fizzbuzz:

    def fizzbuzz(self,number):
        answer = ""
        if number % 3 == 0:
            answer += "Fizz"
        if number % 5 == 0:
            answer += "Buzz"
        if answer == "":
            answer = str(number)
        return answer