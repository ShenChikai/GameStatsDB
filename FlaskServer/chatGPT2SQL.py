import sys
import typing
from revChatGPT.revChatGPT import Chatbot

class User2SQL:
    # set up basic configuration
    def __init__(self) -> None:
        self.user_input = None
        self.exist = True
        self.config = config = {
            "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..EGaGgz2azysRhDy9.tVGyrv4CU5e0ISPxjIzzZ58ZGY4draIyo5mrDiobxSXodc8KzeWtybPh_hny0NUKGqjgCqeYCCQntKi1z-cOSq9Q6UdlNa3olQhCK4Y5Rzyu8vsBpZulfJ48rMokhn7RnQgwlL9YI8bmPA3HFg-0gTE2m-CKBHq79_7c4u7eOjxGeTcbLgVD2uzBGp7FlbHhMhJZg4k_TsDf3jki7BGVhF78pXj1cl5UDN2cakG0jnPD-Kk-h4Qjp7vMjlU2FYp26iNUe6aXUfEQAAhvmGCD7-2QZxZGfkel-nl7xj1LdCF12rpOlFfNYTiE5kWyBIHVnxdCs-_rDqedbfK28iw46LgQdTKJqlOhNp4R8279YYiIn46rkwlZFM2TjXoDYfzJXsL5BDhSl7mbWL411a-e3nZQcEokP8ltdED7WgJ8bRhC_XiQ9F_FQb-OOE9c3EvxgARRms5A41z5HIM7WYYhnTWg2VWrcfLlMjfgiPk_GMjwWl-5bhh9xkuXeKzQ4bJRDmccYTfj5BQOt4Zy1DWcoGKt5diphdRQMpfTcZvRqwt_4m2ugkEF__3g-aCjWJ3pef8odI4qSihULPKq0_mfywF5X5VR8YBofGicscDgZiZ5y3Ni6fL_KQTe-1KhXNbGck0UYtMvOGtDOPkyH0-J_wGSx7be3sdyqifGUJ2IhFJepdITLxqMgMt3-kcGsZJXzrUVf3dPg5799mEPV_pVi_ePjvutJ44OQhl57CBg5zFxVP9soYM6eO-oqcasQdDHOM1MZiStN218NEfunNJoCDEF3wJ24TQMn7q_YXnbEUPghJRQ059QOjHXosJnkjU4z_FS2ZdBZPm1stpX9WEQfCYr38xVkQWQDqhhYIWA5rtY_GkDAIXyi1hZ4PZKfvYymyFpB0Cnsy_ZIRZZBjo9nrYq18eN0n4VslgAuVDTSyoWDrVEiPIbKxAdDUAd7ySd8MKgtKEz26SacOjV5FRVGCqj56WGhsAJ5N7PUg2fV9Vk3PDy81nUhCAdF5BTUqGczHINLCig4WzQSm0knf8aoypmrGbsUPSU5RQffSVS4QkD4nnZN5jafFdqBR_1yIrSkMPCuLhW8FxMdz9do9XgPGuwYe_KlD0tWSNrbDp_xFf_7JAG1p8LXGhe_EKJj4_UWQud9VgT7SshTZ9Rp1skcFOwP5nXWNDR2bxzwuFvWZQ0NxvFeV_i0yJ1X2q1Y8MiGesl2G3U5vGfPcY2PAUUrSDpM6uyAEIEqvDZau2FSUsaooaZQrWjNSnonr5eb29buOliw1P_pz_NAn2KTCfJ81zNjt98toOfmaT5cCV_LN7ELiiG9pcEyT6w7uQ6oJrzolsBgJJzgMTg9os9XDkkDrxv56cGKKrkQNYIAnXGXOuYElFu0-S8N12t_Bls7UHw5A37u6ZJy-STqaBzFAmU2uNotiJqFtzcAA20-bW7ONgkXtbp4zrjkjKRthY8R6NliyeD72uR4p0126qniSgLnqtHOMDD6_zVG5TloGOi8PUagSYxBx08URUg54-pjaUT7IL6nkX4JgTqdOEDeOmieeHBMIj3sGdjuwiAf4_aUafwIwaJcCqPhOh7Y2YRFmpsjng-ZZR775-haCgdhq1IxhjWgMNQAfz9OxYrqRhWxCll15jpkKqymUcg9vzJBssn17icqTv38BcZZUPKObptHaxwXKmMqMWxHt7IhQflTP55UVm4NPdaaMNEaPFP2N1xUwPR5WcmSCextxtBpgiP8HzbxJutF3gsB2EeRk73MHpoU-Ds-6JhnX1e0qJQYlFge_u3T6JHuacEjZCvOI1OIBV4wQpwUpTnjTBumuxExofjiY8M7m2I4GfFAEAw5df4g6lvB3YxXj55kJOuM0JYsOziKP8gRvMv4wDTTU9QKjZ1REO4cOEABODvyFbBMEoeHpL0iqf-wstyL9G7Q2_wNEMYiq8amQ3yMERwPzY0jYJaSi4IjDb9LFMo7i171UMi0wEXbpN5m5pJUqddOZdQva1nYYxDyJspgjms1A0BSJz8zgYmql1N_qGZdKKROZErhaobfLjk6Fx_W0btae7TU1nUvtNJcAwhT6H1UP-OfLcV9lFTkoxMI9bXMQh9J30vmgGqIYQnStVdsw2WOouIvF9HjXxufas3Dmon4kSDTayhSksN3zJZn9Y8Y2oZG5rh6X0atVSs-EsVRBc8zFFXx4_nU2uTAXOmUDQRZxK0R5M0ADCQu_rM5ACpMqwM3OdqFNPQ.75tGkcc1Ci3EWkzT2KS5Ig"
        }
        self.__run_chatbot__()
    # Initialize the chatbot
    def __run_chatbot__(self) -> None:
        self.chatbot = Chatbot(self.config, conversation_id=None)
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
            print("Question is either not in the correct format or we do not have such information in our database!")
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

if __name__ == '__main__':
    main()
