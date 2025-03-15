class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26
        self.sheet = {}

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.sheet:
            del self.sheet[cell]

    def getValue(self, formula: str) -> int:
        formula = formula[1:] 
        parts = formula.split('+')

        def get_cell_value(part):
            if part.isdigit(): 
                return int(part)
            return self.sheet.get(part, 0)
        
        return sum(get_cell_value(part) for part in parts)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)