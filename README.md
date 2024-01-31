# This repository is the main repository for the Automation Project.
# It contains all the automation projects done by groups of developers.

# Table of Contents
* [AmazonAutomation](#AmazonAutomation)
* [InstagramAutomation](#InstagramAutomation)
* [BestBuyAutomation](#BestBuyAutomation)
* [JobsiteAutomation](#JobsiteAutomation)


# Amazon Automation Project

In this project we will automate performing several actions on Amazon.com. The project is intended to familiarize you with the following programing skills and tools:

- Conditionals, Loops, Function, Variables, Data types
- Exploring modules

## Overview

We are looking to create software for recommending a sit-stand desk and would like to find the best desk for any individual. The following criteria are used to evaluate the best desk:

- Price
- Reviews
- Questions
- Percentage of answered questions.
- Brand

The software should prompt for input as needed and output a ranked list of recommendations.

### Desired features

- Output ranked in table
- Input validation
- How to compare items
- Add item to cart/wishlist
- Compare with top results from google.com
- Able to recommend anything based on criteria
- Monitor for price changes

## Prerequisites

Go through the following [tutorial](https://www.browserstack.com/guide/login-automation-using-selenium-webdriver). This tutorial shows how to log onto a web page. You don't have to follow along, but pay attention to the following as you read through:

- Navigating to a webpage
- Locating the relevant web element
- Performing action on the web element

## Setup

Follow the instructions below to setup your [linux/mac]environment for the project. For other environment, or when in doubt, review the class videos.

1. Clone repository and change directory

        git clone git@github.com:DevOps-Fullstack-PythonCohort/AutomationProject.git
        cd AmazonAutomation

2. Create virtual environment
  
        python -m venv .venv
        source .venv/bin/activate

3. Install dependencies. Repeat if requirements.txt is updated.

        python -m pip install -r requirements.txt

