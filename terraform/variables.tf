variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "vpc_id" {
  description = "VPC ID where resources will be deployed"
  type        = string
}

variable "public_subnets" {
  description = "List of public subnets for the load balancer"
  type        = list(string)
}

variable "private_subnets" {
  description = "List of private subnets for ECS tasks"
  type        = list(string)
}

variable "container_port" {
  description = "Container port for the application"
  type        = number
  default     = 8000
}

variable "image_url" {
  description = "Docker image URL for the application"
  type        = string
}

variable "desired_count" {
  description = "Desired number of ECS tasks"
  type        = number
  default     = 1
}

variable "cpu" {
  description = "Task CPU units"
  type        = string
  default     = "256"
}

variable "memory" {
  description = "Task memory in MB"
  type        = string
  default     = "512"
}

variable "log_group_name" {
  description = "Name of the CloudWatch Logs group"
  type        = string
  default     = "/ecs/blockchain-client"
}