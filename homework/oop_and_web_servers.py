# create a web server which can keep a list of games, films, tv shows & books
# GET /games returns the list of games, GET /films returns the list of films and so on
# POST /games creates a game, ...
# PUT /games/<name> can update the progress of the specified game, ...
# DELETE /games/<name> removes the game from the list which has the <name>, ...
# GET /games/progress returns the name & the progress in percent

# Create classes for these 4 types of data
# games have a name, studio, hours to finish, hours played
# films have a name, studio, length in minutes, minutes watched
# tv shows have a name, studio, number of episodes, number of episodes watched
# books have a name, author, number of pages, number of pages read
