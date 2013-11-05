#!/usr/bin/python
# Lyrics of the song 99 Bottles of Beer

print "\nLyrics of the song 99 Bottles of Beer\n\n"

for i in range(1,100):

	if i == 99:
		print "%d bottle of beer on the wall, %d bottle of beer." %((100-i),(100-i))
		print "Take one down and pass it around, no more bottles of beer on the wall.\n"
		break

	print "%d bottles of beer on the wall, %d bottles of beer." %((100-i),(100-i))
	print "Take one down and pass it around, %d bottles of beer on the wall.\n" %(100-i-1)


print "No more bottles of beer on the wall, no more bottles of beer."
print "Go to the store and buy some more, %d bottles of beer on the wall.\n" %i