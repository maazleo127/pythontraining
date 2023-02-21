# import datetime
# #creating datetime object
# da = datetime.date.today()
# dt = datetime.datetime.now()
# #printing the current exact time
# print(da)
# print(dt)

# # importing all required libraries
# import pytz
# import datetime
# #creating datetime object
# dt = datetime.datetime.now()
# #printing the current exact time
# print(dt)
# #Now we convert this time to UTC
# ut = datetime.datetime.now(pytz.utc)
# # utt = ut.timestamp()
# #now we print UTC time
# print(ut)
# from datetime import datetime
# datetime.utcnow()
# from datetime import datetime,timezone
# now_utc = datetime.now(timezone.utc)
# import datetime

# def UtcNow():
#     now = datetime.datetime.utcnow()
# #     return now
# from datetime import datetime, timezone

# def utc_now():
#     return datetime.utcnow().replace(tzinfo=timezone.utc)