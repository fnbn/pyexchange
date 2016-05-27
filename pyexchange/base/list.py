class BaseExchangeDistributionListService(object):

  def __init__(self, service):
    self.service = service

  def expand_dl(self, dl_name):
    raise NotImplementedError

class BaseExchangeDistributionList(object):

  members = {}  # members of this distribution list

  def __init__(self, service, dl_name, recursive_expand=False):
    self.service = service
    self._init_from_dl_name(dl_name, recursive_expand)

  def _init_from_dl_name(self, dl_name, recursive_expand):
    """ Using already retrieved XML from Exchange, extract properties out of it. """
    raise NotImplementedError
