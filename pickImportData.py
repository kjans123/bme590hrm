class PickImportData:
    def __init__(self):
        self.FilePath = None
        self.outPutArray = None
        self.PickFile()
        self.ImportFile()

    def PickFile(self):
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename
        Tk().withdraw()
        filename = askopenfilename()
        self.FilePath = filename
        

    def ImportFile(self):
        import pandas as pd
        import numpy as np
        df = pd.read_csv(self.FilePath,header=None)
        self.outPutArray = df
