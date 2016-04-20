"""Callcentre which returns words according to rules."""


class CallCentre(object):

    """Class for my epic Callcentre."""

    def __init__(self):
        """
        Constructor for Callcentre.

        Arguments:
            None
        Returns:
            word_dict - a dictionary which contains rules and their corresponding values

            create_word - function, which takes string and returns a string

            some create_word objects

            instructions - dictionary which contains instructions and their corresponding
            create_word objects

            long_instructions - dictionary which contains long instructions and their
            corresponding rules
        """
        self.word_dict = {
            'nouns': ['koer', 'porgand', 'madis', 'kurk', 'tomat'],
            'targets': ['koera', 'porgandit', 'madist', 'kurki', 'tomatit'],
            'verbs': ['sööb', 'lööb', 'jagab', 'tahab', 'ei taha'],
            'adjectives': ['ilus', 'kole', 'pahane', 'magus', 'sinu'],
            'target_adjectives': ['ilusat', 'koledat', 'pahast', 'magusat', 'sinu'],
            'sentence': 'noun verb target .',
            'twosentences': 'sentence sentence',
            'beautifulsentence': 'adjective noun verb targetadjective target .',
            'instructions': ['noun', 'target', 'verb', 'adjective',
                             'targetadjective', 'sentence', 'twosentences',
                             'beautifulsentence']
        }

        def create_word(self, word):
            """
            Create a word according to rules.

            Args:
            word - a string whcih contains instruction
            Return:
            yields a word (string) according to instruction
            """
            while(True):
                if word in self.long_instructions.keys():
                    yield self.create_sentence(self.long_instructions[word])
                else:
                    for noun112 in self.word_dict[word]:
                        yield noun112

        self.noun = create_word(self, "nouns")
        self.target = create_word(self, "targets")
        self.verb = create_word(self, "verbs")
        self.adjective = create_word(self, "adjectives")
        self.target_adjective = create_word(self, "target_adjectives")
        self.sentence = create_word(self, "sentence")
        self.twosentences = create_word(self, "twosentences")
        self.beautifulsentence = create_word(self, "beautifulsentence")

        self.instructions = {
            'noun': self.noun, 'target': self.target, 'verb': self.verb,
            'adjective': self.adjective,
            'targetadjective': self.target_adjective,
            "sentence": self.sentence,
            "twosentences": self.twosentences,
            "beautifulsentence": self.beautifulsentence
        }
        self.long_instructions = {
            "sentence": self.word_dict["sentence"],
            "twosentences": self.word_dict["twosentences"],
            "beautifulsentence": self.word_dict["beautifulsentence"]
        }

    def create_sentence(self, instr1):
        """
        Create a sentence according to instructions.

        Args:
        instr1 - a sentence (string) which contains instructions and random words
        Returns:
        A string that is made according to instructions
        """
        list1 = []
        for w in instr1.split(' '):

            if w not in self.word_dict["instructions"]:
                list1.append(w)
            else:
                list1.append(str(next(self.instructions[w])))

        sentence = " ".join(str(x) for x in list1)

        return sentence
