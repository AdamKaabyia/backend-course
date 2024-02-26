"""
-class voter
    with name,age and addr(address) and a Flag voted that is initialized to zero
    and incramented once voting to insure the user only votes once(validate the vote)

-class vote
    each vote has an id and a candidate
    id is the unique id to(validate the vote) prevent malicious activity
    (for simplicity im using count and incramenting it by 1 each time)

-class candidate
    has name and position

-class election
    with it gets a list of votes and candidates and does:
    store a dictionary with each candidate as the key and the votes he got

    ○ storing the candidates.
    ○ storing the votes themselves.
    ○ casting a vote from a voter, and adding it to the votes
    storage.
    ○ making sure that there are no double votes by the same
    voter.
    ○ counting the votes, showing each candidate how many
    votes they got - fast
"""
import collections


class voter:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr
        self.voted = 0

    def voting(self, count, candidate):
        if vote > 0:
            return
        self.voted += 1
        return vote(count, candidate)


class vote:
    def __init__(self, id, candidate):
        self.id = id
        self.candidate = candidate


class candidate:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class election:
    def __init__(self, candidates, voters):
        self.candidates = {candidate: 0 for candidate in candidates}
        self.voters = voters
        self.votes_cast = []

    def voter_wants_to_vote(self, voter):
        vote = voter.voting()
        if vote is not None and vote not in self.votes_cast:
            self.votes_cast.append(vote)
            self.candidates[vote.candidate] += 1

    def return_winner(self):
        max_index = 0
        max_val = self.candidates[0]
        for k, v in self.candidates:
            if v > max_val:
                max_index = k
                max_val = v
        return max_index
