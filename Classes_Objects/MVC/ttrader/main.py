import models
import controller
# initially load the saved data
models.load()
# start the logon_loop to get everything working
controller.logon_loop()
