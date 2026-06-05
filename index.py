from rmtt_simulator import EventBus, RoboMaster

events = EventBus(socket_port=8889)
simulator = RoboMaster(events)

simulator.start()
