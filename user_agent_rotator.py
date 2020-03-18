from user_agents import user_agent_list
import random


class UserAgentRotator(object):
    """Create a random header from the proxy list

    Parameters
    ----------
    path: str
        path of the file, the user_agent delimiting the list by new line
    """
    random_user_agent = None

    def __init__(self, path='scraper/Example.txt'):
        self.user_agent = self.get_user_agent()

    def get_user_agent(self):
        """ Return the User agent """
        return self.get_random_user_agent()

    def get_random_user_agent(self):
        """ Set the `random_user_agent`(user agent and browser info) and  Return the User agent """
        self.random_user_agent = random.choice(user_agent_list)
        return self.random_user_agent['userAgent']

    def generate_header(self):
        """
        Returns
        -------
        header: Dict[str]
            returns a dict with keys Connection and User-Agent
        """
        header = {
            "User-Agent": self.user_agent['userAgent']
        }
        return header
