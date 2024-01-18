def perplexity_evaluation(original_message: str, corrected_message: str) -> float:
    """
    This function is meant to calculate the perplexity value between the two strings.
    A higher perplexity value means that the quality of the correction or the input message is very poor.
    A lower perplexity value means that not many corrections where made so it could mean that the original message wasn't so poorly written.
    """
    pass


def cos_distance(original_message: str, corrected_message: str) -> float:
    """
    This function is meant to calculate the cos distance between the two strings.
    cos distance ranges from -1 to 1.
        - 1:  the two vectors are diametrically opposed which means complete dissimilarity.
        - 0: enotes orthogonality or no similarity between the two vectors.
        - 1: the two vectors are identical in orientation, indicating maximum similarity.
    """
    pass