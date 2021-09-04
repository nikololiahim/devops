output "ips" {
  description = "A variable for extracting the external IP addresses of the instances"
  value = [
    for k, _ in var.language :
    [k, google_compute_instance.instances[k].network_interface.0.access_config.0.nat_ip]
  ]
}
