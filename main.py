"""Main file for this python app."""
import seaborn as sns
from utilities import FileReader

if __name__ == "__main__":

    reader = FileReader()
    data = reader.read_csv_pdf()
    # print(data)
    data.info()
 
