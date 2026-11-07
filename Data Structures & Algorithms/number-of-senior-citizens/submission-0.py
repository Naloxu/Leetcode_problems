class Solution:
    def countSeniors(self, details: List[str]) -> int:
        number_of_senior = 0
        for detail in details:
            if int(detail[11] + detail[12]) > 60:
                number_of_senior += 1
        return number_of_senior