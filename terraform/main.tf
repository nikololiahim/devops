# This .tf file is used to quickly launch the docker containers
# for the two apps ('moscow_time' and 'moscow_time_scala')

terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "moscow_time" {
  name         = "nikololiahim/moscow_time:latest"
  keep_locally = false
}

resource "docker_container" "moscow_time" {
  image = docker_image.moscow_time.latest
  name  = "moscow_time"
  ports {
    internal = 8000
    external = 8000
  }
}

resource "docker_image" "moscow_time_scala" {
  name         = "nikololiahim/moscow_time_scala:latest"
  keep_locally = false
}

resource "docker_container" "moscow_time_scala" {
  image = docker_image.moscow_time_scala.latest
  name  = "moscow_time_scala"
  ports {
    internal = 9000
    external = 9000
  }
}
