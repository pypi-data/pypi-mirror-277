from typing import List
from swarmauri.core.distances.IDistanceSimilarity import IDistanceSimilarity
from swarmauri.core.vectors.IVector import IVector

class JaccardIndexDistance(IDistanceSimilarity):
    """
    A class implementing Jaccard Index as a similarity and distance metric between two vectors.
    """

    def distance(self, vector_a: IVector, vector_b: IVector) -> float:
        """
        Computes the Jaccard distance between two vectors.

        The Jaccard distance, which is 1 minus the Jaccard similarity,
        measures dissimilarity between sample sets. It's defined as
        1 - (the intersection of the sets divided by the union of the sets).

        Args:
            vector_a (IVector): The first vector.
            vector_b (IVector): The second vector.

        Returns:
            float: The Jaccard distance between vector_a and vector_b.
        """
        set_a = set(vector_a.data)
        set_b = set(vector_b.data)

        # Calculate the intersection and union of the two sets.
        intersection = len(set_a.intersection(set_b))
        union = len(set_a.union(set_b))

        # In the special case where the union is zero, return 1.0 which implies complete dissimilarity.
        if union == 0:
            return 1.0

        # Compute Jaccard similarity and then return the distance as 1 - similarity.
        jaccard_similarity = intersection / union
        return 1 - jaccard_similarity

    def similarity(self, vector_a: IVector, vector_b: IVector) -> float:
        """
        Computes the Jaccard similarity between two vectors.

        Args:
            vector_a (IVector): The first vector.
            vector_b (IVector): The second vector.

        Returns:
            float: Jaccard similarity score between vector_a and vector_b.
        """
        set_a = set(vector_a.data)
        set_b = set(vector_b.data)

        # Calculate the intersection and union of the two sets.
        intersection = len(set_a.intersection(set_b))
        union = len(set_a.union(set_b))

        # In case the union is zero, which means both vectors have no elements, return 1.0 implying identical sets.
        if union == 0:
            return 1.0

        # Compute and return Jaccard similarity.
        return intersection / union
    
    def distances(self, vector_a: IVector, vectors_b: List[IVector]) -> List[float]:
        distances = [self.distance(vector_a, vector_b) for vector_b in vectors_b]
        return distances
    
    def similarities(self, vector_a: IVector, vectors_b: List[IVector]) -> List[float]:
        similarities = [self.similarity(vector_a, vector_b) for vector_b in vectors_b]
        return similarities