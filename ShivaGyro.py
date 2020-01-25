from ev3dev2.sensor.lego import GyroSensor

# Defines a property that sets the compass points for the robot


class ShivaGyro(GyroSensor):
    """
    Defines a property that sets the compass points for the robot
    """

    def __init__(self, port):
        super().__init__(port)
        self.zero_point = self.angle

    @property
    def compass_point(self):
        return self.angle - self.zero_point

    # Sets whatever the gyro is reading to a specified compass point
    @compass_point.setter
    def compass_point(self, current_heading):
        self.zero_point = self.angle - current_heading
