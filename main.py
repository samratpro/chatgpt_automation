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
    page.locator("//input[@id='username']").first.fill(chatgpt_email)
    page.locator("//button[normalize-space()='Continue']").click()
    sleep(1)
    page.wait_for_selector("//input[@id='password']")
    page.locator("//input[@id='password']").first.fill(chatgpt_pass)
    sleep(1)
    page.locator("//button[normalize-space()='Continue']").click()
    page.wait_for_load_state('load')
    sleep(1)

    def text_generator(prompt):
        # Each time it will take new chat
        try:
            page.locator(
                "//div[@class='relative flex h-full max-w-full flex-1 flex-col overflow-hidden']//span[1]//button[1]").click()
        except:
            pass
        try:
            page.locator("//nav[@aria-label='Chat history']/div[2]/div[1]//a").click()
            sleep(2)
        except:
            pass
        page.locator("//textarea[@id='prompt-textarea']").first.fill(prompt)
        page.locator("""button[class='mb-1 mr-1 flex h-8 w-8 items-center justify-center rounded-full bg-black text-white transition-colors hover:opacity-70 focus-visible:outline-none focus-visible:outline-black disabled:bg-[#D7D7D7] disabled:text-[#f4f4f4] disabled:hover:opacity-100 dark:bg-white dark:text-black dark:focus-visible:outline-white disabled:dark:bg-token-text-quaternary dark:disabled:text-token-main-surface-secondary']""").click()
        sleep(10)
        replay = page.locator("//div[@data-message-author-role='assistant']").first.inner_text()
        return replay
    
    
    
    
        
        
    
