from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING

from attrs import Factory, define, field

from griptape.artifacts import TextArtifact
from griptape.drivers import BasePromptDriver
from griptape.tokenizers import HuggingFaceTokenizer
from griptape.utils import PromptStack, import_optional_dependency

if TYPE_CHECKING:
    from huggingface_hub import InferenceClient


@define
class HuggingFaceHubPromptDriver(BasePromptDriver):
    """
    Attributes:
        api_token: Hugging Face Hub API token.
        use_gpu: Use GPU during model run.
        params: Custom model run parameters.
        model: Hugging Face Hub model name.
        client: Custom `InferenceApi`.
        tokenizer: Custom `HuggingFaceTokenizer`.

    """

    api_token: str = field(kw_only=True, metadata={"serializable": True})
    max_tokens: int = field(default=250, kw_only=True, metadata={"serializable": True})
    params: dict = field(factory=dict, kw_only=True, metadata={"serializable": True})
    model: str = field(kw_only=True, metadata={"serializable": True})
    client: InferenceClient = field(
        default=Factory(
            lambda self: import_optional_dependency("huggingface_hub").InferenceClient(
                model=self.model, token=self.api_token
            ),
            takes_self=True,
        ),
        kw_only=True,
    )
    tokenizer: HuggingFaceTokenizer = field(
        default=Factory(
            lambda self: HuggingFaceTokenizer(
                tokenizer=import_optional_dependency("transformers").AutoTokenizer.from_pretrained(self.model),
                max_output_tokens=self.max_tokens,
            ),
            takes_self=True,
        ),
        kw_only=True,
    )

    def try_run(self, prompt_stack: PromptStack) -> TextArtifact:
        prompt = self.prompt_stack_to_string(prompt_stack)

        response = self.client.text_generation(
            prompt, return_full_text=False, max_new_tokens=self.max_output_tokens(prompt), **self.params
        )

        return TextArtifact(value=response)

    def try_stream(self, prompt_stack: PromptStack) -> Iterator[TextArtifact]:
        prompt = self.prompt_stack_to_string(prompt_stack)

        response = self.client.text_generation(
            prompt, return_full_text=False, max_new_tokens=self.max_output_tokens(prompt), stream=True, **self.params
        )

        for token in response:
            yield TextArtifact(value=token)
