#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
# thestr = c.formatmonth(2026,1,0,0)
# print(thestr)

# create an HTML formatted calendar
# c = calendar.HTMLCalendar(calendar.SUNDAY)
# thestr = c.formatmonth(2026,1)
# print(thestr)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2026, 8):
  print(i)

  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#   print(name)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
# print("Teams meetings will be on:")
# for i in range(1,13):
#   cal = calendar.monthcalendar(2026, i)
#   week1 = cal[0]
#   week2 = cal[1]
#   if week1[calendar.FRIDAY] != 0:
#     meetday = week1[calendar.FRIDAY]
#   else:
#     meetday = week2[calendar.FRIDAY]
#   print(f"{calendar.month_name[i]}: {meetday}")

