# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
This module defines the Flow and Task classes which are used to load and execute a series of tasks defined in a JSON file.
Each task is processed by the LLM (Large Language Model) and the results are saved in a JSON file.
"""

import json
import os
import re
from datetime import datetime

from loguru import logger

from actionflow.llm import LLM, Settings
from actionflow.output import Output
from actionflow.tool import Tool


class Task:
    """
    Represents a task to be processed by the LLM.

    :param action: The action to be performed by the task.
    :type action: str
    :param settings: Settings for the task. Defaults to an empty Settings object.
    :type settings: Settings, optional
    """

    def __init__(self, action: str, settings: Settings = None):
        self.action = action
        self.settings = settings if settings else Settings()


class Flow:
    """
    Represents a flow of tasks loaded from a JSON file.

    :param flow_path: str, The file path of the flow.
    :param variables: dict, optional, Variables to be used in the flow. Defaults to an empty dictionary.
    """

    def __init__(self, flow_path: str, variables: dict = None, output_dir: str = None):
        self.flow_path = flow_path
        self._load_flow(flow_path)
        self._validate_and_format_messages(variables or {})
        flow_name = os.path.basename(flow_path).split(".")[0]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        default_output_dir = os.path.join("outputs", f"{flow_name}_{timestamp}")
        self.output_dir = output_dir if output_dir else default_output_dir
        self.output = Output(self.output_dir)
        self.messages = self._get_initial_messages()
        self.messages_file_name = "messages.json"
        self.llm = LLM()
        self.tools = self._get_tools()
        logger.debug(
            f"Flow loaded: {flow_path}, "
            f"output: {self.output}, "
            f"variables: {variables}, "
            f"tasks size: {len(self.tasks)}, "
            f"messages: {self.messages}, "
            f"tools: {self.tools}, "
            f"llm: {self.llm}"
        )

    def _load_flow(self, file_path: str) -> None:
        """
        Load flow from a JSON file.

        :param file_path: The name of the flow.
        :type file_path: str
        :raises FileNotFoundError: If the JSON file does not exist.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}.")

        with open(file_path, "r") as file:
            data = json.load(file)

        self.system_message = data.get("system_message")
        self.tasks = [
            Task(task["action"], Settings(**task.get("settings", {})))
            for task in data.get("tasks", [])
        ]

    def _validate_and_format_messages(self, variables: dict) -> None:
        """
        Validate and format messages with provided variables.

        :param variables: Variables to be used in the flow.
        :type variables: dict
        :raises ValueError: If there are extra or missing variables.
        """
        all_messages = [self.system_message] + [task.action for task in self.tasks]
        all_variables = set(
            match.group(1)
            for message in all_messages
            if message
            for match in re.finditer(
                r"{([^{}]+)}", message.replace("{{", "").replace("}}", "")
            )
        )

        extra_variables = set(variables.keys()) - all_variables
        if extra_variables:
            raise ValueError(f"Extra variables provided: {extra_variables}.")

        missing_variables = all_variables - set(variables.keys())
        if missing_variables:
            raise ValueError(f"Missing variable values for: {missing_variables}.")

        self._format_messages(variables)

    def _format_messages(self, variables: dict) -> None:
        """
        Format messages with provided variables.

        :param variables: Variables to be used in the flow.
        :type variables: dict
        """
        if self.system_message:
            self.system_message = self._format_message(self.system_message, variables)
        for task in self.tasks:
            if task.action:
                task.action = self._format_message(task.action, variables)

    @staticmethod
    def _format_message(message: str, variables: dict) -> str:
        """
        Format a single message with provided variables.

        :param message: The message to be formatted.
        :type message: str
        :param variables: Variables to be used in the flow.
        :type variables: dict
        :return: The formatted message.
        :rtype: str
        """
        return message.format(**variables).replace("{{", "{").replace("}}", "}")

    def run(self):
        """
        Run the flow.

        The flow is processed by the LLM and the results are saved in a JSON file.
        """

        logger.debug(f"Running flow: {self.flow_path}")

        for task in self.tasks:
            pre_task_messages_length = len(self.messages)
            try:
                self._process_task(task)
                logger.debug(self.messages[pre_task_messages_length:])
                self.output.save(self.messages_file_name, self.messages)
            except Exception as e:
                logger.error(e)
                return

        self.output.save(self.messages_file_name, self.messages)
        logger.debug(f"Output folder: {self.output.output_dir}")

    def _get_initial_messages(self) -> list:
        """
        Get initial system and user messages.

        :return: A list of initial messages.
        :rtype: list
        """
        messages = []
        if self.system_message:
            messages.append({"role": "system", "content": self.system_message})
        return messages

    def _get_tools(self) -> list:
        """
        Get tool definitions for tasks.
        """
        return [
            Tool(task.settings.tool_name, self.output).definition
            for task in self.tasks
            if task.settings.tool_name is not None
        ]

    def _process_task(self, task: Task):
        """
        Process a single task.

        :param task: The task to be processed.
        :type task: Task
        """
        self.messages.append({"role": "user", "content": task.action})

        task.settings.tool_choice = (
            "none"
            if task.settings.tool_name is None
            else {"type": "function", "function": {"name": task.settings.tool_name}}
        )

        message = self.llm.respond(task.settings, self.messages, self.tools)
        if message.content:
            self._process_message(message)
        elif message.tool_calls:
            self._process_tool_call(message, task)

    def _process_message(self, message) -> None:
        """
        Process a message from the assistant.

        :param message: The message from the assistant.
        :type message: Message
        """
        self.messages.append({"role": "assistant", "content": message.content})

    def _process_tool_call(self, message, task: Task) -> None:
        """
        Process a tool call from the assistant.

        :param message: The message from the assistant.
        :type message: Message
        :param task: The task to be processed.
        :type task: Task
        """
        tool_name = message.tool_calls[0].function.name
        arguments = message.tool_calls[0].function.arguments
        tool = Tool(tool_name, self.output)
        tool_content = tool.execute(arguments)
        self.messages.append(
            {
                "role": "assistant",
                "content": tool_content,
                "tool_name": tool_name,
            }
        )
