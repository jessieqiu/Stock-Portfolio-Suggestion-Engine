
# coding: utf-8

# In[107]:


class InvestmentPortfolio:
    def __init__(self, tickers, shares):
        self.tickers = tickers
        self.number_of_shares = shares


# In[126]:


def printResults(s):
    if s is not None:
        print("Stocks suggested for you: ", s.tickers)
        print("Corresponding shares for each stock: ", s.number_of_shares)
    else:
        print("Please try again.")


# In[ ]:


#extra feature: mode = aggressive, balanced, conventional


# In[149]:


def getStocks(investment_amount=5000.00, strategy1='Ethical', strategy2=None, mode='balanced'):
    
    #input validation
    
    #Minimum is $5000 USD
    if(investment_amount<5000.00):
        error = "Error: Minimum investment amount is $5000 USD. You entered: $"+str(investment_amount)+" USD."
        print(error)
        return
    #Strategies need to be 'Ethical', 'Growth', 'Index', 'Quality' or 'Value'
    strategies = ['Ethical', 'Growth', 'Index', 'Quality', 'Value' ]
    lower_case_strategies = [s.lower() for s in strategies]
    strategy_list = []
    if strategy1 is not None:
        lower_case_strategy1 = strategy1.lower()
        strategy_list.append(lower_case_strategy1)
    if strategy2 is not None:
        lower_case_strategy2 = strategy2.lower()
        strategy_list.append(lower_case_strategy2)
    error1 = "Error: Strategy must be one of the following: "+ str(strategies) 
    error2 = "You entered: "
    flag = False
    if strategy1 is not None and lower_case_strategy1 not in lower_case_strategies:
        error2 += '\''+ strategy1 + '\''
        flag = True
    if strategy2 is not None and lower_case_strategy2 not in lower_case_strategies:
        if flag:
            error2 += ' and '
        error2 += '\''+strategy2 + '\''
        flag = True
    if flag:
        print(error1)
        print(error2)
        return
        
        
    tickers=[]
    shares=[]
    
    
    for strategy in strategy_list:
        switch (strategy) {
            

        }
    
    
    tickers = ['ANY', 'FIVE', 'TICK', 'SYM', 'BOLS']
    shares = [10, 20, 30, 40, 50]
    #Insert code here to update the 'tickers' and 'ratios' variables
    return(InvestmentPortfolio(tickers, shares))


# In[143]:


s = getStocks(50, 'ethic', "ethical")
printResults(s)


# In[144]:


s = getStocks(80000, 'hahaha', "ethical")
printResults(s)


# In[145]:


s = getStocks(80000, 'ethical', "hohoho")
printResults(s)


# In[146]:


s = getStocks(80000, 'hahaha', "hohoho")
printResults(s)


# In[148]:


s = getStocks(80000, 'ethical')
printResults(s)


# In[ ]:





# In[ ]:




