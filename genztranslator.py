import random

class GenZTranslator():

    def translate_genz(self, text):
        words = text.split(' ')
        i = 0
        x = len(words)
        while i < x:
            if i % 6 == 0 and i != 0:
                if words[i] == words[i].lower():
                    words.insert(i, self.insert_brainrot_term())
                    x += 1
                else:
                    words.insert(i, self.insert_brainrot_term())
                    x += 1
            i += 1
        res = words
        res = ' '.join(self.replace_words(res))
        return res

    def insert_brainrot_term(self):
        tier_one = ["skibidi", "erm", "ohio", "gyatt", "rizzed", "sigma", "yapping"]
        tier_two = ["baby gronk", "fanum taxed", "edged", "kai cenat", "like duke dennis", "sussy", "hit the griddy", "-aah moment", "type shit", "mewing"]
        tier_three = ["is alpha", "gooned", "with freddy frezbear", "type shit", "grimmace shake", "zesty",
                 "in the battle pass", "maxing", "with ice spice", "at the diddy party"]

        wich_term = random.randint(0, ((len(tier_one)*3) + (len(tier_two)*2) + (len(tier_three))) -1)

        main_list = tier_one + tier_one + tier_one + tier_two + tier_two + tier_three

        return main_list[wich_term]

    def replace_words(self, words):
        word_list = ["leader", "toilet", "funny", "talk", "baby", "place", "town", "dance", "party"]
        what_to_replace_with = ["sigma", "skibidi toilet", "skibidi", "yap", "baby gronk", "ohio", "ohio", "hit the gridy", "diddy party"]
        i = 0
        while i < len(words):
            for word in word_list:
                if word == words[i]:
                    words[i] = what_to_replace_with[word_list.index(word)]
            i += 1
        return words

if __name__ == "main":
    erm = input()
    translator = GenZTranslator()
    erm = translator.translate_genz(erm)
    print(erm)

