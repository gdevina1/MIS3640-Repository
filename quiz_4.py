ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=None, votes=0):
        """Initialize candidate.

        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self.name = name
        if winning_states is None:
            self.winning_states = []
        else:
            self.winning_states = winning_states
        # self.winning_states = winning_states
        self.votes = votes

    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        return 'Name of candidate: {}, Winning States: {}, total votes: {}.'.format(self.name, self.winning_states, self.votes)
    
    def __gt__(self,other):
        return self.votes > other.votes    

    def win_state(self, state):
        """Adds a state to winning_states and updates votes.

        state: a string of state abbreviation
        """
        self.winning_states.append(state)
        self.votes += ELECTORS.get(state,0)
        # ELECTORS += get(state)
        # self.votes.append(votes)
    
    def __len__(self):
        return len(self.winning_states)
    

def main():
    trump = Candidate('Donald Trump')
    clinton = Candidate('Hillary Clinton', winning_states=['CA'], votes=55)
    print(trump)
    print(clinton)
    print()
    print('After election:')
    trump.win_state('FL')
    trump.win_state('TX')
    clinton.win_state('MA')
    print(trump)
    print(clinton)
    print('Does Trump win?')
    print(trump > clinton)
    print(len(trump))

if __name__ == '__main__':
    main()
