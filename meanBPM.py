class MeanBPM:

    def __init__(self, inputDataFrame):
        self.inputDataFrame = inputDataFrame
        self.meanBPM = None
        self.getMeanBPM()

    def getMeanBPM(self):
        import pandas as pd
        import numpy as np
        import math as mt
