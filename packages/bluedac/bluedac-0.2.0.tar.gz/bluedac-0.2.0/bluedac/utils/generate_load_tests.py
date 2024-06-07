import yaml
import subprocess

def retrieve_apigw_endpoint(stack):

    apigw_url = subprocess.run(["aws", "cloudformation", "describe-stacks", f"--stack-name={stack}", "--query",
                        "Stacks[0].Outputs[1].OutputValue"], capture_output=True)\
                        .stdout.decode("ascii")

    # Query output is in the format: "https://.../" --> need to strip whitespaces, "" and suffix "/". 
    return apigw_url.strip().strip("\"").removesuffix("/")

def generate_load_tests(project_root: str, stack: str):

    new_stack = input(f"Load test is being generated for {stack}, insert a different stack if you want to change it: ")
    stack = new_stack if new_stack else stack

    artillery_config = {
        "config": {
            "target": retrieve_apigw_endpoint(stack),
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

    with open(f"{project_root}/artillery-{stack}.yml", "w") as load_test_file:
        load_test_file.write(yaml.dump(artillery_config))

    print(f"Load test has been generated. You can find it at {project_root}/artillery-{stack}.yml")