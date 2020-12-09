class BankInterest():
    def __init__(self, summ, perc, period):
        self.summ   = summ
        self.period = period
        self.perc   = perc

    def diff_int(self):
        arr = [] #пустой массив для наполнения его месячными платежами
        mp_cnt = self.period * 12 #общее кол-во месяцев
        rest = self.summ #остаток долга
        #формула - остаток долга/общее кол-во месяцев + остаток долга*процентная ставка/12*100
        mp_real = self.summ / (self.period * 12.0) #первая часть формулы до знака + 
        #цикл, в котором мы рассчитываем ежемесячный платеж, заносим в массив
        while mp_cnt != 0:
            mp = mp_real + (rest * self.perc / 1200)
            arr.append(round(mp, 2)) #округляем до 2 знаком после запятой
            rest = rest - mp_real
            mp_cnt = mp_cnt - 1
        return arr, round(sum(arr), 2)

