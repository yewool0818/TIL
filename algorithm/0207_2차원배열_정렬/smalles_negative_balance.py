class Solution:
    def solution(n, debts):
        amount_dict = {}
        for debt in debts:
            borrower, lender, amount = debt.split()[0], debt.split()[1], debt.split()[2]
            amount_dict[borrower] =  amount_dict.get(borrower, 0) + amount
            amount_dict[lender] =  amount_dict.get(lender, 0)  - amount


        return amount_dict



debts = ['Alex Blake 2', 'Blake Ales 2', 'Casey Alex 5', 
'Blake Casey 7', 'Alex Blake 4', 'Alex Casey 7']

print(Solution.solution(6, debts))
