'''
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to n at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if n=8 and person 5 bribes person 4, the queue will look like this: 1,2,3,5,4,6,7,8.

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state. If anyone has bribed more than two people, the line is too chaotic to compute the answer.

Print the minimum number of bribes necessary ot "Too chaotic" if someone has bribed mroe than 2 people
'''

def minimumBribes(q):
    moves = 0
    for pos, val in enumerate(q):
        # Note: enumerate starts from 0
        if (val-1)-pos > 2:
            print('Too chaotic')
            return
        # checking backwards. (so that we dont have to handle out of index prob)
        # from 2 steps back to current position. 
        # if val is > than val in current pos, moves += 1 
        for j in range(max(0,val-2), pos):
            if q[j] > val:
                moves+=1
    print(moves)

if __name__ == '__main__':
    q=[1,2,3,6,4,5]
    minimumBribes(q)
