locals {
  ips = [
  for k, v in var.language :
    {
      language = k,
      external_ip = google_compute_instance.instances[k].network_interface.0.access_config.0.nat_ip,
      ssh_key_path = v
    }
  ]
}


output "ips" {
  description = "A variable for extracting the external IP addresses of the instances"
  value = local.ips
}

### The Ansible inventory file
resource "local_file" "AnsibleHosts" {
  content = templatefile("hosts.tmpl",
  {
    instance_data = local.ips
  }
  )
  filename = "../ansible/inventory/hosts"
}
