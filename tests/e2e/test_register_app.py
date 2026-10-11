import re
from playwright.sync_api import expect
import pytest

# ------------------------------------------------------------------------
# User story 1 - Sidans titel
# ------------------------------------------------------------------------
# Som besökare vill jag kunna läsa sidans titel,
# så att jag vet att jag är på rätt sida.

# Acceptanskriteria 1
# AK1: När jag kommer till sidan ska sidans titel visas
# 1. Titeln ""Registrera dig" ska visas

# Scenario 1
# 1. Ladda sidan
# 2. Kontrollera att titeln i AK 1 visas


@pytest.mark.register
def test_register_app_get_title(register_app_page):

    # 1. Kontrollera att titeln "registrera dig" visas""
    assert "Registrera dig" in register_app_page.title()


# ------------------------------------------------------------------------
# User story 2 - Sidans rubrik
# ------------------------------------------------------------------------
# Som besökare vill jag kunna läsa sidans rubrik,
# för att ytterligare vara förvissad om att jag är på rätt sida.

# Acceptanskriteria 1
# AK1: När jag kommer till sidan ska sidans rubrik visas
# 1. Rubriken "Registrera dig" ska visas

# Scenario 1
# 1. Ladda sidan
# 2. Kontrollera att rubriken i AK 1 visas


@pytest.mark.register
def test_register_app_get_header(register_app_page):

    # 1. Kontrollera att rubriken "Registrera dig" visas
    main_header = register_app_page.get_by_role(
        "heading",
        name=re.compile("Registrera dig"))

    expect(main_header).to_be_visible()

# ------------------------------------------------------------------------
# User story 3 - Inmatning namn
# ------------------------------------------------------------------------
# Som besökare vill jag kunna ange mitt namn,
# så att jag kan registrera mitt namn.

# Acceptanskriteria 1
# AK1: Man ska kunna skriva in Namn i ett textfält
# 1. Namnet ändras

# Scenario 1
# 1. Ladda sidan
# 2. Kontrollera att det finns ett inmatningsfält för namn
# 3. Skriv in ett nytt namn
# 4. Kontrollera att det nya namnet visas i textfältet


@pytest.mark.register
def test_register_app_input_name(register_app_page):

    # 1. Kontrollera att det finns ett inmatningsfält för namn
    name_field = register_app_page.get_by_label("Namn")

    expect(name_field).to_be_visible()

    # 2. Skriv in ett nytt namn
    name_field.fill("Barbapappa")

    # 3. Kontrollera att det nya namnet visas i textfältet
    expect(name_field).to_have_value("Barbapappa")


# ------------------------------------------------------------------------
# User story 4 - Inmatning födelseår
# ------------------------------------------------------------------------
# Som besökare vill jag kunna ange mitt födelseår,
# så att jag kan registera mitt födelseår.

# Acceptanskriteria 1
# AK1: Man ska kunna skriva in ett födelseår i ett textfält
# 1. Födelseåret adressen ändras

# Scenario 1
# 1. Ladda sidan
# 2. Kontrollera att det finns ett inmatningsfält för födelseår
# 3. Skriv in ett nytt födelseår
# 4. Kontrollera att det nya födelseåret visas i textfältet


@pytest.mark.register
def test_register_app_input_birth_year(register_app_page):

    # 1. Kontrollera att det finns ett inmatningsfält för födelseår
    birth_year_field = register_app_page.get_by_label("Födelseår")

    expect(birth_year_field).to_be_visible()

    # 2. Skriv in ett nytt födelseår
    birth_year_field.fill("1977")

    # 3. Kontrollera att det nya födelseåret visas i textfältet
    expect(birth_year_field).to_have_value("1977")


# ------------------------------------------------------------------------
# User story 5 - Födelseår matas in med rätt syntax
# ------------------------------------------------------------------------
# Som besökare vill jag att appen rättar mig om jag skriver in födelseår fel,
# så att jag vet att jag skrivit rätt format.

# Acceptanskriteria 1
# AK1: När jag skriver in ett födelseår som inte är fyra siffror
# ska sidan varna mig
# 1. En varningstext visas

# Scenario 1
# 1. Ladda sidan
# 2. Skriv in ett födelseår som inte är fyra siffror
# 3. Kontrollera att det visas en varningstext "Skriv årtal med fyra siffror."


@pytest.mark.register
def test_register_app_incorrect_birth_year(register_app_page):

    # 1. Skriv in ett födelseår som inte är fyra siffror
    birth_year_field = register_app_page.get_by_label("Födelseår")

    birth_year_field.fill("19777")

    # 2. Kontrollera att det visas en varningstext "Skriv årtal med
    # fyra siffror."
    error_message = register_app_page.get_by_text(
        "Skriv årtal med fyra siffror.",
    )

    expect(error_message).to_be_visible()


# ------------------------------------------------------------------------
# User story 6 - Imnatning E-post adress
# ------------------------------------------------------------------------
# Som besökare vill jag kunna ange min E-post adress,
# så att jag kan kontaktas med mail.

# Acceptanskriteria 1
# AK1: Man ska kunna skriva in en E-post adress i ett textfält
# 1. E-post adressen ändras

# Scenario 1
# 1. Ladda sidan
# 2. Kontrollera att det finns ett inmatningsfält för E-post adress
# 3. Skriv in en E-post adress
# 4. Kontrollera att den nya E-post adressen visas i textfältet.


