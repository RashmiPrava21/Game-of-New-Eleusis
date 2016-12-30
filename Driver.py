import os
import God
if __name__ == '__main__':
    path = os.path.join('.','players')
    dir_list = os.listdir( path )
    print len(dir_list)
    print dir_list
    for i in range(0, len(dir_list)):
        team_name = dir_list[i]
        player_path = os.path.join(path,team_name)
        if os.path.isdir(player_path) is False:
            continue
        player = __import__('players.'+team_name+'.player', None, None, ["Player"])
        player_instance = player.Player()
        god_instance = God.God.get_instance()
        god_instance.register_player(player_instance)
    god_instance = God.God.get_instance()
    god_instance.set_rule("if(equal(color(previous), B), equal(color(current), R), equal(color(current), B))")
    god_instance.play()
    print god_instance.get_scores()