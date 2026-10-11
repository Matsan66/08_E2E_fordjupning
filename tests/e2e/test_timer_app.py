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
# 1. Titeln ""Timer app" ska visas

# Scenario 1
# 1. Ladda sidan
# 2. Kontrollera att titeln i AK 1 visas


@pytest.mark.timer
def test_timer_app_get_title(timer_app_page):

    # Visas titeln "Timer app" på sidan
    assert "Timer app" in timer_app_page.title()

# ------------------------------------------------------------------------
# User story 2 - Starta en timer
# ------------------------------------------------------------------------
# Som besökare vill jag kunna starta en timer,
# så att jag vet när tiden är ute.

# Acceptanskriteria
# AK1: När jag kommer till sidan ska knappen "Add timer" visas
# 1. Knappen med texten "Add timer" ska finnas
# AK2: När jag klickar på knappen "Add timer" ska en timer visas
# 1. En timer ska ha skapats

# Scenario
# 1. Ladda sidan
# 2. Kontrollera knappen "Add timer" visas
# 3. Klicka på knappen "Add timer"
# 4. Kontrollera att en timer visas


@pytest.mark.timer
def test_timer_app_open_timer(timer_app_page):

    # 1. Kontrollera knappen "Add timer" visas
    timer_button = timer_app_page.get_by_role(
        "button", name=re.compile("Add timer"))

    expect(timer_button).to_be_visible()

    # 2. Klicka på knappen "Add timer"
    timer_button.click()

    # 3. Kontrollera att en timer visas
    timer_widget = timer_app_page.get_by_role(
        "heading", name=re.compile("Break"))

    expect(timer_widget).to_be_visible()

# ------------------------------------------------------------------------
# User story 3 - Ta bort en timer
# ------------------------------------------------------------------------
# Som besökare vill jag kunna ta bort en timer,
# så att sidan återställs för ny användning.

# Acceptanskriteria
# AK1: Det ska finnas en Papperskorg ikon för att ta bort timern
# 1. En knapp med ikonen av en papperskorg ska visas
# AK2: När jag klickar på knappen för papperskorg ska timern försvinna
# 1. Timern ska försvinna

# Scenario
# 1. Ladda sidan
# 2. Klicka på knappen "Add timer"
# 3. Kontrollera att en timer skapats
# 4. Kontrollera att det finns en ikon för pappeskorg
# 5. Klicka på ikonen för papperskorg
# 6. ontrollera att timern försvinner


@pytest.mark.timer
def test_timer_app_delete_timer(timer_app_page):

    # 1. Klicka på knappen "Add timer"
    timer_app_page.get_by_role(
        "button", name=re.compile("Add timer")).click()

    # 2 Kontrollera att en timer skapats
    timer_widget = timer_app_page.get_by_role(
        "heading", name=re.compile("Break"))

    expect(timer_widget).to_be_visible()

    # 3. Kontrollera att det finns en ikon för pappeskorg
    expect(timer_app_page.get_by_text(" 🗑️ ")).to_be_visible()

    # 4. Klicka på ikonen för papperskorg
    timer_app_page.get_by_text(" 🗑️ ").click()

    # 5. Kontrollera att timern försvinner
    expect(timer_widget).not_to_be_visible()


# ------------------------------------------------------------------------
# User story 4 - Öppna en anteckning
# ------------------------------------------------------------------------
# Som besökare vill jag kunna lägga till en anteckning,
# så att jag kan lägga till viktiga saker.

# Acceptanskriteria
# AK1: När jag kommer till sidan ska knappen "Add note" visas
# 1. Knappen med texten "Add note" ska finnas
# AK2: När jag klickar på knappen "Add note" ska en ny anteckning skapas
# 1. En anteckning ska ha öppnats

# Scenario
# 1. Ladda sidan
# 2. Kontrollera att knappen "Add note" visas
# 3. Klicka på knappen "Add note"
# 4. Kontrollera att en ny anteckning visas


@pytest.mark.timer
def test_timer_app_open_note(timer_app_page):

    # 1. Kontrollera att knappen "Add note" visas
    note_button = timer_app_page.get_by_role(
        "button", name=re.compile("Add note"))

    expect(note_button).to_be_visible()

    # 2. Klicka på knappen "Add note"
    note_button.click()

    # 3. Kontrollera att en ny anteckning visas
    note_widget = timer_app_page.get_by_role(
        "heading", name=re.compile("Click to change text"))

    expect(note_widget).to_be_visible()


# ------------------------------------------------------------------------
# User story 5 - Ta bort en anteckning
# ------------------------------------------------------------------------
# Som besökare vill jag kunna ta bort en anteckning,
# så att sidan bara innehåller aktuell information.

# Acceptanskriteria
# AK1: Det ska finnas en Papperskorg ikon för att ta bort anteckningen
# 1. En knapp med ikonen av en papperskorg ska visas
# AK2: När jag klickar på knappen för papperskorg ska anteckningen försvinna
# 1. Anteckningen ska försvinna

