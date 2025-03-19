output "ecs_cluster_id" {
  description = "The ID of the ECS Cluster"
  value       = aws_ecs_cluster.app_cluster.id
}

output "ecs_service_name" {
  description = "The name of the ECS Service"
  value       = aws_ecs_service.app_service.name
}

output "load_balancer_dns" {
  description = "DNS name of the Application Load Balancer"
  value       = aws_lb.app_lb.dns_name
}