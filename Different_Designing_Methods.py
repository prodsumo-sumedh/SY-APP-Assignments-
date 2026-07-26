# Observer Pattern
class Subject:
   def __init__ (self):
      self._Observers = []

   def attach(self, observer): 
      self._Observers.append (observer)

   def detach(self, observer): 
      self._Observers.remove(observer)

   def notify(self, message):
      for observer in self._Observers:
         observer.update(message)

class Observer:
   def update(self, message):
       print(f"Recieved message: {message}" )

#Usage
subject = Subject()
observer1 =Observer()
observer2 = Observer()

subject.attach(observer1) 
subject.attach(observer2)
subject.notify("Hello Observers!")

# Output
'''Recieved message: Hello Observers!
   Recieved message: Hello Observers!'''
