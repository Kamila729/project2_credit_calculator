import requests
from bank_interest import BankInterest



url = "https://api.telegram.org/bot1483572011:AAHxHuKPZTBAMzD37OOC0eMEyqWwr8tshd8/"

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):  
    results = data['result']
    return results[-1]

def get_chat_data(update):  
    chat_id = update['message']['chat']['id']
    text = update['message']['text']
    return chat_id,text


def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    cid ,t = get_chat_data(last_update(get_updates_json(url)))

    if t == '/start':
        send_mess(cid, 'Доброго времени суток! Я помогу Вам рассчитать ежемесячные платежи по дифференцируемому кредиту. Введите «сумму кредита», «процентную ставку», «срок кредита», через пробел в одну строку и я выдам ответ!')
        return

    loan_amount, perc, period = (int(i) for i in t.split())

    #                   Сумма,  процент, срок(год)
    BI = BankInterest(loan_amount, perc, period)
    payments, summ = BI.diff_int()

    my_text = ''

   
        
    for j,p in enumerate(payments):
        my_text += "Платеж {:7d} : {:.2f} руб.".format(j+1,p)+'\n'
            
   
    my_text += "Всего выплачено: {:.2f} руб.".format(summ)+'\n'

    send_mess(cid, my_text)
main()          
            