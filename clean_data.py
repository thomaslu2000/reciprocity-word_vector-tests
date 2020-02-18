"""

This script Lemmatizes words for possibly a slight boost in performance and removes punctuation and stop words
And outputs the resulting text

"""

from nltk import word_tokenize, pos_tag, WordNetLemmatizer, download
from nltk.corpus import wordnet, stopwords

stopwords = set(stopwords.words('english'))

punctuation = ",.?-—()"

lemmatizer = WordNetLemmatizer() 

def get_wordnet_pos(tag):
    """Map POS tag to first character lemmatize() accepts"""
    tag = tag[0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


def clean(text):
    text = text.lower()
    tokens = ["num" if w.isnumeric() else w for w in word_tokenize(text) if w not in stopwords and w not in punctuation]
    return " ".join(lemmatizer.lemmatize(w, pos=get_wordnet_pos(pos)) for w, pos in pos_tag(tokens))



hiking = [
    "The beauty of Joshua Tree National Park is in part its close proximity to LA. No matter where you are or what Google maps seems to say, people from LA will tell you that your destination is only about a half hour away… depending on traffic. Well, Joshua Tree isn’t a half hour drive but it is only 130 miles; 130 easy miles due east just outside of Palm Springs. The park is made up of 794,000 acres that straddle the Mojave and Colorado deserts. The first time I drove through the western gate it felt like I was stepping into one of Dr. Suess’s books with the spiny Joshua Tree’s shaking their pom-poms across the valley floor. Legend has it that Mormon pioneers saw the outstretched arms of the trees and were reminded of the biblical character Joshua, who was to lead them to the promised land. The name stuck.",
    "For years I have been looking at dreamy photos online of people hiking the Narrows in Zion National Park.  Silky, turquoise water flowing through deep, dark canyons. 2000 foot vertical cliffs. Faint beams of sunlight bouncing off the colorful canyon walls. It looks like something that only exists in fairy tales. Well last weekend, I finally got the chance to backpack the Narrows, and I know now that no photograph can do the Narrows justice. Yet, I couldn’t help myself. So here’s a few of my favorite photos from the weekend.  Hiking the Narrows was an amazing experience, and hopefully these photos inspire you visit the Narrows soon. For more information on the Narrows, ",
    "In April, I went to Zion National Park for the first time. Man was I impressed. With the towering monoliths, crazy sandstone formations, and epic views, I easily could have spent a few weeks here exploring. But out of all of the things we did, the East Mesa Trail hike to the top of Observation Point stood out as one of my favorite hikes. It was way less crowded than the hike up Angel’s Landing, and there’s nothing like hiking up the side of a sheer cliff face, with zilch between you and the valley floor. While the morning started out a little grey, eventually sun broke through, making for some fine photo opportunities. Here’s a map and a collection of some of my favorite shots from the hike.",
    "Pick a shorter hike, something that will take you a few hours or an afternoon, rather than an all day epic. I like to choose hikes on a network of trails where I can head out for a longer loop if I’m feeling up to it, or choose a shorter route if the weather turns out to be truly terrible.  And of course trails that have a cafe nearby for post-hike lattes get bonus points. Make sure you read up on the trail beforehand. If there are creeks to ford, steep slippery sections or if the trail is prone to flooding, save it for a dry day.",
]

cooking = [
    "Baked Persimmon Crisp is a simple and stunning dessert that can also be served as breakfast on a cold morning. You get the crisps for the butter breadcrumbs mixture and the softness of the persimmon. It’s a mouthful delicious treat that barely takes any effort at all. This year has been one of most exciting one so far! With a couple of photography projects, making new friends, attending culinary events, trying different ingredients and cooking nearly non-stop, I have no idea when the months zoomed by and made us reach November. There are no regrets, only more contentment and a desire to continue learning. When one spends the day doing what they appreciate, it makes the time worth living for. It makes one look forward to the next day. Amongst all this, when a much needed escape gets planned, you can only imagine the excitement (smiling from cheek to cheek). Yes, we are going on a petite trip! We are getting ready to explore and absorb. So while I plan, pack and organize, you go ahead and try this extremely easy dessert.",
    "Well, that’s me, a weird soul in this planet who could never enjoy ice cream to that extent. Yes, I will take a tiny bite or a spoonful when it gets really hot or when I am in a rare ice cream mood. Few weeks’ back, I got this crazy idea to make ice cream at home. It started as a pure experiment and turned out to be a success. Honestly speaking, I never felt so proud of myself after making something successfully for the very first time. And what made me even happier was when everybody who tasted it, enjoyed it.",
    "A decent chocolate treat is soul satisfying, mood uplifting and can switch any miserable day to a chirpy one. Living in west coast, I shouldn’t ever nag about the weather but it’s been blue off late and it yelled for some sugar rush to boost my spirit. Plus, with all the Valentine’s Day chocolate delicacies that are floating in the virtual food world and food channels, it’s tough not to flow with the temptation. It’s nothing bad, only food and good food, if I may say. Well, chocolate is good for health in several ways, obviously as long as you don’t over do it. I had mentioned it several times in past that I am not a chocoholic but at times, the craving hits hard. And if that’s an airy, fluffy, velvety mousse, which melts in your mouth, I could dig in and gobble non-stop.",
    "I was surprised and smiling from cheek to cheek as I saw those cream puffs rising tall. Kept my fingers crossed and hoped that it doesn’t fall flat after a while. It didn’t and they were still standing firm when I took them out of the oven. I kept staring impatiently for them to cool down and after a while, I held one in my hand.. they were perfect at least in my world. Cream Puffs filled with Strawberry"
]

tech = [
    "Mobile technology is a form of technology that is mostly used in cellular communication and other related aspects. It uses a form of platform where by many transmitters have the ability to send data at the same time on a single channel. This platform is called Code-division multiple access (CDMA). This platform allows many users to make use of single frequencies because it restricts the likelihood of interference of frequencies from two or more sources",
    "The mobile technology has improved from a simple device used for phone call and messaging into a multi-tasking device used for GPS navigation, internet browsing, gaming, instant messaging tool etc.",
    "The mobile technology started as a remarkable achievement in the world of technology but now, it is transforming into user comfort technology due to its present diverse functionality. When the mobile was first introduced, it used to be basically for SMS, Calls and games. But it has presently transformed into a digital world and has made life and business much easier; marketers now have the ability to sell their products with ease through mobiles technology",
    "The mobile has made it possible for users to transfer files and other files through Bluetooth and wifi. The mobile is also equipped with internet connectivity, making it easy for the user to gain information and also to download files from the internet"
]

disney = [
    "Cinderella is another one of those stories that technically exists outside of this version of it — it was even a Disney short three decades earlier — but not really. This is what people think of when they think of the girl with the glass slipper. Heck, this is kind of what people think of when they think of the very concept of the Disney Princess, the idea that anyone can find true love and magic if they just believe.",
    "A regular inhabitant in the top spot of best Pixar movies ever, this Andrew Stanton 2003 gem is a wonderful, hysterical, moving piece of family entertainment. The story of a clownfish named Marlin (Albert Brooks) trying to find his abducted son Nemo (Alexander Gould) is the perfect balance of visual whimsy, emotional relatability, and adventure storytelling. It’s not just one of the best Pixar films, it’s one of the best animated films by any company.",
    "check out one of the most progressive animated films of its era, a movie that tells the Chinese legend of Mulan, a girl forced to impersonate a man to fight for her people. A lot of the Disney titles of the late ’90s are kind of goofy comedies but this is a rich, empowering drama that has stood the test of time.",
    "Only the second Disney film ever, this is one of the most iconic films in the company’s history. The puppet who wanted to be a real boy is one of the foundational films in the history of animation, not just Disney. It showed what could be done by a team of creators who respected both the source material and their audience. If you haven’t seen it since you were a kid, you owe it to yourself to revisit Geppetto, Jiminy Cricket, and the unforgettable puppet."
]

for text in [hiking, cooking, tech, disney]:
    for s in text:
        print(clean(s))
        print()
    print("-------------------------------")
    print()
