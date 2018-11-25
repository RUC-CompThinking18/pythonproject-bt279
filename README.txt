My project is a bot that every 10 seconds will produce a mix of a video game title and something the video game industry has done to exploit
its employees. The code works with 3 functions: the bot() function, which grabs a random game from the igdb api and a random entry from my own
list of misconducts and plugs those into the mixer() which randomly places the misconduct into the game title, and finally the 
cant_stop_wont_stop() function which acts as a timer to keep calling the bot() function every 10 seconds. You simply run the program and it
will keep producing title mixes, until you kill the program.

The reason I decided to create this program was because I do believe it is an issue that should be addressed, especially with some of the 
recent stories that have come out about this topic. 1 of those stories is the recent shutting down of Telltale Game's studios leaving 
nearly 300 emplyees without jobs, severence pay, and only about a week of health care remaining. Another of these stories came from 
Rockstar Studios, where in an interview with some of higher ups in the studio about their upcoming game, said that their empolyees were working 
100 hour work weeks to meet deadlines. These are just some of many of the many things the games' industry has done to exploit its employees.
As someone who would like to begin working on game development as a career this is a topic I care about, as hearing these things make me 
second guess my ambitions, even though it is the industry that should change, not my ambitions.

I was fairly well versed in Python when creating this project so I didn't run into too many complications aside from using the api, as I had
never used one before. It took a decent amount of reading the documentation and looking up how things like "api keys" worked before I could
use it to fit my needs. After that it was basically just a matter of how I wanted to divide up the functions and what I could do with what 
I knew at the time. I started with the mixer() function as the only thing it would need was 2 strings and some basic string maniuplation that
I was familiar with, and wouldn't need the api stuff to make this function. Once I got the api stuff figured out I made the bot() function
and had it use the mixer() function I had created earlier. All that was left was to have the function run indefinetly rather than have to call
it for each title mix, so I made the cant_stop_wont_stop() function as a basic timer so the user wouldn't have to keep calling the function
to get new title mixes. Overall I was fairly comfortable with what I was programming, but I still learned something new in the case of the api
stuff I used in this project. 