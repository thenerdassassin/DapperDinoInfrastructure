import aws_cdk as core
import aws_cdk.assertions as assertions

from dapper_dino_infrastructure.dapper_dino_infrastructure_stack import DapperDinoInfrastructureStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dapper_dino_infrastructure/dapper_dino_infrastructure_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DapperDinoInfrastructureStack(app, "dapper-dino-infrastructure")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
