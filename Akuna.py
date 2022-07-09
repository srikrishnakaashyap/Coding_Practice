import fileinput
from typing import List, Tuple
from datetime import timedelta, datetime

# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
RAW_TRADE_HEADER = ["trade_id", "trade_date", "time_of_trade", "portfolio", "exchange", "product", "product_type", "expiry_dt", "qty", "strike_price", "side"]
"""


class Solution:
    raw_trade_list = []

    def check_time(self, date1, date2):

        c = date1 - date2

        print(c.total_seconds() <= 60)
        return c.total_seconds() <= 60

    def process_raw_trade(self, raw_trade: List):
        if raw_trade[4] == "CBOE":
            if int(raw_trade[-2]) > 0:
                raw_trade.append("BUY")
            else:
                raw_trade.append("SELL")
        self.raw_trade_list.append(raw_trade)

    def run(self) -> List[Tuple[str, str]]:
        raw_trade_list = sorted(self.raw_trade_list, key=lambda x: datetime.strptime(
            x[1] + " " + x[2], '%Y-%m-%d %H:%M:%S'))

        print(raw_trade_list)

        n = len(raw_trade_list)
        answer = []
        for i in range(n):
            if raw_trade_list[i][3] == "Broker":

                temp_answer = []
                j = i - 1
                while(j >= 0 and self.check_time(
                        datetime.strptime(
                            raw_trade_list[i][1] + " " + raw_trade_list[i][2], '%Y-%m-%d %H:%M:%S'),
                        datetime.strptime(raw_trade_list[j][1] + " " + raw_trade_list[j][2], '%Y-%m-%d %H:%M:%S'))):

                    if raw_trade_list[j][3] != "Broker" and raw_trade_list[i][5] == raw_trade_list[j][5] and raw_trade_list[i][6] == raw_trade_list[j][6] and raw_trade_list[i][10] == raw_trade_list[j][10] and raw_trade_list[i][7] == raw_trade_list[j][7] and raw_trade_list[i][9] == raw_trade_list[j][9]:

                        temp_answer.append(
                            (raw_trade_list[i][0], raw_trade_list[j][0]))
                    j -= 1

                answer += reversed(temp_answer)

        return answer


if __name__ == '__main__':
    solution = Solution()
    solution.raw_trade_list = [['vgv2os', '2022-01-9', '23:59:59', 'Akuna24', 'CME', 'TSLA', 'P', '2022-05-31', '850', '880', 'SELL'], ['gutvzg', '2022-01-10', '15:12:54', 'Akuna31', 'CME', 'TSLA', 'C', '2022-05-24', '950', '880', 'BUY'], [
        '377tvk', '2022-01-10', '00:00:01', 'Broker', 'CME', 'TSLA', 'C', '2022-05-24', '900', '880', 'BUY'], ['0puaap', '2022-01-10', '15:34:32', 'Akuna17', 'CBOE', 'FB', 'C', '2022-05-24', '800', '800', 'BUY']]


print(solution.run())
