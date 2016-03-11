# #1#	Taking arguments
# # from sys import argv
# 
# # script, first, second, third = argv
# 
# # print "The script is called:", script
# # print "Your first variable is:", first
# # print "Your second variable is:", second
# # print "Your third variable is:", third
# 
# #2#
# # from sys import argv
# # 
# # script, user_name = argv
# # prompt = '> '
# # 
# # print "Hi %s, I'm the %s script." % (user_name, script)
# # print "I'd like to ask you a few questions."
# # print "Do you like me %s?" % user_name
# # likes = raw_input(prompt)
# # 
# # print "Where do you live %s?" % user_name
# # lives = raw_input(prompt)
# # 
# # print "What kind of computer do you have?"
# # computer = raw_input(prompt)
# # 
# # print """
# # Alright, so you said %s about liking me.
# # You live in %s.  Not sure where that is.
# # And you have a %s computer.  Nice.
# # """ % (likes, lives, computer)
# 
# txt = open('object.txt', 'r+')
# 
# # print "Here's your file %r:" % filename
# print txt.read()
# print txt
# txt.truncate()
# a0 = 'This is a new line \n'
# a1 = 'This is a new line \n'
# a2 = 'This is a new line'
# 
# txt.write(a0)
# txt.write(a1)
# txt.write(a2)
# print txt.read()
# txt.close()


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()