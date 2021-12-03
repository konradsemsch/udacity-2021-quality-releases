#!/bin/bash
az deployment group create --resource-group quality-release-rg --name quality-release-log-analytics --template-file log-analytics-template.json