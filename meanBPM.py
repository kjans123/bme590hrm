class MeanBPM:

    """"Class that analyzes raw ECG data (time and voltages) and
returns average BPM over a user specified interval as well as a numpy array
of times when a beat occured. Also returns number of beats detected.

    :param inputDataFrame:  takes as input two-column pandas data frame of ECG
                            data with times and voltages

    :param timeRange: takes as input a time range over which to anayze the ECG
                      data

    :param timeUnit: time unit of ECG data (s=seconds, m=minutes,
                     ms=milliseconds)
    :returns meanBPM: returns the average BPM over user specified interval
    :returns num_beat_times: returns the number of beats detected
    :returns np_beat_times: returns numpy array of times when beats occured
    :raises ImportError: raises error if tkinter, pandas, scipy, numpy or
                         cleanData is not found
    :raises FileNotFoundError: raises error is standardPattern.csv is not found
    :raises AttributeError: raises error if no dataframe is input
    :raises IndexError: raises error if input time range is greater than the
                        length of the ECG test
    :raises ValueError: raises error if time range is 0 or less than 0
    :raises IndexError: raises error if only one heartbeat is detected
                        in time range
    """
    def __init__(self, inputDataFrame, timeRange=None, timeUnit="s"):
        self.inputDataFrame = inputDataFrame
        self.timeUnit = timeUnit
        self.voltageListUnbiased = None
        self.voltageNorm = None
        self.timeList = None
        self.meanBPM = None
        self.num_beat_times = None
        self.np_beat_times = None
        self.beatTimes = None
        self.normalize_data()
        self.timeRange = timeRange
        self.get_beat_times_over_interval()

    def get_standard_pattern(self):
        """"method that gets standard pattern from standardPattern.csv and
returns voltage values list

        :param: takes as input standardPattern.csv file
        :returns valsUnbiased: list of standard Pattern voltages
                               minus their mean
        :raises FileNotFoundError: raises error is standardPattern.csv
                                   is not found
        :raises Import Error: raises error if pandas or numpy is not found
        """
        import logging
        str1 = logging.DEBUG
        logging.basicConfig(filename="bme590hrmlogs.txt",
                            format='%(levelname)s %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
        try:
            import pandas as pd
            logging.info("sucess: imported pandas for meanBPM")
            import numpy as np
            logging.info("success: imported numpy for meanBPM")
            try:
                standFilePath = "standardPattern.csv"
                sdf = pd.read_csv(standFilePath, header=None)
                vals = sdf.values
                vals = vals.squeeze()
                vals = vals.tolist()
                valsUnbiased = vals - np.mean(vals)
                logging.debug("standardPattern file found, \
imported and normalized")
                valsNorm = np.sum(valsUnbiased**2)
                return(valsUnbiased)
            except FileNotFoundError:
                print("standardPattern.csv file not found")
                logging.warning("standardPattern.csv file not found")
        except ImportError:
            print("pandas and/or numpy not found. Check virtual env")
            logging.warning("pandas and/or numpy not found. \
Check virtual env")

    def normalize_data(self):
        """"method that normalizes the input data by subtracting the mean and by
finding the variation for later division. Uses cleanData function
to output two lists (times and voltages).

        :param inputDataFrame: takes as input a raw data frame from ECG data.
        :returns voltageListUnbiased: returns an unbiased list of voltages
        :returns voltageNorm: returns the varation of the ECG voltages
        :returns timeList: returns a list of times over the ECG strip
        :raises AttributeError: raises error if no dataframe is input
        :raises ImportError: raises import error if numpy is not found
        """
        import logging
        str1 = logging.DEBUG
        logging.basicConfig(filename="bme590hrmlogs.txt",
                            format='%(levelname)s %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
        try:
            import numpy as np
            logging.info("success: imported numpy for meanBPM")
            from cleanData import cleanData
            logging.info("success: imported cleanData for meanBPM")
            try:
                voltageList, timeList = cleanData(self.inputDataFrame)
                voltageListUnbiased = voltageList-np.mean(voltageList)
                voltageNorm = np.sum(voltageListUnbiased**2)
                logging.debug("input data found and normalized")
                self.voltageListUnbiased = voltageListUnbiased
                self.voltageNorm = voltageNorm
                self.timeList = timeList
            except AttributeError:
                print("no dataframe input. Please be sure to run \
ImportFile or multiImportFile")
                logging.warning("no dataframe input detected.")
        except ImportError:
            print("numpy and/or cleanData not found")
            logging.warning("numpy not found. Check virtual env")

    @property
    def timeRange(self):
        return self.__timeRange

    @timeRange.setter
    def timeRange(self, timeRange):
        """"method that sets the user input of time interval. If nothing is input,
the timeRange variable sets to NONE. If NONE is detected
as the value of the timeRange variable, this set the
time range interval to the maximum time in the ECG strip.

        :param timeRange: takes as input time interval from class input
        :returns timeRange: returns either the user input time range or, if no
                            user input, returns the max time in the ECG strip.
        """
        import logging
        str1 = logging.DEBUG
        logging.basicConfig(filename="bme590hrmlogs.txt",
                            format='%(levelname)s %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
        if timeRange is None:
            self.__timeRange = max(self.timeList)
            logging.debug("No user input. Max time range interval set.")
        else:
            self.__timeRange = timeRange
            logging.debug("User input detected. Input time range interval \
being used of " + str(self.__timeRange))

    def get_index_of_interval(self):
        """"method that finds the index of the time interval set from the timeRange
method.

        :param timeRange: takes as input the time range variable set from the
                          timeRange method.
        :returns last_time_index: returns the closest index position from the
                                  list of times in the ECG strip to
                                  the user specified time interval,
        :raises IndexError: raises error if the input time range is outside of
                            the time captured from the ECG data.
        :raises ValueError: raises error if user has input a time equal to or
                            less than 0.
        """
        import logging
        str1 = logging.DEBUG
        logging.basicConfig(filename="bme590hrmlogs.txt",
                            format='%(levelname)s %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
        user_interval = self.timeRange
        if user_interval > max(self.timeList):
            raise IndexError('time range is outside of max time on strip')
            logging.warning("user input time range outside of \
max time on strip")
        elif user_interval <= 0:
            raise ValueError("input time interval is less than 0")
            logging.warning("user input time range is less than 0")
        for i in range(len(self.timeList)):
            if self.timeList[i] >= user_interval:
                last_time_index = i
                break
        logging.debug("found index on time list of user time interval. \
Index: " + str(last_time_index))
        return(last_time_index)

    def get_beat_times_over_interval(self):
        """"method that gets the index locations and times of every hearbeat over
the user specified interval. It achieves this via correlation between
the standard pattern voltages and the ECG voltages. The correlation
is divided by the variation of the ECG voltage data. Once found,
all peaks are located. To filter out peaks that are not beat events,
finds mean of all peaks as well as stdev.
Cuts out all peaks that are below the mean plus the stdev divided by 1.5.

        :param sdList: retrieves the list of standard pattern voltages from the
                       method get_standard_pattern.
        :param last_time_index: gets the index of the last time from the method
                                get_index_of_interval.
        :param voltageListUnbiased: gets the unbiased list of data voltages
                                    from the method normalize data.
        :param voltageNorm: gets the variation of the of the ECG data from the
                            method normalize_data.
        :param timeList: gets the list of all times from the
                         method normalize_data.
        :returns beatTimes: list of all times when a beat occured.
        :returns num_beat_times: number of beat events detected.
        :raises IndexError: raises error if only one heartbeat is detected
                            in the user specified time interval.
        :raises ImportError: raises error if numpy, scipy or statistics is not
                             found.
        """
        import logging
        str1 = logging.DEBUG
        logging.basicConfig(filename="bme590hrmlogs.txt",
                            format='%(levelname)s %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
        try:
            import numpy as np
            logging.info("success: imported numpy for meanBPM")
            from scipy import signal
            logging.info("success: imported scipy-signal for meanBPM")
            import statistics as st
            logging.info("success: imported statistics for meanBPM")
            sdList = self.get_standard_pattern()
            last_time_index = self.get_index_of_interval()
            voltageCor = np.correlate(self.voltageListUnbiased,
                                      sdList)/self.voltageNorm
            logging.debug("found correlation between input data and standard \
pattern")
            max_peaks_all = signal.find_peaks_cwt(voltageCor, np.arange(1, 35))
            max_peaks_all = max_peaks_all.tolist()
            max_peaks = []
            for i in range(len(max_peaks_all)):
                if max_peaks_all[i] <= last_time_index:
                    max_peaks.append(max_peaks_all[i])
            logging.debug("found all peaks within user specified \
time. Num peaks= " + str(len(max_peaks)))
            peaksList = []
            for i in range(len(max_peaks)):
                peaksList.append(voltageCor[max_peaks[i]])
            peaksMean = np.mean(peaksList)
            logging.debug("found mean of all peaks " + str(peaksMean))
            peaksSTDev = st.pstdev(peaksList)
            logging.debug("found stdev of all peaks " + str(peaksSTDev))
            high_peaks_list = []
            for i in range(len(max_peaks)):
                if peaksList[i] > (peaksMean+peaksSTDev/1.5):
                    high_peaks_list.append(max_peaks[i])
            if len(high_peaks_list) <= 1:
                logging.warning("only 1 heartbeat found in time interval specified. \
Time interval: " + str(self.__timeRange) + str(self.timeUnit))
                raise IndexError("only 1 heartbeat found in time \
interval specifed. Please choose longer time interval")
            beatTimes = []
            for i in range(len(high_peaks_list)):
                beatTimes.append(self.timeList[high_peaks_list[i]])
            logging.debug("beat times found " + str(len(beatTimes)))
            self.num_beat_times = len(beatTimes)
            self.beatTimes = beatTimes
        except ImportError:
            print("numpy, scipy and/or statistics not found. \
Check virtual env")
            logging.warning("numpy/scipy/statistics not found. \
Check virtual env")

    def convert_beat_times_list_to_np_array(self):
        """"converts the list of beat times from get_beat_times_over_interval to
a numpy array.

        :param beatTimes: takes as input the list of beatTimes from
                          get_beat_times_over_interval method.
        :returns np_beat_times: returns the beat times as a numpy array.
        :raises ImportError: raises error if numpy is not detected.
        """
        import logging
        str1 = logging.DEBUG
        logging.basicConfig(filename="bme590hrmlogs.txt",
                            format='%(levelname)s %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
        try:
            import numpy as np
            logging.info("success: imported numpy for meanBPM")
            beatTimes = self.beatTimes
            np_beat_times = np.array(beatTimes)
            self.np_beat_times = np_beat_times
            logging.debug("converted beat times to numpy array")
        except ImportError:
            print("numpy not found. Check virtual env")
            logging.warning("numpy not found. Check virtual env")

    def get_mean_bpm(self):
        """"method that calculates the average bpm from the list of all beat times.
Does this by finding the difference between every adjacent beat time
and averaging those times. Depending on user input time unit, converts
that number into beats per minute.

        :param beatTimes: takes as input the list of all times when a
                          beat occured from get_beat_times_over_interval method
        :returns meanBPM: returns the average beats per minute measurement over
                          the user specified interval. If the user input
                          a time unit of seconds, multiplies averaged
                          difference of all times by 60. If the user inputs
                          a time of minutes, does nothing. If the
                          user input a time of milliseconds, multiplies
                          averaged difference by 60,000.
        :raises ImportError: raises error if numpy is not found.
        """
        import logging
        str1 = logging.DEBUG
        logging.basicConfig(filename="bme590hrmlogs.txt",
                            format='%(levelname)s %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
        try:
            import numpy as np
            logging.info("success: imported numpy for meanBPM")
            beatTimes = self.beatTimes
            timeDiff = np.diff(beatTimes)
            timeMean = np.mean(timeDiff)
            logging.debug("average time per beat over specified \
interval is: " + str(timeMean) + " " + str(self.timeUnit))
            if self.timeUnit == "s":
                avgBPM = 1/timeMean * 60
                self.meanBPM = round(avgBPM, 3)
                logging.debug("average bpm is: " + str(self.meanBPM))
            elif self.timeUnit == "m":
                avgBPM = 1/timeMean
                self.meanBPM = round(avgBPM, 3)
                logging.debug("average bpm is: " + str(self.meanBPM))
            elif self.timeUnit == "ms":
                avgBPM = (1/timeMean * 1000)*60
                self.meanBPM = round(avgBPM, 3)
                logging.debug("average bpm is: " + str(self.meanBPM))
        except ImportError:
            print("numpy not found. Check virtual env")
            logging.warning("numpy not found. Check virtual env")

    def detect_abnormal_heart_rate(self):
        """"method that checks to see if meanBPM is outside of normal
        range (20 to 250 bpm)

        :param meanBPM: takes as input the calculated mean bpm
        :returns: print warning to check time units and log entry
        """
        import logging
        str1 = logging.DEBUG
        logging.basicConfig(filename="bme590hrmlogs.txt",
                            format='%(levelname)s %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
        if self.meanBPM <= 20 or self.meanBPM >= 250:
            print(str(self.meanBPM) + " is an abnormal heart rate. \
Check entered time units")
            logging.warning("abnormal heart rate of " + str(self.meanBPM))
