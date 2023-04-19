import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
  def __init__(self):
    self.running_process = None

  def on_modified(self, event):
    if self.running_process:
      self.running_process.kill()
    self.running_process = subprocess.Popen(["python3", 'src/main.py'])

if __name__ == "__main__":
  event_handler = ReloadHandler()
  observer = Observer()
  observer.schedule(event_handler, ".", recursive=True)
  observer.start()

  event_handler.on_modified(None)

  try:
    while True:
      observer.join()
  except KeyboardInterrupt:
    observer.stop()
