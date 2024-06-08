import yaml
import subprocess

def retrieve_apigw_endpoint(stack):

        apigw_url = subprocess.run(["aws", "cloudformation", "describe-stacks", f"--stack-name={stack}", "--query",
                            "Stacks[0].Outputs[1].OutputValue"], capture_output=True)\
                            .stdout.decode("ascii")

        if apigw_url:
            # Query output is in the format: "https://.../" --> need to strip whitespaces, "" and suffix "/". 
            return apigw_url.strip().strip("\"").removesuffix("/")     
        else:
            print(f"It seems like something went wrong with {stack} retrieving. You must deploy it first.")
            return "INSERT_APIGW_BASE_URL"

def generate_load_tests(project_root: str, stack: str):

    stack_env = input(f"Load test is being generated for {stack} environment, insert a different one if you want to change it: ")
    
    # Split on '-' char and remove last match (actual environment),
    # then re-join them attaching just inserted stack_env (if inserted). 
    stack = '-'.join(stack.split('-')[:-1])+f'-{stack_env}' if stack_env else stack

    artillery_config = {
        "config": {
            "target": retrieve_apigw_endpoint(stack),
            "plugins": [{
                "apdex": {}
            }, {
                "ensure": {}
            }],
            "ensure": {
                "thresholds": {
                    "conditions": [{
                        "expression": "aggregate.apdex.satisfied > aggregate.apdex.tolerated and aggregate.apdex.frustrated < 0.1 * aggregate.apdex.satisfied"
                    }]
                }
            },
            "phases": [{
                "duration": 0,
                "arrivalRate": 0,
                "rampTo": 0,
                "name": ""
            }]
        },
        "scenarios": [{
            "flow": [{
                "loop": [
                    {
                    "get": {"url": 'INSERT_LAMBDA_URL'}
                }, {
                    "post": {"url": 'INSERT_LAMBDA_URL'}
                }
                ], "count": 0
            }]
        }]
    }

    with open(f"{project_root}/artillery-{stack.split('-')[-1]}.yml", "w") as load_test_file:
        load_test_file.write(yaml.dump(artillery_config))

    print(f"Load test has been generated. You can find it at {project_root}/artillery-{stack}.yml")