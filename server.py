import socket
import select
import queue

BUFFERSIZE = 512

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('127.0.0.1', 4321))
listener.listen(10)

incoming = [listener]
outgoing = []

messageQueue = queue.Queue()

try:
  while True:
    messages = []

    while messageQueue.empty() == False:
      messages.append(messageQueue.get())

    ins, outs, ex = select.select(incoming, outgoing, [])
    for i in ins:
      if i is listener:
        #new connection
        (conn, addr) = i.accept()
        print ('Connection address:' + addr[0] + " " + str(addr[1]))
        incoming.append(conn)
        outgoing.append(conn)
      else:
        data = i.recv(BUFFERSIZE)
        if data:
          #receieved data
          print ('received data:' + data.decode('utf-8'))
          messageQueue.put(data)
          if i not in outgoing: 
            outgoing.append(i)
        else:
          #a disconnection
          outgoing.remove(i)
          i.close()
    for i in outs:
      for m in messages:
        i.send(m)
        print ('sent data:' + m.decode('utf-8'))
finally:
  listener.close()