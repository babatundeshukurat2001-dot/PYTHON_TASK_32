import unittest


from mbti import (
    QUESTIONS,
    DIMENSIONS,
    PERSONALITY_TRAITS,
    is_valid_response,
    get_valid_response,
    count_letters,
    determine_personality_type,
    format_question,
    run_test,
)


def make_input(answers):
    """Return a fake input() that hands back the answers one by one."""
    answer_iterator = iter(answers)

    def fake_input(prompt=""):
        return next(answer_iterator)

    return fake_input


class QuestionBankTest(unittest.TestCase):

    def test_there_are_twenty_questions(self):
        self.assertEqual(20, len(QUESTIONS))

    def test_every_question_has_option_a_and_option_b(self):
        for question in QUESTIONS:
            self.assertEqual(2, len(question))

    def test_each_dimension_uses_five_questions(self):
        for letters, question_numbers in DIMENSIONS.items():
            self.assertEqual(5, len(question_numbers), letters)

    def test_every_question_belongs_to_exactly_one_dimension(self):
        all_numbers = []
        for question_numbers in DIMENSIONS.values():
            all_numbers.extend(question_numbers)
        self.assertEqual(list(range(1, 21)), sorted(all_numbers))

    def test_dimension_question_numbers_match_the_pdf(self):
        self.assertEqual([1, 5, 9, 13, 17], DIMENSIONS["EI"])
        self.assertEqual([2, 6, 10, 14, 18], DIMENSIONS["SN"])
        self.assertEqual([3, 7, 11, 15, 19], DIMENSIONS["TF"])
        self.assertEqual([4, 8, 12, 16, 20], DIMENSIONS["JP"])


class ResponseValidationTest(unittest.TestCase):

    def test_a_is_valid(self):
        self.assertTrue(is_valid_response("A"))

    def test_b_is_valid(self):
        self.assertTrue(is_valid_response("B"))

    def test_lowercase_is_accepted(self):
        self.assertTrue(is_valid_response("a"))
        self.assertTrue(is_valid_response("b"))

    def test_surrounding_spaces_are_ignored(self):
        self.assertTrue(is_valid_response("  A "))

    def test_other_letters_are_rejected(self):
        self.assertFalse(is_valid_response("F"))
        self.assertFalse(is_valid_response("C"))

    def test_empty_text_is_rejected(self):
        self.assertFalse(is_valid_response(""))

    def test_more_than_one_letter_is_rejected(self):
        self.assertFalse(is_valid_response("AB"))
        self.assertFalse(is_valid_response("A B"))

    def test_digits_are_rejected(self):
        self.assertFalse(is_valid_response("1"))


class GetValidResponseTest(unittest.TestCase):

    def test_returns_valid_answer_in_uppercase(self):
        messages = []
        answer = get_valid_response("Q", make_input(["b"]), messages.append)
        self.assertEqual("B", answer)
        self.assertEqual([], messages)

    def test_retries_until_a_or_b_is_entered(self):
        messages = []
        answer = get_valid_response("Q", make_input(["F", "x", "A"]), messages.append)
        self.assertEqual("A", answer)
        self.assertEqual(
            [
                "Expected A or B as Response",
                "I know this is an error, Please retry again",
                "Expected A or B as Response",
                "I know this is an error, Please retry again",
            ],
            messages,
        )


class ScoringTest(unittest.TestCase):

    def test_all_a_answers_give_estj_counts(self):
        counts = count_letters(["A"] * 20)
        self.assertEqual({"E": 5, "I": 0, "S": 5, "N": 0,
                          "T": 5, "F": 0, "J": 5, "P": 0}, counts)

    def test_all_b_answers_give_infp_counts(self):
        counts = count_letters(["B"] * 20)
        self.assertEqual({"E": 0, "I": 5, "S": 0, "N": 5,
                          "T": 0, "F": 5, "J": 0, "P": 5}, counts)

    def test_single_answer_lands_in_the_right_dimension(self):
        responses = ["B"] + ["A"] * 19          # question 1 is E vs I
        counts = count_letters(responses)
        self.assertEqual(4, counts["E"])
        self.assertEqual(1, counts["I"])

    def test_all_a_is_estj(self):
        self.assertEqual("ESTJ", determine_personality_type(["A"] * 20))

    def test_all_b_is_infp(self):
        self.assertEqual("INFP", determine_personality_type(["B"] * 20))

    def test_mixed_answers_give_entp(self):
        responses = ["A"] * 20
        for number in DIMENSIONS["SN"]:
            responses[number - 1] = "B"         # all N
        for number in DIMENSIONS["JP"]:
            responses[number - 1] = "B"         # all P
        self.assertEqual("ENTP", determine_personality_type(responses))

    def test_majority_decides_each_letter(self):
        responses = ["A"] * 20
        for number in [1, 5, 9]:               
            responses[number - 1] = "B"
        self.assertEqual("I", determine_personality_type(responses)[0])

    def test_wrong_number_of_responses_is_rejected(self):
        with self.assertRaises(ValueError):
            determine_personality_type(["A"] * 19)


class TraitDescriptionTest(unittest.TestCase):

    def test_all_sixteen_types_have_a_description(self):
        self.assertEqual(16, len(PERSONALITY_TRAITS))

    def test_every_reachable_type_has_a_description(self):
        for first in "EI":
            for second in "SN":
                for third in "TF":
                    for fourth in "JP":
                        personality_type = first + second + third + fourth
                        self.assertIn(personality_type, PERSONALITY_TRAITS)

    def test_each_description_has_a_name_and_text(self):
        for name, description in PERSONALITY_TRAITS.values():
            self.assertTrue(name)
            self.assertTrue(description)


class FormatQuestionTest(unittest.TestCase):

    def test_shows_both_options_labelled_a_and_b(self):
        text = format_question(("tough-minded, just", "tender-hearted, merciful"))
        self.assertIn("A.tough-minded, just", text)
        self.assertIn("B.tender-hearted, merciful", text)


class RunTestTest(unittest.TestCase):

    def test_full_session_shows_name_and_personality(self):
        messages = []
        answers = ["Ada Obi"] + ["A"] * 20
        run_test(make_input(answers), messages.append)
        output = "\n".join(messages)
        self.assertIn("Ada Obi", output)
        self.assertIn("ESTJ", output)

    def test_invalid_answers_are_asked_again(self):
        messages = []
        answers = ["Ada Obi", "F", "B"] + ["A"] * 19
        run_test(make_input(answers), messages.append)
        output = "\n".join(messages)
        self.assertIn("Expected A or B as Response", output)
        self.assertIn("I know this is an error, Please retry again", output)

    def test_session_shows_the_users_responses(self):
        messages = []
        answers = ["Ada Obi"] + ["B"] * 20
        run_test(make_input(answers), messages.append)
        output = "\n".join(messages)
        self.assertIn("INFP", output)
        self.assertIn("1. B", output)
        self.assertIn("20. B", output)


if __name__ == '__main__':
    unittest.main()

