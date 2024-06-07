from   datetime import datetime

import pandas   as pd 
import os, sys
import datetime as dt

# here = os.path.dirname(__file__)
# sys.path.append(os.path.join(here, '..'))
from  ..innerIO  import marketIndex    as mIndex
from  ..innerIO  import stockInfo      as sd
from  ..common   import code
from  .          import func  

def GetInterIndexCorrelation(indexNm1, indexNm2, sDate='20000101',  eDate='20991231', addDays=0, 
                             rptGb='기본', period='일'):
    """
    (input)
        indexNm1/2 : BDI 등 
        addDays    : indexNm1의 날짜 조정 일수 (예) 3 : indexNm1 일자 + 3일 = indexNm2 일자
        rptGb      : '기본' 원본 값으로 계산 / '증감' : 증감값으로 계산 / '전체' : 원본값 및 증감값으로 모두 계산
    (output)
        상관계수 return
    """
    
    columns=['인덱스1','인덱스2','분석대상건수']
    if rptGb in ['기본', '전체']:  columns += ['상관계수', 'p-value']
    if rptGb in ['증감', '전체']:  columns += ['증감값상관계수','증감값p-value','증감값유사도', '증감값비유사도']
    
    resData = []
            
    # 1년 365일 모든 일자에 대해 경제지수 데이터 생성 (없는 경우 전일 데이터 값으로 생성)
    # 선행일수 고려 증권거래일자와 매핑을 하기 위한 사전 작업
    dfIndex1 = mIndex.MarketIndex(indexNm1)
    dfIndex2 = mIndex.MarketIndex(indexNm2)
    if period=='일':
        dfIndex2 = func.makeFullDayData(dfIndex2)    
    if period=='주':
        dfWeeks = func.getISOWeeks(sDate=sDate, eDate=eDate, addDays=addDays)
    else:
        dfWeeks = []
        
    if period != '일':
        dfIndex1 = func.addPeriodGrp(dfIndex1, indexNm1, dfWeeks=dfWeeks, period=period, sDate=sDate, eDate=eDate, addDays=0)
    dfIndex2 = func.addPeriodGrp(dfIndex2, indexNm2, dfWeeks=dfWeeks, period=period, sDate=sDate, eDate=eDate, addDays=addDays)
    dfMerge = pd.merge(dfIndex1, dfIndex2)
                    
    # 병합한 데이터로 Correlation Value 계산 
    corrVal = func.CalcCorrRelation(dfMerge[indexNm1].values.tolist(), dfMerge[indexNm2].values.tolist(), rptGb=rptGb)

    if len(corrVal) > 0:
        resData.append([indexNm1, indexNm2] + corrVal)        

    retVal = pd.DataFrame(resData, columns=columns)
        
    return retVal


