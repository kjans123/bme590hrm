class MaxMinVoltsTimeDur:
    """"class that takes as input dataframe with time and voltage columns.
    Analyzes for max and min voltages. Returns maximum on ECG time strip.

    :param inputDataFrame: takes as input two-column pandas data frame of ECG
                           data with times and voltages
    :param timeUnit: time unit of ECG data (s=seconds, m=minutes,
                     ms=milliseconds)
    :returns max_time_strip: returns the max time on the ECG strip
    :returns tuple_min_max_volts: returns a tuple of form (max_volts,min_volts)
                                  for max voltage and min voltage in strip
    :raises ImportError: raises error if cleanData file is not found
    :raises AttributeError: raises error if no dataframe is input to class
    """
    def __init__(self, inputDataFrame, timeUnit="s"):
        self.inputDataFrame = inputDataFrame
        self.timeUnit = timeUnit
        self.max_time_strip = None
        self.tuple_min_max_volts = None
        self.get_data()

    def get_data(self):
        """"method that imports data via cleanData function. Finds max and min
        voltages as well as the maximum time on the ECG strip"

        :param: takes as input a pandas dataframe
        :raises ImportError: raises error if cleanData file is not found
        :raises AttributeError: raises error if no dataframe is input to class
        """
        import logging
        str1 = logging.DEBUG
        logging.basicConfig(filename="bme590hrmlogs.txt",
                            format='%(levelname)s %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
        try:
            from cleanData import cleanData
            try:
                voltageList, timeList = cleanData(self.inputDataFrame)
                volt_max = max(voltageList)
                volt_min = min(voltageList)
                self.tuple_min_max_volts = (volt_max, volt_min)
                self.max_time_strip = max(timeList)
                logging.debug("max volts: " + str(volt_max))
                logging.debug("min volts: " + str(volt_min))
                logging.debug("max time: " + str(self.max_time_strip) +
                              " " + str(self.timeUnit))
            except AttributeError:
                print("no dataframe input")
                logging.warning("no dataframe found")
        except ImportError:
            print("cleanData not found. Check file is in local dir")
            logging.warning("cleanData not found. Check file is in local dir")
