class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "+":
                add1 = record[-1]
                add2 = record[-2]
                record.append(add1 + add2)
            elif op == "D":
                doub = record[-1]
                record.append(doub * 2)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        total = 0
        for num in record:
            total += int(num)
        return total