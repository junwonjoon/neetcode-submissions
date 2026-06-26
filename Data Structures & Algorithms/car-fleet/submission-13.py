class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return 0
        if len(position) == 1:
            return 1
        #[position, eta]
        position_w_t = [[position[i], 1/(speed[i]/(target - position[i]))] for i in range(len(speed))]
        position_w_t = sorted(position_w_t, key=lambda x: x[0], reverse=True)
        fleet = 1
        i = 1
        lst = []
        cnt = 1
        print(position_w_t)
        while i < len(position_w_t):
            #later car is faster, then it converge
            if position_w_t[i][1] <= position_w_t[i-1][1]:
                position_w_t[i][1] = position_w_t[i-1][1]
            else:
                fleet += 1
            i += 1
        print(position_w_t)
        return fleet    