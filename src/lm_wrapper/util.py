from src.lm_wrapper.gritlm import GritWrapper
from src.lm_wrapper.huggingface_util import HuggingFaceWrapper


def init_embedding_model(model_name):
    if 'GritLM/' in model_name:
        return GritWrapper(model_name)
    if model_name not in ['colbertv2', 'bm25']:
        return HuggingFaceWrapper(model_name)  # HuggingFace model for retrieval