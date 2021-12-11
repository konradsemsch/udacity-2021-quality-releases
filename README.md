
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

![04-terraform-init](./screenshots/04-terraform-init.png)

![05-terraform-apply](./screenshots/05-terraform-apply.png)

## Automated Testing

The following screenshots show the outcomes of executing different test suites in the pipeline.

### JMeter

Executing a total of 400 requests at different endpoints of the deployed ``FakeRestApi`` to Azure Service App using JMeter.

![06-tests-jmeter](./screenshots/06-tests-jmeter.png)

### Selenium

Executing a set of functional tests with Selenium against the ``https://www.saucedemo.com`` website.

![07-tests-selenium](./screenshots/07-tests-selenium.png)

### Postman

Executing a set of regression and validation tests with Postman against the ``http://dummy.restapiexample.com`` API.

![08-tests-postman-regression](./screenshots/08-tests-postman-regression.png)

![09-tests-postman-validation](./screenshots/09-tests-postman-validation.png)

![10-tests-postman-overview](./screenshots/10-tests-postman-overview.png)

## Monitoring & Observability

### Azure Monitor

In the following screenshot you see the alert that was triggered by the stress tests executed by JMeter. Attached is the email notification, alert rule as well as graph that illustrates the number of requests made against the resource.

![11-azure-monitor-email](./screenshots/11-azure-monitor-email.png)

![12-azure-monitor-rule](./screenshots/12-azure-monitor-rule.png)

![13-azure-monitor-graph](./screenshots/13-azure-monitor-graph.png)

### Azure Log Analytics

NOTE: Still working on connecting log analytics, but wanted to submit my project already.

### Artefacts

Lists all artefacts produced by the pipeline.

![artefacts](./screenshots/artefacts.png)