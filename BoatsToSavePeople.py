class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        fir_per = 0
        las_per = len(people) - 1
        numOfBoats = 0
        for i in range(len(people)):
            if limit - people[las_per] < people[fir_per] and fir_per <= las_per:
                numOfBoats = numOfBoats + 1
                las_per = las_per - 1
            elif limit - people[las_per] >= people[fir_per] and fir_per <= las_per:
                numOfBoats = numOfBoats + 1
                las_per = las_per - 1
                fir_per = fir_per + 1
            else:
                break
        return numOfBoats
