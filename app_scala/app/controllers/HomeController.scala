package controllers

import models.Time
import play.api.mvc._

import javax.inject._

/** This controller creates an `Action` to handle HTTP requests to the
  * application's home page.
  */
@Singleton
class HomeController @Inject() (cc: ControllerComponents)
    extends AbstractController(cc) {
  def index: Action[AnyContent] = Action {
    Ok(views.html.index(Time.apply))
  }

}
