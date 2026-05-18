import Pyro5.api
from rmi.message import Message

class Requestor:
    def doOperation(self, remote_ref, method_id, arguments):
        proxy = Pyro5.api.Proxy(remote_ref.uri)

        request_msg = Message.build_request(
            remote_ref.object_name,
            method_id,
            arguments
        )

        reply_msg = proxy.handle_request(request_msg)

        return reply_msg