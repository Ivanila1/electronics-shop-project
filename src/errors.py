class InstantiateCSVError(Exception):
    def __init__(self,  *args, **kwargs):
        self.message = "файл поврежден"
