from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from openai import OpenAI

client = OpenAI()


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class PostGenerationInput(BaseModel):
    """Input schema for LLMforTEXT"""
    argument:str=Field(..., description="A complete prompt which will define the nuance and matter of the social media post.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

class LLMforTEXT(BaseTool):
    name:str = "this tool will generate custom posts for social media (linkedin for now)"
    description: str = (
        "This tool will Take the data from marketing researcher and generate custom text to be posted on social media platform."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument:str) -> str:
        response = client.chat.completions.create({
            model:"gpt-40",
            messages:[
                {
                    role:'user',
                    content:self.args_schema
                }
            ]
        })

        return response.choices[0].message.content
