from gologin import GoLogin
from playwright.sync_api import sync_playwright
from time import sleep


chatgpt_email = "chatgpt_email"
chatgpt_pass = "chatgpt_pass"

# All function will be place this indentation, to keep open chatgpt browser
with sync_playwright() as p:
    gl = GoLogin({
        "token": "gologinapitoken",
        "profile_id": "profile_id",
        # "extra_params":["--headless"]
    })

    debugger_address = gl.start()
    browser = p.chromium.connect_over_cdp("http://" + debugger_address)
    default_context = browser.contexts[0]
    page = default_context.pages[0]
    page.goto(
        'https://chatgpt.com/auth/login?sso=&oai-dm=1',
            timeout=60000)  # 1 min
    page.wait_for_load_state('load')
    sleep(1)
    page.locator("//button[@data-testid='login-button']").click()
    page.wait_for_load_state('load')
    page.locator('#username').first.fill(chatgpt_email)
    page.locator("//button[normalize-space()='Continue']").click()
    sleep(1)
    page.wait_for_selector("#password")
    page.locator('#password').first.fill(chatgpt_pass)
    sleep(1)
    page.locator("//button[normalize-space()='Continue']").click()
    sleep(4)

    def text_generator(prompt):
        # Each time it will take new chat
        try:
            page.locator("//div[@class='pb-0.5 last:pb-0']//a").click()
            sleep(2)
        except:
            pass
        page.locator("#prompt-textarea").first.fill(prompt)
        page.locator("""//form[@class='w-full']//button""").click()
        sleep(10)
        replay = page.locator("//div[@data-message-author-role='assistant']").first.inner_text()
        return replay
    
    
    
    
        
        
    