def GetStockIndexCorrelation(priceType, indexNm, shCodes=[], sDate='00000101',  eDate='99991231', 
                             addDays=0, rptGb='기본', period='일', extDt='',prtInd=True):    
    """
    (input)
        priceType : 시가/고가/저가/종가
        indexNm : BDI 등 
        shCodes : '000980' (특정종목), ['123456','005880'] (리스트). [ ] (데이터가 없으면 전 종목 분석)
        addDays : 주식거래 날짜 조정 일수 (예) 3 : 주식거래일자 + 3일 = indexNm2 일자
        rptGb   : '기본' 원본 값으로 계산 / '증감' : 증감값으로 계산 / '전체' : 원본값 및 증감값으로 모두 계산
    (output)
        상관계수 return
    """
     
    columns=['종목코드','종목명','분석대상건수']
    if rptGb in ['기본', '전체']:  columns += ['상관계수', 'p-value']
    if rptGb in ['증감', '전체']:  columns += ['증감값상관계수','증감값p-value','증감값유사도', '증감값비유사도']

    resData = []   
    
    # 1년 365일 모든 일자에 대해 경제지수 데이터 생성 (없는 경우 전일 데이터 값으로 생성)
    # 선행일수 고려 증권거래일자와 매핑을 하기 위한 사전 작업
   
    dfIndex = mIndex.MarketIndex(indexNm)
    avgPeriod, upPeriod, downPeriod = func.getAvgTurnAround(dfIndex[indexNm].values.tolist())
    
    if period=='일':
        dfIndex = func.makeFullDayData(dfIndex, eDate=extDt)
        
    if period=='주':
        dfWeeks = func.getISOWeeks(sDate=sDate, eDate=eDate, addDays=addDays)
    else:
        dfWeeks = []
        
    dfIndex = func.addPeriodGrp(dfIndex, indexNm, dfWeeks=dfWeeks, period=period, sDate=sDate, eDate=eDate, addDays=addDays)
    if len(shCodes) == 0:
        shCodes = code.StockItemList().query("시장구분 != 'KONEX'")['종목코드'].values.tolist()
    elif type(shCodes) == str:
        shCodes = [shCodes]
    elif type(shCodes) == type(pd.DataFrame([])):
        shCodes = shCodes.values.tolist()  
    if prtInd:
        print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '분석시작', indexNm)


    for i, shCode in enumerate(shCodes):

        shName  = code.StockItem(shCode)['종목명']                        
        shName = shName.iloc[0] if len(shName) > 0 else ''   

        dfStock = sd.StockTrade(shCode)[['일자', priceType]]
        if dfStock['일자'].iloc[0] < sDate or eDate < dfStock['일자'].iloc[len(dfStock)-1]:
            dfStock = dfStock.query("'" + sDate + "' <= 일자 and 일자 <= '" + eDate + "'")       

        # 주가정보와 지표정보를 선행 기준에 의해 병합
        # dfMerge = dfStock.merge(dfIndex)[['일자', priceType, 'Signal일자', indexNm]]
        if period != '일':
            dfStock = func.addPeriodGrp(dfStock, priceType, dfWeeks=dfWeeks, period=period, sDate=sDate, eDate=eDate, addDays=0)
                
        dfMerge = pd.merge(dfStock, dfIndex)

        # 병합한 데이터로 Correlation Value 계산 
        corrVal = func.CalcCorrRelation(dfMerge[priceType].values.tolist(), dfMerge[indexNm].values.tolist(), rptGb)        
        
        if len(corrVal) > 0:
            resData.append([shCode, shName] + corrVal)        

        # resData.append([shCode, shName, corVal[0], corVal[1], mergeData[0][1], mergeData[recCnt-1][1], recCnt])
        if prtInd:
            print('\r' + dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i+1, '/', len(shCodes), shCode, shName, ' '* 40, '\r', end='')

    resData.sort(key = lambda x: x[3], reverse=True)

    retVal = pd.DataFrame(resData, columns=columns)
    retVal['전체평균기간'] = avgPeriod
    retVal['상승평균기간'] = upPeriod
    retVal['하락평균기간'] = downPeriod
        
    return retVal

# def _MakeFullDayData(listData, indexGrowthSign='B', consecutiveCntForSignChange=1):
    
#     """
#     indexGrowthSign : 지수가 오를 때 신호  
#       - B(매수) : 예) 운임지수, 인구 등
#       - S(매도) : 예) 인건비, 유가, 환율 등 
#     consecutiveCntForSignChange : 매수/매도 사인이 바뀌기 위해 필요한 연속 증가(감소) 일수
#     """
  
#     # 경제지수 input data 정렬 및 중복 제거 (크롤링 시 중복 발생하는 케이스 )
#     # 날짜 형식도 8자리 숫자로 통일
#     listData.sort()    
#     dfList = [ [data[0].replace('-','').replace('/',''), data[1] ]
#                for idx, data in enumerate(listData) if idx == 0 or data[0] > listData[idx-1][0] ]
    
#     # 변수 초기화
#     resData = []
#     sDate = str(dfList[0][0])
#     eDate = str(dfList[len(dfList) - 1][0])

#     listIdx = 0
#     signal = 'S'
#     plusConsecutiveCnt = 0
#     minusConsecutiveCnt = 0
    
#     for x in pd.date_range(sDate, eDate):        
#         cDate = datetime.strftime( x, '%Y%m%d')
        
#         if cDate == dfList[listIdx][0]:
#             curVal = dfList[listIdx][1]
            
#             if listIdx > 0:

#                 if lastVal < curVal:
#                     plusConsecutiveCnt  += 1
#                     minusConsecutiveCnt  = 0
#                 elif lastVal > curVal:
#                     plusConsecutiveCnt   = 0
#                     minusConsecutiveCnt += 1                
                
