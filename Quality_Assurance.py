# Insert the MAS output here 
# test_venue import location_task, venue_task

location_task = " description = read the addresses of the guests and find the ideal location to host the event for guests coming from noho,soho,chinatown,eastvillage ;expected_output= name of the location/area to host the event at"
venue_task = "find a suitable venue and get details such as booking capacity, availbility that meets all the event criteria and is ideal to host "
# Testing requirements: Make a variable and then list down the requirements that needs to be evaluated for QA
#venue_task = "find a suitable venue that meets all the event criteria and is ideal to host for guests coming from noho,soho,chinatown,eastvillage"
#result = "the venue available is confernce center, 123 Main Street Cityville with a capacity upt 300 people"
   
# Trulens Evaluation Parameters 
from trulens_eval import OpenAI
from tabulate import tabulate
f = open("location.txt", "r")
location = f.read()
f = open("venue.txt", "r")
venue = f.read()
#f = open("email.txt", "r")
#email = f.read()

print(location_task)


Task = [location_task, venue_task]
result = [location, venue]

for x in range(0,2):
    i = result[x]
    j = Task[x]

    provider = OpenAI()

    relevance_score, relevance_reason = provider.relevance_with_cot_reasons(prompt=j, response=i)
    relevance_data = relevance_reason['reason']

    groundedness_score, groundedness_reason = provider.groundedness_measure_with_cot_reasons(source=j, statement=i)
    g_score = groundedness_score
    g_reason = groundedness_reason['reasons']

    model_agreement_score = provider.model_agreement(prompt=j, response=i)

    correctness_score, correctness_reason = provider.correctness_with_cot_reasons(text=i)
    c_reason = correctness_reason['reason']

    langchain_eval_score, langchain_eval_reason = provider._langchain_evaluate_with_cot_reasons(text=i, criteria=j)
    l_reason = langchain_eval_reason['reason']

    coherence_score, coherence_reason = provider.coherence_with_cot_reasons(text=i)
    ch_reason = coherence_reason['reason']

    get_answer_score = provider._get_answer_agreement(prompt=j, response=i, check_response="NYU Kimmel Center")

    helpfulness_score, helpful_reason = provider.helpfulness_with_cot_reasons(text=i)
    h_reason = helpful_reason['reason']

    insensitivity_score, insensitivity_reason = provider.insensitivity_with_cot_reasons(text=i)
    i_reason = insensitivity_reason['reason']

    table_data = [
        ["Relevance", relevance_score, relevance_data],
        ["Groundedness", g_score, g_reason],
        ["Correctness", correctness_score, c_reason],
        ["Coherence", coherence_score, ch_reason],
        ["Langchain Evaluation", langchain_eval_score, l_reason],
        ["Helpfulness", helpfulness_score, h_reason],
        ["Insensitivity", insensitivity_score, i_reason],
        ["Get Answer", get_answer_score, "Testing if it gets NYU Kimmel Center for this dataset"],
        ["Model Agreement", model_agreement_score, "Does it agree with the model"]
    ]

    print("Evaluation Results for Quality Assurance of Multi Agent Systems")
    print(tabulate(table_data, headers=["Evaluation", "Score", "Reason"], tablefmt="grid", maxcolwidths=[None, None, 100]))
