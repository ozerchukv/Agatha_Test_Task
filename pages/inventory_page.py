from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def add_item_to_cart(self):
        """Click the 'Add to cart' button for the first item."""
        self.driver.find_element(*self.add_to_cart_button).click()

    def go_to_cart(self):
        """Click on the shopping cart icon to navigate to the cart page."""
        self.driver.find_element(*self.cart_link).click()

    def logout(self):
        """Open the menu and click 'Logout'."""
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.logout_link).click()
