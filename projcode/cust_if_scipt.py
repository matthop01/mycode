#!usr/bin/env python3


#Premier league teams and their names
#bonus for ManU
failmessage = 'Try again'
partialmessage = 'Yes, but not the best team. '
message = 'Correct'
message2 = ' Glory, Glory, Man United. Go Red Devils'
citymessage = 'Whatever.'
#while True: EPLTeam.lower() != {PremierLeague}
EPLTeam = input("Name the current teams in the English Premier League ........ ")
PremierLeague = {"Manchester United", "Wolverhampton","Arsenal","Liverpool","Chelsea",
"Tottenham","Everton","Southampton","Brighton","Aston Villa","Bournemouth","Burnley","Newcastle","Norwich", "Sheffield", "Watford", "Leicester", "Crystal Palace", "West Ham","Manchester City"}
if EPLTeam.lower() == ('manchester united'):
    message = message + message2
elif EPLTeam.lower() == ('man united'):
    message = message + message2
elif EPLTeam.lower() == ('manu'):
    message = message + message2
elif EPLTeam.lower() == (PremierLeague):
    message = partialmessage + ' . Nice try but try again'
elif EPLTeam.lower() == ('wolverhampton'):
    message = partialmessage + ' Try again'
elif EPLTeam.lower() == ('arsenal'):
    message = partialmessage + ' Not Champions League either. Try again'
elif EPLTeam.lower() == ('liverpool'):
    message = partialmessage + ' You walk alone!!!! Try again'
elif EPLTeam.lower() == ('manchester city'):
    message = citymessage + ' There is no need for that language. Goodbye!'
else:
    message = failmessage
    
print(message)
