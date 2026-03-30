class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for cmd in operations:
            if cmd == "+":
                record.append(record[-1] + record[-2])
            elif cmd == "D":
                record.append(record[-1] * 2)
            elif cmd == "C":
                record.pop()
            else:
                record.append(int(cmd))

        return sum(record)