# Scenario
# 1. Ladda sidan
# 2. Klicka på knappen "Add note"
# 3. Kontrollera att anteckningen visas
# 4. Kontrollera att papperskorgen visas
# 5. Klicka på papperskorgen
# 6. Kontrollera att anteckningen försvinner


@pytest.mark.timer
def test_timer_app_delete_note(timer_app_page):

    # 1. Klicka på knappen "Add note"
    timer_app_page.get_by_role(
        "button", name=re.compile("Add note")).click()

    # 2. Kontrollera att anteckningen visas
    note_widget = timer_app_page.get_by_role(
        "heading", name=re.compile("Click to change text"))

    expect(note_widget).to_be_visible()

    # 3. Kontrollera att papperskorgen visas
    expect(timer_app_page.get_by_text(" 🗑️ ")).to_be_visible()

    # 4. Klicka på papperskorgen
    timer_app_page.get_by_text(" 🗑️ ").click()

    # 6. Kontrollera att anteckningen försvinner
    expect(note_widget).not_to_be_visible()

# ------------------------------------------------------------------------
# User story 6 - Byt plats på Widgets
# ------------------------------------------------------------------------
# Som besökare vill jag kunna ändra plats på widgets,
# så att jag kan skifta fokus på det som är viltigt.

# Acceptanskriteria
# AK1: När jag har två widgets öppna ska verje widget ha en sorteringspil
# 1. Knapparna för att flytta upp en widget ska finnas
# AK2: När jag klickar den nedersta sorteringspilen ska widgeten
# flyttas över den andra
# 1. Den nedre widgeten ska vara överst

# Scenario
# 1. Ladda sidan
# 2. Öppna en timer
# 3. Öppna en anteckning
# 4. Kontrollera anteckningen har en sorteringspil
# 5. Klicka på sorteringspilen
# 6. Kontrollera att anteckningen är placerad över timern


@pytest.mark.timer
def test_move_note_above_timer(timer_app_page):

    # 1. Öppna en timer
    timer_app_page.get_by_role(
        "button", name="Add timer").click()

    # 3. Öppna en anteckning
    timer_app_page.get_by_role(
        "button", name="Add note").click()

    note_widget = timer_app_page.locator(".widget").filter(
        has=timer_app_page.get_by_role(
            "heading", name=re.compile("Click to change text")
        )
    )

    # 4. Kontrollera att anteckningen är placerad under timern
    previous_widget = note_widget.locator(
        "xpath=preceding-sibling::div[contains(@class, 'widget')][1]"
    )

    expect(previous_widget).to_have_count(1)

    expect(
        previous_widget.get_by_role(
            "heading", name=re.compile("Break"))).to_be_visible()

    # 5. Kontrollera att anteckningen har en sorteringspil
    up_button = note_widget.locator(".icon.up")

    expect(up_button).to_be_visible()

    # 6. Klicka på sorteringspilen
    up_button.click()

    # 7. Kontrollera att anteckningen är placerad över timern
    next_widget = note_widget.locator(
        "xpath=following-sibling::div[contains(@class, 'widget')][1]"
    )

    expect(next_widget).to_have_count(1)

    expect(
        next_widget.get_by_role(
            "heading", name=re.compile("Break")
        )
    ).to_be_visible()

    # ------------------------------------------------------------------------
    # User story 7 - Ändra värde på timern
    # ------------------------------------------------------------------------
    # Som besökare vill jag kunna ändra tiden på timern,
    # så att jag kan ange längden på en rast.

    # Acceptanskriteria
    # AK1: När timern är öppen ska det finnas en knapp för inställningar
    # 1. Knappen för att öppna inställningar ska finnas
    # AK2: När jag klickar på knappen för inställningar ska
    # inställningsfönstret för timern öppnas
    # 1. Inställningarna för timern ska öppnas
    # AK3: Det ska finnas en textruta där man kan skriva in en ny tid
    # 1. Det ska finnas en textruta
    # 2. Det ska gå att skriva in en ny tid i textrutan
    # AK4: Det ska finnas en knapp som återställer tiden på timern
    # 1. Det ska finnas en knapp för återställninbg av timern
    # AK5: När jag klickar på knappen för att återställa timern ska den
    # visa angivet värde
    # 1. Det angivna värdet ska visas

    # Scenario
    # 1. Ladda sidan
    # 2. Öppna en timer
    # 3. Kontrollera att det finns en ikon för inställningar
    # 4. Klicka på ikonen för inställningar
    # 5. Kontrollera att inställningarna för timern visas
    # 6. Kontrollera att det finns en textruta för inmatning av tid
    # 7. Skriv in en ny tid i textfältet
    # 8. Kontrollera att det finns en knapp för att återställa timern
    # 9. Klicka på knappen för att återställa timern
    # 10. Kontrollera att timern fått det nya värdet


