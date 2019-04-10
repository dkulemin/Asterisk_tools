with open('output.txt', 'w') as fin:
    for i in range(597760, 597800):
        print('        %s=> {' % i, file=fin)
        print('                if(${BLACKLIST()} = 1) {Hangup();}', file=fin)
        print('                NoCDR();', file=fin)
        print('                Playback(cannot-complete-as-dialed);', file=fin)
        print('                Playback(check-number-dial-again);', file=fin)
        print('                Hangup();', file=fin)
        print('        };', file=fin)
