class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        answers = {}

        def navigate(index):
            if index >= len(questions):
                answers[index] = 0
            if index in answers:
                return

            points, skipped = questions[index]
            
            navigate(index+1)
            navigate(index+skipped+1)

            best = max(
                answers[index+1],
                points+answers[index+skipped+1]
            )

            answers[index] = best
        
        navigate(0)
        return answers[0]
