from collections.abc import Iterator

from attrs import Factory, define, field

from griptape.artifacts import TextArtifact
from griptape.drivers import BasePromptDriver
from griptape.tokenizers import HuggingFaceTokenizer
from griptape.utils import PromptStack, import_optional_dependency


@define
class HuggingFacePipelinePromptDriver(BasePromptDriver):
    """
    Attributes:
        params: Custom model run parameters.
        model: Hugging Face Hub model name.
        tokenizer: Custom `HuggingFaceTokenizer`.

    """

    SUPPORTED_TASKS = ["text2text-generation", "text-generation"]
    DEFAULT_PARAMS = {"return_full_text": False, "num_return_sequences": 1}

    max_tokens: int = field(default=250, kw_only=True, metadata={"serializable": True})
    model: str = field(kw_only=True, metadata={"serializable": True})
    params: dict = field(factory=dict, kw_only=True, metadata={"serializable": True})
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
        pipeline = import_optional_dependency("transformers").pipeline

        generator = pipeline(
            tokenizer=self.tokenizer.tokenizer,
            model=self.model,
            max_new_tokens=self.tokenizer.count_output_tokens_left(prompt),
        )

        if generator.task in self.SUPPORTED_TASKS:
            extra_params = {"pad_token_id": self.tokenizer.tokenizer.eos_token_id}

            response = generator(prompt, **(self.DEFAULT_PARAMS | extra_params | self.params))

            if len(response) == 1:
                return TextArtifact(value=response[0]["generated_text"].strip())
            else:
                raise Exception("completion with more than one choice is not supported yet")
        else:
            raise Exception(f"only models with the following tasks are supported: {self.SUPPORTED_TASKS}")

    def try_stream(self, prompt_stack: PromptStack) -> Iterator[TextArtifact]:
        raise NotImplementedError("streaming is not supported")
