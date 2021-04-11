from data_collector import DataCollector

class DataCollectorAPI(DataCollector):
    def __init__(self):
        self.base_url = "data_collector"

    def get_patients(self):
        #result = requests.get(f'{self.base_url}/patients')
        result = "api"
        return result
