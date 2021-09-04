terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file("devops2021-324917-service-account.json")
  project     = "devops2021-324917"
  region      = "europe-north1"
  zone        = "europe-north1-a"
}

resource "google_compute_network" "vpc_network" {
  name                    = "terraform-network"
  auto_create_subnetworks = "true"
}

resource "google_compute_firewall" "rules" {
  description = "Firewall rules to allow SSH and HTTP traffic through"
  name        = "allow-ssh"
  network     = google_compute_network.vpc_network.name
  allow {
    protocol = "tcp"
    ports = [
      "22", "80"
    ]
  }
  target_tags = [
    "python-instance",
    "scala-instance"
  ]
  source_ranges = [
    "0.0.0.0/0"
  ]
}

resource "google_compute_instance" "instances" {
  for_each     = var.language
  description  = "An instance for the ${title(each.key)} application."
  name         = "${each.key}-instance"
  machine_type = "f1-micro"
  tags = [
    "${each.key}-instance"
  ]
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }
  metadata = {
    ssh-keys = "${each.key}:${file(each.value)}"
  }

  network_interface {
    network = google_compute_network.vpc_network.self_link
    access_config {
    }
  }
}
