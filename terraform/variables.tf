variable "credentials" {
  description = "Credentials"
  type = string
  default = "~/.gc/my-creds.json"
}

variable "project" {
  description = "Project"
  default = "ny-rides-wiliam"
}


# variable "type" {
#   description = "Project Type"
#   default = "AbortIncompleteMultipartUpload"
# }

variable "region" {
  description = "Project Region"
  default = "southamerica-east1"
}

variable "zone" {
  description = "VM zone"
  default = "southamerica-east1-a"
}

variable "disk_image" {
  description = "Name of the SO image"
  default = "ubuntu-2204-jammy-v20250722"
}

variable "location" {
  description = "Project Location"
  default = "BR"
}

# variable "bq_dataset_name" {
#     description = "My BigQuerry Dataset Name"
#     default = "demo_dataset"
# }

# variable "gcs_bucket_name" {
#   description = "My Storage Bucket Name"
#   default = "terraform-demo-467100-terra-bucket"
# }

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default = "STANDARD"
}

variable "instance_name" {
  description = "VM Instance name"
  type = string
}