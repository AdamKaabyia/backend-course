class Voter:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr
        self.voted = False

    def vote(self, candidate):
        if not self.voted:
            self.voted = True
            return Vote(Vote.next_id(), candidate)
        else:
            print(f"{self.name} has already voted!")
            return None


class Vote:
    _id_count = 0

    @classmethod
    def next_id(cls):
        cls._id_count += 1
        return cls._id_count

    def __init__(self, id, candidate):
        self.id = id
        self.candidate = candidate


class Candidate:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Election:
    def __init__(self, candidates):
        self.candidates = {candidate.name: 0 for candidate in candidates}
        self.votes_cast = []

    def cast_vote(self, voter, candidate):
        new_vote = voter.vote(candidate)
        if new_vote and all(vote.id != new_vote.id for vote in self.votes_cast):
            self.votes_cast.append(new_vote)
            self.candidates[new_vote.candidate.name] += 1

    def return_winner(self):
        return max(self.candidates, key=self.candidates.get)


# Setup voters and candidates
voters = [Voter(f"Voter {i}", 18 + i, f"Street {i} House {i}") for i in range(1, 6)]
candidates = [Candidate(f"Candidate {i}", "President") for i in range(1, 3)]

# Simulate an election
election_2024 = Election(candidates)

# Simulate voting
for i, voter in enumerate(voters):
    candidate_choice = candidates[i % len(candidates)] # Alternate candidate choice for voters
    election_2024.cast_vote(voter, candidate_choice)

# Determine the winner
winner = election_2024.return_winner()
print(f"The winner is {winner} with {election_2024.candidates[winner]} votes.")