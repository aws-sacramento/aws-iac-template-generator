# Steps to deploy the entire stack into an AWS account with SAM CLI

## Prerequisites
- **Make sure you have aws and sam cli's installed**
- **Make sure you have admin access(to deploy all resources) to the aws account**
- **Clone this repository and change directory into it**

## To deploy with default parameters, issue the following set of commands:**
```bash
    $ sam build
    $ sam deploy --resolve-image-repos --region us-west-1 

```

## To deploy with override parameters, issue the following set of commands:**
You can override the environment(stage) and API Token value by using the following parameters in 
the deploy command:

```bash
    $ sam deploy --resolve-image-repos --region us-west-1 --parameter-overrides DeployStage=dev SecretToken=mysecrettoken

```
  

## Warm start strategies:
- **(README.md)https://medium.com/@marcos.duarte242/keeping-your-aws-lambdas-warm-strategies-to-avoid-cold-starts-c3b50a001a6c**

## Cold start analytics:
- **https://betterprogramming.pub/analysing-cold-starts-on-a-nodejs-lambda-360dfb52a08f**