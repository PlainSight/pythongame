import socket
import select
import queue
import random
import pickle
import time

BUFFERSIZE = 512

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('127.0.0.1', 4321))
listener.listen(10)

incoming = [listener]
outgoing = []

class Minion:
  def __init__(self, ownerid):
    self.x = 50
    self.y = 50
    self.ownerid = ownerid

minionmap = {}

def updateWorld(message):
  arr = pickle.loads(message)
  print(str(arr))
  playerid = arr[1]
  x = arr[2]
  y = arr[3]

  if playerid == 0: return

  minionmap[playerid].x = x
  minionmap[playerid].y = y

try:
  while True:
    time.sleep(0.01)

    ins, outs, ex = select.select(incoming, outgoing, [])
    for i in ins:
      if i is listener:
        #new connection
        (conn, addr) = i.accept()
        print ('Connection address:' + addr[0] + " " + str(addr[1]))
        incoming.append(conn)
        outgoing.append(conn)
        playerid = random.randint(1000, 1000000)
        playerminion = Minion(playerid)
        minionmap[playerid] = playerminion
        conn.send(pickle.dumps(['id update', playerid]))
      else:
        #error here
        data = i.recv(BUFFERSIZE)
        if data:
          #receieved data
          print ('received data:')
          updateWorld(data)
          if i not in outgoing: 
            outgoing.append(i)
        else:
          #a disconnection
          outgoing.remove(i)
          incoming.remove(i)
          i.close()
    for i in outs:
      update = ['player locations']

      for key, value in minionmap.items():
        update.append([value.ownerid, value.x, value.y])
      
      i.send(pickle.dumps(update))
      print ('sent update data')
      updates = False
finally:
  listener.close()