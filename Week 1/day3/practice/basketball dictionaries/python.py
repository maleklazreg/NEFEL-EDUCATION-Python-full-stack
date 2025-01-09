from python1 import Players
class Player:
    def __init__(self, player_member):
        self.name = player_member["name"]
        self.age = player_member["age"]
        self.position = player_member["position"]
        self.team = player_member.team["team"]

    def 