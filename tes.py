import Automate

app = Automate.Application()

result = app.Give_Fake_Data_toInput("email")
# options = app.Chrome_options()

# options.add_argument("--headless=new")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# app.Start_Driver(options=options)

# app.driver.set_window_size(1200, 900)

app.findThisTypesInputs(["text", "email"])
print(result)


