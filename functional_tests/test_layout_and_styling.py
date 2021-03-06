from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She starts a new list and sees the input is nicely
        # centered there too
        inputbox = self.get_item_input_box()
        # inputbox.send_keys('testing')
        # inputbox.send_keys(Keys.ENTER)
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )
