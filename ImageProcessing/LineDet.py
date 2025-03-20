import cv2
import numpy as np
import matplotlib.pyplot as plt

def line_detection(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    kernel_hor = np.array([[-1, -1, -1], [2, 2, 2], [-1, -1, -1]], dtype=np.float32)  # Horizontal
    kernel_ver = np.array([[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]], dtype=np.float32)  # Vertical
    kernel_diag1 = np.array([[-1, -1, 2], [-1, -1, 2], [-1, -1, 2]], dtype=np.float32)  # 45-degree diagonal
    kernel_diag2 = np.array([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]], dtype=np.float32)  # -45-degree diagonal
    g_hor = cv2.filter2D(img, -1, kernel_hor)
    g_ver = cv2.filter2D(img, -1, kernel_ver)
    g_diag1 = cv2.filter2D(img, -1, kernel_diag1)
    g_diag2 = cv2.filter2D(img, -1, kernel_diag2)
    g_hor = np.abs(g_hor)
    g_ver = np.abs(g_ver)
    g_diag1 = np.abs(g_diag1)
    g_diag2 = np.abs(g_diag2)
    T = 140
    g_hor = (g_hor >= T).astype(np.uint8) * 255
    g_ver = (g_ver >= T).astype(np.uint8) * 255
    g_diag1 = (g_diag1 >= T).astype(np.uint8) * 255
    g_diag2 = (g_diag2 >= T).astype(np.uint8) * 255
    g_all = cv2.bitwise_or(cv2.bitwise_or(g_hor, g_ver), cv2.bitwise_or(g_diag1, g_diag2))
    return g_all

for i in range(1,6):
    g=line_detection(f"captcha{i}.jpeg")
    cv2.imwrite(f"output{i}.png", g)
