class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return biggest_h_index(citations)


def biggest_h_index(citations):
    max_h= -float("inf")
    for h_index in range(len(citations)+1):
        if is_valid(h_index, citations):
            max_h = max(max_h, h_index)
    return max_h




def is_valid(h_index, citations):
    num_ge_citations = h_index
    num_le_citations = len(citations) - h_index

    middle_index = num_le_citations

    #citations including and beyond middle paper
    #should have >= h_index citations
    ge_is_valid = True
    if num_ge_citations:
        if not citations[middle_index] >= h_index:
            ge_is_valid = False
    
    #citations before middle paper
    #should have <= h_index citations
    le_is_valid = True
    if num_le_citations:
        if not citations[middle_index-1] <= h_index:
            le_is_valid = False
    
    return le_is_valid and ge_is_valid


