from crewai import Agent, Task, Crew
import os
from langchain_cohere import ChatCohere
os.environ["COHERE_API_KEY"] = ""
llm = ChatCohere()
os.environ["SERPER_API_KEY"] = ''
from crewai_tools import ScrapeWebsiteTool, SerperDevTool, FileReadTool
from langchain_community.tools.gmail import GmailCreateDraft
from langchain_community.tools.gmail.get_thread import GmailGetThread
from langchain_community.agent_toolkits import GmailToolkit
from tools import CreateDraftTool

from langchain_core.messages import ToolCall
from langchain_community.tools.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)

# Can review scopes here https://developers.google.com/gmail/api/auth/scopes
# For instance, readonly scope is 'https://www.googleapis.com/auth/gmail.readonly'
credentials = get_gmail_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file="credentials.json",
)
api_resource = build_resource_service(credentials=credentials)




# Initialize the tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
file_read_tool = FileReadTool(file_path="Guestlist.JSON")

# Agent 1: Location Finder
location_finder = Agent(
    role="Location Finder",
    goal="To read the address of the expected guest list and Find a location/area that is the most ideal for all the guests to meet at",
    tools=[file_read_tool, search_tool, scrape_tool],
    verbose=True,
    backstory=("specializes in crunching guest list data and pinpointing the optimal location for any gathering"
               "Its internal file reader allows it to process guest lists with lightning speed."
               " Utilizing a sophisticated search engine, Compass can analyze addresses and identify geographic trends"
               "it can scrape relevant data from online resources, further enhancing its location selection process."
              )
)

# Agent 2: Venue Coordinator
venue_coordinator = Agent(
    role="Venue Coordinator",
    goal="Book an appropriate venue at the location"
         "based on event requirements and the number of guests that are coming which can be counted using the file",
    tools=[search_tool, scrape_tool, file_read_tool],
    verbose=True,
    backstory=(
        "With a keen sense of space and "
        "understanding of event logistics, "
        "you excel at finding and securing "
        "the perfect venue that fits the event's theme, "
        "size, and budget constraints."
    )
)

# Agent 3: Marketing and Communications Agent
communications_agent = Agent(
    role="Communications manager",
    goal="send out invitation email to the guests",
    tools=[file_read_tool, search_tool, GmailGetThread(api_resource=api_resource),CreateDraftTool.create_draft],
    verbose=True,
    backstory=("You are a skilled writer, adept at crafting clear, concise, and effective email responses."
              "Your strength lies in your ability to communicate effectively, ensuring that each response is tailored to address the specific needs and context of the email."
              "Craft invitation emails according to the specified event type and should contain all the necessary information required"
              "read the guest list file to collect the email addresses and send the invitation emails to the guest"
              )
)

location_task= Task(
    description = "read the addresses of the guests and find the ideal location to host the event at",
    expected_output= "name of the location/area to host the event at",
    human_input = True,
    agent = location_finder
)

from pydantic import BaseModel
class VenueDetails(BaseModel):
    name: str
    address: str
    capacity: int
    booking_status: str

venue_task = Task(
    description="Find a venue in the location that location_finder found that is available at {tentative_date} "
                "that meets criteria for {event_topic}, {event_description}, {budget}, {venue_type}.",
    expected_output="All the details of a specifically chosen"
                    "venue you found to accommodate the event.",
    human_input=True,
    output_json=VenueDetails,
    output_file="venue_details.json",  
    agent=venue_coordinator
)



communications_task = Task(
    description="Promote the {event_topic} at the location and venue decided by the location_finding agent and the venue_coordinator "
                "Draft emails to invite the guests on the guest list by collecting their email address from the input file"
                "sending them emails with the venue location, dtae, time and event name"
                "Use the tool provided to draft each of the responses."
				"When using the tool pass the following input: to (sender to be responded),subject,message"
				"You MUST create all drafts before sending your final answer."
				"Your final answer MUST be a confirmation that all responses have been drafted.",
    expected_output="invitation email drafted in my email ishashamim17@gmail.com with to='email' of every guest adressesing their name; subject= {event_topic} and body= event details ",
    async_execution=False,
    agent=communications_agent
)


event_management_crew = Crew(
    agents=[location_finder, venue_coordinator, communications_agent],
    tasks=[location_task, venue_task, communications_task],
)

event_details = {
'event_topic': "Tech Innovation Conference",
'event_description': "A gathering of tech innovators "
"and industry leaders "
"to explore future technologies.",
'tentative_date': "2024-09-15",
'budget': 20000,
'venue_type': "Conference Hall"
}

result = event_management_crew.kickoff(inputs=event_details)
import json
from pprint import pprint

with open('venue_details.json') as f:
    data = json.load(f)
pprint(data)

