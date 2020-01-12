import stem.control


with stem.control.Controller.from_port() as controller:
  controller.authenticate()

  tor_pid = controller.get_pid()
  list_of_connected = stem.util.proc.connections(pid=tor_pid)
  print("Size of list %d" %  len(list_of_connected))
  print("Mermory usage: %s" % stem.util.proc.get_memory_usage(pid=tor_pid)[1])
  print("CPU: %s" % stem.util.proc.stats(tor_pid,stem.util.proc.Stat.CPU_UTIME))
  print("CPU: %s" % stem.util.proc.stats(tor_pid,stem.util.proc.Stat.CPU_STIME))