from typing import Optional, Any
from asyncflows.actions.base import (
    StreamingAction,
    DefaultModelInputs,
)
from asyncflows import Action, BaseModel
from asyncflows.actions.utils.prompt_context import TextElement
from asyncflows.models.config.model import OptionalModelConfig, ModelConfig
import json
import logging
import os
import tempfile
import base64
from typing import Optional, AsyncIterator
from asyncflows.models.config.value_declarations import (
    VarDeclaration,
    TextDeclaration,
    LambdaDeclaration,
    Declaration,
    LinkDeclaration,
    # ConstDeclaration,
)
import aiohttp
import tenacity
from asyncflows.utils.async_utils import (
    iterator_to_coro,
)
from asyncflows.actions.base import (
    StreamingAction,
    DefaultModelInputs,
    BaseModel,
    Field,
)

from asyncflows.actions.utils.prompt_context import (
    RoleElement,
    PromptElement,
    QuoteStyle,
    TextElement,
    PromptContextInConfigTemplate,
)
from asyncflows.models.config.model import OptionalModelConfig, ModelConfig

import litellm

from asyncflows.utils.async_utils import Timer, measure_async_iterator
from asyncflows.utils.secret_utils import get_secret
from asyncflows.utils.singleton_utils import SingletonContext

from asyncflows.actions.prompt import Prompt, Inputs as PromptInputs


async def render_templates(prompt_elements: list[PromptElement], context: dict[str, Any]) -> list[PromptElement]:
    new_list = []
    for element in prompt_elements:
        if isinstance(element, TextElement):
            element = TextElement(
                role=element.role,
                text=await TextDeclaration(text=element.text).render(context),
            )
        new_list.append(element)
    return new_list
