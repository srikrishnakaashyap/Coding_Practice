import fileinput
from typing import List, Tuple
from datetime import timedelta
# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
RAW_TRADE_HEADER = ["trade_id", "trade_date", "time_of_trade", "portfolio", "exchange", "product", "product_type", "expiry_dt", "qty", "strike_price", "side"]
"""


class Solution:

    raw_trade_list = []

    def check_time(self, date1, date2):

        date1 = date1.split(":")
        date2 = date2.split(":")
        if date1[0] == "00":
            date1[0] = "24"

        if date2[0] == "00":
            date2[0] = "24"

        time1 = timedelta(hours=int(date1[0]), minutes=int(
            date1[1]), seconds=int(date1[2]))
        time2 = timedelta(hours=int(date2[0]), minutes=int(
            date2[1]), seconds=int(date2[2]))

        if time1.seconds > time2.seconds and time1.seconds - time2.seconds <= 60:
            return True
        return False

    def process_raw_trade(self, raw_trade: List):
        # print(type(raw_trade[2]))
        if raw_trade[4] == "CBOE":
            if int(raw_trade[-2]) > 0:
                raw_trade.append("BUY")
            else:
                raw_trade.append("SELL")
        self.raw_trade_list.append(raw_trade)

    def run(self) -> List[Tuple[str, str]]:

        raw_trade_list = self.raw_trade_list
        n = len(raw_trade_list)
        answer = []
        for i in range(n):
            if raw_trade_list[i][3] != "Broker":

                j = i + 1
                if j < n:
                    self.check_time(raw_trade_list[j][2], raw_trade_list[i][2])
                while(j < n and self.check_time(raw_trade_list[j][2], raw_trade_list[i][2]) and raw_trade_list[j][3] == "Broker"):
                    if raw_trade_list[i][5] == raw_trade_list[j][5] and raw_trade_list[i][6] == raw_trade_list[j][6] and raw_trade_list[i][10] == raw_trade_list[j][10] and raw_trade_list[i][7] == raw_trade_list[j][7] and raw_trade_list[i][9] == raw_trade_list[j][9]:

                        answer.append(
                            (raw_trade_list[j][0], raw_trade_list[i][0], raw_trade_list[i][2]))
                    j += 1

        temp = sorted(answer, key=lambda x: x[2])
        answer2 = []
        for t in temp:
            answer2.append((t[0], t[1]))
        return answer2


if __name__ == '__main__':
    solution = Solution()
    for row in fileinput.input():
        raw_trade = list(row.strip().replace(" ", "").split(","))
        solution.process_raw_trade(raw_trade)

    print(solution.run())
