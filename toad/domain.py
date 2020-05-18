# classi per i dati di dominio
class Measurement:
    def __init__(self, name, provider, measuredAt, closeAsk, closeBid, highAsk, highBid, lowAsk, lowBid, openAsk, openBid, volume):
        self._name = name
        self._provider = provider
        self._measuredAt = measuredAt
        self._closeAsk = closeAsk
        self._closeBid = closeBid
        self._highAsk = highAsk
        self._highBid = highBid
        self._lowAsk = lowAsk
        self._lowBid = lowBid
        self._openAsk = openAsk
        self._openBid = openBid
        self._volume = volume

    def __str__(self):
        return f"Measurement({self.name}, {self.volume}, {self.measuredAt}, ask: [{self.lowAsk, self.highAsk}], bid: [{self.lowBid, self.highBid}])"

    @property
    def name(self): return self._name

    @property
    def provider(self): return self._provider

    @property
    def measuredAt(self): return self._measuredAt

    @property
    def closeAsk(self): return self._closeAsk

    @property
    def closeBid(self): return self._closeBid

    @property
    def highAsk(self): return self._highAsk

    @property
    def highBid(self): return self._highBid

    @property
    def lowAsk(self): return self._lowAsk

    @property
    def lowBid(self): return self._lowBid

    @property
    def openAsk(self): return self._openAsk

    @property
    def openBid(self): return self._openBid

    @property
    def volume(self): return self._volume
