package models

import java.time.{LocalDateTime, ZoneId}

class Time(val hours: String, val minutes: String, val seconds: String)

object Time {
  def currentTime: (String, String, String) = {
    val time = LocalDateTime.now(ZoneId.of("Europe/Moscow"))
    val formattedTime =
      Vector(time.getHour, time.getMinute, time.getSecond).map("%02d".format(_))
    (formattedTime(0), formattedTime(1), formattedTime(2))
  }

  def apply: Time = {
    val time = currentTime
    new Time(time._1, time._2, time._3)
  }
}
