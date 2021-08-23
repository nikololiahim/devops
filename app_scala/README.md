# moscow_time_scala

A simple web-application that shows the current time in Moscow, Russian Federation. This time, it was created with Scala
Play Framework.

## Getting Started

### Dependencies

All the tools and dependencies required to run this app can be installed via [`coursier`](https://get-coursier.io/):

```shell
$ cs setup
```

This command does [a lot of things](https://alexarchambault.github.io/posts/2020-09-21-cs-setup.html), but the most
important part is that it makes sure that you have:

- JVM
- Scala and most common Scala tools installed. If you don't have them installed `coursier` will install them for you.

Alternatively, you can rely on [Intellij Idea](https://www.jetbrains.com/idea/) and
its [Scala Plugin](https://plugins.jetbrains.com/plugin/1347-scala). If you have these two installed, you already have
everything to run the app.

### Installing

#### Locally

```shell
$ git clone https://github.com/nikololiahim/devops
$ cd app_scala
```

or you can [import the app as an `sbt` project from Intellij Idea](https://www.jetbrains.com/help/idea/sbt-support.html)
.

#### Docker

The Docker image for this app is publicly
available [on Dockerhub](https://hub.docker.com/r/nikololiahim/moscow_time_scala).

### Executing program

#### Locally

```shell
$ sbt run
```

#### In Docker

```shell
$ docker run nikololiahim/moscow_time_scala:latest
```

After that you can go to [localhost:9000](http://localhost:9000/) and see the app in action.

## Authors

| Name           | E-mail                        | Telegram        |
|----------------|-------------------------------|---------------|
| Mikhail Olokin | m.olokin@innopolis.university | @nikololiahim |

## Version History

* 0.0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

* [Scala Play Example Project](https://github.com/playframework/play-scala-starter-example)
* [Play Framework docs](https://www.playframework.com/)
* [`sbt-docker-plugin` docs](https://www.scala-sbt.org/sbt-native-packager/formats/docker.html)
* [this](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc) `README.md` template
