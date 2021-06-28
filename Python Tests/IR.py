import lirc
sockid = lirc.init("myprogram")
print(lirc.nextcode())
lirc.deinit()
