class MultiPickAndImportData:
    """"class that imports in a list of all csv files names in current directory

    :returns: (superList)-a list of all csv files in working directory
    :raises ImportError: raises error if glob is not found
    """

    def __init__(self):
        self.superList = None
        self.ImportMultiFile()

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
            self.superList = glob.glob("*.csv")
            logging.info("succesfully imported glob \
and gathered csv file names")
            print(self.superList)
        except ImportError:
            print("failed to import glob. Check if package is installed")
            loggin.warning("glob not found")
testClass = MultiPickAndImportData()
