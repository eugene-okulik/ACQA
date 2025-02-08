sort_by_dropdown_loc = "//select[@id='sorter']"
desc_sorting_btn_loc = "//a[@title='Set Descending Direction']"
asc_sorting_btn_loc = "//a[@title='Set Ascending Direction']"
clothes_price_loc = "//span[contains(@id, 'product-price-')]"

last_clothe_on_page_loc = "//ol[contains(@class, 'products')]/li[12]"
last_clothe_xs_size_loc = "//li[@class='item product product-item'][12]/descendant::div[text()='XS']"
last_clothe_first_color_loc = (
    "//li[@class='item product product-item'][12]/descendant::div[@class='swatch-option color'][1]"
)
add_to_cart_btn_loc = "//li[@class='item product product-item'][12]/descendant::button[@title='Add to Cart']"

last_clothe_name_loc = "//li[@class='item product product-item'][12]/descendant::a[@class='product-item-link']"
add_success_message_loc = "//div[@data-ui-id='message-success']/div"

my_cart_loc = "//a[@class='action showcart']"
cart_counter_parent_loc = "//a[@class='action showcart']/span[contains(@class,'counter')]"
cart_counter_child_loc = "//span[@class='counter-number']"
remove_btn_loc = "//a[@title='Remove item']"
confirm_modal_loc = "//button[contains(@class, 'action-accept')]"
empty_cart_block_loc = "//div[@id='ui-id-1']"
empty_cart_text_loc = "//div[@id='ui-id-1']/descendant::strong[@class='subtitle empty']"
