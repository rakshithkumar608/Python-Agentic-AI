# Advanced data types

# datetime, time, calender
# timedelta

import arrow # type: ignore

brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")


from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavor", "color"])

