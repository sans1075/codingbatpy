# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean
# indicating if we are on vacation, return a string of the form "7:00" indicating when the
# alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it
# should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00"
# and weekends it should be "off".

def alarm_clock(day, vacation):
    if vacation and (day == 0 or day == 6): return "off" # Returns off if it is vacation weekend
    if vacation or day == 0 or day == 6: return "10:00" # Returns 10:00 if it is weekend or vacation weekday
    return "7:00" # Returns 7:00 for a regular weekday
