import Pyro5.api
from rmi.invoker import Invoker
from server.servico_clinica import ServicoClinicaVeterinaria

@Pyro5.api.expose
class RemoteServer:
    def __init__(self):
        service = ServicoClinicaVeterinaria()
        self.invoker = Invoker(service)

    def handle_request(self, request_msg):
        return self.invoker.invoke(request_msg)

def main():
    daemon = Pyro5.api.Daemon(host="localhost")
    uri = daemon.register(RemoteServer(), objectId="vetclinic")

    print("======================================")
    print("Servidor RMI Clínica Veterinária ONLINE")
    print("Copie a URI abaixo e cole no cliente:")
    print(uri)
    print("======================================")

    daemon.requestLoop()

if __name__ == "__main__":
    main()