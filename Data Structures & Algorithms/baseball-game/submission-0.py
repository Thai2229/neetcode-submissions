class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for symbol in operations:
            if symbol == "+":
                record.append(int(record[-1]) + int(record[-2]))
            elif symbol == "C":
                record.pop()
            elif symbol == "D":
                record.append(int(record[-1]) * 2)
            else: 
                record.append(int(symbol))
            
        return sum(record)