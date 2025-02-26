from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_to_cart(login):
    """Log in, add an item to the cart, and verify it was added."""
    inventory_page = InventoryPage(login)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(login)
    assert cart_page.is_item_in_cart(), "Item was not added to the cart."


def test_remove_from_cart(login):
    """Add an item to the cart, remove it, and verify the cart is empty."""
    inventory_page = InventoryPage(login)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(login)
    cart_page.remove_item()
    assert not cart_page.is_item_in_cart(), "Item was not removed from the cart."


def test_proceed_to_checkout(login):
    """Add an item to the cart, navigate to checkout, and verify checkout page is displayed."""
    inventory_page = InventoryPage(login)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(login)
    cart_page.proceed_to_checkout()

    assert cart_page.is_checkout_page_displayed(), "Checkout page was not displayed."


def test_logout(login):
    """Log out of the application and verify the user is redirected to the login page."""
    inventory_page = InventoryPage(login)
    inventory_page.logout()

    assert "saucedemo.com" in login.current_url, "Logout failed."
