import torch
import numpy as np
import pandas as pd
from typing import Union, List
from torch.utils.data import Dataset

from nlpx.llm import TokenizeVec
from nlpx.text_token import BaseTokenizer, TokenEmbedding, get_texts_max_length


class TextDataset(Dataset):

	def __init__(self, texts: Union[List[str], np.ndarray, pd.Series], labels: Union[List, np.ndarray, pd.Series]):
		super().__init__()
		self.texts = texts.values if isinstance(texts, pd.Series) else texts
		self.labels = labels.values if isinstance(labels, pd.Series) else labels

	def __getitem__(self, index: int):
		return self.texts[index], self.labels[index]

	def __len__(self):
		return len(self.labels)


class TextDFDataset(Dataset):

	def __init__(self, data_df: pd.DataFrame):
		super().__init__()
		self.data = data_df.values

	def __getitem__(self, index: int):
		return self.data[index]

	def __len__(self):
		return len(self.data)


class TextVecCollator:

	def __init__(self, tokenize_vec: Union[TokenizeVec, TokenEmbedding], max_length: int = None):
		self.tokenize_vec = tokenize_vec
		self.max_length = max_length

	def __call__(self, examples):
		texts, labels = zip(*examples)
		labels = torch.tensor(labels, dtype=torch.long)

		if isinstance(self.tokenize_vec, TokenizeVec):
			return self.tokenize_vec.encode_plus(texts, max_length=self.max_length, padding='max_length',
												truncation=True, add_special_tokens=True,
												return_token_type_ids=True,return_attention_mask=True,
												return_tensors='pt'), labels
		elif isinstance(self.tokenize_vec, TokenEmbedding):
			return self.tokenize_vec(texts, self.max_length), labels

		raise ValueError("Invalid tokenize_vec, it must be a TokenizeVec or TokenEmbedding.")


class TokenizeCollator:

	def __init__(self, tokenizer, max_length: int = None):
		self.tokenizer = tokenizer
		self.max_length = max_length

	def __call__(self, examples):
		texts, labels = zip(*examples)
		labels = torch.tensor(labels, dtype=torch.long)

		if isinstance(self.tokenizer, BaseTokenizer):
			return torch.tensor(self.tokenizer.batch_encode(texts, self.max_length), dtype=torch.long), labels

		max_length = self.max_length or get_texts_max_length(texts, cut_type='char') + 2
		result = self.tokenizer.batch_encode_plus(texts, max_length=max_length, padding='max_length',
												  return_token_type_ids=True, return_attention_mask=True,
											  	  truncation=True, add_special_tokens=True, return_tensors='pt')
		result['labels'] = labels
		return result
