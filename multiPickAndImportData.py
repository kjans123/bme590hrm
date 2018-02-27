class MultiPickAndImportData:
    """"class that imports in a list of all csv files names in current directory

    :returns: (superList)-a list of all csv files in working directory
    :raises ImportError: raises error if glob is not found
    """

    def __init__(self):
        self.superList = None
        self.dfList = None
        self.ImportMultiFile()
        self.ConvertMultiFile()

    def ImportMultiFile(self):
        """"method for actually importing in list of csv file names

        :returns: list of all string csv file names
        :raises ImportError: raises error if glob is not found
        """
        try:
            import glob
            import logging
            str1 = logging.DEBUG
            logging.basicConfig(filename="bme590hrmlogs.txt",
                                format='%(levelname)s %(asctime)s %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
            superList = glob.glob("*.csv")
            filterList = list(filter(lambda x: x != "standardPattern.csv",
                              superList))
            self.superList = filterList
            logging.info("succesfully imported glob \
and gathered csv file names")
        except ImportError:
            import logging
            print("failed to import glob. Check if package is installed")
            logging.warning("glob not found")

    def ConvertMultiFile(self):
        """"method for converting the list of csv files into list of
        pandas dataframes

        :returns: list of pandas dataframes
        :raises ImportError: raises error if pandas is not found
        """
        try:
            import pandas as pd
            import logging
            str1 = logging.DEBUG
            logging.basicConfig(filename="bme590hrmlogs.txt",
                                format='%(levelname)s %(asctime)s %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
            pandasList = []
            for i in range(len(self.superList)):
                df = pd.read_csv(self.superList[i], header=None)
                pandasList.append(df)
                logging.debug("succesfully converted " +
                              str(self.superList[i]) + " to dataframe")
            self.dfList = pandasList
        except ImportError:
            import logging
            print("no panda package found. Virtual env might not be activated")
            logging.warning("pandas package not found")
