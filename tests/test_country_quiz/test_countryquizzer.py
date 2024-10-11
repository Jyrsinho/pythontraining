from source.country_quiz.countryquizzer import countryquiz, Countryquiz


def test_country_quiz_should_call_sleep_three_times():
    countryquiz = Countryquiz()
    countryquiz.create_a_question()
    

