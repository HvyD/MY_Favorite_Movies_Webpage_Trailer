import fresh_tomatoes
import media

hot_tub_time_machine = media.Movie("Hot Tub Time Machine",
                                   "A group of friends go back to an 80's party via a Time Machine thats a Hot Tub",
                                   "https://upload.wikimedia.org/wikipedia/en/6/64/Hot_tub_time_machine_poster.jpg",
                                   "https://www.youtube.com/watch?v=_TXNEE6SaoI" )

#print(hot_tub_time_machine.storyline)                  

apocalypse_now_redux = media.Movie("Apocalypse Now Redux",
                                   "Follow Captain Willard through Vietnam to exterminate Colonel Walter E. Kurtzs",
                                   "https://upload.wikimedia.org/wikipedia/en/e/ec/Apocalypse_Now_Redux.jpg",
                                   "http://www.youtube.com/watch?v=CxENJ2LwecY")
            
#print(apocalypse_now_redux.storyline)
big_trouble_in_little_china = media.Movie("Big Trouble in Little China",
                     			  "Truck driver and Bad Ass Jack Burton goes on an adventure to save his friends girl and his truck",
                    			  "https://upload.wikimedia.org/wikipedia/en/7/76/Big_Trouble_in_Little_China_Film_Poster.jpg",
                    			  "https://www.youtube.com/watch?v=1P0A8pS1JF8")
#print(big_trouble_in_little_china.storyline)
school_of_rock = media.Movie("School of Rock",
                             "A rocker uses music to teach children",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "http://www.youtube.com/watch?v=3PsUJFEBC74")
#print(school_of_rock.storyline)
the_goonies = media.Movie("The Goonies",
                          "A group of kids find a treasure map in an attic and go out on an adventure to find the treasure to save there homes",
                          "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Goonies.jpg",
                          "http://www.youtube.com/watch?v=hJ2j4oWdQtU")
#print(the_goonies.storyline)
hitchhikers_guide_to_the_galaxy = media.Movie("The Hitchhikers Guide to the Galaxy",
                          "A human travels around the universe with alien friend after earth is destroyed for a Bi-way",
                          "https://upload.wikimedia.org/wikipedia/en/7/7a/Hitchhikers_guide_to_the_galaxy.jpg",
                          "http://www.youtube.com/watch?v=MbGNcoB2Y4I")
#print(hitchhikers_guide_to_the_galaxy.storyline)

movies = (hot_tub_time_machine, apocalypse_now_redux, big_trouble_in_little_china, school_of_rock, the_goonies, hitchhikers_guide_to_the_galaxy)
fresh_tomatoes.open_movies_page (movies)





