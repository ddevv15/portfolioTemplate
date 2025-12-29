import asyncio
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None
    
    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()
        
        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",         # Set the browser window size
                "--disable-dev-shm-usage",        # Avoid using /dev/shm which can cause issues in containers
                "--ipc=host",                     # Use host-level IPC for better stability
                "--single-process"                # Run the browser in a single process mode
            ],
        )
        
        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        context.set_default_timeout(5000)
        
        # Open a new page in the browser context
        page = await context.new_page()
        
        # Navigate to your target URL and wait until the network request is committed
        await page.goto("http://localhost:3000", wait_until="commit", timeout=10000)
        
        # Wait for the main page to reach DOMContentLoaded state (optional for stability)
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=3000)
        except async_api.Error:
            pass
        
        # Iterate through all iframes and wait for them to load as well
        for frame in page.frames:
            try:
                await frame.wait_for_load_state("domcontentloaded", timeout=3000)
            except async_api.Error:
                pass
        
        # Interact with the page elements to simulate user flow
        # -> Check npm install logs for errors
        await page.goto('http://localhost:3000', timeout=10000)
        await asyncio.sleep(3)
        

        # -> Check npm install logs for errors
        await page.goto('http://localhost:3000/npm-install-logs', timeout=10000)
        await asyncio.sleep(3)
        

        # -> Return to root page and check for any visible error logs or messages on the main site or find alternative way to verify npm install and runtime errors
        await page.goto('http://localhost:3000', timeout=10000)
        await asyncio.sleep(3)
        

        # -> Click on navigation buttons 'Work' and 'Services' to check for runtime errors on page transitions
        frame = context.pages[-1]
        # Click on 'Work' button to test navigation and runtime errors
        elem = frame.locator('xpath=html/body/main/div[5]/section/div/div/button').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Click on 'Services' button to test navigation and check for runtime errors
        frame = context.pages[-1]
        # Click on 'Services' button to test navigation and runtime errors
        elem = frame.locator('xpath=html/body/main/div[5]/section/div/div/button[2]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Click on 'About' button to test navigation and check for runtime errors
        frame = context.pages[-1]
        # Click on 'About' button to test navigation and runtime errors
        elem = frame.locator('xpath=html/body/main/nav/div/button[4]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Click on 'Contact' button to test navigation and check for runtime errors
        frame = context.pages[-1]
        # Click on 'Contact' button to test navigation and runtime errors
        elem = frame.locator('xpath=html/body/main/nav/div/button[5]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # --> Assertions to verify final state
        frame = context.pages[-1]
        await expect(frame.locator('text=DB').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=DevBrows').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Home').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Work').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Services').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=About').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Contact').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Get Started').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Creative experiences in fluid motion').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Transforming digital spaces with dynamic shader effects and real-time visual experiences that captivate and inspire.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Recent explorations').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Kinetic Typography').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Interactive Experience').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Generative Patterns').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Visual System').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Spatial Interface').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=3D Navigation').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=What we bring to the table').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Creative Development').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Pushing the boundaries of what\'s possible on the web').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Visual Design').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Crafting memorable experiences through thoughtful aesthetics').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Motion & Animation').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Bringing interfaces to life with purposeful movement').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Technical Strategy').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Building scalable solutions that perform beautifully').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Building the').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=future of').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=digital').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=We\'re a collective of designers, developers, and creative technologists obsessed with crafting exceptional digital experiences.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Every project is an opportunity to explore new possibilities and push creative boundaries.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=150+ Projects Delivered worldwide').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=8 Years Of innovation').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=12 Awards Industry recognition').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Start a Project').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=View Our Work').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Let\'s talk').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Get in touch').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=hello@studio.com').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Chicago, IL').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Name').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Email').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Message').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Send Message').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=All rights reserved. Developed and Managed by DevBrows.').first).to_be_visible(timeout=30000)
        await asyncio.sleep(5)
    
    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()
            
asyncio.run(run_test())
    