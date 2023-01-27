import speech_recognition as sr
import webbrowser as web

path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
# path = "C:/Program Files/Google/Chrome/Application/chrome.exe $s"

print(" ---- ")
print(path)

dest = 'www.facebook.com'

print(" URL is ", dest)

# web.register("chrome", None, web.BackgroundBrowser(path))
# prompt the open method in the webbrower module so that it gets to find the code

# web.get(path).open(dest)


web.open(dest)
