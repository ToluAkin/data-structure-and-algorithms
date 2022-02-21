# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    max = 0
    times = S.splitlines()
    meetingTimes = [(0,0)]
    meetingDays = {"Mon": 0, "Tue": 1440, "Wed": 2880, "Thu": 4320, "Fri": 5760, "Sat": 7200, "Sun": 8640}
    
    for meeting in times:
        meetingSplit = meeting.split(' ')
        currentMeetingTime = meetingSplit[1].split('-')
        startMeetingSplit = currentMeetingTime[0].split(':')
        endMeetingSplit = currentMeetingTime[1].split(':')

        startingMeetingMinutes = meetingDays[meetingSplit[0]] + int(startMeetingSplit[0]) * 60 + int(startMeetingSplit[1])
        endingMeetingMinutes = meetingDays[meetingSplit[0]] + int(endMeetingSplit[0]) * 60 + int(endMeetingSplit[1])

        newTuple = (startingMeetingMinutes, endingMeetingMinutes)
        meetingTimes.append(newTuple)

    meetingTimes.append((10080, 10080))
    meetingTimes.sort()
    print(meetingTimes)

    for i in range(1, len(meetingTimes)):
        time = meetingTimes[i][0] - meetingTimes[i-1][1]
        if time > max:
            max = time
    return max
print(solution('Sun 10:00-20:00\nFri 05:00-10:00\nFri 16:30-23:50\nSat 10:00-24:00\nSun 01:00-04:00\nSat 02:00-06:00\nTue 03:30-18:15\nTue 19:00-20:00\nWed 04:25-15:14\nWed 15:14-22:40\nThu 00:00-23:59\nMon 05:00-13:00\nMon 15:00-21:00'))
# 'Mon 01:00-23:00\nTue 01:00-23:00\nWed 01:00-23:00\nThu 01:00-23:00\nFri 01:00-23:00\nSat 01:00-23:00\nSun 01:00-21:00'