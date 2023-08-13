from src.errors import InstantiateCSVError

def test_errors():
    instantiateCSVerror = InstantiateCSVError()
    assert instantiateCSVerror.message == "файл поврежден"
