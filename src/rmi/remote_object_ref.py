class RemoteObjectRef:
    def __init__(self, uri, object_name):
        self.uri = uri
        self.object_name = object_name

    def __str__(self):
        return f"RemoteObjectRef(uri={self.uri}, object={self.object_name})"