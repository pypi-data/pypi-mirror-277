import json
from aws_cdk import (
    aws_codedeploy as codedeploy,
    RemovalPolicy,
    Duration,
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    aws_cloudwatch as cloudwatch
)

class StackUtils():

    @staticmethod
    def get_rs_info(environment: str):
        """Retrieve informations about release strategy from configuration file. """

        with open("bluedac_config.json", "r") as config:
            release_strategy = json.loads(config.read())["release_strategy"][environment]

        return release_strategy

    @staticmethod
    def apply_deployment_strategy(stack, environment, lambda_fun: lambda_.Function):
        """Applies desired release strategy to specified lambda function. """

        release_strategy = StackUtils.get_rs_info(environment)

        match release_strategy["name"]:
            case "canary":
                traffic_routing = codedeploy.TimeBasedCanaryTrafficRouting(
                    interval=Duration.minutes(release_strategy["interval"]),
                    percentage=release_strategy["percentage"]
                )

            case "linear":
                traffic_routing = codedeploy.TimeBasedLinearTrafficRouting(
                    interval=Duration.minutes(release_strategy["interval"]),
                    percentage=release_strategy["percentage"]
                )

        new_version = lambda_fun.current_version
        new_version.apply_removal_policy(RemovalPolicy.RETAIN);

        alias = lambda_.Alias(
            lambda_fun,
            f"{release_strategy["name"]}-{lambda_fun.function_name}",
            alias_name=f"{lambda_fun.function_name}-{new_version}-alias",
            version=new_version
        )

        failure_alarm = cloudwatch.Alarm(
            lambda_fun,
            f"{release_strategy["name"]}Alarm-{lambda_fun.function_name}",
            metric=alias.metric_errors(),
            threshold=1,
            alarm_description=f"${lambda_fun.function_name} ${new_version.version} {release_strategy["name"]} deployment failed.",
            evaluation_periods=1
        )

        config = codedeploy.LambdaDeploymentConfig(
            stack,
            f"{release_strategy["name"]}DeploymentConfig-{lambda_fun.function_name}",
            traffic_routing=traffic_routing
        )

        codedeploy.LambdaDeploymentGroup(
            lambda_fun,
            f"{release_strategy["name"]}DeploymentGroup-{lambda_fun.function_name}",
            alias=alias,
            deployment_config=config,
            alarms=[failure_alarm],
        )