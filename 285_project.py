
# coding: utf-8

# In[79]:


import requests
import datetime


# In[80]:


class InvestmentPortfolio:
    def __init__(self, tickers, shares):
        self.tickers = tickers
        self.number_of_shares = shares


# In[81]:


def printResults(s):
    if s is not None:
        print("Stocks suggested for you: ", s.tickers)
        print("Corresponding shares for each stock: ", s.number_of_shares)
    else:
        print("Please try again.")


# In[82]:


def get_current_price(date, stock_symbol):
    req = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stock_symbol + '&apikey=Z552XY642X21K4LB')
    close = 1000
    if req is not None:
        #print(req.json())
        count = 0
        #print('tests', 'Note' in req.json())
        while 'Note' in req.json() and count<10000:
            count+=1
            if(count%100==0):
                req = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stock_symbol + '&apikey=Z552XY642X21K4LB')    
        if('Note' not in req.json()):
            close =  req.json()['Time Series (Daily)'][date]['4. close'] 
        print('count', count)
        if count>=10000:
            print("API access error, please try again later")
    else:
        print("API access error, please try again later")
        
    return close


# In[83]:


def get_monthly_low_high(date, stock_symbol):
#    print(datetime.datetime.now())
    req = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + stock_symbol + '&apikey=Z552XY642X21K4LB')
#     r.status_code
#     r.text
    #print(date)
    low=0
    high=0
    if req is not None:
        count = 0
        #print('tests', 'Note' in req.json())
        while 'Note' in req.json() and count<5000:
            count+=1
            if(count%100==0):
                req = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + stock_symbol + '&apikey=Z552XY642X21K4LB')
        if('Note' not in req.json()):
            low = req.json()['Monthly Time Series'][date]['3. low']
            high = req.json()['Monthly Time Series'][date]['2. high']
        #print('count', count) 
        if count>=5000:
            print("API access error, please try again later")
    else:
        print("API access error, please try again later")
    #print(low, high)

    return low, high


# In[84]:


def distribute(money, stocks_list):
    date = '2018-12-14'
    #stock_name = 'MSFT'
    percent = []
    for stock_name in stocks_list:
        print(stock_name)
        low = 100
        high = 200
        low_s, high_s = get_monthly_low_high(date, stock_name)
        low = float(low_s)
        high = float(high_s)
        current = float(get_current_price(date,stock_name))
        print('l,h', low, high)
        print('c', current)
        if current<low and low!=0:
            percent.append([(low-current)/low+1.00,stock_name, current])
        elif current > high:
            print('price too high')
            percent.append([0.01, stock_name, current])
        else:
            print('l,h,c', low, high, current)
            range_ = high-low
            if range_== 0:
                range_ = 1
            loc = (current-low)/range_
            percent.append([-1* loc +1.00, stock_name, current]) 
    print('before', percent)

    #percent.sort( reverse=True)
    percent.sort()
    
    print('after',percent)
    
    sum_= 0.00
    for p in percent:
        print('p',p[0])
        sum_+= p[0]
    print('sum', sum_)
    if sum_ <=0:
        sum_ = 1
    for p in percent:
        p[0]= p[0]/sum_
    print('new p', percent)
       
    for p in percent:
        
        print('money, price',money, p[2])
        share = int(money*p[0]/p[2])
        print('money, price, share',money, p[2], share)

        
        #money = money - share*p[2]
        p.append(share)
    
    print ('final', percent)
    
    val =0
    for p in percent:
        val+=p[2]*p[3]
    print('val', val)
    return percent


# In[85]:


# Due to the limitation of 5 API calls per minute from the free API we use, if you put two strategies, 
# there will be 6 stocks (greater than 5 API calls per minute) 
# therefore you need to wait a little while for the program to finish
#distribute(50000, ['AAPL','GOOG'])
#distribute(50000, ['MSFT','TWLO','GOOG','A','FB','AMZN'])


# In[ ]:





# In[86]:


def get_recommendations(strategy):
    dic=[]
    
    if strategy == 'ethical':  
        print(1)
        dic.append('AAPL')
        dic.append('ADBE')
        dic.append('VOO')
    elif strategy == 'growth':  
        print(2)  
        dic.append('JPM')
        dic.append('BAC')
        dic.append('WFC')
    elif strategy == 'index':
        print(3)
        dic.append('GRPN')
        dic.append('WMT')
        dic.append('AMD')
    elif strategy == 'quality':
        print(4)
        dic.append('GOOGL')
        dic.append('AMZN')
        dic.append('MSFT')

    elif strategy == 'value':
        print(5)
        dic.append('TWLO')
        dic.append('NVDA')
        dic.append('MDB')
    
    return dic    


# In[ ]:





# In[87]:


def input_validation(lower_case_strategies, investment_amount, strategy1, strategy2=None):
    #input validation
    
    #Minimum is $5000 USD
    if(investment_amount<5000.00):
        error = "Error: Minimum investment amount is $5000 USD. You entered: $"+str(investment_amount)+" USD."
        print(error)
        return False, []
    strategy_list = [] #lower cased strategies
    if strategy1 is not None:
        lower_case_strategy1 = strategy1.lower()
        strategy_list.append(lower_case_strategy1)
    if strategy2 is not None:
        lower_case_strategy2 = strategy2.lower()
        strategy_list.append(lower_case_strategy2)
    error1 = "Error: Strategy must be one of the following: "+ str(lower_case_strategies) 
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
    return flag, strategy_list


# In[88]:


def getStocks(investment_amount=5000.00, strategy1='Ethical', strategy2=None):
    
    
    #Strategies need to be 'Ethical', 'Growth', 'Index', 'Quality' or 'Value'
    strategies = ['Ethical', 'Growth', 'Index', 'Quality', 'Value' ]
    lower_case_strategies = [s.lower() for s in strategies]
    
    
     #input validation
    invalid, strategy_list = input_validation(lower_case_strategies, investment_amount, strategy1, strategy2)
    if invalid or not strategy_list:
        return
        
    
    
    
    shares=[]
    #tickers = ['TICK', 'SYM', 'BOLS']
    #shares = [10, 20, 30]
    stocks= []
    for strategy in strategy_list:
        stocks.extend(get_recommendations(strategy))
        print(stocks)
        
   
    results = distribute(investment_amount, stocks)
    print('here', results);        
    
    #return(InvestmentPortfolio(stocks, shares))
    return results


# In[ ]:


s1 = getStocks(80000, 'index')
s1


# In[ ]:


s2 = getStocks(10000, 'ethical', 'growth')
s2


# In[ ]:


s3 = getStocks(80000, 'quality','value')
s3


# In[61]:


#some test cases below


# In[62]:


s = getStocks(50, 'ethic', "ethical")
printResults(s)


# In[63]:


s = getStocks(80000, 'hahaha', "ethical")
printResults(s)


# In[64]:


s = getStocks(80000, 'ethical', "hohoho")
printResults(s)


# In[65]:


s = getStocks(80000, 'hahaha', "hohoho")
printResults(s)


# In[66]:


s = getStocks(80000, 'ethic')
printResults(s)


# In[ ]:





# In[ ]:




