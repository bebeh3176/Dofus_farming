from Divers import fonction_principal, Fct_script
import time

def findcolor(color,initial = (0,0),final = (1440,900), tol = 2, sauf = []):
    color = np.uint8([[[color[0],color[1],color[2] ]]])
    hsv_color = cv2.cvtColor(color,cv2.COLOR_RGB2HSV)

    lower_limit = np.array([hsv_color[0][0][0]-tol, hsv_color[0][0][1]-tol, hsv_color[0][0][2]-tol])
    upper_limit = np.array([hsv_color[0][0][0]+tol, hsv_color[0][0][1]+tol, hsv_color[0][0][2]+tol])

    frame = pyautogui.screenshot()
    hsv = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    height, width =  mask.shape
    zone_chercher = np.zeros((height,width,1), np.uint8)
    cv2.rectangle(zone_chercher,initial,final,(255),-1)
    for k in range(len(sauf)):
        cv2.rectangle(zone_chercher,(sauf[k][0],sauf[k][1]),(sauf[k][2],sauf[k][3]),(0),-1)

    res = cv2.bitwise_and(zone_chercher,zone_chercher, mask= mask)

    # if(len(sauf)):
    #     cv2.imshow('mask',mask)
    #     cv2.imshow('mask2',zone_chercher)

    # if(test):
        # affiche = cv2.rectangle(mask,initial,final,(200),-1)
        # for k in range(len(sauf)):
        #     cv2.rectangle(affiche,(sauf[k][1],sauf[k][0]),(sauf[k][3],sauf[k][2]),(100),-1)
        # cv2.imshow('mask',mask)
        # cv2.imshow('cherche',zone_chercher)
        # cv2.imshow('res',res)
        # k = cv2.waitKey()

    result1,result2 = np.where(res == 255)

    length = len(result1)
    if(length):
        return (result2[0],result1[0])
    return None



# while True:
#     # img = cv2.imread('Picture/{}.PNG'.format(','), 0)
#     # img =  img[0:9, 0:6]
#     # print(img.size)
#     # cv2.imshow('image',img)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()
#     # cv2.imwrite( ",.PNG", img );
#     print(fonction_principal.MAP_POS())
#     time.sleep(2)