#                 # 특정 일수 이상 index 수치가 연속 증가 시 SELL -> BUY
#                 if   indexGrowthSign == 'B' and signal == 'S' and plusConsecutiveCnt  >= consecutiveCntForSignChange :
#                     signal = 'B'
#                 # 특정 일수 이상 index 수치가 연속 감소 시 BUY -> SELL
#                 elif indexGrowthSign == 'B' and signal == 'B' and minusConsecutiveCnt >= consecutiveCntForSignChange :
#                     signal = 'S'
#                 # 특정 일수 이상 index 수치가 연속 증가 시 BUY -> SELL
#                 elif indexGrowthSign == 'S' and signal == 'B' and plusConsecutiveCnt  >= consecutiveCntForSignChange :
#                     signal = 'S'
#                 # 특정 일수 이상 index 수치가 연속 감소 시 SELL -> BUY
#                 elif indexGrowthSign == 'S' and signal == 'S' and minusConsecutiveCnt >= consecutiveCntForSignChange :
#                     signal = 'B'                             
                
#                 # if   indexGrowthSign == 'B' and lastVal < curVal and signal == 'S' :
#                 #     signal = 'B'
#                 # elif indexGrowthSign == 'B' and lastVal > curVal and signal == 'B' :
#                 #     signal = 'S'
#                 # elif indexGrowthSign == 'S' and lastVal < curVal and signal == 'B' :
#                 #     signal = 'S'
#                 # elif indexGrowthSign == 'S' and lastVal > curVal and signal == 'S' :
#                 #     signal = 'B'                    
                    
#             lastVal = curVal
#             listIdx += 1
            
#         resData.append([cDate, lastVal, signal])
    
#     return resData

# def _MergeStockIndex(listStock, listMarketIndex, sDate, eDate, advance):
#     idxS = 0
#     idxE = 0
    
#     mergeData = []
    
#     # 일별 주가와 일별 경제 지수 merge (선행 advance일수 반영)
#     while idxS < len(listStock) and idxE < len(listMarketIndex):
        
#         if listStock[idxS][0] < listMarketIndex[idxE][0]:
#             idxS += 1
#         elif listStock[idxS][0] > listMarketIndex[idxE][0]:
#             idxE += 1        
#         else:
#             if (idxE + advance) >= 0 and sDate <= listStock[idxS][0] and listStock[idxS][0] <= eDate:
#                 mergeData.append( listStock[idxS] + listMarketIndex[idxE + advance] )
                
#             idxS += 1
#             idxE += 1

#     return mergeData

# def _GetDailySimulationData(investAmt, mergeData, feeRatio, taxRatio, priceType, indexNm):    
#     resData = []
#     stockCnt = 0
#     cashAmt = investAmt

#     # 거래 simulation 실행
#     for _, data in enumerate(mergeData):
#         feeAmt = 0                # 매수/매도 시 증권 수수료
#         taxAmt = 0                # 매도 시 세금
#         stockPrice = int(data[1]) # 주가 (매수,매도가)
#         tradeAmt = 0              # 매수/매도 시 거래대금
        
#         if stockCnt > 0 and data[4] == 'S':
#             tradeAmt = stockCnt * stockPrice
#             feeAmt   = int((tradeAmt * feeRatio)/100) * (-1)
#             taxAmt   = int((tradeAmt * taxRatio)/100) * (-1)
#             stockCnt = 0
#             cashAmt  = cashAmt + tradeAmt + taxAmt + feeAmt
#         elif stockCnt == 0 and data[4] == 'B':
#             stockCnt = int( cashAmt * (1 - feeAmt/100) / stockPrice) # 보유 현금 중 거래세 0.015%를 제한 금액내에서 투자
#             tradeAmt = stockCnt * stockPrice * (-1)
#             feeAmt   = int((tradeAmt * feeRatio)/100) 
#             cashAmt  = cashAmt + tradeAmt + feeAmt
            
# #         else:
# #             continue
            
#         resData.append( data + [stockCnt, tradeAmt, feeAmt, taxAmt, cashAmt, cashAmt + stockCnt * stockPrice] )             
        
#     return pd.DataFrame(resData, columns=['거래일자', priceType, 'Index기준일자', indexNm, 'Signal',
#                                           '보유주수','거래금액', '수수료', '거래세', '현금', '평가금액'])


