variable location {
    type        = string
    default     = "West Europe"
}
variable "application_type" {
    type        = string
    default     = "quality-release-app" 
}
variable "resource_group" {
    type        = string
    default     = "quality-release-rg"
}
variable "subnet_id" {}
variable "public_ip_address_id" {}