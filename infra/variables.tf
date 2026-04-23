variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name prefix"
  type        = string
}

variable "container_port" {
  description = "Streamlit container port"
  type        = number
  default     = 8501
}

variable "desired_count" {
  description = "Number of ECS tasks"
  type        = number
  default     = 0
}

variable "image_uri" {
  description = "Full ECR image URI, including tag"
  type        = string
}