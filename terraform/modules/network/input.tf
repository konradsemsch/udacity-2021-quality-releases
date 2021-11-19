# Resource Group
variable location {
    type        = string
    default     = "West Europe"
}
variable "resource_group" {
    type        = string
    default     = "quality-release-rg"
}
# Network
variable virtual_network_name {
    type        = string
    default     = "quality-relase-vm"
}
variable address_space {
    type        = list(string)
    default     = ["10.5.0.0/16"]
}
variable "address_prefix_test" {
    type        = string
    default     = "10.5.1.0/24"
}
variable "application_type" {
    type        = string
    default     = "quality-release-app" 
}


