import pytest
import screenTracker as scrtr
import dataPoints as dp

# virtual tracking screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# region of interest inside the virtual screen
ROI_WIDTH = 50
ROI_HEIGHT = 50

# size of real display
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 1800

####################### screen 2 display Tests #################################

def test_screen2display_1_1():
    point = (1,1)

    roi = dp.ScreenROI(0,0,ROI_WIDTH,ROI_HEIGHT)
    display = dp.Display(DISPLAY_WIDTH,DISPLAY_HEIGHT,0,0)

    tracker = scrtr.Screen()
    p = tracker.screen2display(point,roi,display)
    
    assert p == (point[0]/ROI_WIDTH * DISPLAY_WIDTH,
                 point[1]/ROI_HEIGHT * DISPLAY_HEIGHT)

def test_screen2display_55_1():
    point = (55,1)

    roi = dp.ScreenROI(0,0,ROI_WIDTH,ROI_HEIGHT)
    display = dp.Display(DISPLAY_WIDTH,DISPLAY_HEIGHT,0,0)

    tracker = scrtr.Screen()
    p = tracker.screen2display(point,roi,display)
    
    assert p == (DISPLAY_WIDTH, 
                 point[1]/ROI_HEIGHT * DISPLAY_HEIGHT)

def test_screen2display_55_55():
    point = (55,55)

    roi = dp.ScreenROI(0,0,ROI_WIDTH,ROI_HEIGHT)
    display = dp.Display(DISPLAY_WIDTH,DISPLAY_HEIGHT,0,0)

    tracker = scrtr.Screen()
    p = tracker.screen2display(point,roi,display)
    
    assert p == (DISPLAY_WIDTH,
                DISPLAY_HEIGHT)


def test_screen2display_0_0():
    point = (0,0)

    roi = dp.ScreenROI(0,0,ROI_WIDTH,ROI_HEIGHT)
    display = dp.Display(DISPLAY_WIDTH,DISPLAY_HEIGHT,0,0)

    tracker = scrtr.Screen()
    p = tracker.screen2display(point,roi,display)
    
    assert p == (0, 0)

def test_screen2display_1_1_pos_50_50():
    point = (51,51)
    pos = (50,50)

    roi = dp.ScreenROI(pos[0],pos[1],ROI_WIDTH,ROI_HEIGHT)
    display = dp.Display(DISPLAY_WIDTH,DISPLAY_HEIGHT,0,0)

    tracker = scrtr.Screen()
    p = tracker.screen2display(point,roi,display)
    
    assert p == ((point[0] - pos[0])/ROI_WIDTH * DISPLAY_WIDTH,
                 (point[1] - pos[1])/ROI_HEIGHT * DISPLAY_HEIGHT)


def test_screen2display_55_55_pos_50_50():
    point = (105,105) 
    pos = (50,50)

    roi = dp.ScreenROI(pos[0],pos[1],ROI_WIDTH,ROI_HEIGHT)
    display = dp.Display(DISPLAY_WIDTH,DISPLAY_HEIGHT,0,0)

    tracker = scrtr.Screen()
    p = tracker.screen2display(point,roi,display)
    
    assert p == (DISPLAY_WIDTH,
                 DISPLAY_HEIGHT)


def test_screen2display_0_0_pos_50_50():
    point = (0,0)
    pos = (50,50)

    roi = dp.ScreenROI(pos[0],pos[1],ROI_WIDTH,ROI_HEIGHT)
    display = dp.Display(DISPLAY_WIDTH,DISPLAY_HEIGHT,0,0)

    tracker = scrtr.Screen()
    p = tracker.screen2display(point,roi,display)
    
    assert p == (0, 0)

####################### screen 2 display Tests #################################


    
    

