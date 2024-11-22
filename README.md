# MAS-Quality-Assurance
Multi-Agent System Quality Assurance
This repository provides Python implementations for testing and analyzing the quality assurance of multi-agent systems (MAS) based on Large Language Models (LLMs). It includes use cases and evaluation methods to ensure the reliability, efficiency, and performance of LLM-powered MAS. The repository contains three key files:

# 1. Event_Planning.py
Purpose: Implements an LLM-based multi-agent system designed to automate the event planning process.
Agents Involved:
Location Finder: Determines the optimal location for an event based on a guest list.
Venue Coordinator: Selects and books a suitable venue in the selected location.
Communications Manager: Drafts and sends event invitation emails to all guests.
Output: Generates email drafts for all guests with event details.
Use Case: Evaluates the MAS under different testing scenarios to identify quality assurance parameters like relevance, correctness, and coherence.
# 2. Quality_Assurance.py
Purpose: Tests the event planning MAS for application and system performance.
Functionality:
Integrates Trulens for evaluating quality metrics such as relevance, groundedness, and correctness of outputs.
Uses AgentOps to measure system-level parameters like session cost, token usage, and time duration.
Scenarios Tested:
Ideal conditions.
Missing or adversarial data.
Scalability with increased workload.
Output: A detailed performance report that identifies strengths and areas for improvement in the MAS.
# 3. Seed_Select.py
Purpose: Analyzes the performance of MAS under different hierarchical structures to find the most efficient configuration for seed selection and farm management recommendations.
Functionality:
Tests various MAS structures such as flat, hierarchical, hybrid, centralized, and decentralized setups.
Uses LangTrace to record metrics like total tokens used, execution time, and cost for each structure.
Output: A comparison of MAS structures to determine the best-suited architecture for specific use cases.
Installation
Clone the repository:
git clone https://github.com/<your-username>/MAS-Quality-Assurance.git
Navigate to the project directory:
cd Multi-Agent System Quality Assurance
This repository provides Python implementations for testing and analyzing the quality assurance of multi-agent systems (MAS) based on Large Language Models (LLMs). It includes use cases and evaluation methods to ensure the reliability, efficiency, and performance of LLM-powered MAS. The repository contains three key files:

Files
1. Event_Planning.py
Purpose: Implements an LLM-based multi-agent system designed to automate the event planning process.
Agents Involved:
Location Finder: Determines the optimal location for an event based on a guest list.
Venue Coordinator: Selects and books a suitable venue in the selected location.
Communications Manager: Drafts and sends event invitation emails to all guests.
Output: Generates email drafts for all guests with event details.
Use Case: Evaluates the MAS under different testing scenarios to identify quality assurance parameters like relevance, correctness, and coherence.
2. Quality_Assurance.py
Purpose: Tests the event planning MAS for application and system performance.
Functionality:
Integrates Trulens for evaluating quality metrics such as relevance, groundedness, and correctness of outputs.
Uses AgentOps to measure system-level parameters like session cost, token usage, and time duration.
Scenarios Tested:
Ideal conditions.
Missing or adversarial data.
Scalability with increased workload.
Output: A detailed performance report that identifies strengths and areas for improvement in the MAS.
3. Seed_Select.py
Purpose: Analyzes the performance of MAS under different hierarchical structures to find the most efficient configuration for seed selection and farm management recommendations.
Functionality:
Tests various MAS structures such as flat, hierarchical, hybrid, centralized, and decentralized setups.
Uses LangTrace to record metrics like total tokens used, execution time, and cost for each structure.
Output: A comparison of MAS structures to determine the best-suited architecture for specific use cases.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/<your-username>/MAS-Quality-Assurance.git
Navigate to the project directory:
bash
Copy code
cd MAS-Quality-Assurance
Install the required Python dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Run Event Planning MAS:
bash
Copy code
python Event_Planning.py
Test Quality Assurance:
bash
Copy code
python Quality_Assurance.py
Evaluate MAS Structures:
bash
Copy code
python Seed_Select.pyQuality-Assurance
Install the required Python dependencies:
pip install -r requirements.txt
Usage
Run Event Planning MAS:
python Event_Planning.py
Test Quality Assurance:
python Quality_Assurance.py
