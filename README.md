## 📊 Veckouppgift 8 E2E Fördjupning

## 1️⃣ Gruppövning

1. Skriv user stories som beskriver vad användaren ska kunna göra:  
- skapa och ta bort widgets - timer och anteckning
- byta plats på två widgets
- ändra tidsinställning på timer
- starta, pausa, återställ
- ändra texten för anteckning
- ändra temafärg

2. Formulera acceptanskriterier för alla user stories.  


3. Skriv ner testscenarier för varje acceptanskriterium. (Ett scenario kan täcka in flera acceptanskriterier.)


4. Implementera E2E-tester i Playwright för utvalda scenarier. Gör så många ni hinner med.

### Testfall
```
- test_timer_app_get_title
- test_timer_app_open_timer
- test_timer_app_delete_timer
- test_timer_app_open_note
- test_timer_app_delete_note
- test_move_note_above_timer
- test_change_timer_value
- test_change_note_text
- test_change_from_light_to_dark_theme
```
User stories, Acceptanskriterier och Testsceanrios finns i testfilen "test_timer_app.py"

En fixture används för att öppna och läsa in sidan Timer app som ett page objekt
```python
import pytest
from playwright.sync_api import Page

@pytest.fixture
def timer_app_page(page: Page):
    """Öppnar Timer app."""
    page.goto("https://lejonmanen.github.io/timer-vue/")
    return page
``` 

Run tests with:
### pytest -m timer -v   


## 2️⃣ Öva mera - om du hinner

### Testfall
```
- test_register_app_get_title
- test_register_app_get_header
- test_register_app_input_name
- test_register_app_input_birth_year
- test_register_app_incorrect_birth_year
- test_register_app_input_mail_address
- test_register_app_incorrect_mail_address
- test_register_app_input_password
- test_register_app_input_to_short_password
- test_register_app_submit_button_activation
```
User stories, Acceptanskriterier och Testsceanrios finns i testfilen "test_register_app.py"

En fixture används för att öppna och läsa in sidan Timer app som ett page objekt
```python
import pytest
from playwright.sync_api import Page

@pytest.fixture
def register_app_page(page: Page):
    """Öppnar register app."""
    page.goto("https://tap-ht24-testverktyg.github.io/form-demo/")
    return page
``` 

Run tests with:
### pytest -m register -v   