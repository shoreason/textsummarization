import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# This is a naive text summarization algorithm
# Created by Sho Fola Soboyejo
# Mar, 2018

class BaseSummarizer(object):

    # Naive method for splitting a text into sentences
    def split_content_to_sentences(self, content):
        content = content.replace("\n", ". ")
        return content.split(". ")

    def organize_summary(self, top_sentences):
        summary = []

        for (sentence, score) in top_sentences.items():
            if sentence:
                # summary.append(". ")
                summary.append(sentence.strip())
        return ("\n").join(summary)

    def filter_top_sentences(self, scored_sentences, sentence_score_threshold):
        # {k:v for (k,v) in dict1.items() condition}
        # dictionary comprehension to select sentences above score threshold
        filtered_sentences = {sentence: score for (sentence, score) in scored_sentences.items() if score > sentence_score_threshold}

        return filtered_sentences

    def score_sentences(self, content, freq_table):

        # Split the content into sentences
        sentences = self.split_content_to_sentences(content)

        scored_sentences = {}

        for sentence in sentences:
            sentence_score = 0
            for word, frequency in freq_table:
                words = sentence.split()
                if word in words:
                    sentence_score+=1
            # print(u'{}:{}'.format(sentence, sentence_score))
            scored_sentences[sentence] = sentence_score

        return scored_sentences


    # Generate word frequency table
    def get_freq_words(self, content, freq_threshold, clean_text=False):

        # https://github.com/tistre/nltk-examples

        # clean text

        # NLTK's default stopwords
        default_stopwords = set(nltk.corpus.stopwords.words('english'))

        # tokenize
        words = nltk.word_tokenize(content)

        # Remove single-character tokens (mostly punctuation)
        words = [word for word in words if len(word) > 1]

        # Remove numbers
        words = [word for word in words if not word.isnumeric()]

        # Lowercase all words (default_stopwords are lowercase too)
        words = [word.lower() for word in words]

        # Remove stopwords
        words = [word for word in words if word not in default_stopwords]

        # Calculate frequency distribution
        fdist = nltk.FreqDist(words)

        # for word, frequency in fdist.most_common(freq_threshold):
        #     print(u'{}:{}'.format(word, frequency))

        return fdist.most_common(freq_threshold)




