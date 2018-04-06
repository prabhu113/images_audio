import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
EYE_COLOR = GREEN
CAT_COLOR_1 = BLACK
CAT_COLOR_2 = (25, 25, 25)
MOUTH_COLOR = (91, 73, 73)
INSIDE_EAR = (80, 48, 99)#(91, 73, 73)
WHISKER_COLOR = (91, 73, 73)
NOSE = (111, 53, 147)
eyesOpen = False
savedScale = 1
savedCatScale = 1


#variables
def draw_cat(screen,x, y, scale,tick):
    global eyesOpen
    global savedScale
    if tick == 60:eyesOpen = not eyesOpen
    if tick == 10:eyesOpen = True
    if savedScale != scale:
        savedScale = scale
    headSize = 20*scale
    halfHead = headSize/2
    thirdHead = headSize/3
    earOffset = 3*scale
    pupleOffset = 2*scale

    pi = 3.14159
    # body
    pygame.draw.ellipse(screen, CAT_COLOR_2,
                        [x - headSize - thirdHead, y + thirdHead, (headSize + thirdHead) * 2,
                         headSize * 2], 0)
    pygame.draw.ellipse(screen, CAT_COLOR_1,[x - headSize, y + (headSize * 2),thirdHead*2,halfHead], 0)
    pygame.draw.ellipse(screen, CAT_COLOR_1,
                        [x + headSize- (thirdHead * 2), y + (headSize * 2), thirdHead * 2, halfHead], 0)
    pygame.draw.line(screen, CAT_COLOR_1,[x - headSize+thirdHead/2, y + (headSize * 2)],[(x - headSize+thirdHead/2)-thirdHead/2, y +headSize+thirdHead],scale)
    pygame.draw.line(screen, CAT_COLOR_1, [x + headSize - thirdHead / 2, y + (headSize * 2)],
                     [(x + headSize + thirdHead / 2) - thirdHead / 2, y + headSize + thirdHead], scale)

    #leftEar
    pygame.draw.polygon(screen,CAT_COLOR_1 ,[[x-(halfHead),y-(headSize*2)],[x-headSize,y],[x,y]],0)
    pygame.draw.polygon(screen, INSIDE_EAR, [[x - (halfHead), y - (headSize * 2)+earOffset], [x - headSize+earOffset, y-earOffset], [x-earOffset, y-earOffset]], 0)
    pygame.draw.polygon(screen,CAT_COLOR_1 ,[[x-(halfHead),y-headSize],[x-headSize,y],[x,y]],0)
    #rightEar
    pygame.draw.polygon(screen, CAT_COLOR_1 , [[x + (halfHead), y - (headSize * 2)], [x + headSize, y], [x, y]], 0)
    pygame.draw.polygon(screen, INSIDE_EAR, [[x + (halfHead), y - (headSize * 2)+earOffset], [x + headSize-earOffset, y-earOffset], [x+earOffset, y-earOffset]], 0)
    pygame.draw.polygon(screen, CAT_COLOR_1 ,[[x+(halfHead),y-headSize],[x+headSize,y],[x,y]],0)
    #head
    pygame.draw.circle(screen,CAT_COLOR_1 ,(x,y),headSize,0)

    if eyesOpen:
        #leftEye
        pygame.draw.ellipse(screen,EYE_COLOR,[x-(thirdHead*2),y-(thirdHead*2),halfHead,headSize-(thirdHead)],0)
        pygame.draw.ellipse(screen,BLACK,[x-(thirdHead*2)+pupleOffset,y-(thirdHead*2),halfHead-pupleOffset*2,headSize-(thirdHead)],0)
        #rightEye
        pygame.draw.ellipse(screen,EYE_COLOR,[x+(headSize/6),y-(thirdHead*2),halfHead,headSize-(thirdHead)],0)
        pygame.draw.ellipse(screen,BLACK,
                            [x + (headSize / 6)+pupleOffset, y - (thirdHead * 2), halfHead-pupleOffset*2, headSize - (thirdHead)], 0)

    #nose
    pygame.draw.polygon(screen,NOSE,[[x,y+thirdHead],[x-thirdHead/2,y],[x+thirdHead/2,y]],0)
    #mouth
    pygame.draw.arc(screen, MOUTH_COLOR, [x,y,halfHead,halfHead],3*pi/2,2*pi,scale)
    pygame.draw.arc(screen, MOUTH_COLOR, [x, y, halfHead, halfHead], pi, 3 * pi/2, scale)
    pygame.draw.arc(screen, MOUTH_COLOR, [x-halfHead, y, halfHead, halfHead], 3 * pi / 2, 2 * pi, scale)
    pygame.draw.arc(screen, MOUTH_COLOR, [x-halfHead, y, halfHead, halfHead], pi, 3 * pi / 2, scale)
    #wiskers Left
    pygame.draw.line(screen, WHISKER_COLOR,[x-thirdHead,y+thirdHead/2],[x-headSize-thirdHead,y-headSize/5],scale)
    pygame.draw.line(screen, WHISKER_COLOR, [x - thirdHead, y + 1+ thirdHead / 2],
                     [x - headSize - thirdHead, y+1 + thirdHead / 2], scale)
    pygame.draw.line(screen, WHISKER_COLOR, [x - thirdHead, y+2 + thirdHead / 2],
                     [x - headSize - thirdHead, y+2 + thirdHead + headSize / 5], scale)
    #wiskers Right
    pygame.draw.line(screen, WHISKER_COLOR,[x+thirdHead,y+thirdHead/2],[x+headSize+thirdHead,y-headSize/5],scale)
    pygame.draw.line(screen, WHISKER_COLOR, [x+thirdHead,y+1+thirdHead/2], [x+headSize+thirdHead,y+1+thirdHead/2], scale)
    pygame.draw.line(screen, WHISKER_COLOR, [x+thirdHead,y+2+thirdHead/2], [x+headSize+thirdHead,y+2+thirdHead+headSize/5], scale)
