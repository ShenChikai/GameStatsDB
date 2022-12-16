import sys
import typing
from revChatGPT.revChatGPT import Chatbot

class User2SQL:
    # set up basic configuration
    def __init__(self) -> None:
        self.user_input = None
        self._session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..zntfGvFp9Mc4qItH.ubL8lvqBYHomcat_R6ZMHoaRZMlOjMvLtReYCoMSxIy0bFQkaLVsRpxm3Xhg7JVjom3ljyRvL73yKK_0HUquo2IPZtIc9mzx7an6FMJrc_yvO7SFf0np4f9btRUv6WUevdAtKOmykPb9_9nlcdOsU1MBiNidRznAl_mpW-ymcbovPbm0LK6exXh_NLje6btXJqbXa6d3OhVFgQAT_JX5sUjci1GU7wy9qfH0VdOGfwTucg_ROLtPfs_DEx28eZrh4Yv-71CM25hTKyHE1muZMEaVzjaeE93bbZhFNenKpSfBLwdXhvD7vvzIHcq7y8Pni1_Eak8NF2INS7RFGYdYWw0lW9aMTpYwNt64Dxu_S39Jizx_KGvrYTWL699_VqgjQa8Jqb0y4RyvxDd5ePbi-_QXUOZm1dd8kBvoSoM3KoCycgm1SnQLM9FVaS_F5p29w48j61i5A-7d5bRYmaCAZ1Hy7oALXmvDOZygS4mfZm6S8P8eOnlaEAf3AqDv33DAwTbaS2zVdrSSzE4PoUq0z1ehnNNRgNI4nNBD0YoZlaHtyz4DttGg5a4LNvf8aBCC63q-TlaKFoBINILhFtXjINq4EvbyJypJeD_IK2PIYxvFeTru1YyaBnu-fkOum5ZA5ApMigXHFYI0FPcnVCJXUrrukixpCogT1Bq72prkMdR92lW9yN958EgC0KRZuR0Wi0jU_pBJ4U0btGMMeqVBsf5BGdP00rVOsIXgS66QYmAyfjXYSejBw3zrZPpIqvcNgMemPm3SnYMk7oXqXlqFREyTFX3nxpwFNgmq3hZg7qmjuFmH2qB8ZrYjMfqLNacIBlm5EQw_-uy8zBzWfWyO-zMYsar82Lgpx8cX5Eu3dAPeaSRT_LX6N88q91ccWv4xV6qgMEn675K-wzhTQXb4dSekA1f9b3OoDUGOXllNUB8BSA3sqZFP2_jjPjtHp4YkiOkXKJ57cKQ7VS3XWKa4IvuYBH6usU-klbhYBe3nhafNPwgtjFz2mEp7jXD6Q1WiEmTqSylXL3FnOwKhvZb9oDKQs40fAYNOwqH200G6LjvPDcWo1OslD7mAo37anKg3QmLvURh3wQ3a85efcW8N9mhqX5WYWDSFSC5oHeQjDVxGyI29RA3h3n9aC8iz1KeRY9wgQ9QdELHQ4mPqMidFLLHDNkIidwrmARPsB4oj8BZh99oBBW81fX3fEBZA8xQPCM7SSPXx-iV3zbkAYJKkiBCC6s5cxwPt5DsP_Ga0N-rl3rPuVvpu67jfvvmiqxCu3zcZI5SxjN-IyW9VwMgtcqa7USM07u2Nytl8048KYn7yCvmmzR7pWzi5f0Gl5kjAhm_laquW9YamXD-z7uN6Z-JibAgKypShEh-JAXpJvbojmhLYfYEXO0ILsaKwPAX6HRwDRoC5b4Wo-CZqPImq5YQlxkIKAPMHLhpYvztkfXWfVOCEsyudM6y2C6pZHI-dh1G2MubtLN2_kINeMLIsg9V-0lEnthVt39vnG8yyBsgF3pthH0Rwms_XuV60Jkn41hXMRBe1S8Ku7ZIkiXVI5wof0hiDn8v5RKazmBX6R-oi3_wivNR98VAq2WKsg2L5n3XbyZEMuLXw0N_n4TZOUbI9ORnVxIWDJZHmUCaek0oDeZfyZdfnR1fsygbfry_aWDAFpkX2FEwcn6rKUhk5qXLDD01lXDciyAI4nmKc7fwL2fAnJaE7g8rcO3oy2cI5XLWeQCf736bxGFONWKoYY99CnnKFz5leAroZis99bEHBLkyORICHgChgI9amERz9DU0oSModqrfynC_X4s-n9rZ2niDuuJ-ADIqRa01Po3Kc-9Kj3xT_3_SZItAaO5a1rKe55vFAOkbsHldh1eK_-JmDcz1XUSSVZ4156rDW8WsJmZAUfbN04XEOkgFgiuAVt3NTiI8-H8UUWp7WJVPTEJtRSQv5hnTMY51_AV6K6jZPV0j4NxdN08LF0vchuOjPUG71JrqoIdcdPnco7_lgHFZ3PuSxMqda0-nJIhsTiqju33orUMeej4zZ2P2RT_A_uK-F8TCB-UBb9ErSRLH69QhYVCifsHslQw9jiX-YFQOHZf2EcAaioDsaw5wrdS13lGHLij5dfCLqjTxrchqZbAe2KDXOU3F0z5IGAOLm9IwbqYb4cF7_6S8FANaf_3n6xuuAR2qSlvvnYcN6LqYeAhHeEdezgaTIQrH_z8oX566sFqjjDjeS-3l9tHlOPru0VZVk.e0Kg07ipw8wRUGFkjZS9kQ"
        self._config = {"session_token": self._session_token}
        self._run_chatbot()
    # Initialize the chatbot
    def _run_chatbot(self) -> None:
        try:
            self.chatbot = Chatbot(self._config, conversation_id=None)
        except:
            raise ConnectionRefusedError
    # Need to run this function to set up the input format for chatbot
    def get_user_input(self, user_input: str) -> None:
        self.user_input = user_input
        self.pre_condition_setup()
    # Set up the pre-conditions and concat with user input as the input message
    def pre_condition_setup(self) -> None:
        prereq = "Suppose I have following table in my mySQL Database: \n"
        gametable1 = "1. Table Game which has GID (Game ID), GName (Game Name), Sales (the sale amount of this game)"
        gametable2 = ", ReleaseDate (datetime type, e.g. 2004-11-01 00:00:00 stands for November 1, 2004), IsF2P (is the game free to play or not? varchar: True or False)\n"
        Award = "2. Table Award which has AID (Award ID), AName (Award Name), VotedByWho (who vote the award? jury or fan\n"
        company = "3. Table Company which has CID (Company ID), CName (CompanyName), MarketCap (Market capitalization), Earnings, EmployeeCount, Revenue, Country\n"
        Platform = "4. Table Platform which has PID (Platform ID), PName (Platform Name), FoundDate (datetime type, which has the same format with ReleaedDate in table Game\n)"
        Stock = "5. Table Stock which has Ticker, Country, Exchange(e.g. 'NYQ'), FiftyTwoWeekHigh, FiftyTwoWeekLow, Market(e.g us_market)\n"
        GameNominatedByAward = "6. Table GameNominatedByAward which has GID, AID, YearNominated(int), DidWin(whether or not the game win the award; 1 for yes, 0 for no)\n"
        GameHasGenre = "7. Table GameHasGenre which has GID and Genre(which is the genre of the game)\n"
        CompanyOwnsPlatform = "8. Table CompanyOwnsPlatform which has CID and PID\n"
        CompanyOwnsGame = "9. Table CompanyOwnsGame which has CID and GID\n"
        PlatformHostsGame = "10. Table PlatformHostsGame which has PID and GID\n"
        GameIsAvailableOn = "11. Table GameIsAvailableOn which has GID and OS (operating system)\n"
        CompanyHasStock = "12. Table CompanyHasStock which has CID and Ticker\n"
        TimeTickerPrice = "13. Table TimeTickerPrice which has Date (datetime type, same format as ReleasedDate in Table Game), Ticker, Open, High, Low, Close, Adj_Close, Volumn\n"
        question = "Can you write a SQL query that answer the following question:\n"
        allprereq = prereq+gametable1+gametable2+Award+company+Platform+Stock+GameNominatedByAward+GameHasGenre+CompanyOwnsPlatform+CompanyOwnsGame+PlatformHostsGame\
            + GameIsAvailableOn + CompanyHasStock +TimeTickerPrice +question
        self.user_input = allprereq + self.user_input
    # Get response from the ChatGPT and get sql query from response2SQL
    def get_response(self) -> str:
        self.response = self.chatbot.get_chat_response(self.user_input, output="text")['message']
        return self.response2SQL()
    # parse the response and get sql query
    def response2SQL(self) -> str:
        try:
            query = self.response.split("\n```\n")[1].rstrip('\n').split('\n')
        except:
            raise ValueError
        query = " ".join(query)
        if query[-1] != ";":
            query += ";"
        return query

def main():
    # Initialize User2SQL object
    newChat = User2SQL()
    # Get User Input from stdin
    user_input = input("What kind of question do you have?\n\tFor example, you could try ask: What is the Game Name that has highest sales?\n")
    # update user input in object
    newChat.get_user_input(user_input)
    # Get SQL query
    response = newChat.get_response()
    print(response)

# if __name__ == '__main__':
#     main()
