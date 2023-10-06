import cv2
import pandas as pd
import os
from os.path import join as pjoin

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)


def show_ui_with_cap(ui_no):
    print(capUI[capUI['gui-no'] == ui_no])
    ui_img_path = pjoin(rico_dir, str(ui_no) + '.jpg')
    img = cv2.imread(ui_img_path)
    cv2.imshow(str(ui_no) + '- press "q" to exit', cv2.resize(img, (img.shape[1]//2, img.shape[0]//2)))
    if cv2.waitKey() == ord('q'):
        return False
    cv2.destroyAllWindows()
    return True


def show_all_ui_caps():
    ui_cap = capUI.groupby('gui-no').groups
    for ui_no in ui_cap:
        print('\n*** Press "q" to exit ***')
        if not show_ui_with_cap(ui_no):
            return


if __name__ == '__main__':
    cap_csv_file = 'CapUI.csv'
    rico_dir = '\\Data\\rico\\rico_sca'
    capUI = pd.read_csv(cap_csv_file)

    show_all_ui_caps()
    # show_ui_with_cap(ui_no=61313)
