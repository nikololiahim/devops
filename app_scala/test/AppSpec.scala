import org.scalatestplus.play.PlaySpec
import org.scalatestplus.play.guice.GuiceOneAppPerSuite
import play.api.http.Status.{NOT_FOUND, OK}
import play.api.test.FakeRequest
import play.api.test.Helpers._

import java.time.format.DateTimeFormatter
import java.time.{LocalDateTime, ZoneId}

class AppSpec extends PlaySpec with GuiceOneAppPerSuite {

  def currentTime: String = {
    val timeFormatter = DateTimeFormatter.ofPattern("HH:mm:ss")
    val formattedTime =
      timeFormatter.format(LocalDateTime.now(ZoneId.of("Europe/Moscow")))
    formattedTime
  }

  "/" should {
    "return status code 200 on a good request" in {
      val someOK = route(app, FakeRequest(GET, "/")).map(status(_))

      someOK must be(Some(OK))
    }
    "return status code 404 on a bad request" in {
      route(app, FakeRequest(GET, "/wrong_request")).map(status(_)) must be(
        Some(NOT_FOUND)
      )
    }
  }

  "HomeController" should {
    "display current time in Moscow" in {
      val home = route(app, FakeRequest(GET, "/")).get
      contentType(home) must be(Some("text/html"))
      status(home) mustBe OK
      contentAsString(home) must include(currentTime)
    }
  }

}
