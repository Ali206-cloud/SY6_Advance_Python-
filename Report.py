# Decorator
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper
class Report:
    def __init__(self, title):
        self.title = title
        self.content = []

    def add(self, text):
        self.content.append(text)
    @classmethod
    def sample_report(cls):
        report = cls("Monthly Report")
        report.add("Sales increased")
        report.add("Profit improved")
        return report

    def __str__(self):
        return self.title + "\n" + "\n".join(self.content)

    def __len__(self):
        return len(self.content)
class Formatter:
    @staticmethod
    @uppercase
    def format(text):
        return text
report = Report.sample_report()
print(report)
print("Sections:", len(report))
print(Formatter.format("End of Report"))