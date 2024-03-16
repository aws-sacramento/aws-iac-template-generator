# Lambda Authorizer Function

The authorizer function consists of a node application for validating an API Token  [Using AWS Lambda Authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html/).


## Overview
An API Token header `authorizationToken` will be evaluated against an AWS Secret to validate the incoming request from the AWS API Gateway.


![AWS Lambda Authorizer Function](https://docs.aws.amazon.com/images/apigateway/latest/developerguide/images/custom-auth-workflow.png "AWS Lambda Authorizer Architecture")