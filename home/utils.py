# home/utils.py

from datetime import datetime, time

def is_restaurant_open() -> bool:
    """
        Determines if the restaurant is currently open based on defined operating hours.
            Returns True if open, False otherwise.
                """

                    # Get current day and time
                        now = datetime.now()
                            current_day = now.strftime("%A")  # e.g., "Monday", "Tuesday", etc.
                                current_time = now.time()

                                    # Define opening hours (example: 9 AM to 10 PM)
                                        # You can customize these hours for each day if needed
                                            opening_hours = {
                                                    "Monday": (time(9, 0), time(22, 0)),
                                                            "Tuesday": (time(9, 0), time(22, 0)),
                                                                    "Wednesday": (time(9, 0), time(22, 0)),
                                                                            "Thursday": (time(9, 0), time(22, 0)),
                                                                                    "Friday": (time(9, 0), time(23, 0)),   # open later on Fridays
                                                                                            "Saturday": (time(10, 0), time(23, 0)),
                                                                                                    "Sunday": (time(10, 0), time(21, 0)),  # closes earlier on Sunday
                                                                                                        }

                                                                                                            # Get today's open and close times
                                                                                                                if current_day not in opening_hours:
                                                                                                                        return False  # In case the day is not defined

                                                                                                                            open_time, close_time = opening_hours[current_day]

                                                                                                                                # Check if current time falls within the range
                                                                                                                                    if open_time <= current_time <= close_time:
                                                                                                                                            return True
                                                                                                                                                else:
                                                                                                                                                        return False
                                                                                                                                                        