# import modules
import logging
from src.data import *
from src.utils import *

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

class Crawler(object):
    """

    """
    def __init__(self, city, grouptype=None, citylist=None, url=None):
        """

        :param city:The object city
        :param grouptype:
        :param citylist:
        :param url: request url and
        """
        self.logger = logging.getLogger()
        if url is None:
            self.dictURL = dictURL
        if grouptype is None:
            self.dictGroupType = dictGroupType
        if citylist is None:
            self.dictCityList = dictCity
        self.strCity = city
        if self.strCity not in self.dictCityList:
            self.logger.error("{0} dos not exist in the Lianjia datebase.".format(self.strCity))
        else:
            self.strCityPara = self.dictCityList[self.strCity]
        self.logger.info("Crawler for {0} is successfully initialed".format(self.strCity))

    def _request(self, _url, _header=None, _cookie=None):
        pass



Crawler("上海")
