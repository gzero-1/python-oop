from data_factory import DataCollectorFactory


class DataLoader(object):
    def __init__(self):
        pass

    def load_data(self):
        data_collector = self.__get_instance("DataCollectorCSV")
        print(data_collector)
        return data_collector.get_patients()

    def __get_instance(self, collector_name):
        data_collector = DataCollectorFactory.get_data_collector_instance(
            "DataCollectorCSV")

        return data_collector
