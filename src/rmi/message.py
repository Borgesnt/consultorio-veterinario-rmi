class Message:
    @staticmethod
    def build_request(object_reference, method_id, arguments):
        return {
            "type": "request",
            "objectReference": object_reference,
            "methodId": method_id,
            "arguments": arguments
        }

    @staticmethod
    def build_reply(status, result):
        return {
            "type": "reply",
            "status": status,
            "result": result
        }