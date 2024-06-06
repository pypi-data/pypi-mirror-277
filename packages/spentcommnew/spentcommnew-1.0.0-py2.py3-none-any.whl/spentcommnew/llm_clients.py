import os
from openai import AzureOpenAI
from groq import Groq
import openai

from kph.src.config.config import config

# Initialize the AzureOpenAI client
openai_client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # config.openai_client.api_key,
)

azure_openai_client_gpt4 = AzureOpenAI(
    api_version=config.azure_openai_clients.gpt4.api_version,
    azure_endpoint=config.azure_openai_clients.gpt4.azure_endpoint,
    api_key=config.azure_openai_clients.gpt4.api_key,
    azure_deployment=config.azure_openai_clients.gpt4.azure_deployment,
)

azure_openai_client_gpt35_16k = AzureOpenAI(
    api_version=config.azure_openai_clients.gpt35_16k.api_version,
    azure_endpoint=config.azure_openai_clients.gpt35_16k.azure_endpoint,
    api_key=config.azure_openai_clients.gpt35_16k.api_key,
    azure_deployment=config.azure_openai_clients.gpt35_16k.azure_deployment,
)

anyscale_client = openai.OpenAI(
    base_url=os.getenv("ANYSCALE_API_BASE"),  # config.anyscale_client.base_url,
    api_key=os.getenv("ANYSCALE_API_KEY"),  # config.anyscale_client.api_key,
)

groc_client = Groq(
    api_key=config.groq_client.api_key,
)

emb_client = AzureOpenAI(
    api_version=config.azure_openai_clients.text_embedding.api_version,
    azure_endpoint=config.azure_openai_clients.text_embedding.azure_endpoint,
    api_key=config.azure_openai_clients.text_embedding.api_key,
    azure_deployment=config.azure_openai_clients.text_embedding.azure_deployment,
)
