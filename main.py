import src.load_data
import src.process
import src.data

from data import load_data
data_sorted1 = data.load_data()
processor = Process()
data_sorted2 = processor.apply_filters(data_sorted1)

