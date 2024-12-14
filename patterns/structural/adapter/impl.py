# Целевой интерфейс
class Report:
    """Целевой интерфейс, с которым работает клиент."""

    def get_title(self):
        pass

    def get_content(self):
        pass


# Адаптируемый класс
class OldReportSystem:
    """Старая система отчетности, которая генерирует отчеты в виде строк."""

    def generate_report(self):
        return "Old Report Title\nOld Report Content"


# Адаптер
class ReportAdapter(Report):
    """Адаптер, который преобразует старый формат отчетов в новый."""

    def __init__(self, old_report_system: OldReportSystem):
        self.old_report_system = old_report_system
        self._parse_report()

    def _parse_report(self):
        report = self.old_report_system.generate_report()
        lines = report.split('\n')
        self.title = lines[0]
        self.content = lines[1]

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content


# Клиентский код
def client_code(report: Report):
    """Функция клиентского кода, использующая целевой интерфейс.

    Args:
        report (Report): Объект, реализующий интерфейс Report.
    """
    print(f"Title: {report.get_title()}")
    print(f"Content: {report.get_content()}")


if __name__ == "__main__":
    old_report_system = OldReportSystem()
    adapter = ReportAdapter(old_report_system)

    client_code(adapter)
