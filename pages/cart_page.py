from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")  # Selector for items in the cart
        self.remove_button = (By.XPATH, "//button[text()='Remove']")  # Button to remove item
        self.checkout_button = (By.ID, "checkout")  # Checkout button

    def is_item_in_cart(self):
        """Check if at least one item is present in the cart."""
        return len(self.driver.find_elements(*self.cart_items)) > 0

    def remove_item(self):
        """Click the 'Remove' button to remove an item from the cart."""
        self.driver.find_element(*self.remove_button).click()

    def proceed_to_checkout(self):
        """Click the 'Checkout' button to start the checkout process."""
        self.driver.find_element(*self.checkout_button).click()

    def is_checkout_page_displayed(self):
        """Verify that the checkout page has loaded successfully."""
        return "checkout-step-one.html" in self.driver.current_url
