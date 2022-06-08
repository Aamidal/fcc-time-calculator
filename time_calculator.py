def add_time(start, duration, day = None):

    time, period = start.split()

    #converting arguments to integers
    hours, minutes = map(int, time.split(':')) 
    add_hr, add_min = map(int, duration.split(':'))
    noon = ('PM', 'AM')

    new_day = ''
    later = ''

    # Cap minutes to 59, hours to 12.
    excess, minutes = divmod(minutes + add_min, 60)
    hours += excess
    cycles, hours = divmod(hours + add_hr, 12)

    # AM or PM
    period = abs(noon.index(period) - (cycles % 2))
    passed = (period + cycles) // 2

    # Making it Timely
    if hours == 0: 
      hours = 12

    if minutes < 10: 
      minutes = f'0{minutes}'

    if day:
        week = (
            'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
            'Saturday', 'Sunday'
        )
        new_day = f', {week[(week.index(day.capitalize()) + passed) % 7]}'

    if passed == 1:
        later = ' (next day)'
    elif passed != 0:
        later = f' ({passed} days later)'

    return f'{hours}:{minutes} {noon[period]}{new_day}{later}'