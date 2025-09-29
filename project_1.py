from selene import browser, be, have
browser.open('https://ya.ru')
browser.element('[name="text"]').should(have.attribute('value', '')).type('Куры по QA').press_enter()
close_selectors = [
    '[class*="Distribution-ButtonClose"]',
    '[aria-label*="закрыть"]',
    '[title*="Нет, спасибо"]',
    'button[type="button"]:last-child'
]
for selector in close_selectors:
    if browser.element(selector).matching(be.visible):
        browser.element(selector).click()
        break
def check_text_variants(*text_variants):
    for text in text_variants:
        if browser.element('html').matching(have.text(text)):
            print(f"Найден текст: {text}")
            return True
    return False
if check_text_variants("Тестировщиком", "Тестирование"):
    print("Один из вариантов текста найден")
else:
    print("Ни один из вариантов не найден")