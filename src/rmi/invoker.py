from rmi.message import Message

class Invoker:
    def __init__(self, service_object):
        self.service_object = service_object

    def getRequest(self, request_msg):
        return request_msg

    def sendReply(self, reply_msg):
        return reply_msg

    def invoke(self, request_msg):
        request = self.getRequest(request_msg)

        method_id = request["methodId"]
        args = request["arguments"]

        try:
            if not hasattr(self.service_object, method_id):
                reply = Message.build_reply("ERROR", f"Método {method_id} não existe.")
                return self.sendReply(reply)

            method = getattr(self.service_object, method_id)
            result = method(args)

            reply = Message.build_reply("OK", result)
            return self.sendReply(reply)

        except Exception as e:
            reply = Message.build_reply("ERROR", str(e))
            return self.sendReply(reply)