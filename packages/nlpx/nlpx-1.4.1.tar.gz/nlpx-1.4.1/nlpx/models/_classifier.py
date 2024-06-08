import torch
from torch import nn
from ._text_cnn import TextCNN
from ._attention import RNNAttention


class EmbeddingClassifier(nn.Module):
	"""
	Examples
	--------
	>>> from nlpx.text_token import TokenEmbedding
	>>> from nlpx.models import TextCNN, RNNAttention, EmbeddingClassifier
	>>> tokenizer = TokenEmbedding(pretrained_path)
	>>> attn = RNNAttention(tokenizer.embed_dim, num_heads=2, out_features=len(classes))
	>>> classifier = EmbeddingClassifier(atten, embedding=tokenizer.embedding)
	>>> classifier = EmbeddingClassifier(atten, num_embeddings=tokenizer.vocab_size, embed_dim=tokenizer.embed_dim)
	"""

	def __init__(self, classifier, embedding=None, num_embeddings: int = None, embed_dim: int = None):
		super().__init__()
		self.classifier = classifier
		if embedding is None:
			self.embedding = nn.Embedding(num_embeddings, embed_dim)
		elif isinstance(embedding, nn.Embedding):
			self.embedding = embedding
		elif isinstance(embedding, torch.Tensor):
			self.embedding = nn.Embedding.from_pretrained(embedding)
		else:
			self.embedding = nn.Embedding.from_pretrained(torch.tensor(embedding, dtype=torch.float))

	def forward(self, input_ids, labels=None):
		embedding = self.embedding(input_ids)
		return self.classifier(embedding, labels)


class TextCNNClassifier(EmbeddingClassifier):
	"""
	Examples
	--------
	>>> from nlpx.text_token import Tokenizer
	>>> from nlpx.models import TextCNNClassifier
	>>> tokenizer = Tokenizer(corpus)
	>>> classifier = TextCNNClassifier(embed_dim, len(classes), num_embeddings=tokenizer.vocab_size)
	"""

	def __init__(self, embed_dim: int, num_classes: int, embedding=None, num_embeddings: int = None,
				 kernel_sizes=(2, 3, 4), cnn_channels: int = 64, activation=nn.ReLU(inplace=True),
				 num_hidden_layer: int = 0, batch_norm=False, layer_norm=False, drop_out: float = 0.0):
		classifier = TextCNN(embed_dim, kernel_sizes, cnn_channels, num_classes, activation, num_hidden_layer, batch_norm,
						   layer_norm, drop_out)
		super().__init__(classifier, embedding, num_embeddings, embed_dim)


class RNNAttentionClassifier(EmbeddingClassifier):
	"""
	Examples
	--------
	>>> from nlpx.text_token import Tokenizer
	>>> from nlpx.models import RNNAttentionClassifier
	>>> tokenizer = Tokenizer(corpus)
	>>> classifier = RNNAttentionClassifier(embed_dim, len(classes), num_embeddings=tokenizer.vocab_size)
	"""

	def __init__(self, embed_dim: int, num_classes: int, embedding=None, num_embeddings: int = None,
				 hidden_size: int = 64, num_layers: int = 1, num_heads: int = 1, rnn=nn.GRU, drop_out: float = 0.0):
		classifier = RNNAttention(embed_dim, hidden_size, num_layers, num_heads, num_classes, rnn, drop_out)
		super().__init__(classifier, embedding, num_embeddings, embed_dim)