# def TradeSimulation(priceType, indexNm, shCodes=[], 
#                     sDate='00000101',  eDate='99991231', investAmt=10000000, advance=-1, feeRatio=0.015, taxRatio=0.3, indexGrowthSign='B',
#                     consecutiveCntForSignChange=1):
#     """
#     (input)
#         priceType : 시가/고가/저가/종가 (과거 데이터로 투자모형 시뮬레이션 시 사용될 일별 주가. 실제 거래 적용 시 시가거래가 현실적으로 가능)
#         indexNm : DJI@DJT(다우운송지수), SPI@SPRLX(S&P소비지수), IPE@EBK24(브렌트유지수), COM@HRCG24(강철가격지수) 등 
#         shCodes : '000980' (특정종목), ['123456','005880'] (리스트). [ ] (데이터가 없으면 전 종목 분석)
#         advance : 선행일수 (예) -3 : 3일전 경제지표 변동에 의해 당일 거래 Signal 분석 (음수값만 의미가 있음) 
#         indexGrowthSign : 지수가 오를 때 신호  
#         - B(매수) : 예) 운임지수, 환율 등 분석 시
#         - S(매도) : 예) 인건비, 유가, 환율 등 분석 시 
#     (output)
#         분석대상(shCodes)이 단일종목인 경우, 일자별 simulation 내역 return
#         복수 종목인 경우 simulation summary 데이터 return
#     """
     
#     # 1년 365일 모든 일자에 대해 경제지수 데이터 생성 (없는 경우 전일 데이터 값으로 생성)
#     # 선행일수 고려 증권거래일자와 매핑을 하기 위한 사전 작업

#     # listMarketIndex = _MakeFullDayData( de.ReadMarketIndex(indexNm, objTyp='list')['data'], indexGrowthSign )    

#     indexValueList = mIndex.MarketIndex(indexNm, objTyp='list')

#     listMarketIndex = _MakeFullDayData(indexValueList, indexGrowthSign=indexGrowthSign, 
#                                     consecutiveCntForSignChange=consecutiveCntForSignChange )    

#     if type(shCodes) == str:
#         # listStock = sd.ReadStockTrade(shCodes)[['일자', priceType]].values.tolist()
#         listStock = sd.ReadStockTrade(shCodes)[['일자', priceType]].astype({priceType:'int64'}).values.tolist()
        
#         # 주가정보와 지표정보를 선행 기준에 의해 병합
#         mergeData = _MergeStockIndex(listStock, listMarketIndex, sDate, eDate, advance)

#         # 병합한 데이터로 거래 simulation 수행 
#         retVal = _GetDailySimulationData(investAmt, mergeData, feeRatio, taxRatio, priceType, indexNm)

#         colNm = 'Sign'
#     else:
#         resData = []
#         colNm = '거래횟수'

#         if type(shCodes) == type(pd.DataFrame([])):
#             shCodes = shCodes.values.tolist()  
        
#         print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'total cnt >> ', len(shCodes))

#         for i, shCode in enumerate(shCodes):
            
#             shName  = code._GetCmpnyName(shCode)['종목명']
#             shName = shName.iloc[0] if len(shName) > 0 else ''   

#             listStock = sd.ReadStockTrade(shCode)[['일자', priceType]].values.tolist()

#             # 주가정보와 지표정보를 선행 기준에 의해 병합
#             mergeData = _MergeStockIndex(listStock, listMarketIndex, sDate, eDate, advance)

#             # 병합한 데이터로 거래 simulation 수행 
#             # print(shCode, shName, flush=True)
#             df = _GetDailySimulationData(investAmt, mergeData, feeRatio, taxRatio, priceType, indexNm)
                     
#             if len(df) > 0:
#                 idxLast = len(df) - 1
#                 resData.append( [ shCode, shName, 
#                                  len(df[df['거래금액']>0]), 
#                                  df['거래일자'].iloc[0], df['거래일자'].iloc[idxLast], 
#                                  df[priceType].iloc[0], df[priceType].iloc[idxLast], 
#                                  df['평가금액'].iloc[0], df['평가금액'].iloc[idxLast],
#                                 int ( int(df[priceType].iloc[idxLast]) / int(df[priceType].iloc[0]) * 100 - 100), 
#                                 int ( int(df['평가금액'].iloc[idxLast]) / int(df['평가금액'].iloc[0]) * 100 - 100)
#                                 ])
                    
#             print('\r' + dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'proc_cnt >> ', i+1, ' '* 40, '\r', end='')

#         resData.sort(key = lambda x: x[8], reverse=True)

#         retVal = pd.DataFrame(resData, columns=['종목코드','종목명',colNm,'시작일자','종료일자','시작일_'+priceType,'종료일_'+priceType,
#                                                 '시작일_평가금액','종료일_평가금액','시가_증감율','평가금액_증감율'])
        
#     return retVal