import csv
import datetime
import os.path
import sys


class CodingAssignment(object):
    def __init__(self):
        self._data = None
        self._error_data = None
        self._report = None

    def _save_error(self, entry, message):
        entry.append(message)
        self._error_data.append(entry)

    def _parse_entry(self, entry):
        if type(entry) != list:
            self._save_error(entry, "Failed parsing")
            return None
        if len(entry) != 4:
            self._save_error(entry, "Wrong number of columns")
            return None
        if entry[0] == "TIME_STAMP":  # Header
            return None
        # Timestamp
        try:
            timestamp = str(entry[0]).strip()
            datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        except:
            self._save_error(entry, "Invalid timestamp")
            return None
        # Account ID
        try:
            account_id = int(str(entry[1]).strip())
        except:
            self._save_error(entry, "Invalid Account ID")
            return None
        # Employee
        employee = str(entry[2]).strip()
        # Amount
        try:
            amount = float(str(entry[3]).strip())
        except:
            self._save_error(entry, "Invalid Amount")
            return None
        return [timestamp, account_id, employee, amount]

    def load_data(self, input_file):
        if not os.path.isfile(input_file):
            raise ValueError("The input file {0} does not exist".format(input_file))
        self._data = []
        self._error_data = []
        try:
            with open(input_file, "r") as csv_file:
                reader = csv.reader(csv_file, delimiter=",")
                for entry in reader:
                    formatted_entry = self._parse_entry(entry)
                    if formatted_entry:
                        self._data.append(formatted_entry)
        except IOError:
            raise

    def generate_report(self):
        report = {}
        for entry in self._data:
            if entry[0] == "TIME_STAMP":
                continue
            month = entry[0][0:7]
            account_id = entry[1]
            amount = entry[3]
            if account_id not in report:
                report[account_id] = {month: float(amount)}
            elif month not in report[account_id]:
                report[account_id][month] = float(amount)
            else:
                report[account_id][month] += float(amount)
        self._report = report

    def save_error_file(self, error_file):
        try:
            with open(error_file, "w", newline="") as csv_file:
                writer = csv.writer(csv_file, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
                for entry in self._error_data:
                    writer.writerow(entry)
        except FileNotFoundError:
            raise

    def save_report(self, output_file):
        report = self._report
        try:
            with open(output_file, "w", newline="") as csv_file:
                writer = csv.writer(csv_file, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
                writer.writerow(["ACCOUNT_ID", "MONTH", "SUM AMOUNT"])
                for account_id in report.keys():
                    for month in report[account_id]:
                        sum_amount = "{0:.2f}".format(report[account_id][month])
                        writer.writerow([account_id, month.replace("-", "/"), sum_amount])
        except FileNotFoundError:
            raise
        if self._error_data:
            self.save_error_file(output_file + ".err")


def main():
    print("CodingAssignment")

    if len(sys.argv) != 3:
        raise ValueError("Invalid arguments")

    coding_assignment = CodingAssignment()
    coding_assignment.load_data(sys.argv[1])
    coding_assignment.generate_report()
    coding_assignment.save_report(sys.argv[2])

    print("Finished")


if __name__ == "__main__":
    main()
