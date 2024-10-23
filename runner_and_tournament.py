
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.time = 0
        self.speed = speed

    def run(self):
        self.time += 0.1
        self.distance = self.speed * 2 * self.time

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)
        return finishers


if __name__ == "__main__":
    h = Runner("Hussein", 10)
    a = Runner("Andrey", 9)
    n = Runner("Nick", 3)
    all_results = Tournament(90, n, h, a).start()
    print(all_results)
    print(h.time)
    print(all_results.get(max(all_results)))
