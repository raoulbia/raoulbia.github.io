Title: AWS Playbook
Date: 2025-03-18
Category: Cloud Deployments
Slug: was_playbook
Summary: AWS Playbook

<br>

### AWS Playbook
```
aws configure sso --use-device-code

aws ecr get-login-password --region eu-central-1 --profile AdministratorAccess-Verodat-390402554384 | docker login --username AWS --password-stdin 390402554384.dkr.ecr.eu-central-1.amazonaws.com/hr-assistant-slack-crewai-mcp

aws sts get-caller-identity --profile AdministratorAccess-Verodat-390402554384

docker build -t hr-assistant-slack-crewai-mcp .

docker tag hr-assistant-slack-crewai-mcp:latest 390402554384.dkr.ecr.eu-central-1.amazonaws.com/hr-assistant-slack-crewai-mcp:latest

aws ecr get-login-password --region eu-central-1 --profile AdministratorAccess-Verodat-390402554384 | docker login --username AWS --password-stdin 390402554384.dkr.ecr.eu-central-1.amazonaws.com

docker push 390402554384.dkr.ecr.eu-central-1.amazonaws.com/hr-assistant-slack-crewai-mcp:latest

aws ecs register-task-definition --cli-input-json file://path/to/your/task-definition.json --profile AdministratorAccess-Verodat-390402554384

aws ecs update-service --cluster default --service hr-assistant-service --force-new-deployment --region eu-central-1 --profile AdministratorAccess-Verodat-390402554384

aws ecs describe-services --cluster default --services hr-assistant-service --region eu-central-1 --profile AdministratorAccess-Verodat-390402554384

```

