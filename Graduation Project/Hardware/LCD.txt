import drivers
from time import sleep
display = drivers.Lcd()
      if classIndex_traffic_sign == 14:  # Stop sign has index 14
            display.lcd_display_string("STOP", 1)  # Display on line 1
            sleep(2)
            display.lcd_clear()
        
        elif classIndex_traffic_sign == 7:  # Speed Limit 100 km/h sign has index 7
            display.lcd_display_string("Speed Limit 100", 1)  # Display on line 1
            sleep(2)
            display.lcd_clear()

        elif classIndex_traffic_sign == 33:  # Turn Right Ahead sign has index 33
            display.lcd_display_string("Turn Right Ahead", 1)  # Display on line 1
            sleep(2)
            display.lcd_clear()
        
        elif classIndex_traffic_sign == 34:  # Turn Left Ahead sign has index 34
            display.lcd_display_string("Turn Left Ahead", 1)  # Display on line 1
            sleep(2)
            display.lcd_clear()