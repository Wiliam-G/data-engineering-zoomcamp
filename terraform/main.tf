terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.45.0"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = file(var.credentials)
  project = var.project
  region  = var.region
}

resource "google_compute_instance" "default" {
  name = var.instance_name
  machine_type = "e2-standard-2"
  zone = var.zone

  boot_disk {
    initialize_params {
      image = var.disk_image
    }
  }

  network_interface {
    network = "default"
    access_config {
      
    }
  }

}
