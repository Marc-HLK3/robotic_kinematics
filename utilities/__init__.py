from robotic_kinematics.utilities.file_reader import FileReader
if __name__ == "__main__":

    reader1 = FileReader(file_path="test.csv")
    data = reader1.read_csv_pdf()
    reader2 = FileReader()
    data = reader2.read_csv_pdf()