@pytest.mark.timer
def test_change_timer_value(timer_app_page):

    # 1. Öppna en timer
    timer_app_page.get_by_role(
        "button", name="Add timer").click()

    # 2. Kontrollera att det finns en knapp för inställningar
    expect(timer_app_page.get_by_text("⚙️️")).to_be_visible()

    # 3. Klicka på ikonen för inställningar
    timer_app_page.get_by_text("⚙️️").click()

    # 4. Kontrollera att inställningarna för timern visas
    expect(timer_app_page.locator(".settings-menu")).to_be_visible()

    # 5. Kontrollera att det finns en textruta för inmatning av tid
    time_input = timer_app_page.get_by_role("textbox")

    expect(time_input).to_be_visible()

    # 6. Skriv in en ny tid i textfältet
    time_input.fill("10:00")

    # 7. Kontrollera att det finns en knapp för att återställa timer

    reset_button = timer_app_page.get_by_role(
        "button", name=re.compile("Reset"))

    expect(reset_button).to_be_visible()

    # 8. Klicka på knappen för att återställa timern
    reset_button.click()

    # 9. Kontrollera att timern fått det nya värdet
    expect(time_input).to_have_value("10:00")

    # ------------------------------------------------------------------------
    # User story 7 - Ändra texten för anteckning
    # ------------------------------------------------------------------------
    # Som besökare vill jag kunna ändra texten på en anteckning,
    # så att den visar korrekt information.

    # Acceptanskriteria
    # AK1: När en anteckning är skapad ska man kunna klicka på texten
    # för att markera den
    # 1. Texten ska markeras för ändring då man klickar på den
    # AK2: Om jag ändrar texten och trycker enter ska den nya texten
    # ersätta den ursprungliga
    # 1. Den nya texten ska ersätta den gamla då man trycker enter

    # Scenario
    # 1. Ladda sidan
    # 2. Öppna en anteckning
    # 3. Kontrollera att "Click to change text" visas
    # 4. Klicka på "Click to change text"
    # 5. Kontrollera att texten ändras för inmatning
    # 6. Skriv in en ny text
    # 7. Tryck enter
    # 8. Kontrollera att den nya texten ersatt den gamla


@pytest.mark.timer
def test_change_note_text(timer_app_page):
    # 1. Öppna en anteckning
    timer_app_page.get_by_role(
        "button", name="Add note").click()

    # 2. Kontrollera att "Click to change text" visas
    note_text = timer_app_page.get_by_role(
        "heading", name=re.compile("Click to change text"))

    expect(note_text).to_be_visible()

    # 3. Klicka på "Click to change text"
    note_text.click()

    # 4. Kontrollera att texten ändras för inmatning
    expect(note_text).not_to_be_visible()

    # 5. Skriv in en ny text i textboxen
    text_box = timer_app_page.get_by_role("textbox")

    expect(text_box).to_be_visible()

    text_box.fill("Dagens första rast")

    # 6. Tryck enter
    text_box.press("Enter")

    # 7. Kontrollera att den nya texten ersatt den gamla
    new_note_text = timer_app_page.get_by_role(
        "heading", name="Dagens första rast"
    )

    expect(new_note_text).to_be_visible()

    # ------------------------------------------------------------------------
    # User story 8 - Ändra temafärg
    # ------------------------------------------------------------------------
    # Som besökare vill jag kunna ändra tema på sidan,
    # så att jag kan variera utseendet.

    # Acceptanskriteria
    # AK1: När jag öppnar sidan ska knappar för att ändra tema visas
    # 1. Kontrollera att det finns en Knapp med texten "Dark"
    # AK2: Om jag klickar på knappen ska sidans tema ändras till mörkt tema
    # 1. Sidans tema skall ändras till mörkt

    # Scenario
    # 1. Ladda sidan
    # 1. Kontrollera att "Light" theme är valt
    # 2. Kontrollera att det finns en Knapp med texten "Dark"
    # 3. Klicka på knappen med texten "Dark"
    # 4. Kontrollera att sidans tema ändrades till Dark


@pytest.mark.timer
def test_change_from_light_to_dark_theme(timer_app_page):
    # 1. Säkerställ att sidans tema är "Light"
    light_button = timer_app_page.get_by_role(
        "button", name="Light")

    if not re.search(r"\bselected\b", light_button.get_attribute("class")):
        light_button.click()

    # 2. Kontrollera att "Light" är det valda temat
    expect(light_button).to_have_class(
        re.compile(r"\bselected\b")
    )

    # 3. Kontrollera att det finns en Knapp med texten "Dark"
    dark_button = timer_app_page.get_by_role(
        "button", name="Dark")

    expect(dark_button).to_be_visible()

    # 4. Kontrollera att "Dark" inte är ett valt tema
    expect(dark_button).not_to_have_class(
        re.compile(r"\bselected\b")
    )

    # 5. Klicka på knappen med texten "Dark"
    dark_button.click()

    # 6. Kontrollera att sidans tema ändrades från Light till Dark
    expect(dark_button).to_have_class(
        re.compile(r"\bselected\b"))

    expect(light_button).not_to_have_class(
        re.compile(r"\bselected\b")
    )
