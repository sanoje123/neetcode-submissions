class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = sorted(zip(position,speed), reverse=True)
        
        for pos, sp in cars:
            time = (target - pos) / sp

            if not fleets:
                fleets.append(time)
                continue

            if fleets[-1] < time:
                fleets.append(time)


        return len(fleets)

            
            