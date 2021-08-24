import com.typesafe.sbt.packager.docker.DockerChmodType

name := "app_scala"
maintainer := "m.olokin@innopolis.university"
version := "1.0"

lazy val `app_scala` = (project in file("."))
  .enablePlugins(PlayScala)
  .enablePlugins(DockerPlugin)

Universal / javaOptions ++= Seq(
  "-Dpidfile.path=/dev/null"
)

resolvers += "Akka Snapshot Repository" at "https://repo.akka.io/snapshots/"
Compile / doc / sources := Seq.empty
Compile / packageDoc / publishArtifact := false

scalaVersion := "2.13.5"

libraryDependencies ++= Seq(jdbc, ehcache, ws, specs2 % Test, guice)
libraryDependencies += "org.scalatestplus.play" %% "scalatestplus-play" % "5.1.0" % Test

dockerExposedPorts += 9000
dockerChmodType := DockerChmodType.UserGroupWriteExecute
dockerAlias := DockerAlias(
  None,
  Some("nikololiahim"),
  "moscow_time_scala",
  Some("latest")
)

wartremoverErrors ++= Warts.unsafe
