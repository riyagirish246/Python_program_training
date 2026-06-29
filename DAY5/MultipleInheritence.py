class GrandFather:
    def Skill(self):
        print("Reading Current Affairs")

class Father(GrandFather):
    def FatherSkill(self):
        print("Makes Money")
class Son(Father):
    def SonSkill(self):
        print("1.Watching Reels\n2.Sleeping\n3.Studying")

son=Son()
son.SonSkill()
son.FatherSkill()
son.Skill()