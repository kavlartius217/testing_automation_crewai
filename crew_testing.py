from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
import os


@CrewBase
class TestingBot():
  """This crew aims to automate testing"""
  agents_config="/home/kavin/testing_automation_poc/agents_testing.yaml"
  tasks_config="/home/kavin/testing_automation_poc/tasks_testing.yaml"

  @agent
  def code_analyzer_agent(self)->Agent:
    return Agent(
      config=self.agents_config['code_analyzer_agent'],
      verbose=True
    )

  
  @agent
  def test_case_generator_agent(self)->Agent:
    return Agent(
      config=self.agents_config['test_case_generator_agent'],
      verbose=True
    )


  @agent
  def test_executor_agent(self)->Agent:
    return Agent(
      config=self.agents_config['test_executor_agent'],
      verbose=True,
      allow_code_execution=True,
      #code_execution_mode="safe",
      max_execution_time=300,
      max_retry_limit=3
    )


  @agent
  def bug_analyzer_agent(self)->Agent:
    return Agent(
      config=self.agents_config['bug_analyzer_agent'],
      verbose=True
    )

  @task
  def code_analysis_task(self)->Task:
    return Task(
      config=self.tasks_config['code_analysis_task']
    )

  @task
  def test_case_generation_task(self)->Task:
    return Task(
      config=self.tasks_config['test_case_generation_task']
    )

  @task
  def test_executor_task(self)->Task:
    return Task(
      config=self.tasks_config['test_executor_task']
    )

  @task
  def bug_analysis_task(self)->Task:
    return Task(
      config=self.tasks_config['bug_analysis_task']
    )

  @crew
  def crew(self)->Crew:
    return Crew(
      agents=[self.code_analyzer_agent(),self.test_case_generator_agent(),self.test_executor_agent(),self.bug_analyzer_agent()],
      tasks=[self.code_analysis_task(),self.test_case_generation_task(),self.test_executor_task(),self.bug_analysis_task()],
      process=Process.sequential,
      verbose=True
    )

test_1=TestingBot()
result = test_1.crew().kickoff({
    "code": """class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]
""",
    "framework": "Pytest"
})

print(result)
