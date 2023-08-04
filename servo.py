"""
Library to use position servos directly connected to a signal pin on a micro:bit

Right now only pin0, pin1, and pin2 are supported.

Notes: 

    * Power should be supplied from a different source than the micro:bit directly
        as most servos work best with at least 4.5V.

    * The servo should be connected to the micro:bit's ground as well

    * I feel pretty good about the position servo code, but the rotation servo code
        might need some tweaks.

=================
Copyright 2023 CodeJoy

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in the
Software without restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS 
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from microbit import *

class servo:
    def __init__(self, pin, type = "position"):
        """Creates a new servo object

        :param pin: a micro:bit pin object (pin0, pin1, pin2)
        :param type: the type of servo (position or rotation)
        """
        # Confirm the pin is valid
        if pin not in [pin0, pin1, pin2]:
            raise ValueError("Invalid pin. Must be pin0, pin1, or pin2.")
        
        self.pin = pin
        
        type = type.lower()
        # Confirm that the type is valid
        if type not in ["position", "rotation"]:
            raise ValueError("Invalid type parameter. Must be 'position' or 'rotation'.")
        self.type = type

    # Internal method to convert degrees to pulse width
    def _deg_to_pulse(self, deg):
        if self.type == "position":
            return int((deg / 180 * 105) + 25)
        
        raise ValueError("Invalid type. Must be 'position'.")
    
    # Internal method to convert speed to pulse width
    def _speed_to_pulse(self, speed):
        if self.type == "rotation":
            if speed == 0:
                return 0
            return int((-speed / 100 * 49) + 70)
        
        raise ValueError("Invalid type. Must be 'rotation'.")
        
    def set_angle(self, new_angle: int):
        """Sets the angle of a position servo. An error will be thrown 
            if the servo is not a position servo.

        :param new_angle: the angle to set the servo to (0-180) [int]
        """

        deg = int(new_angle)
        if self.type != "position":
            raise ValueError("Servo is not a position servo.")
        
        if deg < 0 or deg > 180:
            raise ValueError("Angle must be between 0 and 180 degrees.")
        
        pulse = self._deg_to_pulse(deg)
        self.pin.write_analog(pulse)

    def set_speed(self, new_speed: int):
        """Sets the speed of a rotation servo. An error will be thrown 
            if the servo is not a rotation servo.

        :param new_speed: the speed to set the servo to (-100 to 100) [int]
        """

        speed = int(new_speed)
        if self.type != "rotation":
            raise ValueError("Servo is not a rotation servo.")
        
        if speed < -100 or speed > 100:
            raise ValueError("Speed must be between -100 and 100.")

        pulse = self._speed_to_pulse(speed)
        self.pin.write_analog(pulse)