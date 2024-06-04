import typing as t
import tiktoken
from airouter.models import LLM, map_context_size

def get_tokenizer(model):
  try:
    encoding = tiktoken.encoding_for_model(model)
  except KeyError:
    print("Warning: model not found. Using cl100k_base encoding.")
    encoding = tiktoken.get_encoding("cl100k_base")

  return encoding

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
  """Return the number of tokens used by a list of messages."""

  encoding = get_tokenizer(model)

  if model in {
    "gpt-3.5-turbo-0613",
    "gpt-3.5-turbo-16k-0613",
    "gpt-4-0314",
    "gpt-4-32k-0314",
    "gpt-4-0613",
    "gpt-4-32k-0613",
  }:
    tokens_per_message = 3
    tokens_per_name = 1
  elif model == "gpt-3.5-turbo-0301":
    tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
    tokens_per_name = -1  # if there's a name, the role is omitted
  elif "gpt-3.5-turbo" in model:
    print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
    return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
  elif "gpt-4" in model:
    print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
    return num_tokens_from_messages(messages, model="gpt-4-0613")
  else:
    print(f"Warning: unknown `num_tokens_from_messages` for model {model}. Falling back to default gpt-4 configuration")
    return num_tokens_from_messages(messages, model="gpt-4-0613")
  num_tokens = 0
  for message in messages:
    num_tokens += tokens_per_message
    for key, value in message.items():
      num_tokens += len(encoding.encode(value))
      if key == "name":
        num_tokens += tokens_per_name
  num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
  return num_tokens

def model_can_generate_max_tokens(
    model: t.Union[str, LLM],
    messages,
    max_tokens,
) -> bool:
  if isinstance(model, str):
    model = LLM.from_str(model)

  num_tokens = num_tokens_from_messages(messages=messages, model=model.value)

  # current tokens + max tokens
  total_tokens = num_tokens + max_tokens
  model_context_size = map_context_size[model]

  return total_tokens < model_context_size
