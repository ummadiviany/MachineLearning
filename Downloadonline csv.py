import wget
url = 'https://thingspeak.com/channels/539123/field/4.csv'
#url='https://apmonitor.com/che263/uploads/Main/goog.csv'
filename=wget.download(url)
