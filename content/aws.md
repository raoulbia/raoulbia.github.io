Title: AWS Playbook
Date: 2025-03-18
Category: Cloud Deployments
Slug: was_playbook
Summary: AWS Playbook

<br>

### AWS Playbook
```
aws configure sso --use-device-code

aws ecr get-login-password --region eu-central-1 --profile <Profile-Name> | docker login --username AWS --password-stdin <123>.dkr.ecr.eu-central-1.amazonaws.com/<Repository-Name>

aws sts get-caller-identity --profile <Profile-Name>

docker build -t <Repository-Name> .

docker tag <Repository-Name>:latest <123>.dkr.ecr.eu-central-1.amazonaws.com/<Repository-Name>:latest

aws ecr get-login-password --region eu-central-1 --profile <Profile-Name> | docker login --username AWS --password-stdin <123>.dkr.ecr.eu-central-1.amazonaws.com

docker push <123>.dkr.ecr.eu-central-1.amazonaws.com/<Repository-Name>:latest

aws ecs register-task-definition --cli-input-json file://path/to/your/task-definition.json --profile <Profile-Name>

aws ecs update-service --cluster default --service hr-assistant-service --force-new-deployment --region eu-central-1 --profile <Profile-Name>

aws ecs describe-services --cluster default --services hr-assistant-service --region eu-central-1 --profile <Profile-Name>

```

