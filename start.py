import subprocess
import watchdog
import watchdog.observers

class ReloadHandler(watchdog.events.FileSystemEventHandler):
  def __init__(self):
    self.running_process = None

  def on_modified(self, event):
    if event is not None and '__pycache__' in event.src_path:
      return
    
    if self.running_process:
      self.running_process.kill()
    self.running_process = subprocess.Popen(["python3", 'src/main.py'])

if __name__ == "__main__":
  event_handler = ReloadHandler()
  observer = watchdog.observers.Observer()
  observer.schedule(event_handler, "./src", recursive=True)
  observer.start()

  event_handler.on_modified(None)

  try:
    while True:
      observer.join()
  except KeyboardInterrupt:
    observer.stop()
