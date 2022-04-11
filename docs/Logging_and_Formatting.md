**Logging**
Logs are used for tracking what our application is doing and what errors it encounters. We can come at a later date & inspect problems so we can solve bugs.

```
import logging # logging is the python module used for logs

# we can configure multiple sutff, one is in which file to log (or files)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

# there are 5 levels of logging debug, info, warning, error & critical
logging.debug("Detailed message intented mostly for developers")
logging.info("General info about what action we are currently starting/finishing")
logging.warning("Some problem was encountered, but we were able to finish the task")
logging.error("Failed to do an action, maybe failed to add a new user")
logging.critical("Something bad happened, our whole app may stop")
```

**More info**
https://docs.python.org/3/howto/logging.html
https://realpython.com/python-logging/


**Formatting**
TODO
