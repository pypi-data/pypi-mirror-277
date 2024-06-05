"""
    A collection of models related to embeddings.
"""

import numpy as np
from typing import List
from ..utils.log import logger

class SkipGram:
    """
        Default skipgram model as it was in word2vec.
    """

    def __init__(self, vocab_size: int, dim: int, mean: np.float32 = 0, std: np.float32 = 1):
        self.vocab_size = vocab_size
        self.dim = dim
        self.core = np.random.normal(mean, std, (2*vocab_size, dim,))
        # The bottom half of the matrix is "context" vectors

    def __getitem__(self, item: int):
        return self.core[item]

    def step_positive(self, input: int, context: int, lr: np.float32):
        """
            Takes a positive step, which means, gets the input vector
            closer to the given context vectors.

            Args:
                input (int): An integer representing a token-id.

                context (int): An integer representing the token-id
                    of a context word.

                lr (np.float32): Learning rate. No default values given.
        """
        new_input = self.core[input] + lr * self.core[self.vocab_size + context]
        new_context = self.core[self.vocab_size + context] + lr * self.core[input]
        self.core[input] = new_input
        self.core[self.vocab_size + context] = new_context

    def step_negative(self, input: int, negative: int, lr: np.float32):
        """
            Takes a negative step, which means, gets the input vector
                further from the given negative vectors.

            Args:
                input (int): An integer representing a token-id.

                negative (int): An integer representing the token-id
                    of a negative word.

                lr (np.float32): Learning rate. No default values given.
        """
        new_input = self.core[input] - lr * self.core[self.vocab_size + negative]
        new_negative = self.core[self.vocab_size - negative] + lr * self.core[input]
        self.core[input] = new_input
        self.core[self.vocab_size + negative] = new_negative

    def loss(self, inputs: List[int], contexts: List[List[int]], negatives: List[List[int]]) -> np.float32:
        """
            Calculate the loss of an embedding system with the
            dot product similarity.

            Args:
                inputs: A list of integers containing token-ids of
                    all relevant tokens.

                contexts: A list-matrix of integers containing all
                    relevant context token-ids.

                negatives: A list-matrix of integers containing all
                    relevant negative token-ids.

            Returns:
                The calculated total error of the model, of type
                numpy.float32.
        """
        e: np.float32 = 0
        for i, input in enumerate(inputs):
            for context in contexts[i]:
                e -= np.dot(self.core[input], self.core[self.vocab_size + context])
            for negative in negatives[i]:
                e += np.dot(self.core[input], self.core[self.vocab_size + negative])
        return e / (np.size(contexts, axis=0) + np.size(negatives, axis=0))

    def fit(self, inputs: List[int], contexts: List[List[int]], negatives: List[List[int]],
            epochs: int = 1, lr: np.float32 = 0.001, lr_decay: np.float32 = 1):
        """
            Train the SkipGram model on given tokens, context tokens and negative
            tokens.

            Args:
                inputs: A list of integers containing token-ids of
                    all relevant tokens.

                contexts: A list-matrix of integers containing all
                    relevant context token-ids.

                negatives: A list-matrix of integers containing all
                    relevant negative token-ids.

                epochs (int): Integer representing the total count of
                    epochs to train the model during.

                lr (np.float32): Learning rate of the training. Default
                    value is 0.001.

                lr_decay (mp.float32): Decay of the learning rate to
                    perform after each epoch. By default, the value is
                    1. Meaning, there is no decay.
        """
        for epoch in range(epochs):
            for i, input in enumerate(inputs):
                for context in contexts[i]:
                    self.step_positive(input, context, lr)
                for negative in negatives[i]:
                    self.step_negative(input, negative, lr)
            logger.info(f"Loss at epoch {epoch + 1}: {self.loss(inputs, contexts, negatives)}")
            lr *= lr_decay

    def save(self, path: str):
        """
            Save the core embedding vector-matrix of the model.
            The saved file will be a numpy array file.

            Args:
                path (str): Path of the embedding file. Extension
                    needs to be included. The file will naturally
                    be a .npy file.
        """
        np.save(path, self.core)

    @staticmethod
    def load(path: str):
        """
            Load a SkipGram model from an .npy or compatible file.

            Args:
                path (str): Path to the ndarray file.

            Returns:
                Returns the SkipGram object created from the embedding
                vectors.
        """
        core = np.load(path)
        vocab_size = core.shape[0] // 2
        dim = core.shape[1]
        model = SkipGram(vocab_size, dim)
        model.core = core
        return model





