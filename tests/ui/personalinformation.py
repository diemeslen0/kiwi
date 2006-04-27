from kiwi.ui.test.player import Player

player = Player(['examples/validation/personalinformation.py'])
app = player.get_app()

player.wait_for_window("Form")
app.Form.name.set_text("")
app.Form.name.set_text("J")
app.Form.name.set_text("Jo")
app.Form.name.set_text("Joh")
app.Form.name.set_text("Joha")
app.Form.name.set_text("Johan")
app.Form.age.set_text("")
app.Form.age.set_text("  ")
app.Form.age.set_text(" ")
app.Form.age.set_text("1 ")
app.Form.age.set_text("1")
app.Form.age.set_text("12")
app.Form.age.set_text("1")
app.Form.age.set_text("1 ")
app.Form.age.set_text(" ")
app.Form.age.set_text("  ")
app.Form.age.set_text(" ")
app.Form.age.set_text("9 ")
app.Form.age.set_text("9")
app.Form.age.set_text("99")
app.Form.GtkToggleButton.clicked()
app.Form.ProxyEntry.set_text("")
app.Form.ProxyEntry.set_text("  /  /    ")
app.Form.ProxyEntry.set_text(" /  /    ")
app.Form.ProxyEntry.set_text("/  /    ")
app.Form.ProxyEntry.set_text("  /    ")
app.Form.ProxyEntry.set_text(" /    ")
app.Form.ProxyEntry.set_text("/    ")
app.Form.ProxyEntry.set_text("    ")
app.Form.ProxyEntry.set_text("   ")
app.Form.ProxyEntry.set_text("  ")
app.Form.ProxyEntry.set_text(" ")
app.Form.ProxyEntry.set_text("")
app.Form.ProxyEntry.set_text("02/14/1969")
app.Form.GtkToggleButton.clicked()
app.Form.ProxyEntry.set_text("")
app.Form.ProxyEntry.set_text("  /  /    ")
app.Form.ProxyEntry.set_text(" /  /    ")
app.Form.ProxyEntry.set_text("/  /    ")
app.Form.ProxyEntry.set_text("  /    ")
app.Form.ProxyEntry.set_text(" /    ")
app.Form.ProxyEntry.set_text("/    ")
app.Form.ProxyEntry.set_text("    ")
app.Form.ProxyEntry.set_text("   ")
app.Form.ProxyEntry.set_text("  ")
app.Form.ProxyEntry.set_text(" ")
app.Form.ProxyEntry.set_text("")
app.Form.ProxyEntry.set_text("02/13/1969")
app.Form.height.set_text("")
app.Form.height.set_text("1")
app.Form.height.set_text("12")
app.Form.height.set_text("123")
app.Form.height.set_text("1234")
app.Form.height.set_text("12345")
app.Form.weight.set_text("")
app.Form.weight.set_text("87")
app.Form.weight.set_text("")
app.Form.weight.set_text("88")
app.Form.weight.set_text("")
app.Form.weight.set_text("89")
app.Form.weight.set_text("")
app.Form.weight.set_text("90")
app.Form.weight.set_text("")
app.Form.weight.set_text("91")
app.Form.weight.set_text("")
app.Form.weight.set_text("92")
app.Form.weight.set_text("")
app.Form.weight.set_text("93")
app.Form.weight.set_text("")
app.Form.weight.set_text("92")
app.Form.weight.set_text("")
app.Form.weight.set_text("91")
app.Form.weight.set_text("")
app.Form.weight.set_text("90")
app.Form.weight.set_text("")
app.Form.weight.set_text("89")
app.Form.weight.set_text("")
app.Form.weight.set_text("90")
app.Form.height.set_text("")
app.Form.height.set_text("1")
app.Form.height.set_text("12")
app.Form.age.set_text("")
app.Form.age.set_text("  ")
app.Form.age.set_text(" ")
app.Form.age.set_text("1 ")
app.Form.age.set_text("1")
app.Form.age.set_text("12")
app.Form.GtkToggleButton.clicked()
app.Form.ProxyEntry.set_text("")
app.Form.ProxyEntry.set_text("Brazilian")
app.Form.GtkToggleButton.clicked()
app.Form.ProxyEntry.set_text("")
app.Form.ProxyEntry.set_text("Yankee")
app.Form.ProxyEntry.set_text("")
app.Form.ProxyEntry.set_text("Other")
app.Form.ProxyEntry.set_text("")
app.Form.ProxyEntry.set_text("Yankee")
app.Form.ProxyEntry.set_text("")
app.Form.ProxyEntry.set_text("Brazilian")
app.Form.ProxyEntry.set_text("")
app.Form.ProxyEntry.set_text("Yankee")
app.Form.gender.select_item_by_label("Male")
app.Form.gender.select_item_by_label("Female")
app.Form.status_single.clicked()
app.Form.status.clicked()
app.Form.status.clicked()
app.Form.status_single.clicked()
app.Form.ok_btn.clicked()
player.finish()
