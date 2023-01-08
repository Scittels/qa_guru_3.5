import os

from selene.support.shared import browser
from selene import command, have


def test_send_full_form():
    browser.open('/automation-practice-form')
    # Ads off
    browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    # Filling form
    browser.element('#firstName').type('Elena')
    browser.element('#lastName').type('Skripal')
    browser.element('#userEmail').type('scittelsoO@gmail.com')

    browser.all('[for^=gender-radio-2]').element_by(have.text('Female')).click()
    browser.element('#userNumber').type('8912345678')


    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('September')
    browser.element('.react-datepicker__year-select').type(1990)
    browser.element('.react-datepicker__day--004:not(.react-datepicker__day--outside-month)').click()
    browser.element('#subjectsInput').type('commerce').press_enter()
    browser.element('[for ="hobbies-checkbox-1"]').click()
    browser.element('[for ="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'resources/cat.jpg')))

    browser.element('#currentAddress').type('Batumi')

    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').press_enter()

    # result
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Elena Skripal',
        'scittelsoO@gmail.com',
        'Female',
        '8912345678',
        '04 September,1990',
        'Commerce',
        'Sports, Reading',
        'cat.jpg',
        'Batumi',
        'Haryana Karnal'
    )
    )