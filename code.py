import configparser
import csv

def ini_to_excel_csv(ini_file_path, excel_csv_path):
    config = configparser.ConfigParser()
    config.read(ini_file_path)

    with open(excel_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header row (Sections and Keys)
        header = ["Section"]
        all_keys = set()
        for section in config.sections():
            for key in config.options(section):
                all_keys.add(key)
        header.extend(sorted(list(all_keys)))
        csv_writer.writerow(header)

        # Write data rows
        for section in config.sections():
            row = [section]
            for key in sorted(list(all_keys)):
                value = config.get(section, key, fallback='')
                row.append(value)
            csv_writer.writerow(row)

# Example usage:
ini_to_excel_csv("D:\Python\trial\preprocess.ini", 'output.csv')