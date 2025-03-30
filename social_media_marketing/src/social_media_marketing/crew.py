from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, after_kickoff
from crewai_tools import ScrapeWebsiteTool
from crewai.tools import tool

import pandas as pd
from pydantic import BaseModel, Field

from openai import OpenAI
client = OpenAI()


# Adding classes for structured output

class Posts(BaseModel):
	facebook_post:str = Field(..., description='A post tailored for Facebook...')
	linkedin_post:str = Field(..., description='A post tailored for LinkedIn...')
	x_post:str = Field(..., description=' A post tailored for X (Twitter)...')
	url_from_DALL:str = Field(..., description='Only the URL that comes after running the generateLogoFunction tool...')


# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


# CUSTOM TOOLS
web_scrap = ScrapeWebsiteTool()

@tool('generateLogoFunction')
def generateLogoFunction(prompt:str)-> str:
	"""Takes in prompt and Generates Logo in image format and returns URL of the image"""
		# response = client.images.generate(
		# 	model='dalle-3',
		# 	prompt=prompt,
		# 	size='1024x1024',
		# 	quality="hd",
		# 	n=1
		# )
		# return response.data[0].url
	print(prompt)
	return 'https://upload.wikimedia.org/wikipedia/en/a/ae/Love_TV_Logo.png'


@CrewBase
class SocialMediaMarketing():
	"""SocialMediaMarketing crew"""

	def __init__(self):
		self.name = ''
	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools

		


	@agent
	def business_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['business_analyst'],
			verbose=True
		)

	@agent
	def market_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['market_researcher'],
			verbose=True
		)
	
	@agent
	def content_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['content_strategist'],
			verbose=True
		)
	

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def analyze_business(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_business'],
			tools=[web_scrap],
		)

	@task
	def conduct_market_research(self) -> Task:
		return Task(
			config=self.tasks_config['conduct_market_research'],
			tools=[web_scrap],
		)
	@task
	def generate_social_media_content(self) -> Task:
		return Task(
			config=self.tasks_config['generate_social_media_content'],
			tools=[generateLogoFunction],
			output_pydantic=Posts,
			output_file='content.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the SocialMediaMarketing crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
	@after_kickoff
	def costing(self):
		try:
			if not hasattr(self, 'executed_crew'):
				raise Exception("Crew hasn't executed yet.")
			usage_metrics = self.executed_crew.usage_metrics
			costs = 0.15 * (usage_metrics.prompt_tokens + usage_metrics.completion_tokens)/1000000
			print(f"Total Costs : ${costs:.4f}")
			df_usage_metrics = pd.Dataframe([usage_metrics.dict()])
			print(df_usage_metrics)
			df_usage_metrics.to_csv('cost.csv', index=False)

		except Exception as e:
			raise Exception(f"An error occured while calculating costs: {e}")
    

