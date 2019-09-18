import pandas as pd
import matplotlib.pyplot as plt
url = 'https://thingspeak.com/channels/539123/field/4.csv'
data=pd.read_csv(url)
print('min:   '+str(min(data['field4'])))
print('max:   '+str(max(data['field4'])))
#print(data)
plt.figure()
#time=data['created_at']
#print(time)
#plt.xlim(time)
#plt.ylim(0,100)
x=plt.plot(data['field4'])
plt.xlabel('Time')
plt.ylabel('% of Moisture')
plt.title('Field4')
plt.legend(x, ('Field4'))
plt.legend() 
plt.show()
