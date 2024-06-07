import pandas    as pd
import datetime  as dt
from ..common    import code
from ..analysis  import backtest  as bt
import ray

@ray.remote
def _index_backtest_ray(shCode, indexNm, pType, frDt, toDt, addDays, max_retention_days, multiRetentionInd, maxItemNum,          
                       cashAmt, taxRatio, expenseRatio, dayMaxTradeNum, dfZeroCross, retType, idx):
    _, dfReport, _ = bt._index_backtest(shCode=shCode, indexNm=indexNm, pType=pType, frDt=frDt, toDt=toDt
                                    , addDays=addDays , max_retention_days = max_retention_days 
                                    , multiRetentionInd = multiRetentionInd, maxItemNum = maxItemNum          
                                    , cashAmt = cashAmt, taxRatio = taxRatio, expenseRatio = expenseRatio     
                                    , dayMaxTradeNum = dayMaxTradeNum     
                                    , dfZeroCross = dfZeroCross
                                    , retType = retType )    
    if idx % 200 == 0:
        x = code.StockItem(shCode)['종목명']
        shName = x.values[0] if len(x) > 0 else None
        print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), idx, shCode, shName)
    return dfReport

def index_backtest_ray(shCode='', indexNm='', pType='종가', frDt='19960101', toDt='20991231'
                    , indexGrowthSign='B'       # 시장지수가 오를 때 매수(B)/매도(S) 신호 (defualt : 'B')
                    , daysForSignChange=1       # 매수/매도 사인 발생하기 위해 필요한 시장지수 연속 증가(감소) 일수 (default : 1)
                    , addDays=-1                # 선행일수 반영. 예) -1(1일전), 0(당일) 시장지수를 활용하여 매매(양수는 의미없음)
                    , max_retention_days = 9999 # S(매도) 사인이 발생하기 전이라도 (max_retention_days)일 이후 매도 처리
                    , multiRetentionInd = False # 매수(B) 이후 매도(S) 전 추가 매수(B) 발생 여부 (default : False)
                    , maxItemNum = 1            # 분산 투자 지수 (각 종목 매수 시 전체 금액의 1/N만큼 투자) (default : 1)
                                                # backtest 대상 종목수 이내 설정 가능(큰 경우 자동보정처리)
                    , cashAmt = 100000000       # 초기 투자금 (default : 1억)
                    , taxRatio = 0.2            # 거래세(%) (default : 0.2)
                    , expenseRatio = 0.015      # 거래수수료(%) (default : 0.015) 
                    , dayMaxTradeNum = 1        # 일 최대 매수 가능 종목수 (default : 1)                   
                   ):
    print('\r' + dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '분석시작')
    ray.init()
    
    dfRet = pd.DataFrame([])
    result = []
    
    shCodeList = code.getShcodeList(shCode)
    rLen = len(shCodeList)    
    retType = 'SUM' if rLen > 1 else 'DET'
    
    dfZeroCross = bt.getMarketIndex(indexNm, daysForSignChange=daysForSignChange, indexGrowthSign=indexGrowthSign)
    putZeroCross = ray.put(dfZeroCross)
    
    for idx, xCode in enumerate(shCodeList):
        dfReport = _index_backtest_ray.remote(xCode, indexNm, pType, frDt, toDt, addDays, max_retention_days, 
                                             multiRetentionInd, maxItemNum,          
                                             cashAmt, taxRatio, expenseRatio, dayMaxTradeNum, putZeroCross, retType, idx)      
            
        result.append(dfReport)
    
    result = ray.get(result)
    
    # 병렬처리 결과 merge
    for dfReport in result:
        dfRet = pd.concat([dfRet, dfReport])

    ray.shutdown()
    
    return dfRet