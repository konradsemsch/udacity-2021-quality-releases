
# Overview

This is the final project of the ``Cloud DevOps using Microsoft Azure Nanodegree Program``. You will find a set of screenshots with short explanations as per the project submission guidelines.

# Successful Pipeline Screenshots

## Environment Creation & Deployment

### Azure Pipeline

The following screenshots show different run of the Azure Pipeline, division of stages in the pipeline, as well as a detailed view of all individual jobs in the pipeline.

![01-pipeline-runs](./screenshots/01-pipeline-runs.png)

![02-pipeline-run-overview](./screenshots/02-pipeline-run-overview.png)

![03-pipeline-jobs-overview.png](./screenshots/03-pipeline-jobs-overview.png)

### Terraform

The following screenshot demonstrate application of Terraform in the pipeline in order to deploy the entire infrastructure used in this project.

![05-terraform-apply](./screenshots/05-terraform-apply.png)

## Automated Testing

The following screenshots show the outcomes of executing different test suites in the pipeline.

### JMeter

Executing a large number of requests requests at different endpoints of the deployed ``FakeRestApi`` to Azure Service App using JMeter both for endurance and stress testing. Please note that html reports for both of these tests are available in the `artefacts` directory of the `submission` folder.

![061-tests-jmeter-endurance](./screenshots/061-tests-jmeter-endurance.png)

![062-tests-jmeter-stress](./screenshots/061-tests-jmeter-stress.png)

### Selenium

Executing a set of functional tests with Selenium against the ``https://www.saucedemo.com`` website.

![070-tests-selenium.png](./screenshots/070-tests-selenium.png)

### Postman

Executing a set of regression and validation tests with Postman against the ``http://dummy.restapiexample.com`` API.

![080-tests-postman-regression](./screenshots/080-tests-postman-regression.png)

![090-tests-postman-validation](./screenshots/090-tests-postman-validation.png)

![100-tests-postman-overview](./screenshots/100-tests-postman-overview.png)

## Monitoring & Observability

### Azure Monitor

In the following screenshot you see the alert that was triggered by the stress tests executed by JMeter. Attached is the email notification, alert rule as well as graph that illustrates the number of requests made against the resource at the point the rule was triggered.

![110-azure-monitor-email](./screenshots/110-azure-monitor-email.png)

![120-azure-monitor-rule](./screenshots/120-azure-monitor-rule.png)

![130-azure-monitor-graph](./screenshots/130-azure-monitor-graph.png)

### Azure Log Analytics

Azure Log Analytics was connected to the deployed VM on which the selenium tests were executed and logs persisted. After the connection was established the logs could be querried and analyzed.

![140-custom-logs](./screenshots/140-custom-logs.png)

### Artefacts

Lists all artefacts produced by the pipeline. I've downloaded them and they are available in the submission zip in the `artefacts` directory of the `submission` folder.

![150-pipeline-artefacts](./screenshots/150-pipeline-artefacts.png)