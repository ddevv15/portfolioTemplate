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
        # -> Simulate device types (mobile and desktop) and verify use-mobile detects device correctly
        frame = context.pages[-1]
        # Click DevBrows button to check if it triggers any device detection or related UI for use-mobile hook testing
        elem = frame.locator('xpath=html/body/main/nav/button').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Simulate desktop device environment and verify use-mobile detection
        frame = context.pages[-1]
        # Click DevBrows button again or toggle to simulate desktop device environment for use-mobile hook testing
        elem = frame.locator('xpath=html/body/main/nav/button').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Scroll through the page to activate use-reveal hooks
        await page.mouse.wheel(0, await page.evaluate('() => window.innerHeight'))
        

        # -> Scroll further and observe if elements reveal smoothly on scroll as expected for use-reveal hook
        await page.mouse.wheel(0, await page.evaluate('() => window.innerHeight'))
        

        # --> Assertions to verify final state
        frame = context.pages[-1]
        await expect(frame.locator('text=Creative experiences in fluid motion').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Transforming digital spaces with dynamic shader effects and real-time visual experiences that captivate and inspire.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Recent explorations').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Kinetic Typography').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Generative Patterns').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Spatial Interface').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=What we bring to the table').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Pushing the boundaries of what\'s possible on the web').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Crafting memorable experiences through thoughtful aesthetics').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Bringing interfaces to life with purposeful movement').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Building scalable solutions that perform beautifully').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Building the future of digital').first).to_be_visible(timeout=30000)
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
        await expect(frame.locator('text=All rights reserved. Developed and Managed by DevBrows (https://devbrows.com).').first).to_be_visible(timeout=30000)
        await asyncio.sleep(5)
    
    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()
            
asyncio.run(run_test())
    