import Algorithmia
import requests
from bs4 import BeautifulSoup

input1 = "Like most cities in America, there are certain areas of Orlando which are more dangerous than others. Some areas travelers should be cautious of are: " +\
"Parramore District, area in downtown Orlando is a location where a lot of the area's homeless population congregates and crime rates are higher in this area. " +\
"Orange Blossom Trail, south of Sand Lake Road is known to be a a bit of an unofficial red light district. Drug and prostitution related crime is common here. Prostitution is not legal in Orlando, so you could spend a night in jail if you decide to indulge." +\
"Pine Hills, located around Silver Star Road and Pine Hills Road west of John Young Parkway. This is a lower income area that has struggled with high crime rates. The Greyhound bus station is in Pine Hills and is a place to use caution. " +\
"While it is unlikely that any one individual would experience serious crime in these areas, tourists stand out in these areas, and can unwittingly do things that can make them targets for criminal behavior, so it is sensible to stay away. " +\
"While crime in the Orlando area is not particularly high, with the annual tourists far outnumbering the regional population (~2million), a substantial amount of local crime ends up being directed at tourists. The most common crimes are theft of items from cars and hotels, so following common sense travel precautions are particularly important in an area like Orlando. " +\
"Never leave valuable items in your car unattended, get any purchased items to your hotel room as soon as possible. " +\
"Never leave small children unattended for any length of time, especially at a pool. Most hotel pools do not have lifeguards. " +\
"Hotel room invasions do occur, especially open-air hotel and motel rooms when the victim leaves their hotel room unlocked and not dead-bolted. When you are in a hotel room, always lock your doors behind you, even if you expect someone in a minute or two. " +\
"Pets are better off left with a friend or in a kennel. If you choose to bring your pet, note that most theme parks and hotels prohibit pets but may provide kennels for a fee. Also note above about interior temperatures in parked cars. " +\
"For truly the safest experience, consider staying on Disney-owned property. If this is not possible, the area of Lake Buena Vista would be a preferred location. In addition to its accessibility to attractions, it offers a much safer, less urbanized area for comfort. "

input = "Like most cities in America, there are certain areas of Orlando which are more dangerous than others. Some areas travelers should be cautious of are: " +\
"Parramore District, area in downtown Orlando is a location where a lot of the area's homeless population congregates and crime rates are higher in this area. " +\
"Orange Blossom Trail, south of Sand Lake Road is known to be a a bit of an unofficial red light district. Drug and prostitution related crime is common here. Prostitution is not legal in Orlando, so you could spend a night in jail if you decide to indulge. " +\
"Pine Hills, located around Silver Star Road and Pine Hills Road west of John Young Parkway. This is a lower income area that has struggled with high crime rates. The Greyhound bus station is in Pine Hills and is a place to use caution. " +\
"While it is unlikely that any one individual would experience serious crime in these areas, tourists stand out in these areas, and can unwittingly do things that can make them targets for criminal behavior, so it is sensible to stay away. " +\
"While crime in the Orlando area is not particularly high, with the annual tourists far outnumbering the regional population (~2million), a substantial amount of local crime ends up being directed at tourists. The most common crimes are theft of items from cars and hotels, so following common sense travel precautions are particularly important in an area like Orlando. " +\
"Never leave valuable items in your car unattended, get any purchased items to your hotel room as soon as possible. " +\
"Never leave small children unattended for any length of time, especially at a pool. Most hotel pools do not have lifeguards. " +\
"Hotel room invasions do occur, especially open-air hotel and motel rooms when the victim leaves their hotel room unlocked and not dead-bolted. When you are in a hotel room, always lock your doors behind you, even if you expect someone in a minute or two. " +\
"Pets are better off left with a friend or in a kennel. If you choose to bring your pet, note that most theme parks and hotels prohibit pets but may provide kennels for a fee. Also note above about interior temperatures in parked cars. " +\
"For truly the safest experience, consider staying on Disney-owned property. If this is not possible, the area of Lake Buena Vista would be a preferred location. In addition to its accessibility to attractions, it offers a much safer, less urbanized area for comfort."




# page = requests.get('http://wikitravel.org/en/Orlando').text
#
# soup = BeautifulSoup(page, 'html.parser')
# print(soup)


client = Algorithmia.client('clientkey')
algo = client.algo('nlp/Summarizer/0.1.3')
print(algo.pipe(input))
