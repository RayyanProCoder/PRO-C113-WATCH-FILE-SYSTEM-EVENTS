from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
    
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")
    
    def on_modified(self, event):
        print(f"Hey there! {event.src_path} has been modified.")
    
    def on_moved(self, event):
        print(f"Someone moved {event.src_path} to {event.dest_path}.")

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=True)

try:
    observer.start()
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()

observer.join()
