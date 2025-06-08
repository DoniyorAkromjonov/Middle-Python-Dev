class Note:
    def __init__(self, header, desc, date):
        self.header = header
        self.desc = desc
        self.date = date

    def __str__(self):
        return f"Header: {self.header} \nDescription: {self.desc} \nDeadline: {self.date}"
    print("-------------------------------------------------------------------------------------------------------")








