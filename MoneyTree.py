def compound_interest(premium,input_years,interest):
    future_val  =   premium * (1 + interest)**input_years
    return future_val



if __name__ == '__main__':
    
    premium =   30000 * 1.15
    invested_amt    =   []
    input_years =   10
    return_amount   =   28800 * 15
    output_years    =   15
    interest    =   0.08 
    for i in range(1, input_years + 1):
        future_val  =   compound_interest(premium,i,interest)
        invested_amt.append(future_val)
#         print future_val
    total_invested_amt  =   sum(invested_amt)
    idle_amount =   compound_interest(total_invested_amt, 4, interest)
#     print idle_amount
    print 'Invested Amount in 10 years with %.2f interest is %d ' %(interest, total_invested_amt)
    print 'Invested Amount in 14 years with %.2f interest is %d ' %(interest, idle_amount)
    print 'Amount I will get in return in 15 years is %d ' %return_amount
    print 'Amount deficient is %d' %(idle_amount - return_amount)