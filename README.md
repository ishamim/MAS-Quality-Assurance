# MAS-Quality-Assurance
Multi-Agent System Quality Assurance
This repository provides Python implementations for testing and analyzing the quality assurance of multi-agent systems (MAS) based on Large Language Models (LLMs). It includes use cases and evaluation methods to ensure the reliability, efficiency, and performance of LLM-powered MAS. The repository contains three key files:

# 1. Event_Planning.py
* Purpose: Implements an LLM-based multi-agent system designed to automate the event planning process.
* Agents Involved:
  * Location Finder: Determines the optimal location for an event based on a guest list.
  * Venue Coordinator: Selects and books a suitable venue in the selected location.
  * Communications Manager: Drafts and sends event invitation emails to all guests.
* Output: Generates email drafts for all guests with event details.
# 2. Quality_Assurance.py
* Purpose: Tests the event planning MAS for application and system performance.
* Functionality: Integrates Trulens for evaluating quality metrics such as relevance, groundedness, and correctness of outputs.
* Uses AgentOps to measure system-level parameters like session cost, token usage, and time duration.
* Scenarios Tested:
  * Ideal conditions.
  * Missing or adversarial data.
  * Scalability with increased workload.
* Output: A detailed performance report that identifies strengths and areas for improvement in the MAS.

# Installation
* Clone the repository: git clone https://github.com/ishamim/MAS-Quality-Assurance.git
* Navigate to the project directory: cd Multi-Agent System Quality Assurance
* Install the required Python dependencies: pip install -r requirements.txt

# Usage
* Run Event Planning MAS: python Event_Planning.py
* Test Quality Assurance: python Quality_Assurance.py
