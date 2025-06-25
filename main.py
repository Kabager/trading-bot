def place_sell_order():
	# DO:
    # 	1. Вычислить количество актива для продажи (на основе
    # 	некоего заданного порогового значения, например, 
    # 50% общего баланса)
    # 2. Отправить POST-запрос к API биржи для выполнения
    # операции SELL
    # RETURN: Цена совершения сделки
	pass


def place_buy_order():
	# DO:
    #     1. Вычислить количество актива для покупки (на основе
    #     некоего заданного порогового значения, например, 
    #     50% общего баланса)
    #     2. Отправить POST-запрос к API биржи для выполнения
    #     операции BUY
    # RETURN: Цена совершения сделки
	pass


is_Next_Operation_Buy = True


def attemptToMakeTrade():
    # currentPrice = getMarketPrice()
    # percentageDiff = (currentPrice - lastOpPrice)/lastOpPrice*100
    # IF isNextOperationBuy:
    #     tryToBuy(percentageDiff)
    # ELSE:
    #     tryToSell(percentageDiff)
	pass


def tryToBuy(percentageDiff):
    # IF percentageDiff >= UPWARD_TREND_THRESHOLD OR percentageDiff <= DIP_THRESHOLD:
    #     lastOpPrice = placeBuyOrder()
    #     isNextOperationBuy = False
	pass


def tryToSell(percentageDiff):
    # IF percentageDiff >= PROFIT_THRESHOLD OR percentageDiff <= STOP_LOSS_THRESHOLD:
    #     lastOpPrice = placeSellOrder()
    #     isNextOperationBuy = True
	pass


def createLog(msg):
    # DO:
    #     1. Вывести msg в терминал
    #     2. Записать msg в файл журнала, добавив отметку времени
	pass


def bot_start():
	while True:
		# attemptToMakeTrade()
        # sleep(30 seconds)
		pass
