class DivByNull:
    def __init__(self, delimoe, delitel):
        self.delimoe = delimoe
        self.delitel = delitel

    @staticmethod
    def divide_by_null(delimoe, delitel):
        try:
            return delimoe / delitel
        except:
            return (f"делить на ноль нельзя")


div = DivByNull(456, 123)

print(DivByNull.divide_by_null(10, 0))
print(DivByNull.divide_by_null(10, 2))

print(div.divide_by_null(100, 0))
