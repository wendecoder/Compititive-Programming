class Solution:
    def increment(self, arr, start, end, val):
        arr[start] += val
        if end + 1 < len(arr):
            arr[end+1] -= val
        

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0 for _ in range(n)]
        for book in bookings:
            start, end ,seat = book
            self.increment(arr, start-1, end-1, seat)
            # print(arr)
        res = [0 for _ in range(n)]
        res[0] = arr[0]
        for i in range(1, n):
            res[i] = res[i-1] + arr[i]
        # print(res)
        return res
