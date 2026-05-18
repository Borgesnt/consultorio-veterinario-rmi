import json

class Marshaller:
    @staticmethod
    def marshall(data):
        return json.dumps(data).encode("utf-8")

    @staticmethod
    def unmarshall(data_bytes):
        return json.loads(data_bytes.decode("utf-8"))