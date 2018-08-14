'''
cheating way is
def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())

but i wanted to write pure code, without any pythonic cheating things
like in pure c
'''

def song_decoder(song):
    # of course i can use search and replace
    # but i want to implement my own stupid parser

    keyword = "WUB"
    original_string = list(song)
    i = 0

    while i < len(original_string):
        if i < len(keyword) - 1:
            i += 1
            continue

        # I want to use the same cycle twice
        # just because i can

        match = True
        replace = False
        j = 0

        while j < len(keyword):

            # match searching part
            if keyword[-j - 1] != original_string[i - j] and not replace:
                match = False
                break
            elif keyword[-j - 1] == original_string[i - j] and j == (len(keyword) - 1) and not replace:
                j = 0
                replace = True
                continue

            if replace:
                if j == (len(keyword) - 1):

                    if i != 0 and original_string[i - 1] == ' ':
                        del (original_string[i - 1])
                        i -= 1

                    if i == len(original_string) - 1:
                        # if its end - delete it
                        del (original_string[i])
                    elif i == 0:
                        # if its beginning - delete it
                        del (original_string[i])
                        i -= 1
                    else:
                        original_string[i] = ' '


                else:
                    del (original_string[i])
                    i -= 1

            j += 1

        i += 1

    return ''.join(original_string)