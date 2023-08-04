# MicroPython Servo Library for the micro:bit

This is an implementation of a servo control library. It may require some tweaking based on the type of servos you are using. I tested with a number of different position servos and it worked well.
_____

## Important notes:
* Power should be supplied from a different source than the micro:bit directly as most servos work best with at least 4.5V.

* The servo should be connected to the micro:bit's ground as well

* I feel pretty good about the position servo code, but the rotation servo code might need some tweaks.

* Only pins 0, 1 and 2 are currently supported

_____
## Adding the library

In the [micro:bit Python Editor](https://python.microbit.org/):
1. Select the "Project" tab on the menu on the left side of interface
2. Click the "Create file" button
3. Name the file "servo.py" and click the "Create" button
4. Copy the content of the [servo.py file from this github repo](https://github.com/CodeJoyEducation/microbit-servo-python/blob/main/servo.py)
7. Click back over to the main.py and import the new library by adding the line below under the `from microbit import *` line:
  * `from servo import servo`

Now just check out the documentation below to see how to use the library in your code!

---
## API Reference

### servo(pin, type)
You must create a new instance of the servo class for each servo you would like to control

for example to have a servo attached to pin 2 move from 0 to 180 degrees with 1 second in between your code would look like this:
```
    from microbit import *
    from servo import servo
    # ... any other needed libraries ...

    position_servo = servo(pin2, 'postion')

    while True:
        position_servo.set_angle(0)
        sleep(1000)
        position_servo.set_angle(180)
        sleep(1000)
        # ... the rest of your code ...
```
---

### set_angle
Move the servo to a new angle

`<some_servo>.set_angle(new_angle)`

_where `<some_servo>` is the variable name you gave the instance of the servo_

This method has 1 arguments:
* `new_angle`: This is an integer that represent the new angle (0 - 180)

```
    # Creates an servo object for pin1 and sets its position to 90 degrees
    pservo = servo(pin1, 'position')
    pservo.set_angle(90)
```

Note: Attempting to set_angle on a rotation servo will result in an error

---

### set_speed
Move the servo to a new angle

`<some_servo>.set_speed(new_speed)`

_where `<some_servo>` is the variable name you gave the instance of the servo_

This method has 1 arguments:
* `new_speed`: This is an integer that represent the new speed (-100 - 100)

```
    # Creates an servo object for pin1 and sets its position to -50%
    rservo = servo(pin1, 'rotation')
    rservo.set_speed(-50)
```

Note: Attempting to set_speed on a position servo will result in an error
_____

## License

Copyright 2023 CodeJoy

Permission is hereby granted, free of charge, to any person obtaining a copy ofthis software and associated documentation files (the “Software”), to deal in the
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
