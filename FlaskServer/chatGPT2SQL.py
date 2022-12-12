import sys
import typing
from revChatGPT.revChatGPT import Chatbot

class User2SQL:
    # set up basic configuration
    def __init__(self) -> None:
        self.user_input = None
        self._session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..UqvptnwsjahZyU9Z.yBXPYGpRxzytn6QaFqGQSHf9zFQoBKRAZbNRZvzmKEZTdit_GsyGTW_16vfzPSkEoZauHogpIKqWzHnPBZvZnzJno01XMMQQJ6yqMjD70mP_X05ORMOfSpQyoCa_40Ie8jeEacHEvHm1oPUHoZ1EA8z2TxfA9ja13bwOs9lCquJxKEbIHPt4Q2iOfG_YgO6EKoqa9iKmQe3mgqPltJDBdKKmV4MpBXwDW9mP79gJC6_n34fxxaChb_XEquNBh-vSD68L3JQpt4XC_f2OpD-C71VvONlKWf6-rYmnD-k64pk4EWyffI8oqbhU6rEjsLoWAoGEbBeDgj6FQBzIN8qMpz_XuqC86ErWR8k5YsDmC_p4YudnES-zukD9jE4IP4dH_RzMUGPMj3FS0sqcxInbW1S4pEdSZwK7yunfffI-qglSnoOUSmCG0BdjzSPAP0H412fpyJlEKFi9DH8RJ4syLHK7tP_zzdpCgCEKeoLJzd8heqBs9PoqV0HRV5oIlqJhkqPTKP-GUlhNaTY1GkTe7r_sflvfXMt1PmVsmktZ2RVor9VBQI4ZSTnszkp8G-hHIR4xPvhaHZ7zLUqxO8JWGgRK8cptPJ47G2v5OiBxQkhXX9wA5E2J-6DbK4V2568piD80bxZyKzJcutTm69pqQidkJZgyQfCaOaeRuOjkp-qwigq-ly2W9tjAyIc3DvZ5xFzwbtBkq5CuXiM8f2KKzId5IRavw8Jbomo-CHA872UBVQxlVlblY79qsA2Fh5qc1i-6doYLaO1r7mEykAHDg5i6LS_MNv4QHk6-EgyViFS6TfJgUh_Nh1AWwMEdDYMnb9kauW78eAL9coHxSgie_jvfKVJg2Wr8Z62hHbStUp1xdvsjaCmTOxHeQK_FjRTQQYnwVTvV-zBPmfRI6EJxoOZpMISjS4rOZJ_UOnMqme_2WiMsC-CBAJ09nKvL2yKnHludbOwiWUVX6TWPT5YSgEXLStW2tCAZc8kTHkquHBty05y918S_1XLzsSZDSHiOoeKsc7soYIKC5WxF-XmadHt5jpZ85iGDiPoQvNtq36oNACd--GUKYdBBwssOvKr57f84u4sQ3r20ciqUxFZxMKptKXd-AyDl06H0zG2SthQQyVvQjWtIKNGSlereHo91OFRuZ6SK-YoSQxUJ9lX95NuuCYZXFLed7WN3EZgD6SwSwrOHbHwW2zigvG0lL92Za4ZPDB61Dd_wn3VkQR8VDgGHVTRakNLNl9ZmVzEG9n15zYo3knswQn6aIuC6Ri8F35Pe_3Vd92cB98MLg_MnBtK4RJXWaldrBas98S_QjlBK_XTmc2EpesdqbtM7NJxDaPCdAfWNV5pV_vBWEWkD8bINT066-uWxr-olwtoypGEC4-H2azu-Arx-7aSw8x8X2o1M3JxQit7VLAtq22PD-9ZD6EPCKI6sRzw3GSR7H3I70yCQdQ3YymutkV9KKvTjFnVo4AnYWhUl9bbqoReyUz85-n9i-Of2dxzwrf4ZDsRgEU9EtlXEw9veezhuqxyrLjMKQB761nb3SL7zoZzPaiOSvjWql_Kx1Vpm4OXkQVPGUedQJQ3KWWdf4N7_7lJPWv5-7L6Fh7908QPPayFig8iI_CT69nY9CWeXwfHWAE3yp4mAiAICrdmtW4O2O9tefRbYil4rHknsHJKyQnRaH0_pWjtxuVexS2iEVcPtOJUMDKQgsGXG3C_-4WUbKVcwi0NcPJhrS4hsjDT5LDbHcHFRjRlc4BRe5tOEH3z8Fi_q_3X82mkqCHMsDrpJPqgJFMijfFIN4laFWjnj0bNgb9WjseS2ABLy7dUw9aWQUR_1fUhIgM3Oyvan8RsEK7JSUt3-RVlQIX5kAeWdI95IY-orOrTOsec23qkYhBAq3QZMh42WMxqyJd8pv8MVKCRqB9nbT-4xvR_lAOs63RfPXqRHplwTK2SJSp9wGmTizgZzjmsmuicP5JhBOLrwVaoMUKWNW5yrolBh4P-HJ-xeUmltfiG5lGFo8wgj5RzVk-F42M5pXbNhGjlmhoNPEQ8_K-PvpwnBPIkxbrvu_uZX3c1HOAvzkRgw_grdPl6V90Gm0DO8yi6cEHcgrjcuWWALDtgwDru_tEsuDb6DpRoesGLhvnzjE6jF_jWCcURBF_jyPlUU4OXbLL4NAF0u6MhlHJGvtrbVBu8eJjcM3R2YzPCKHFgIqmQIGC0jYhtgjPAs9gptFfVlbE0Hk1Fqe4WvZvVL.AYJFInj3ENwb3nkwXs_bvg"
        self._config = {"session_token": self._session_token}
        self.__run_chatbot__()
    # Initialize the chatbot
    def __run_chatbot__(self) -> None:
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
        gametable2 = ", ReleasedDate (datetime type, e.g. 2004-11-01 00:00:00 stands for November 1, 2004), IsF2P (is the game free to play or not? True or False)\n"
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
