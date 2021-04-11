from builtins import object
from data_collector import DataCollector
from data_api import DataCollectorAPI


class DataCollectorFactory(object):
    @staticmethod
    def get_data_collector_instance(collector_type):
        instance = None
        print(DataCollector.__subclasses__())
        for cls in DataCollector.__subclasses__():
            print(f"This should be the class {cls}")
            print(f"{cls.__name__}--{type(cls.__name__)}")
            if cls.__name__ == collector_type:
                instance = cls()
                print("fount it !!!!!!!!!!!!!!!!!!!!!!!")

                return instance

# csv = DataCollectorFactory.get_data_collector_instance("DataCollectorCSV")
# print(csv)
# print(csv.get_patients())
