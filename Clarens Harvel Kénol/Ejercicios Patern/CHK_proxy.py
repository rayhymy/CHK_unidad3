import time

class Producer:
    """Define the 'resource-intensive' object to instantiate!"""
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")

class Proxy:
    """"Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print("Artist checking if Producer is available...")

        if self.occupied == 'No':
            #If the producer is available, create a producer object!
            self.producer = Producer()
            time.sleep(2)

            #Make the producer meet the guest!
            self.producer.meet()

        else:
            #otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")

#Instantiate a Proxy
p = Proxy()

#lake the proxy: Artist produce until Producer is available
p.produce()

#change the state to 'occupied'
p.occupied = 'Yes'

#lake the Producer produce
p.produce()



"""Author: Clarens Harvel Kenol
Group: GITI9072-E"""