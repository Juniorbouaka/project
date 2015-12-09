import vinepy, time
from random import randint as rd
from sys import stdout as title

vine = vinepy.API(username="tonmail@gmail.com", password="tonmotdepasse")
my_id = vine._user_id


user = vine.get_user(user_id=my_id)
title.write("\x1b]2;" + str(user.name) + "_" + str(user.id) + "\x07")


def ecrire(texte):
	global user
	txt = open("desktop/LogsVine/" + str(user.name) + "_" + str(user.id) + "logs.txt", "a")
	txt.write(texte + "\n")
	txt.close()


def follow_popular(channel_id = 1):
	global vine
	ecrire("Lancement du fm : " + time.strftime('%d/%m/%y %H:%M',time.localtime()))
	timeline = vine.get_channel_popular_timeline(channel_id = channel_id)
	p = timeline[1] # le premier post sur lequel fm
	i, page, erreur = 0, 1, False # nombre de personnes suivies
	while i<230 and not(erreur):
		likes = p.likes(page = page)
		for x in likes:
			if not(x.following) and x.userId != my_id: # si on ne le suit pas deja et que c'est pas nous
				try:
					vine.follow(user_id = x.userId) # on le follow
				except: # si on a trop follow !
					ecrire("Erreur : trop de follow, stop.")
					erreur = True
					break
				i += 1
		if not(likes.nextPage>0): # si il n'y a plus d'autres likes
			ecrire("Pas eu suffisamment de likes sur la publi.")
			break # on sort du while
		page += 1
	ecrire("Fin du fm : " + time.strftime('%d/%m/%y %H:%M',time.localtime()))
	ecrire("Nb de personnes suivies : " + str(i))
	ecrire("")
	return True

time.sleep(60*(rd(0,60)))
while True:
	follow_popular()
	time.sleep(3600+60*rd(0,5))
	
