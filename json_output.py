class Json_Output:
    """"Class that creates a dictionary for all of the output variables
    previously calculated from ECG data. Once dictionary is created, outputs
    dictionary as JSON file.

    :param filename: takes as input filename of the csv data file
    :param time_range: takes as input the entered time range of the user
    :param time_unit: takes as input the entered time unit of the user
    :param avg_BPM: takes as input the calculated mean BPM
    :param num_beats: takes as input the number of detected beats in the
                      time range
    :param times_of_beats: takes as input a list of all times when a beat
                           was detected
    :param max_min_volt: takes as input a tuple of the max and min voltages
                         detected in the ECG strip
    :param max_time: takes as input the maximum time on the ECG strip
    :returns data: returns above as dictionary (see example)
                   {"time_range": 27.775,
                   "max_time": 27.775,
                   "times_of_beats": [0.6809999999999999, 1.492, 2.281, 3.072,
                   3.861, 4.678, 5.331, 6.327999999999999, 7.169, 7.978, 8.769,
                   9.542, 10.380999999999998, 11.235999999999999, 12.058,
                   12.886, 13.708, 14.503, 15.3, 16.092, 16.914, 17.783,
                   18.605999999999998, 19.392, 20.183, 20.958000000000002,
                   21.744, 22.555999999999997, 23.372,
                   24.2, 25.044, 25.85, 26.625],
                   "max_min_volt": [1.05, -0.68],
                   "mean_BPM": 74.006,
                   "time_unit": "s",
                   "number_of_beats": 33}
    :raises ImportError: raises Import Error if json package is not found
    """
    def __init__(self, filename, time_range, time_unit, avg_BPM,
                 num_beats, times_of_beats, max_min_volt, max_time):
        self.filename = filename
        self.time_range = time_range
        self.time_unit = time_unit
        self.avg_BPM = avg_BPM
        self.num_beats = num_beats
        self.times_of_beats = times_of_beats
        self.max_min_volt = max_min_volt
        self.max_time = max_time
        self.data = None
        self.create_dictionary()
        self.create_json_file()

    def create_dictionary(self):
        """"method that creates the dictionary for use to create the json file

        :param time_range: takes as input the entered time range of the user
        :param time_unit: takes as input the entered time unit of the user
        :param avg_BPM: takes as input the calculated mean BPM
        :param num_beats: takes as input the number of detected beats in the
                          time range
        :param times_of_beats: takes as input a list of all times when a beat
                               was detected
        :param max_min_volt: takes as input a tuple of the max and min voltages
                             detected in the ECG strip
        :param max_time: takes as input the maximum time on the ECG strip
        :returns data: returns above as dictionary (see example)
                       {"time_range": 27.775,
                       "max_time": 27.775,
                       "times_of_beats": [0.6809999999999999, 1.492,
                       2.281, 3.072,
                       3.861, 4.678, 5.331, 6.327999999999999,
                       7.169, 7.978, 8.769,
                       9.542, 10.380999999999998, 11.235999999999999, 12.058,
                       12.886, 13.708, 14.503,
                       15.3, 16.092, 16.914, 17.783,
                       18.605999999999998, 19.392, 20.183, 20.958000000000002,
                       21.744, 22.555999999999997,
                       23.372, 24.2, 25.044, 25.85, 26.625],
                       "max_min_volt": [1.05, -0.68],
                       "mean_BPM": 74.006,
                       "time_unit": "s",
                       "number_of_beats": 33}
        """
        import logging
        str1 = logging.DEBUG
        logging.basicConfig(filename="bme590hrmlogs.txt",
                            format='%(levelname)s %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
        data = {'time_range': self.time_range,
                'time_unit': self.time_unit,
                'mean_BPM': self.avg_BPM,
                'number_of_beats': self.num_beats,
                'times_of_beats': self.times_of_beats,
                'max_min_volt': self.max_min_volt,
                'max_time': self.max_time,
                }
        self.data = data
        logging.debug("dictionary for " + str(self.filename) + " created")

    def create_json_file(self):
        """"method that creates the json file from the dictionary

        :param data: takes as input the data filled dictionary
        :param filename: takes as input the file name of the raw data ECG file
        :returns: json file with the same file names as the raw data
                  ECG csv file
        :raises ImportError: raises error if json package is not found
        """
        import logging
        str1 = logging.DEBUG
        logging.basicConfig(filename="bme590hrmlogs.txt",
                            format='%(levelname)s %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
        try:
            import json
            new_filename = str(self.filename).replace(".csv", "") + ".json"
            with open(new_filename, 'w') as f:
                json.dump(self.data, f)
            logging.info("json package imported")
            logging.debug("json file for: " + str(self.filename) + " created")
        except ImportError:
            print("json package not found")
            logging.warning("json package not found")
