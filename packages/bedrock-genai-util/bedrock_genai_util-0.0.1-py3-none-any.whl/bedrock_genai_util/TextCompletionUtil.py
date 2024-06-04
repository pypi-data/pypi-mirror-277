import logging
from bedrock_util.bedrock_genai_util.MetaBedrockUtil import MetaBedrockUtil
from bedrock_util.bedrock_genai_util.MistralBedrockUtil import MistralBedrockUtil
from bedrock_util.bedrock_genai_util.AwsTitanBedrockUtil import AwsTitanBedrockUtil
from bedrock_util.bedrock_genai_util.AnthropicBedrockUtil import AnthropicBedrockUtil
from bedrock_util.bedrock_genai_util.CohereBedrockUtil import CohereBedrockUtil
from bedrock_util.bedrock_genai_util.model_map import model_map


logger = logging.getLogger(__name__)


def generate_text_completion(bedrock_client, model: str, prompt, guardrail_identifier=None, guardrail_version=None,
                             **model_kwargs):
    if model is None or model_map.get(model) is None:
        logger.warning(f"Invalid model: {model}")
        return None

    fm_provider = model_map[model]
    fm_utils = {
        "Amazon": AwsTitanBedrockUtil,
        "Anthropic": AnthropicBedrockUtil,
        "Cohere": CohereBedrockUtil,
        "Meta": MetaBedrockUtil,
        "Mistral AI": MistralBedrockUtil
    }

    try:
        fm = fm_utils[fm_provider]()
        result = fm.text_completion(bedrock_client=bedrock_client, model=model, prompt=prompt,
                                    guardrail_identifier=guardrail_identifier,
                                    guardrail_version=guardrail_version, **model_kwargs)
        logger.info(f"Text completion generated for model: {model}")
        return result
    except KeyError:
        logger.error(f"Unsupported provider: {fm_provider}")
    except Exception as e:
        logger.exception(f"Error generating text completion for model: {model}")

    return None
