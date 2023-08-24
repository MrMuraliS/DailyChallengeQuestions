from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create a WebDriver instance
driver = webdriver.Chrome(ChromeDriverManager().install())

# Get the initial window handles
initial_handles = driver.window_handles

# Open the browser window manually (by the user)

# Get the updated window handles after manual opening
updated_handles = driver.window_handles

# Find the new window handle by comparing handles
new_window_handle = None
for handle in updated_handles:
    if handle not in initial_handles:
        new_window_handle = handle
        break

# Use the new window handle as needed
if new_window_handle:
    driver.switch_to.window(new_window_handle)
    # Perform actions in the new window

# Close the WebDriver instance
driver.quit()
