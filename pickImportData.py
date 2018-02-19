class PickImportData:

    """"class that import csv file via tkinter GUI and converts
    to pandas DataFrame

    :returns: (FilePath)-string that is the file path for csv file
    :returns: (outPutArray)-pandas DataFrame converted from csv file
    :raises ImportError: raises error if tkinter or pandas is not found
    """
    def __init__(self):
        self.FilePath = None
        self.outPutArray = None
        self.PickFile()
        self.ImportFile()

    def PickFile(self):

        """method by which the user selects CSV file via tkinter GUI

        :returns: string file path for csv file
        :raises ImportError: raises error if tkinter is not found
        """

        try:
            from tkinter import Tk
            from tkinter.filedialog import askopenfilename
            Tk().withdraw()
            filename = askopenfilename()
            self.FilePath = filename
        except ImportError:
            print("tkinter not imported. Check virtual env is activated")

    def ImportFile(self):

        """method by which the chosen csv file is converted to pandas DataFrame

        :returns: csv file as pandas DataFrame
        :raises ImportError: raises error if pandas is not found
        """

        try:
            import pandas as pd
            df = pd.read_csv(self.FilePath, header=None)
            self.outPutArray = df
            print(df)
        except ImportError:
            print("pandas not found. Check virtual env is activated")
