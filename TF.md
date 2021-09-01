# Terraform Best Practices

1. Don’t commit the .tfstate file
   ([source](https://openupthecloud.com/terraform-best-practices/))
2. `terraform fmt` to lint the .tf file
3. `terraform validate` to ensure the correctness of .tf file before
calling `terraform apply`
4. Commit the `.terraform.lock.hcl` file to make sure that `terraform`
uses the same version of plugins and providers
