from bankaccount import BankAccount


class NewConstructor(BankAccount):
    def __init__(self, file):
        new_file = open(file, 'rt')
        lines = new_file.readlines()
        super().__init__(int(lines[1]))
        self.balance = int(lines[0])
        new_file.close()




