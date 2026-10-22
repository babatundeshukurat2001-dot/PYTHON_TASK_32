QUESTIONS = [
    ("expend energy, enjoy groups", "conserve energy, enjoy one-on-one"),
    ("Interpret literally", "look for meaning and possibilities"),
    ("logical, thinking, questioning", "empathetic, feeling, accommodating"),
    ("organized, orderly", "flexible, adaptable"),
    ("more outgoing, think out loud", "more reserved, think to yourself"),
    ("practical, realistic, experiential", "imaginative, innovative, theoretical"),
    ("candid, straight forward, frank", "tactful, kind, encouraging"),
    ("plan, schedule", "unplanned, spontaneous"),
    ("seek many tasks, public activities, interaction with others",
     "seek private, solitary activities with quiet to concentrate"),
    ("standard, usual, conventional", "different, novel, unique"),
    ("firm, tend to criticize, hold the line", "gentle, tend to appreciate, conciliate"),
    ("regulated, structured", "easy-going, live and let live"),
    ("external, communicative, express yourself", "internal, reticent, keep to yourself"),
    ("focus on here-and-now", "look to the future, global perspective, big picture"),
    ("tough-minded, just", "tender-hearted, merciful"),
    ("preparation, plan ahead", "go with the flow, adapt as you go"),
    ("active, initiate", "reflective, deliberate"),
    ("facts, things, what is", "ideas, dreams, what could be, philosophical"),
    ("matter of fact, issue-oriented", "sensitive, people-oriented, compassionate"),
    ("control, govern", "latitude, freedom"),
]


DIMENSIONS = {
    "EI": [1, 5, 9, 13, 17],
    "SN": [2, 6, 10, 14, 18],
    "TF": [3, 7, 11, 15, 19],
    "JP": [4, 8, 12, 16, 20],
}

PERSONALITY_TRAITS = {
    "ISTJ": ("The Logistician",
             "Practical, fact-minded and dependable. You value duty, order and doing things properly."),
    "ISFJ": ("The Defender",
             "Warm, loyal and protective. You quietly look after the people who matter to you."),
    "INFJ": ("The Advocate",
             "Idealistic and insightful. You are driven by deep values and a wish to help others grow."),
    "INTJ": ("The Architect",
             "Strategic and independent. You see the big picture and make long-term plans to reach it."),
    "ISTP": ("The Virtuoso",
             "Calm, hands-on and curious about how things work. You solve problems as they appear."),
    "ISFP": ("The Adventurer",
             "Gentle, artistic and flexible. You live in the moment and stay true to your own values."),
    "INFP": ("The Mediator",
             "Thoughtful and imaginative. You look for meaning and want to live by your ideals."),
    "INTP": ("The Logician",
             "Analytical and inventive. You love ideas, theories and finding out why things are so."),
    "ESTP": ("The Entrepreneur",
             "Energetic and bold. You enjoy action, take risks and think well on your feet."),
    "ESFP": ("The Entertainer",
             "Spontaneous and fun-loving. You bring energy to a room and enjoy sharing experiences."),
    "ENFP": ("The Campaigner",
             "Enthusiastic and creative. You spot possibilities everywhere and inspire the people around you."),
    "ENTP": ("The Debater",
             "Quick-witted and curious. You enjoy challenging ideas and exploring new angles."),
    "ESTJ": ("The Executive",
             "Organized and direct. You like clear rules, take charge and get things done."),
    "ESFJ": ("The Consul",
             "Caring and sociable. You enjoy helping others and keeping the group together."),
    "ENFJ": ("The Protagonist",
             "Charismatic and encouraging. You naturally lead and bring out the best in people."),
    "ENTJ": ("The Commander",
             "Confident and decisive. You organize people and resources to reach ambitious goals."),
}

ERROR_LINE_ONE = "Expected A or B as Response"
ERROR_LINE_TWO = "I know this is an error, Please retry again"


def is_valid_response(response):
    return response.strip().upper() in ("A", "B")


def get_valid_response(prompt, input_func=input, output_func=print):
    while True:
        response = input_func(prompt)
        if is_valid_response(response):
            return response.strip().upper()
        output_func(ERROR_LINE_ONE)
        output_func(ERROR_LINE_TWO)


def format_question(question):
    option_a, option_b = question
    return f"A.{option_a}        B.{option_b}"


def count_letters(responses):
    if len(responses) != len(QUESTIONS):
        raise ValueError(f"Expected {len(QUESTIONS)} responses, got {len(responses)}")

    counts = {}
    for letters in DIMENSIONS:
        counts[letters[0]] = 0
        counts[letters[1]] = 0

    for letters, question_numbers in DIMENSIONS.items():
        for number in question_numbers:
            if responses[number - 1].upper() == "A":
                counts[letters[0]] += 1
            else:
                counts[letters[1]] += 1
    return counts


def determine_personality_type(responses):
    counts = count_letters(responses)
    personality_type = ""
    for letters in DIMENSIONS:
        first, second = letters
        personality_type += first if counts[first] > counts[second] else second
    return personality_type


def run_test(input_func=input, output_func=print):
    name = input_func("What is your name\n").strip()

    responses = []
    for question in QUESTIONS:
        responses.append(get_valid_response(format_question(question) + "\n",
                                            input_func, output_func))

    counts = count_letters(responses)
    personality_type = determine_personality_type(responses)
    title, description = PERSONALITY_TRAITS[personality_type]

    output_func("")
    output_func(f"Name: {name}")
    output_func("Your responses:")
    for number, response in enumerate(responses, start=1):
        output_func(f"{number}. {response}")
    output_func("")
    output_func("Your scores:")
    for letters in DIMENSIONS:
        first, second = letters
        output_func(f"{first}: {counts[first]}  vs  {second}: {counts[second]}")
    output_func("")
    output_func(f"Your personality type: {personality_type} - {title}")
    output_func(description)
    return personality_type