@pytest.mark.register
def test_register_app_input_mail_address(register_app_page):

    # 1. Kontrollera att det finns ett inmatningsfält för E-post adress
    e_mail_field = register_app_page.get_by_label("E-post")

    expect(e_mail_field).to_be_visible()

    # 2. Skriv in en ny E-poast adress
    e_mail_field.fill("John.doe@test.se")

    # 3. Kontrollera att det nya födelseåret visas i textfältet
    expect(e_mail_field).to_have_value("John.doe@test.se")


# ------------------------------------------------------------------------
# User story 7 - E-post adress matas in med rätt syntax
# ------------------------------------------------------------------------
# Som besökare vill jag att appen rättar mig om jag skriver in E-post
# adressen fel, så att jag vet att jag skrivit rätt format.

# Acceptanskriteria 1
# AK1: När jag skriver in E-post adress som inte har rätt format ska
# det visas en varning
# 1. En varningstext visas

# Scenario 1
# 1. Ladda sidan
# 2. Skriv in en E-post adress som inte har formatet email@domän.com
# 3. Kontrollera att det visas en varningstext "Använd formatet:
# email@domän.com"


@pytest.mark.register
def test_register_app_incorrect_mail_address(register_app_page):

    # 1. Skriv in en E-post adress som inte har formatet email@domän.com
    mail_field = register_app_page.get_by_label("E-post")

    mail_field.fill("john.doe.test.se")

    # 2. Kontrollera att det visas en varningstext "Använd formatet:
    # email@domän.com"
    error_message = register_app_page.get_by_text(
        "Använd formatet: email@domän.com",
    )

    expect(error_message).to_be_visible()


# ------------------------------------------------------------------------
# User story 8 - Imnatning lösenord
# ------------------------------------------------------------------------
# Som besökare vill jag kunna ange ett lösenord,
# så att jag senare kan logga in i appen.

# Acceptanskriteria 1
# AK1: Man ska kunna skriva in ett lösenord i ett textfält
# 1. Lösenordet adressen ändras

# Scenario 1
# 1. Ladda sidan
# 2. Kontrollera att det finns ett inmatningsfält för lösenord
# 3. Skriv in ett lösenord
# 4. Kontrollera att det nya lösenordet visas i textfältet.


@pytest.mark.register
def test_register_app_input_password(register_app_page):

    # 1. Kontrollera att det finns ett inmatningsfält för lösenord
    password_field = register_app_page.get_by_label("Lösenord")

    expect(password_field).to_be_visible()

    # 2. Skriv in en ny E-poast adress
    password_field.fill("!Jx6_?h5O")

    # 3. Kontrollera att det nya lösenordet visas i textfältet
    expect(password_field).to_have_value("!Jx6_?h5O")


# ------------------------------------------------------------------------
# User story 9 - Imnatning kort lösenord
# ------------------------------------------------------------------------
# Som besökare vill jag få en varning om jag skriver ett för kort lösenord,
# så att jag kan skriva in ett med rätt längd.

# Acceptanskriteria 1
# AK1: Om man skriver in ett för kort lösenor ska man få en varning
# 1. En varningstext visas

# Scenario 1
# 1. Ladda sidan
# 2. Skriv in ett lösenord som är kortare än fyra tecken
# 3. Kontrollera att det visas en varningstext "Lösenordet ska
# vara minst 4 tecken."


@pytest.mark.register
def test_register_app_input_to_short_password(register_app_page):

    # 1. Skriv in ett lösenord som är kortare än fyra tecken
    password_field = register_app_page.get_by_label("Lösenord")

    password_field.fill("a?N")

    # 2. Kontrollera att det visas en varningstext "Lösenordet ska vara
    # minst 4 tecken."
    error_message = register_app_page.get_by_text(
        "Lösenordet ska vara minst 4 tecken.",
    )

    expect(error_message).to_be_visible()


# ------------------------------------------------------------------------
# User story 10 - Aktivering submit knapp
# ------------------------------------------------------------------------
# Som besökare vill inte kunna klicka submit förrän jag fyllt i allt korrekt,
# så att jag vet att jag gjort rätt.

# Acceptanskriteria 1
# AK1: När man fyllt i alla fält korrekt ska submit knappen aktiveras
# 1. Submit knappen blir synlig

# Scenario 1
# 1. Ladda sidan
# 2. Kontrollera att submitknappen är deaktiverad
# 3. Fyll i alla textfält med korrekta värden
# 4. Kontrollera att submitknappen aktiveras
# 5. Kontrollera att det går att trycka på submit knappen


@pytest.mark.register
def test_register_app_submit_button_activation(register_app_page):

    # 1, Kontrollera att submitknappen är deaktiverad
    submit_button = register_app_page.get_by_role(
        "button",
        name="Ok nu kör vi"
    )

    expect(submit_button).to_be_disabled()

    # 2. Fyll i alla textfält med korrekta värden
    name_field = register_app_page.get_by_label("Namn")
    name_field.fill("Barbapappa")

    birth_year_field = register_app_page.get_by_label("Födelseår")
    birth_year_field.fill("1977")

    e_mail_field = register_app_page.get_by_label("E-post")
    e_mail_field.fill("john.doe@test.se")

    password_field = register_app_page.get_by_label("Lösenord")
    password_field.fill("!Jx6_?h5O")

    # 3. Kontrollera att submitknappen är aktiverad
    expect(submit_button).to_be_enabled()
