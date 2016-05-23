class BaseExchangeDistributionListService(object):

  def __init__(self, service):
    self.service = service

  def expand_dl(self, dl_name):
    raise NotImplementedError

