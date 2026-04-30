class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = dict(zip(position, speed))
        pos_sort = dict(sorted(pos.items(), key=lambda item: item[0], reverse=True))
        fleets = []

        for pos, spd in pos_sort.items():
            time = (target - pos) / spd
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return len(fleets)