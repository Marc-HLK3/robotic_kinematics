import pandas as pd
class FileReader():
    def __init__(self, file_path):
        self.file_path = file_path
    
    def pdf(self):
        try:
            pdf = pd.read_csv(self.file_path)
            return pdf
        except Exception as e:
            print(f"Error reading the file: {e}")
            return None
