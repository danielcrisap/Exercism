from typing import List


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    sorted_word = sorted(word.lower())
    candidate_anagrams = [
        candidate
        for candidate in candidates
        if sorted_word == sorted(candidate.lower())
    ]
    return [
        anagram for anagram in candidate_anagrams if word.lower() != anagram.lower()
    ]
