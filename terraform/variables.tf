variable "credentials" {
  description = "Credentials"
  type = string
  default = "./keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default = "terraform-demo-467100"
}

variable "type" {
  description = "Project Type"
  default = "AbortIncompleteMultipartUpload"
}

variable "region" {
  description = "Project Region"
  default = "us-central1"
}

variable "location" {
  description = "Project Location"
  default = "US"
}

variable "bq_dataset_name" {
    description = "My BigQuerry Dataset Name"
    default = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default = "terraform-demo-467100-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default = "STANDARD"
}