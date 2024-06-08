import json
from typing import List

# from beartype import beartype

from swarms.structs.agent import Agent
from swarms.structs.base_swarm import BaseSwarm
from swarms.utils.loguru_logger import logger
from pydantic import BaseModel, Field
from swarms.structs.conversation import Conversation


class HiearchicalRequest(BaseModel):
    task: str = Field(
        None,
        title="Task",
        description="The task to send to the director agent.",
    )
    agent_name: str = Field(
        None,
        title="Agent Name",
        description="The name of the agent to send the task to.",
    )


class HiearchicalRequestDict(BaseModel):
    task: str = Field(
        None,
        title="Task",
        description="The task to send to the director agent.",
    )
    agent_name: str = Field(
        None,
        title="Agent Name",
        description="The name of the agent to send the task to.",
    )

    class Config:
        schema_extra = {
            "example": {
                "task": "task",
                "agent_name": "agent_name",
            }
        }


"""
Boss -> json -> workers -> json -> Boss


Parse the JSON data and activate the selected agent.

parse -> execute
"""


class HiearchicalSwarm(BaseSwarm):
    """
    A class representing a hierarchical swarm.

    Attributes:
        name (str): The name of the hierarchical swarm.
        description (str): The description of the hierarchical swarm.
        director (Agent): The director agent of the hierarchical swarm.
        agents (List[Agent]): The list of agents in the hierarchical swarm.
        max_loops (int): The maximum number of loops to run the swarm.
        long_term_memory_system (BaseSwarm): The long term memory system of the swarm.
        custom_parse_function (callable): A custom parse function for the swarm.

    Methods:
        swarm_initialization(*args, **kwargs): Initializes the hierarchical swarm.
        find_agent_by_name(agent_name: str = None, *args, **kwargs): Finds an agent in the swarm by name.
        parse_function_activate_agent(json_data: str = None, *args, **kwargs): Parses JSON data and activates the selected agent.
        select_agent_and_send_task(name: str = None, task: str = None, *args, **kwargs): Selects an agent and sends a task to them.
        run(task: str = None, *args, **kwargs): Runs the hierarchical swarm.

    """

    def __init__(
        self,
        name: str = None,
        description: str = None,
        director: Agent = None,
        agents: List[Agent] = None,
        max_loops: int = 1,
        long_term_memory_system: BaseSwarm = None,
        custom_parse_function: callable = None,
        rules: str = None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
        self.director = director
        self.agents = agents
        self.max_loops = max_loops
        self.long_term_memory_system = long_term_memory_system
        self.custom_parse_function = custom_parse_function

        # Set the director to max_one loop
        if self.director.max_loops > 1:
            self.director.max_loops = 1

        # Set the long term memory system of every agent to long term memory system
        if long_term_memory_system is True:
            for agent in agents:
                agent.long_term_memory = long_term_memory_system

        # Initialize the swarm
        self.swarm_initialization()

        # Initialize the conversation message pool
        self.swarm_history = Conversation(
            time_enabled=True,
        )

    def swarm_initialization(self, *args, **kwargs):
        """
        Initializes the hierarchical swarm.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            None

        """
        logger.info(f"Initializing the hierarchical swarm: {self.name}")
        logger.info(f"Purpose of this swarm: {self.description}")

        # Now log number of agnets and their names
        logger.info(f"Number of agents: {len(self.agents)}")
        logger.info(
            f"Agent names: {[agent.name for agent in self.agents]}"
        )

        # Now see if agents is not empty
        if len(self.agents) == 0:
            logger.info("No agents found. Please add agents to the swarm.")
            return None

        # Now see if director is not empty
        if self.director is None:
            logger.info(
                "No director found. Please add a director to the swarm."
            )
            return None

        logger.info(
            f"Initialization complete for the hierarchical swarm: {self.name}"
        )

    def find_agent_by_name(self, agent_name: str = None, *args, **kwargs):
        """
        Finds an agent in the swarm by name.

        Args:
            agent_name (str): The name of the agent to find.

        Returns:
            Agent: The agent with the specified name, or None if not found.

        """
        for agent in self.agents:
            if agent.name == agent_name:
                return agent
        return None

    def parse_function_activate_agent(
        self, json_data: str = None, *args, **kwargs
    ):
        """
        Parse the JSON data and activate the selected agent.

        Args:
            json_data (str): The JSON data containing the agent name and task.

        Returns:
            str: The response from the activated agent.

        Raises:
            json.JSONDecodeError: If the JSON data is invalid.

        """
        try:
            data = json.loads(json_data)

            # Check if the data is a list of agent task pairs
            if isinstance(data, list):
                responses = []
                # Iterate over the list of agent task pairs
                for agent_task in data:
                    name = agent_task.get("name")
                    task = agent_task.get("task")

                    response = self.select_agent_and_send_task(
                        name, task, *args, **kwargs
                    )

                    responses.append(response)
                return responses
            else:
                name = data.get("name")
                task = data.get("task")

                response = self.select_agent_and_send_task(
                    name, task, *args, **kwargs
                )

                return response
        except json.JSONDecodeError:
            logger.error("Invalid JSON data, try again.")
            raise json.JSONDecodeError

    def select_agent_and_send_task(
        self, name: str = None, task: str = None, *args, **kwargs
    ):
        """
        Select an agent from the list and send a task to them.

        Args:
            name (str): The name of the agent to send the task to.
            task (str): The task to send to the agent.

        Returns:
            str: The response from the agent.

        Raises:
            KeyError: If the agent name is not found in the list of agents.

        """
        try:
            # Check to see if the agent name is in the list of agents
            if name in self.agents:
                agent = self.agents[name]
            else:
                return "Invalid agent name. Please select 'Account Management Agent' or 'Product Support Agent'."

            response = agent.run(task, *args, **kwargs)

            return response
        except Exception as e:
            logger.error(f"Error: {e}")
            raise e

    def run(self, task: str = None, *args, **kwargs):
        """
        Run the hierarchical swarm.

        Args:
            task (str): The task to send to the director agent.

        Returns:
            str: The response from the director agent.

        Raises:
            Exception: If an error occurs while running the swarm.

        """
        try:
            loop = 0

            # While the loop is less than max loops
            while loop < self.max_loops:
                # Run the director
                response = self.director.run(task, *args, **kwargs)

                # Log the director's response
                self.swarm_history.add(self.director.agent_name, response)

                # Run agents
                if self.custom_parse_function is not None:
                    response = self.custom_parse_function(response)
                else:
                    response = self.parse_function_activate_agent(response)

                loop += 1

                task = response

            return response
        except Exception as e:
            logger.error(f"Error: {e}")
            raise e
