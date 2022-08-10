fr

Server.add_forward("localhost", 7001)

Clock.bpm=100

d1 >> play("ttt...", dur=[.4,.3,.3], sample=PRand(0,4), amp=1)



d2 >> play("X-X-X-..", dur=.5, sample=PRand(0,4))


d3 >> play("ooo ", dur=cascara, sample=0)





b1 >> bbass([0,2,4], dur=1, pan=1, oct=3)
b2 >> bbass([0,2,4], dur=.5 , oct=5, pan=-1)


tt >> hydra(dur=1)

Clock.bpm=120



from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

def print_handler(address, *args):
    print(f"{address}: {args}")


def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")

dispatcher = Dispatcher()
dispatcher.map("/something/*", print_handler)
dispatcher.set_default_handler(default_handler)

ip = "127.0.0.1"
port = 4000

server = BlockingOSCUDPServer((ip, port), dispatcher)
server.serve_forever()  # Blocks forever