def main():

    title = """
    Swayy is a beautiful new dashboard for discovering and curating online content [Invites]
    """

    content = """
One sunny day, two Monks went for a walk in the forest. As they’re walking, they come to a small stream. Next to the stream they saw a beautiful young girl trying to figure out how to cross the stream without falling in and getting wet. One of the Monks realized what was happening, walked to the girl, picked her up, carried her across the stream, and put her down on the other side. She thanked them and the Monks continued their walk.


After walking in silence for about an hour, the first Monk couldn’t stand it any longer. “How could you do that? You know we’re not supposed to touch a young woman like that! “ he said. The second Monk looked at him, smiled, and said“ I put her down an hour ago, but it seems that you’ve been carrying her for all this time.”

Lesson number one: Don’t carry your failures, your disappointments, your lowest moments with you forever. Put them down and look ahead, don’t dwell on the past. You can’t drive a car by looking in the rearview mirror. Neither should you live your life that way. What does that mean to you? It means accepting your failures and disappointments, learning from them, growing and maturing in spite of the pain and moving on with rebuilding your life.

It means forgiving those who have hurt you or wronged to you. Unforgiveness is like drinking poison and hoping the other person dies. Unforgiveness only poisons yourself. Let it go. Forgive and heal. This also means forgiving yourself, by the way. Forgiving yourself might actually be the hardest of all to do. Accept that you are human and we all make mistakes. Learn from them and move on.

My story: The lowest point in my life was the break-up of my marriage of 25 years. I was devastated, depressed, angry, scared, and every other negative emotion you can imagine. I went through several months of very dark emotions, until one day I just had enough. I realized that I was either going to find a way to stand up out of my own self pity and my own dark thoughts, or get consumed by them. I decided that the way to accomplish this was to focus on helping others rather than trying to worry about myself. I started volunteering as a job coach at a local charity organization; helping people find jobs, change careers, and solve general career problems. It has changed my life. Without realizing it, I had stumbled through the ashes of my life and found my purpose.

Lesson number two: Find a way to see the bigger picture and to get outside yourself and your own problems. Find a way to get out of your own head. Figure out how to do something for others rather than yourself. You would be amazed how your perspective and your mood changes when you force yourself to be altruistic rather than self absorbed. When you have your face buried in your problems and all you can see are your problems, you miss the giant, obvious solution standing 2 feet away.


Lesson number three: Hold on tightly to your hope and your faith. You have to believe that there is hope and a better future for you on the other side of whatever situation you’re in. For me, as a Christian, I had this promise to hold on to: “ I know the plans I have for you, says the Lord. Plans to prosper you not to harm you. Plans for a hope in the future.“ (Jeremiah 29:11). A friend gave me that verse on a little plaque and that plaque became the cornerstone that I rebuilt my life on. Whatever your faith is, when the going gets tough, lean into it with a vengeance. It will get you through.

How did it all work out? It is now almost 2 years later, my life is unrecognizably different. Having found my purpose, I have found peace, fulfillment and happiness in doing what I love, helping people wherever I can. I continue to volunteer as a job coach and have expanded into doing as a business, reaching even more people than before. I am in the process of writing a book, I’m blogging regularly, and have recently discovered Medium.com as another way to reach even more people, and I’m loving it!

American author Merle Miller says this: “Everyone has a burden. What matters is how you carry it” I would paraphrase that to say “Everyone fails. What matters is how you handle it”

If you are going through dark times right now, I hope you will find the hope, faith and encouragement in this article to help you push forward and come out the other side as blessed and fortunate as I have been.
    """

    content1 = """
    Lior Degani, the Co-Founder and head of Marketing of Swayy, pinged me last week when I was in California to tell me about his startup and give me beta access. I heard his pitch and was skeptical. I was also tired, cranky and missing my kids – so my frame of mind wasn’t the most positive.

    I went into Swayy to check it out, and when it asked for access to my Twitter and permission to tweet from my account, all I could think was, “If this thing spams my Twitter account I am going to bitch-slap him all over the Internet.” Fortunately that thought stayed in my head, and not out of my mouth.

    One week later, I’m totally addicted to Swayy and glad I said nothing about the spam (it doesn’t send out spam tweets but I liked the line too much to not use it for this article). I pinged Lior on Facebook with a request for a beta access code for TNW readers. I also asked how soon can I write about it. It’s that good. Seriously. I use every content curation service online. It really is That Good.

    What is Swayy? It’s like Percolate and LinkedIn recommended articles, mixed with trending keywords for the topics you find interesting, combined with an analytics dashboard that shows the trends of what you do and how people react to it. I like it for the simplicity and accuracy of the content curation. Everything I’m actually interested in reading is in one place – I don’t have to skip from another major tech blog over to Harvard Business Review then hop over to another major tech or business blog. It’s all in there. And it has saved me So Much Time



    After I decided that I trusted the service, I added my Facebook and LinkedIn accounts. The content just got That Much Better. I can share from the service itself, but I generally prefer reading the actual post first – so I end up sharing it from the main link, using Swayy more as a service for discovery.

    I’m also finding myself checking out trending keywords more often (more often than never, which is how often I do it on Twitter.com).



    The analytics side isn’t as interesting for me right now, but that could be due to the fact that I’ve barely been online since I came back from the US last weekend. The graphs also haven’t given me any particularly special insights as I can’t see which post got the actual feedback on the graph side (however there are numbers on the Timeline side.) This is a Beta though, and new features are being added and improved daily. I’m sure this is on the list. As they say, if you aren’t launching with something you’re embarrassed by, you’ve waited too long to launch.

    It was the suggested content that impressed me the most. The articles really are spot on – which is why I pinged Lior again to ask a few questions:

    How do you choose the articles listed on the site? Is there an algorithm involved? And is there any IP?

    Yes, we’re in the process of filing a patent for it. But basically the system works with a Natural Language Processing Engine. Actually, there are several parts for the content matching, but besides analyzing what topics the articles are talking about, we have machine learning algorithms that match you to the relevant suggested stuff. For example, if you shared an article about Zuck that got a good reaction from your followers, we might offer you another one about Kevin Systrom (just a simple example).

    Who came up with the idea for Swayy, and why? And what’s your business model?

    Our business model is a subscription model for extra social accounts (extra Facebook / Twitter, etc) and team collaboration.

    The idea was born from our day-to-day need to be active on social media, look for the best content to share with our followers, grow them, and measure what content works best.

    Who is on the team?

    Ohad Frankfurt is the CEO, Shlomi Babluki is the CTO and Oz Katz does Product and Engineering, and I [Lior Degani] do Marketing. The four of us are the founders. Oz and I were in 8200 [an elite Israeli army unit] together. Emily Engelson does Community Management and Graphic Design.

    If you use Percolate or read LinkedIn’s recommended posts I think you’ll love Swayy.

    ➤ Want to try Swayy out without having to wait? Go to this secret URL and enter the promotion code thenextweb . The first 300 people to use the code will get access.

    Image credit: Thinkstock

    """

    bs = BaseSummarizer()
    freq_threshold = 10
    sentence_score_threshold = 1
    clean_text = True
    freq_table = bs.get_freq_words(content, freq_threshold, clean_text)

    scored_sentences = bs.score_sentences(content, freq_table)

    top_sentences = bs.filter_top_sentences(scored_sentences, sentence_score_threshold)

    summary = bs.organize_summary(top_sentences)

    # print summary
    print(summary)

    # Print the ratio between the summary length and the original length
    print("")
    print("Original Length %s" % (len(content)))
    print("Summary Length %s" % len(summary))
    print("Summary Ratio: %s" % (100 - (100 * (len(summary) / len(content)))))

if __name__ == '__main__':
    main()
