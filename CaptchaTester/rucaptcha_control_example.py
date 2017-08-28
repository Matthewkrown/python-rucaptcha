from python_rucaptcha import RuCaptchaControl

from temp_config import RECAPTCHA_KEY

"""
Этот пример показывает работу модуля управления аккаунтом RuCaptcha.
Присутствует возможность получить информацию о балансе средств и отправить жалобу на неверно решённую капчу.
"""
# Введите ключ от рукапчи из своего аккаунта
RUCAPTCHA_KEY = RECAPTCHA_KEY

# Пример получения актуального баланса средств на аккаунте
answer = RuCaptchaControl.RuCaptchaControl(rucaptcha_key=RUCAPTCHA_KEY).get_balance()

print("Your balance is: ", answer['request'], " rub.")


# Пример отправки жалобы на неправильно решённую капчу под ID "666"
wrong_captcha_id = 666

answer = RuCaptchaControl.RuCaptchaControl(rucaptcha_key = RUCAPTCHA_KEY).complaint_on_result(reported_id = wrong_captcha_id)

# Если заявка принята
if answer['status']=='OK':
    print("Заявка принята.")
# Если возникла ошибка
elif answer['status']=='Error':
    print(answer['err'])