class Player:
    def __init__(self, name=None, chair_number=None, role=None, identity=None):
        self._name = name
        self._role = role
        self._identity = identity

        self._president = False
        self._president_candidate = False
        self._chancellor = False
        self._chancellor_candidate = False

        self._vote = None

        self._chair_number = chair_number

    def get_chair_number(self):
        return self._chair_number

    def set_role(self, role):
        self._role = role

    def set_identity(self, identity):
        self._identity = identity

    def get_role(self):
        return self._role

    def get_identity(self):
        return self._identity

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_vote(self, vote: str):
        if vote != ("NO" or "YES"):
            print("Invalid vote")
            return

        self._vote = vote

    def get_vote(self):
        return self._vote

    def reset_vote(self):
        self._vote = None

    def reset_election_status(self):
        self._president = False
        self._president_candidate = False
        self._chancellor = False
        self._chancellor_candidate = False
