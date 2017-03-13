import dota2api
import threading
import signal
import sys
i = input("Enter your API key")
api = dota2api.Initialise(i)
def GetScore1():
	games_list = api.get_top_live_games()['game_list'][0]
	print("timer :",games_list['last_update_time'],"s")
	print (games_list['team_name_radiant'] , ":", games_list['radiant_score'])
	print (games_list['team_name_dire'] , ":" , games_list['dire_score'])
	print (games_list['team_name_radiant'] , "lead by", games_list['radiant_lead'])
	print("===================================================")
def GetScore2():
        try:    
            games_list = api.get_top_live_games()['game_list'][1]
            print("timer :",games_list['last_update_time'],"s") 
            print (games_list['team_name_radiant'] , ":" , games_list['radiant_score'])
            print (games_list['team_name_dire'] , ":" , games_list['dire_score'])
            print (games_list['team_name_radiant'] , "lead by", games_list['radiant_lead'])
            print("===================================================")
        except(KeyError,ValueError):
            print("cant access further matches")
        

def GetScore():
    GetScore1()
    GetScore2()
    threading.Timer(10,GetScore).start()

    
GetScore()

                

                
