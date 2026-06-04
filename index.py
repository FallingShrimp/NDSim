from nd_sim import EventBus, NDSimulator

events = EventBus(socket_port=8889)
simulator = NDSimulator(events)

simulator.start()
