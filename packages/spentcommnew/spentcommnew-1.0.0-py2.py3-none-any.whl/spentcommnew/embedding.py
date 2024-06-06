from kph.src.common.llm_clients import emb_client
from kph.src.config.config import config


def get_embedding(
    text,
    model=config.azure_openai_clients.text_embedding.model,
    dimension=config.azure_openai_clients.text_embedding.dimension_docs,
    client=emb_client,
):
    # OpenAI "text-embedding-3-large" model's default dimension is 3072. Possible values are 256, 512, 1024, and 3072.
    text = text.replace("\n", " ")
    return (
        client.embeddings.create(input=[text], model=model, dimensions=dimension)
        .data[0]
        .embedding
    )
