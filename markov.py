import json, random

class MarkovChain:
    def load(self, file_name='names.txt'):
        """
            Fill the Markov chain with names from a given file.
            If the given `file_name` isn't recognized as an existing
            txt or json file, the value is directly put into the
            Markov Chain.
        """
        if file_name.endswith('.txt'):
            with open(file_name, 'r') as reader:
                for line in reader:
                    self.__add_weights(list(line))
        elif file_name.endswith('.json'):
            self.markov = json.load(open(file_name, 'r'))
        else:
            # If the input is some raw data, directly cast it into the Markov chain.
            self.__add_weights(list(file_name))
    
    def save(self, file_name='markov.json'):
        """Save the current Markov chain to a given file."""
        json.dump(self.markov, open(file_name, 'w'))
    
    def get_name(self):
        """Get a name by walking a random path on the Markov Chain."""
        c, w, i = 'START', '', 0

        while c != '\n' and i < 1000:
            i += 1
            c = self.__pick_random(self.markov[c])
            w += c
        return w.capitalize()

    def print_name(self):
        """Print a name from the `get_name` function."""
        print(self.get_name(), end='')
    
    # --------------------------------------------
    #              PRIVATE FUNCTIONS
    # --------------------------------------------

    def __init__(self):
        self.markov = {}

    def __add_weights(self, words):
        if len(words) == 0:
            return

        words = ['START'] + words + ['\n']

        for i in range(1, len(words)):
            self.__add_to_markov(words[i-1], words[i])
            
    def __add_to_markov(self, val1, val2):
        if len(val1) == 1:
            val1 = val1.lower()
        if len(val2) == 1:
            val2 = val2.lower()

        if val1 not in self.markov:
            self.markov[val1] = {val2: 1}
        elif val2 not in self.markov[val1]:
            self.markov[val1][val2] = 1
        else:
            self.markov[val1][val2] += 1
    
    def __pick_random(self, chain):
        tot = sum(chain.values())
        x = random.randint(1, tot)

        for key in chain:
            x += -1*chain[key]
            if x <= 0:
                return key