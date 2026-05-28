from autofactory import AutoFactory

factory = AutoFactory()

for carname in 'Chevy Volt', 'Fusion', 'Jeep Sahara', 'Tesla Roadster':
    
    car = factory.create_instance(carname)
    car.start()
    car.stop()
