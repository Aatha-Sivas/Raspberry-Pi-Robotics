#IR Test
import lirc
import time
sockid = lirc.init("irexec", blocking=False)

while True:
    try:
        button = lirc.nextcode()
        print("Press a button")
        if len(button) == 0: continue
        print(button[0])
        time.sleep(1)
    except KeyboardInterrupt:
        lirc.deinit()
        break
