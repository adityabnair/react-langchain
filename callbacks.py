# logging the logic for all the LLM calls
from typing import Any, Dict, List
from langchain.schema import LLMResult
from langchain.callbacks.base import BaseCallbackHandler


class AgentCallbackHandler(BaseCallbackHandler):

    # llm_start and llm_end methods taken from BaseCallbackHandler https://python.langchain.com/docs/modules/callbacks/
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        """Run when LLM starts running."""
        print(f"***Prompt to LLM was:***\n{prompts[0]}")
        print("****")

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        """Run when LLM ends running."""
        print(f"***LLM Response:***\n{response.generations[0][0].text}")
        print("****")
