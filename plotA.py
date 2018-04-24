import numpy as np
import matplotlib.pyplot as plt

#score = [12898,4861,4299,2743,3492,4130,1770,3106,8691,344,465,2689,4819,2063,9720,3880,173,2505,7411,18600,1110,936,5886,32,479,55]
#objects = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

score = [1594498, 29035, 6469, 613384, 913608, 42513, 434978]
objects = ("den","denna","denne","det","han","hen","hon")

y_pos = np.arange(len(objects))
plt.bar(y_pos, score, align='center', color='y', alpha=0.5)
#plt.xticks(range(7),objects)
plt.xticks(y_pos, objects)
plt.ylabel('Frequency')
plt.xlim(0,6)
#plt.title('Plot of first letter frequency')
plt.title('Number of mentions of pronouns from tweets')
plt.savefig('TweetFre.png')
plt.show()
