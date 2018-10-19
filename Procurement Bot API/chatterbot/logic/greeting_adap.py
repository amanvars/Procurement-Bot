from chatterbot.logic import LogicAdapter

allowed_words=['how you','good','morning','evening','afternoon','night','hi','hello','namaste','salam','thanks','thank you','thanks lot','thanks a lot','thanks a tonne','thanks tonne','thank you very much','how are you','thank','shukriya','how','are','you']


class GreetingAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(GreetingAdapter, self).__init__(**kwargs)

    def can_process(self, statement):
        if any(x in statement.text.split() for x in allowed_words):
            return True
        else:
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement
        ist=statement.text
        input_string=str(statement.text).split()
        print "In greeting adapter"
        if any(x in input_string for x in ['salam','hi','Hi','hello','Hello','good','Good','morning','evening','afternoon','night','namaste','salam']):
            response=Statement(ist)
            response.remove_response(ist)
            response.confidence=1
            return response

        elif any(x in input_string for x in ['thanks','shukriya','thank you','dhanyawad','thank']):
            response=Statement("You're welcome")
            response.remove_response("You're welcome")
            response.confidence=1
            return response

        elif any(x in input_string for x in ['how','How']) and any(x in input_string for x in ['are']) and any(x in input_string for x in ['you','You']):
            response=Statement("I'm doing good.Thank You")
            response.remove_response("I'm doing good.Thank You")
            return response
        response=Statement("Sorry-I don't have a response to this")
