import random

class CrewMember:
    def __init__(self, name):
        self.name = name
        self.alive = True  

class AmongUsLite:
    def __init__(self):
        self.players = []
        for i in range(6):
            self.players.append(CrewMember(f"Игрок {i+1}"))

        self.traitor = random.choice(self.players)
        print(f"(Предатель выбран тайно)")

    def get_alive(self):
        return [p for p in self.players if p.alive]

    def traitor_kill(self):
        alive = self.get_alive()
        victims = [p for p in alive if p != self.traitor]
        if victims:
            victim = random.choice(victims)
            victim.alive = False
            print(f"Предатель убил {victim.name}")

    def vote(self):
        alive = self.get_alive()
        votes = {}

        for voter in alive:
            choices = [p for p in alive if p != voter]
            vote = random.choice(choices)
            votes[vote.name] = votes.get(vote.name, 0) + 1
            print(f"{voter.name} голосует против {vote.name}")

        max_votes = max(votes.values())
        eliminated = [name for name, count in votes.items() if count == max_votes]

        out_name = random.choice(eliminated)
        for p in self.players:
            if p.name == out_name:
                p.alive = False
                print(f"{p.name} изгнан!")

        return out_name

    def check_win(self):
        alive = self.get_alive()
        if self.traitor.alive == False:
            print("Победа экипажа! Предатель изгнан!")
            return True
        if len(alive) == 1 and alive[0] == self.traitor:
            print("Победа предателя! Остался один!")
            return True
        return False

    def play(self):
        round_num = 1
        print("Игра началась!")

        while True:
            print(f"\nРаунд {round_num}")
            self.traitor_kill()
            if self.check_win():
                break

            self.vote()
            if self.check_win():
                break

            alive_names = [p.name for p in self.get_alive()]
            print("Живые:", ", ".join(alive_names))

            round_num += 1

        print("Игра окончена.")


game = AmongUsLite()
game.play()
