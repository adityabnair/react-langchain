# ReAct - A simple implementation

Based on the paper https://react-lm.github.io/ this project aims to demonstrate the ReAct prompt. It helps bring together the question from the human, the thought process of the agent to determine which tool to 
use, the action taken by the agent and the final result. The langchain library was used along with the ReAct prompt. The tool defined was to count the number of characters in the text provided to the agent 
as part of a prompt. The reasoning was illustrated using the agent scratchpad to record intermediate steps. 

## Screenshots

![ReAct Methodology](https://github.com/adityabnair/react-langchain/assets/64246274/42f346c8-6400-4a72-8c2c-9600190d0610)


## Main Prerequisites

1. At least Python 3.10
2. Access to OpenAI's API credits for usage of gpt-3.5 

### Running

1. Use pipenv to install python libraries from requirements.txt (a virtual environemnt is always recommended)
2. Add environment variable in a .env file to hold the OpenAI API key
3. Run main.py
4. Observe results and can re-reun using a different input text


## Acknowledgments

Thanks to @emarco177 for the langchain development course
